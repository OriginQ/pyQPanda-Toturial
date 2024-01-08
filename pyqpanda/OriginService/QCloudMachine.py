# This code is part of pyqpanda.
#
# (C) Copyright Origin Quantum 2023
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

""" Origin Quantum Computing Cloud Service ToolKit."""

import json
import time
import requests

from typing import List, Dict, Union, Optional, Tuple
from pyqpanda import QCloudService, QProg, QVec, NoiseModel, real_chip_type

class QCloud(QCloudService):
    """
    Quantum Computing Cloud Service Utility Class.

    The primary function of this utility class for the Origin Quantum Computing Cloud Service is to package and send quantum circuits to the remote computing service (Quantum Cloud). 
    It then queries the computation results through polling, supporting various simulators and real hardware.

    User API key authentication is required for computations. Please obtain it here : http://qcloud.originqc.com.cn/
    """

    from enum import Enum, auto
    class CloudQMchineType(Enum):

        Full_AMPLITUDE = 0
        NOISE_QMACHINE = 1
        PARTIAL_AMPLITUDE = 2
        SINGLE_AMPLITUDE = 3
        CHEMISTRY = 4
        REAL_CHIP = 5
        QST = 6
        FIDELITY = 7
    
    class TaskStatus(Enum):
        WAITING = 1
        COMPUTING = 2
        FINISHED = 3
        FAILED = 4
        QUEUING = 5
        SENT_TO_BUILD_SYSTEM = 6
        BUILD_SYSTEM_ERROR = 7
        SEQUENCE_TOO_LONG = 8
        BUILD_SYSTEM_RUN = 9

    def init_qvm(self, token: str, 
                 is_logged: bool = False,
                 use_bin_or_hex = True):
        
        """
        init quantum virtual machine
        """

        self.use_bin_or_hex = use_bin_or_hex
        super().init(token, is_logged)
        ...

    def convert_result_format(self, 
                              input_dict: dict,
                              binary_size : int):
        
        """
        convert result format from binary to hex 

        Args:
            input_dict (dict): origin result dict
            use_bin_or_hex (bool): True -> use binary result format, False -> Hex

        Returns:
            result: dict.
        """

        if(self.use_bin_or_hex): 

            # convert from hex -> bin
            def hex_to_binary(hex_str, binary_length):
                if hex_str.startswith('0X'):
                    hex_str = hex_str[2:]
                binary_str = bin(int(hex_str, 16))[2:]
                return binary_str.zfill(binary_length)

            result_dict = {}
            for key, value in input_dict.items():
                key = key.upper()
                if key.startswith('0X'):  # Check if the key is a hex string
                    result_dict[hex_to_binary(key, binary_size)] = value
                else:
                    result_dict[key] = value
            
            return result_dict

        else:

            # convert from bin -> hex
            def binary_to_hex(binary_str):
                return hex(int(binary_str, 2))

            result_dict = {}
            for key, value in input_dict.items():
                if all(c in '01' for c in key):  # Check if the key is a binary string
                    result_dict[binary_to_hex(key)] = value
                else:
                    result_dict[key] = value

            return result_dict
        
    def _send_request(self, 
                      str_url : str = None, 
                      post_json : str = None):
        """
        Sends a POST request to the specified URL with JSON data.

        Args:
            str_url (str): The URL to send the request to.
            post_json (str): JSON data to be sent in the request body.

        Returns:
            str: Response text from the server.

        Raises:
            RuntimeError: If the request fails.
        """   
        headers = {
            # 'Transfer-Encoding': 'chunked',
            'origin-language': 'en',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json;charset=UTF-8',
            'Authorization': 'oqcs_auth=' + self.user_token
        }

        json_dict = json.loads(post_json)
        response = requests.post(url = str_url, 
                                 headers = headers, 
                                 json = json_dict, 
                                 verify = False, 
                                 timeout = 10)

        # response check
        if response.status_code == 200:
            return response.text
        else:
            print('request failed: ', response.status_code)
            raise RuntimeError("request failed")
        
    def _query_result_json(self, taskid : str):
        """
        Queries the result of a computation task using task ID.

        Args:
            taskid (str): The task ID to query.

        Returns:
            str: Result string of the computation.

        Notes:
            This function polls the server until the computation is complete.
        """
        
        result_recv_string = None

        while True:

            time.sleep(1)

            obj = {"taskId": taskid, "apiKey": self.user_token}

            response_string = self._send_request(super().inquire_url, json.dumps(obj))

            is_retry_again, query_recv_string = super().cyclic_query(response_string)

            if not is_retry_again:
                result_recv_string = query_recv_string
                break 

        return result_recv_string
    
    def _batch_query_result_json(self, taskid : str):
        """
        Queries the result of a batch computation task using task ID.

        Args:
            taskid (str): The task ID to query.

        Returns:
            List[str]: List of result strings for individual computations.

        Notes:
            This function polls the server until the batch computation is complete.
        """   
        
        result_str_list = None

        while True:

            time.sleep(1)

            obj = {"taskId": taskid, "apiKey": self.user_token}

            response_string = self._send_request(super().batch_inquire_url, json.dumps(obj))

            is_retry_again, query_recv_string = super().batch_cyclic_query(response_string)

            if not is_retry_again:
                result_str_list = query_recv_string
                break 

        return result_str_list
    
    def _submit_and_query(self, task_msg : str):
        """
        Submits a computation task and queries the result.

        Args:
            task_msg (str): Message containing the computation task details.

        Returns:
            str: Result JSON of the computation.

        Notes:
            This function combines submission and result querying.
        """

        submit_url = super().compute_url
        recv_string = self._send_request(submit_url, task_msg)

        task_id = super().parse_get_task_id(recv_string)

        result_json = self._query_result_json(task_id)

        return result_json
    
    def _batch_submit_and_query(self, task_msg : str):
        """
        Submits a batch computation task and queries the result.

        Args:
            task_msg (str): Message containing the batch computation task details.

        Returns:
            List[str]: List of result JSONs for individual computations in the batch.

        Notes:
            This function combines submission and result querying for batch computations.
        """
    
        submit_url = super().batch_compute_url
        recv_string = self._send_request(submit_url, task_msg)

        task_id = super().parse_get_task_id(recv_string)

        result_json = self._batch_query_result_json(task_id)

        return result_json
    
    def query_task_state_result(self,
                                task_id : str):
    
        obj = {"taskId": task_id, "apiKey": self.user_token}
        recv_json = self._send_request(super().inquire_url, json.dumps(obj))

        recv_dict = json.loads(recv_json)

        if not recv_dict["success"]:
            message = recv_dict["message"]
            raise Exception(f"query task error : {message}")

        result_list = recv_dict["obj"]["qcodeTaskNewVo"]["taskResultList"]

        status = int(result_list[0]["taskState"])
        backend_type = int(result_list[0]["rQMachineType"])

        # 处理不同的任务状态
        if status == self.TaskStatus.FINISHED.value:  # TaskStatus::FINISHED

            measure_qubits_num = []

            if "measureQubitSize" not in result_list[0]:
                raise RuntimeError("measureQubitSize not found")

            for qubit_size in result_list[0]["measureQubitSize"]:
                qubit_addr = int(qubit_size)
                measure_qubits_num.append(qubit_addr)

            # CloudQMchineType::REAL_CHIP, NOISE_QMACHINE, Full_AMPLITUDE, PARTIAL_AMPLITUDE, SINGLE_AMPLITUDE
            if backend_type in [self.CloudQMchineType.Full_AMPLITUDE.value,
                                self.CloudQMchineType.NOISE_QMACHINE.value, 
                                self.CloudQMchineType.REAL_CHIP.value]:  
                result_string = result_list[0]["taskResult"]

                origin_result = super().query_prob_dict_result(result_string)
                result = self.convert_result_format(origin_result, measure_qubits_num[0])
                return [status, result]
            
            if backend_type ==  self.CloudQMchineType.PARTIAL_AMPLITUDE.value:

                result_string = result_list[0]["taskResult"]
                origin_result = super().query_state_dict_result(result_string)
                result = self.convert_result_format(origin_result, measure_qubits_num[0])
                return [status, result]
            
            if backend_type ==  self.CloudQMchineType.SINGLE_AMPLITUDE.value:
                result_string = result_list[0]["taskResult"]
                return [status, super().query_comolex_result(result_string)]

            elif backend_type == self.CloudQMchineType.QST.value:
                result_string = result_list[0]["qstresult"]
                return [status, super().query_qst_result(result_string)]

            elif backend_type == self.CloudQMchineType.FIDELITY.value:
                fidelity_value = float(result_list[0]["qstfidelity"])
                result_string = json.dumps({"value": fidelity_value})

                return [status, fidelity_value]

            else:
                raise Exception("Wrong backend type")

        elif status == self.TaskStatus.FAILED.value:
            if "errorMessage" in result_list[0]:
                error_message = result_list[0]["errorMessage"]
            else:
                error_message = "Unknown error"

            print("Task process error : ", error_message)
            return [status, {}]

        elif status in [self.TaskStatus.BUILD_SYSTEM_ERROR.value, 
                        self.TaskStatus.SEQUENCE_TOO_LONG.value]:
            error_message = "Real chip build system error" if status == 3 else "Real chip maximum timing sequence"
            raise Exception(f"Task process error: {error_message}")

        else:
            return [status, {}]
        
    def query_batch_task_state_result(self,
                                      task_id : str):
    
        obj = {"taskId": task_id, "apiKey": self.user_token}
        recv_json = self._send_request(super().batch_inquire_url, json.dumps(obj))
        
        recv_dict = json.loads(recv_json)

        if not recv_dict["success"]:
            message = recv_dict["message"]
            raise Exception(f"query task error : {message}")

        state_str = recv_dict["obj"]["taskStatus"]
        status = int(state_str)

        if status == self.TaskStatus.FINISHED.value:  # TaskStatus::FINISHED

            measure_qubits_num = []

            if "measureQubitSize" not in recv_dict["obj"]:
                raise RuntimeError("measureQubitSize not found")

            for qubit_size in recv_dict["obj"]["measureQubitSize"]:
                qubit_addr = int(qubit_size)
                measure_qubits_num.append(qubit_addr)

            result_array = [result_string for result_string in recv_dict["obj"]["taskResult"]]
            
            origin_result = super().query_prob_dict_result_batch(result_array)

            result = []
            for i in range(len(origin_result)):
                result.append(self.convert_result_format(origin_result[i], measure_qubits_num[i]))

            return [status, result]

        elif status == self.TaskStatus.FAILED.value:

            if "errorDetail" in recv_dict["obj"]:
                error_message = recv_dict["obj"]["errorDetail"]
            else:
                error_message = "Unknown error"

            print("Task process error : ", error_message)
            return [status, {}]

        elif status in [self.TaskStatus.BUILD_SYSTEM_ERROR.value, 
                        self.TaskStatus.SEQUENCE_TOO_LONG.value]:
            error_message = "Real chip build system error" if status == 3 else "Real chip maximum timing sequence"
            raise Exception(f"Task process error: {error_message}")

        else:
            return [status, {}]
        
    def estimate_price(self,
                       qubit_num : int,
                       shot : int,
                       qprogCount : int = 1,
                       epoch : int = 1):
        
        data = {
        "qubitNum": qubit_num,
        "shot": shot,
        "qprogCount": qprogCount,
        "epoch": epoch}

        json_string = json.dumps(data)
        recv_string = self._send_request(super().estimate_url, json_string)

        doc = json.loads(recv_string)

        if not doc["success"]:
            message = doc["message"]
            raise RuntimeError(message)
        else:
            estimate_value_str = doc["obj"]
            estimate_value = float(estimate_value_str)

            return estimate_value

    def async_full_amplitude_measure(self, 
                                     prog: QProg, 
                                     shot: int, 
                                     task_name: str = 'QPanda Experiment'):
        """
        Execute a full amplitude measurement on the Quantum Cloud Service.

        Args:
            prog (QProg): Quantum program containing the circuit to be measured.
            shot (int): Number of measurements to perform.
            task_name (str, optional): Task name for identification. Defaults to 'QPanda Experiment'.

        Returns:
            Task_id[str]: A task id for current task
        """
        super().build_init_object(prog, task_name)
        task_msg = super().build_full_amplitude_measure(shot)

        recv_string = self._send_request(super().compute_url, task_msg)
        return super().parse_get_task_id(recv_string)

    def full_amplitude_measure(self, 
                               prog: QProg, 
                               shot: int, 
                               task_name: str = 'QPanda Experiment'):
        """
        Execute a full amplitude measurement on the Quantum Cloud Service.

        Args:
            prog (QProg): Quantum program containing the circuit to be measured.
            shot (int): Number of measurements to perform.
            task_name (str, optional): Task name for identification. Defaults to 'QPanda Experiment'.

        Returns:
            Dict[str, float]: Dictionary containing probabilities of measurement outcomes.
        """
        super().build_init_object(prog, task_name)
        task_msg = super().build_full_amplitude_measure(shot)

        result_json = self._submit_and_query(task_msg)

        origin_result = super().query_prob_dict_result(result_json)
        return self.convert_result_format(origin_result, super().measure_qubits_num[0])
    
    def async_full_amplitude_pmeasure(self, 
                                     prog: QProg, 
                                     qvec: List[int], 
                                     task_name: str = 'QPanda Experiment'):
        """
        Execute a full amplitude probability measurement on the Quantum Cloud Service.

        Args:
            prog (QProg): Quantum program containing the circuit to be measured.
            shot (int): Number of measurements to perform.
            task_name (str, optional): Task name for identification. Defaults to 'QPanda Experiment'.

        Returns:
            Task_id[str]: A task id for current task
        """
        super().build_init_object(prog, task_name)
        task_msg = super().build_full_amplitude_pmeasure(qubit_vec=qvec)

        recv_string = self._send_request(super().compute_url, task_msg)
        return super().parse_get_task_id(recv_string)

    def full_amplitude_pmeasure(self, 
                                prog: QProg, 
                                qvec: List[int], 
                                task_name: str = 'QPanda Experiment'):
        """
        Execute a full amplitude probability measurement on the Quantum Cloud Service.

        Args:
            prog (QProg): Quantum program containing the circuit to be measured.
            qvec (List[int]): List of qubits to be measured.
            task_name (str, optional): Task name for identification. Defaults to 'QPanda Experiment'.

        Returns:
            Dict[str, float]: Dictionary containing probabilities of measurement outcomes.
        """
        super().build_init_object(prog, task_name)
        task_msg = super().build_full_amplitude_pmeasure(qvec)

        result_json = self._submit_and_query(task_msg)

        origin_result = super().query_prob_dict_result(result_json)
        return self.convert_result_format(origin_result, super().measure_qubits_num[0])

    def get_expectation(self, 
                        prog: QProg, 
                        hamiltonian: List[Tuple[Dict[int,str],float]], 
                        qvec: QVec, 
                        task_name: str = 'QPanda Experiment'):
        """
        Calculate the expectation value of a Hamiltonian on the Quantum Cloud Service.

        Args:
            prog (QProg): Quantum program containing the circuit for state preparation.
            hamiltonian (List[Tuple[Dict[int, str], float]]): List of terms in the Hamiltonian along with their coefficients.
            qvec (QVec): List of qubits representing the quantum state.
            task_name (str, optional): Task name for identification. Defaults to 'QPanda Experiment'.

        Returns:
            float: Expectation value of the Hamiltonian.
        """
        super().build_init_object(prog, task_name)
        task_msg = super().build_get_expectation(hamiltonian, qvec)

        result_json = self._submit_and_query(task_msg)

        return super().query_prob_result(result_json)

    def get_state_fidelity(self, 
                           prog: QProg, 
                           shot: int, 
                           chip_id: int = 2, 
                           is_amend: bool = True, 
                           is_mapping: bool = True, 
                           is_optimization: bool = True,
                           compile_level: int = 3,
                           task_name: str = 'QPanda Experiment'):
        """
        Get the state fidelity of the Quantum Real Chip.

        Args:
            prog (QProg): Quantum program containing the circuit for state preparation.
            shot (int): Number of measurements to perform.
            chip_id (int, optional): ID of the quantum chip. Defaults to 2.
            is_amend (bool, optional): Flag for amplitude amplification. Defaults to True.
            is_mapping (bool, optional): Flag for qubit mapping. Defaults to True.
            is_optimization (bool, optional): Flag for gate optimization. Defaults to True.
            task_name (str, optional): Task name for identification. Defaults to 'QPanda Experiment'.

        Returns:
            float: State fidelity value.
        """
        super().build_init_object(prog, task_name)
        task_msg = super().build_get_state_fidelity(shot=shot,
                                                    chip_id=chip_id,
                                                    is_amend=is_amend,
                                                    is_mapping=is_mapping,
                                                    is_optimization=is_optimization,
                                                    compile_level=compile_level)

        result_json = self._submit_and_query(task_msg)

        return super().query_prob_result(result_json)

    def get_state_tomography_density(self, 
                                     prog: QProg, 
                                     shot: int, 
                                     chip_id: int = 2, 
                                     is_amend: bool = True, 
                                     is_mapping: bool = True, 
                                     is_optimization: bool = True, 
                                     compile_level: int = 3,
                                     task_name: str = 'QPanda Experiment'):
        """
        Get the density matrix for state tomography on the Quantum Cloud Service.

        Args:
            prog (QProg): Quantum program containing the circuit for state preparation.
            shot (int): Number of measurements to perform.
            chip_id (int, optional): ID of the quantum chip. Defaults to 2.
            is_amend (bool, optional): Flag for amplitude amplification. Defaults to True.
            is_mapping (bool, optional): Flag for qubit mapping. Defaults to True.
            is_optimization (bool, optional): Flag for gate optimization. Defaults to True.
            task_name (str, optional): Task name for identification. Defaults to 'QPanda Experiment'.

        Returns:
            List[List[complex]]: Density matrix representing the quantum state.
        """
        super().build_init_object(prog, task_name)
        task_msg = super().build_get_state_fidelity(shot=shot,
                                                    chip_id=chip_id,
                                                    is_amend=is_amend,
                                                    is_mapping=is_mapping,
                                                    is_optimization=is_optimization,
                                                    compile_level=compile_level)

        result_json = self._submit_and_query(task_msg)

        return super().query_qst_result(result_json)

    def async_noise_measure(self, 
                            prog: QProg, 
                            shot: int, 
                            task_name: str = 'QPanda Experiment'):
        """
        Measure noise in the quantum computation.

        Args:
            prog (QProg): The quantum circuit to be executed.
            shot (int): The number of shots (measurement repetitions).
            task_name (str, optional): The name of the QPanda Experiment task. Defaults to 'QPanda Experiment'.

        Returns:
            Task_id[str]: A task id for current task
        """

        super().build_init_object(prog, task_name)
        task_msg = super().build_noise_measure(shot=shot)

        recv_string = self._send_request(super().compute_url, task_msg)
        return super().parse_get_task_id(recv_string)

    def noise_measure(self, 
                      prog: QProg, 
                      shot: int, 
                      task_name: str = 'QPanda Experiment'):
        """
        Measure noise in the quantum computation.

        Args:
            prog (QProg): The quantum circuit to be executed.
            shot (int): The number of shots (measurement repetitions).
            task_name (str, optional): The name of the QPanda Experiment task. Defaults to 'QPanda Experiment'.

        Returns:
            Dict[str, float]: A dictionary containing measurement results.
        """

        super().build_init_object(prog, task_name)
        task_msg = super().build_noise_measure(shots=shot)

        result_json = self._submit_and_query(task_msg)

        origin_result = super().query_prob_dict_result(result_json)
        return self.convert_result_format(origin_result, super().measure_qubits_num[0])

    def async_partial_amplitude_pmeasure(self, 
                                   prog: QProg, 
                                   amp_vec: List[str], 
                                   task_name: str = 'QPanda Experiment'):
        """
        Perform partial amplitude measurement in the quantum computation.

        Args:
            prog (QProg): The quantum circuit to be executed.
            amp_vec (List[str]): List of amplitude vectors to be measured.
            task_name (str, optional): The name of the QPanda Experiment task. Defaults to 'QPanda Experiment'.

        Returns:
            Task_id[str]: A task id for current task
        """

        super().build_init_object(prog, task_name)
        task_msg = super().build_partial_amplitude_pmeasure(amplitudes=amp_vec)

        recv_string = self._send_request(super().compute_url, task_msg)
        return super().parse_get_task_id(recv_string)

    def partial_amplitude_pmeasure(self, 
                                   prog: QProg, 
                                   amp_vec: List[str], 
                                   task_name: str = 'QPanda Experiment'):
        """
        Perform partial amplitude measurement in the quantum computation.

        Args:
            prog (QProg): The quantum circuit to be executed.
            amp_vec (List[str]): List of amplitude vectors to be measured.
            task_name (str, optional): The name of the QPanda Experiment task. Defaults to 'QPanda Experiment'.

        Returns:
            Dict[str, complex]: A dictionary containing complex-valued measurement results.
        """

        super().build_init_object(prog, task_name)
        task_msg = super().build_partial_amplitude_pmeasure(amplitudes=amp_vec)

        result_json = self._submit_and_query(task_msg)

        origin_result = super().query_state_dict_result(result_json)
        return self.convert_result_format(origin_result, super().measure_qubits_num[0])
    
    def async_real_chip_measure(self, 
                                prog: Union[QProg, str], 
                                shot: int, 
                                chip_id: int = 2, 
                                is_amend: bool = True, 
                                is_mapping: bool = True, 
                                is_optimization: bool = True, 
                                compile_level: int = 3,
                                task_name: str = 'QPanda Experiment'):
        """
        Perform measurements on a real quantum chip.

        Args:
            prog (QProg): The quantum circuit to be executed.
            shot (int): The number of shots (measurement repetitions).
            chip_id (int, optional): Identifier for the specific quantum chip. Defaults to 2.
            is_amend (bool, optional): Flag indicating whether to perform amendments. Defaults to True.
            is_mapping (bool, optional): Flag indicating whether to perform qubit mapping. Defaults to True.
            is_optimization (bool, optional): Flag indicating whether to perform optimization. Defaults to True.
            task_name (str, optional): The name of the QPanda Experiment task. Defaults to 'QPanda Experiment'.

        Returns:
            taskid[str]: real chip task id
        """

        super().build_init_object(prog, task_name)
        task_msg = super().build_real_chip_measure(shots=shot,
                                                   chip_id=chip_id,
                                                   is_amend=is_amend,
                                                   is_mapping=is_mapping,
                                                   is_optimization=is_optimization,
                                                   compile_level=compile_level)

        recv_string = self._send_request(super().compute_url, task_msg)
        return super().parse_get_task_id(recv_string)

    def real_chip_measure(self, 
                          prog: Union[QProg, str], 
                          shot: int, 
                          chip_id: int = 2, 
                          is_amend: bool = True, 
                          is_mapping: bool = True, 
                          is_optimization: bool = True,
                          compile_level: int = 3,
                          task_name: str = 'QPanda Experiment'):
        """
        Perform measurements on a real quantum chip.

        Args:
            prog (QProg): The quantum circuit to be executed.
            shot (int): The number of shots (measurement repetitions).
            chip_id (int, optional): Identifier for the specific quantum chip. Defaults to 2.
            is_amend (bool, optional): Flag indicating whether to perform amendments. Defaults to True.
            is_mapping (bool, optional): Flag indicating whether to perform qubit mapping. Defaults to True.
            is_optimization (bool, optional): Flag indicating whether to perform optimization. Defaults to True.
            task_name (str, optional): The name of the QPanda Experiment task. Defaults to 'QPanda Experiment'.

        Returns:
            Dict[str, float]: A dictionary containing measurement results.
        """

        super().build_init_object(prog, task_name)
        task_msg = super().build_real_chip_measure(shots=shot,
                                                   chip_id=chip_id,
                                                   is_amend=is_amend,
                                                   is_mapping=is_mapping,
                                                   is_optimization=is_optimization,
                                                   compile_level=compile_level)

        result_json = self._submit_and_query(task_msg)

        origin_result = super().query_prob_dict_result(result_json)
        return self.convert_result_format(origin_result, super().measure_qubits_num[0])
    
    def async_batch_real_chip_measure(self, 
                                      prog_array: Union[List[QProg], List[str]],
                                      shot: int,
                                      chip_id: real_chip_type = real_chip_type.origin_72, 
                                      is_amend: bool = True, 
                                      is_mapping: bool = True,
                                      is_optimization: bool = True,
                                      compile_level: int = 3):
        """
        Measure a batch of quantum programs on a real quantum chip.

        Parameters:
        - prog_array (List[QProg]): List of quantum programs to be executed.
        - shot (int): Number of shots (measurements) to perform for each program.
        - chip_id (real_chip_type, optional): ID of the real quantum chip to use (default is real_chip_type.origin_72).
        - is_amend (bool, optional): Whether to perform amendment on the programs (default is True).
        - is_mapping (bool, optional): Whether to perform qubit mapping (default is True).
        - is_optimization (bool, optional): Whether to perform gate fusion optimization (default is True).

        Returns:
        batch_task_id[str]: batch task id

        Note:
        The function submits a batch of quantum programs for execution on a real quantum chip, 
        retrieves the results, and returns the probabilities of measurement outcomes for each program.

        """

        task_msg = super().build_real_chip_measure_batch(prog_list=prog_array,
                                                         shots=shot,
                                                         chip_id=chip_id,
                                                         is_amend=is_amend,
                                                         is_mapping=is_mapping,
                                                         is_optimization=is_optimization,
                                                         compile_level=compile_level)

        recv_str = self._send_request(super().batch_compute_url, task_msg)
        task_id = super().parse_get_task_id(recv_str)

        return task_id

    def batch_real_chip_measure(self, 
                                prog_array: Union[List[QProg], List[str]],
                                shot: int, 
                                chip_id: real_chip_type = real_chip_type.origin_72, 
                                is_amend: bool = True, 
                                is_mapping: bool = True,
                                is_optimization: bool = True,
                                compile_level: int = 3):
        """
        Measure a batch of quantum programs on a real quantum chip.

        Parameters:
        - prog_array (List[QProg]): List of quantum programs to be executed.
        - shot (int): Number of shots (measurements) to perform for each program.
        - chip_id (real_chip_type, optional): ID of the real quantum chip to use (default is real_chip_type.origin_72).
        - is_amend (bool, optional): Whether to perform amendment on the programs (default is True).
        - is_mapping (bool, optional): Whether to perform qubit mapping (default is True).
        - is_optimization (bool, optional): Whether to perform gate fusion optimization (default is True).

        Returns:
        List[Dict[str, float]]: A list of dictionaries containing the probabilities of measurement outcomes for each program.

        Note:
        The function submits a batch of quantum programs for execution on a real quantum chip, 
        retrieves the results, and returns the probabilities of measurement outcomes for each program.

        """
        task_msg = super().build_real_chip_measure_batch(prog_list=prog_array,
                                                         shots=shot,
                                                         chip_id=chip_id,
                                                         is_amend=is_amend,
                                                         is_mapping=is_mapping,
                                                         is_optimization=is_optimization,
                                                         compile_level=compile_level)
        
        result_json = self._batch_submit_and_query(task_msg)
    
        origin_result = super().query_prob_dict_result_batch(result_json)

        result = []
        for i in range(len(origin_result)):
            result.append(self.convert_result_format(origin_result[i], super().measure_qubits_num[i]))

        return result

    def set_noise_model(self, 
                        model: NoiseModel, 
                        single_gate_params: List[float], 
                        single_param_list: List[float]):
        """
        Set the noise model for quantum computation.

        Parameters:
        - model (NoiseModel): The noise model to be set.
        - single_gate_params (List[float]): List of parameters for single-qubit gates.
        - single_param_list (List[float]): List of parameters for single-qubit gates.

        Returns:
        None
        """
        super().set_noise_model(model,single_gate_params,single_param_list)
        ...

    def set_qcloud_api(self, prefix_url: str):
        """
        Set the QCloud API endpoint.

        Parameters:
        - prefix_url (str): The prefix URL of the QCloud API.

        Returns:
        None
        """
        super().set_qcloud_api(prefix_url)
        ...

    def async_single_amplitude_pmeasure(self, 
                                        prog: QProg, 
                                        amplitude: str, 
                                        task_name: str = 'QPanda Experiment'):
        """
        Measure the single amplitude of a quantum state.

        Parameters:
        - prog (QProg): The quantum program containing the state.
        - amplitude (str): The amplitude to measure.
        - task_name (str): Name of the QPanda Experiment task.

        Returns:
            Task_id[str]: A task id for current task
        """
        super().build_init_object(prog, task_name)
        task_msg = super().build_single_amplitude_pmeasure(amplitude=amplitude)

        recv_string = self._send_request(super().compute_url, task_msg)
        return super().parse_get_task_id(recv_string)
    
    def single_amplitude_pmeasure(self, 
                                  prog: QProg, 
                                  amplitude: str, 
                                  task_name: str = 'QPanda Experiment'):
        """
        Measure the single amplitude of a quantum state.

        Parameters:
        - prog (QProg): The quantum program containing the state.
        - amplitude (str): The amplitude to measure.
        - task_name (str): Name of the QPanda Experiment task.

        Returns:
        complex: The measured amplitude.
        """
        super().build_init_object(prog, task_name)
        task_msg = super().build_single_amplitude_pmeasure(amplitude=amplitude)

        result_json = self._submit_and_query(task_msg)

        return super().query_comolex_result(result_json)

    def pec_error_mitigation(self, 
                             prog: QProg, 
                             shot: int, 
                             expectations: List[str], 
                             chip_id: int = 72, 
                             task_name: str = 'QPanda Experiment'):
        """
        Apply PEC error mitigation to correct measurement errors.

        Parameters:
        - prog (QProg): The quantum program to apply error mitigation.
        - shot (int): Number of shots for measurements.
        - expectations (List[str]): List of measurement expectations.
        - chip_id (int): Chip identifier.
        - task_name (str): Name of the QPanda Experiment task.

        Returns:
        List[float]: List of corrected expectation values.
        """
        super().build_init_object(prog, task_name)

        from pyqpanda import em_method
        task_msg = super().build_error_mitigation(shots=shot,
                                                  chip_id=chip_id,
                                                  expectations=expectations,
                                                  noise_strength=[],
                                                  qemMethod=em_method.pec)

        result_json = self._submit_and_query(task_msg)

        return super().query_prob_vec_result(result_json)

    def read_out_error_mitigation(self, 
                                  prog: QProg, 
                                  shot: int, 
                                  expectations: List[str], 
                                  chip_id: int = 72, 
                                  task_name: str = 'QPanda Experiment'):
        """
        Apply readout error mitigation to correct measurement errors.

        Parameters:
        - prog (QProg): The quantum program to apply error mitigation.
        - shot (int): Number of shots for measurements.
        - expectations (List[str]): List of measurement expectations.
        - chip_id (int): Chip identifier.
        - task_name (str): Name of the QPanda Experiment task.

        Returns:
            Dict[str, float]: Dictionary of corrected expectation values.
        """

        super().build_init_object(prog, task_name)

        from pyqpanda import em_method
        task_msg = super().build_read_out_mitigation(shots=shot,
                                                     chip_id=chip_id,
                                                     expectations=expectations,
                                                     noise_strength=[],
                                                     qemMethod=em_method.READ_OUT)

        result_json = self._submit_and_query(task_msg)

        origin_result = super().query_prob_dict_result(result_json)
        return self.convert_result_format(origin_result, super().measure_qubits_num[0])

    def zne_error_mitigation(self, 
                             prog: QProg, 
                             shot: int, 
                             expectations: List[str], 
                             noise_strength: List[float], 
                             chip_id: int = 72, 
                             task_name: str = 'QPanda Experiment'):
        """
        Apply zero-noise extrapolation (ZNE) error mitigation to correct measurement errors.

        Parameters:
        - prog (QProg): The quantum program to apply error mitigation.
        - shot (int): Number of shots for measurements.
        - expectations (List[str]): List of measurement expectations.
        - noise_strength (List[float]): List of noise strengths.
        - chip_id (int): Chip identifier.
        - task_name (str): Name of the QPanda Experiment task.

        Returns:
        List[float]: List of corrected expectation values.
        """
        super().build_init_object(prog, task_name)

        from pyqpanda import em_method
        task_msg = super().build_error_mitigation(shots=shot,
                                                  chip_id=chip_id,
                                                  expectations=expectations,
                                                  noise_strength=[],
                                                  qemMethod=em_method.zne)

        result_json = self._submit_and_query(task_msg)

        return super().query_prob_vec_result(result_json)
