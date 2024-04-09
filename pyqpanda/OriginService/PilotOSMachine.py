from pyqpanda import *
from io import BytesIO
from urllib.parse import urlparse
from typing import List, Union
import requests
import json
import gzip
import time
import os
import bz2

class QPilotOSMachine(QPilotOSService):
    """This class can submit Quantum Program to PilotOS.

    Attributes
    ----------
    PilotURL : str
        Connect to the target PilotOS address.
    PilotIp : str
        PilotOS IP address.
    PilotPort : str
        PilotOS port.

    """

    def __init__(self, name : str) -> None:
        """Create QPilotOSMMachine object.

        Note
        ----
        Do not include the `self` parameter in the ``Parameters`` section.

        Parameters
        ----------
        name : str
            Quantum Machine type name.

        Returns
        -------
        QuantumMachine
            Always return a Quantum Machine.

        Examples
        --------
        >>> qm = QPilotOSMachine('Pilot')

        """
        self.PilotURL = ''
        self.PilotIp = ''
        self.PilotPort = ''
        return super().__init__(name)
    
    def _build_task_msg(self, prog : List[QProg] = None, shot : int = None, 
                       chip_id : int = None, is_amend : bool = True, is_mapping : bool = True, 
                       is_optimization : bool = True, specified_block : List[int] = [], task_describe : str = '') -> str:
        """Build submit Quantum compute task request json str, however this is a private method.

        Parameters
        ----------
        prog : List[QProg]
            The quantum program you want to compute.
        shot : int
            Repeate run quantum program times.
        chip_id : int
            The quantum chip ID .
        is_amend : bool
            Whether amend task result.
        is_mapping : bool
            Whether mapping logical Qubit to Physical Qubit.
        is_optimization : bool
            Whether optimize your quantum program.
        specified_block : List[int]
            Your specifed Qubit block .
        task_describe : str
            The detailed infomation to describe your quantum program, such as which kind of algorithm, what can this program compute.

        Returns
        -------
        str

        """
        return super().build_task_msg(prog, shot, chip_id, is_amend, is_mapping, is_optimization, specified_block, task_describe)
    
    def _real_chip_expectation(self, prog : Union[QProg, str], hamiltonian : str, qubits : List[int] = None,
                               shot : int = None, chip_id : int = None, is_amend : bool = True, is_mapping : bool = True, 
                               is_optimization : bool = True, specified_block : List[int] = [], task_describe : str = '') -> float:
        """Build submit Quantum expectation task request json str, however this is a private method.

        Parameters
        ----------
        prog : QProg
            The quantum program you want to compute.
        hamiltonian : 
            Hamiltonian parameters.
        qubits : 
            measurement qubit 
        shot : int
            Repeate run quantum program times.
        chip_id : int
            The quantum chip ID .
        is_amend : bool
            Whether amend task result.
        is_mapping : bool
            Whether mapping logical Qubit to Physical Qubit.
        is_optimization : bool
            Whether optimize your quantum program.
        specified_block : List[int]
            Your specifed Qubit block .
        task_describe : str
            The detailed infomation to describe your quantum program.

        Returns
        -------
        float

        """
        if type(prog) == str:
            prog = convert_originir_str_to_qprog(prog, self)[0]
        return super().real_chip_expectation(prog, hamiltonian, qubits, shot, chip_id, is_amend, is_mapping, is_optimization, specified_block, task_describe)
    
    def _async_real_chip_expectation(self, prog : Union[QProg, str], hamiltonian : str, qubits : List[int] = None,
                               shot : int = None, chip_id : int = None, is_amend : bool = True, is_mapping : bool = True, 
                               is_optimization : bool = True, specified_block : List[int] = [], task_describe : str = '') -> str:
        """Build submit Quantum expectation task request json str, however this is a private method.

        Parameters
        ----------
        prog : QProg
            The quantum program you want to compute.
        hamiltonian : 
            Hamiltonian parameters.
        qubits : 
            measurement qubit 
        shot : int
            Repeate run quantum program times.
        chip_id : int
            The quantum chip ID .
        is_amend : bool
            Whether amend task result.
        is_mapping : bool
            Whether mapping logical Qubit to Physical Qubit.
        is_optimization : bool
            Whether optimize your quantum program.
        specified_block : List[int]
            Your specifed Qubit block .
        task_describe : str
            The detailed infomation to describe your quantum program.

        Returns
        -------
        float

        """
        if type(prog) == str:
            prog = convert_originir_str_to_qprog(prog, self)[0]
        return super().async_real_chip_expectation(prog, hamiltonian, qubits, shot, chip_id, is_amend, is_mapping, is_optimization, specified_block, task_describe)

    def get_expectation_result(self, task_id : str) -> list:
        """ get expectation task result

        Parameters
        ----------
        task_id : str
            expectation task id.

        Returns
        -------
        list
            expectation task result.
        """
        return super().get_expectation_result(task_id)

    def _build_query_msg(self, task_id : str) ->str:
        """Build Query Quantum compute task result request json str, however this is a private method.

        Parameters
        ----------
        task_id : str
            The task id of your task.

        Returns
        -------
        str

        """
        return super().build_query_msg(task_id)

    def _tcp_recv(self, ip : str, port : int, task_id : str) -> list:
        """Receive message using TCP protocol, however this is a private method.

        Parameters
        ----------
        ip : str
            The PilotOS IP address.
        port : str
            The PilotOS port.
        task_id : str
            The task id of your task.

        Returns
        -------
        list

        """
        return super().tcp_recv(ip, port, task_id)

    def _parser_sync_result(self, json_str) -> list:
        """Parse sync compute task result to list, however this is a private method.

        Parameters
        ----------
        json_str : str
            The json str contains task result key and value.

        Returns
        -------
        list

        """
        return super().parser_sync_result(json_str)

    def _send_request(self, str_url : str = None, req : str = None, resp : list = None) -> bool:
        """Send request to PilotOS, however this is a private method.

        Parameters
        ----------
        str_url : str
            The http function you want to request.
        req : str
            The json str contains request message.
        resp : list
            The list of response result and reply message.

        Returns
        -------
        bool

        """   
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Content-Encoding': 'bz2',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
        }

        #if len(req) > 1048576:
        #    with gzip.open('request.gz', 'wt') as f:
        #        f.write(req)
        #    with open('request.gz', 'rb') as f:
        #        req = f.read()

        compressed_req = bz2.compress(req.encode())

        try:            
            response = requests.post(url = str_url, headers = headers, data = compressed_req, verify = False, timeout = 70)
        except Exception as e:
            print("An error occurred:", e)
            return False

        # response check
        if response.status_code == 200:
            if response.headers.get('Content-Encoding') == 'bz2':
                # Decompress bz2 response
                decompressed_data = bz2.decompress(response.content)
                # with gzip.GzipFile(fileobj=BytesIO(response.content)) as f:
                #     decompressed_data = f.read()
                resp.append(decompressed_data.decode('utf-8'))
                #print(decompressed_data.decode('utf-8'))
                #with open('decompressed_response.txt', 'wb') as file:
                    #file.write(decompressed_data)
            else:
                resp.append(response.text)
                #print(response.text)
                #with open('response.txt', 'w') as file:
                    #file.write(response.text)
            #print("Response written to file 'response.txt'")
            return True
        else:
            print('request failed!')
            print(response.status_code)
            resp.append(response.text)
            print(response.text)
            return False

    def _get_prog(self, prog : Union[List[str], List[QProg], str, QProg]) ->list:
        """Get QProg list from user input, however this is a private method.

        Parameters
        ----------
        prog : Union[List[str], List[QProg], str, QProg]
            The QProg or OriginIR, Is or not in list.

        Returns
        -------
        List[QProg]

        """ 
        proglist = []
        if isinstance(prog, list):            
            for item in prog:
                if isinstance(item, str):
                    prog_res = convert_originir_str_to_qprog(item, self)
                    proglist.append(prog_res[0])
                elif isinstance(item, QProg):
                    proglist.append(item)
        elif isinstance(prog, QProg):
            proglist.append(prog)
        elif isinstance(prog, str):
            prog_res = convert_originir_str_to_qprog(prog, self)
            proglist.append(prog_res[0])
        return proglist

    def set_config(self, max_qubit : int = None, max_cbit : int = None) -> None: 
        """set Quantum Machine max Qubit and Cbit number function.

        Parameters
        ----------
        max_qubit : int
            The Quantum Machine max available qubits.
        max_cbit : int
            The Quantum Machine max available cbits.

        Returns
        -------
        None

        Examples
        --------
        
        >>> qm.set_config(12, 12)

        """
        super().set_config(max_qubit, max_cbit)

    def init(self, url: str = None, log_cout: bool = False, api_key: str = None) -> None:
        """Init Quantum Machine and connect to PilotOS.

        Parameters
        ----------
        url : str
            The Quantum Machine address you want to connnect.
        log_cout : bool
            Whether record execute log.
        api_key : str
            The unique certificate to login PilotOS, which can get from PilotOS WebSite.

        Returns
        -------
        None

        Examples
        --------
        
        >>> qm.init('PilotOS_url', True, 'your_api_key')

        """
        if url is not None:
            parsed_url = urlparse(url)
            self.PilotURL = url
            self.PilotIp = parsed_url.hostname
            self.PilotPort = parsed_url.port

            super().init_config(url,log_cout)
            login_req = super().build_init_msg(api_key)
            login_url = url + '/management/pilotosmachinelogin'
            resp = []
            if self._send_request(login_url, login_req, resp):
                if super().get_token(resp[0]) == ErrorCode.NO_ERROR_FOUND:
                    pass
                else:
                    print('init failed for parse token failed!!')
            else:
                print('init failed for send request to Pilot failed!!')
        else:
            super().init()
        
    def qAlloc_many(self, qubit_num : int = None) -> list: 
        """Get Qubits to construct Quantum Circuit.

        Parameters
        ----------
        qubit_num : int
            The Qubits number you need to use in circuit.

        Returns
        -------
        List[Qubit]

        Examples
        --------
        
        >>> q = qm.qAlloc_many(6)

        """
        return super().qAlloc_many(qubit_num)

    def cAlloc_many(self, cbit_num : int = None) -> list: 
        """Get Cbits to construct Quantum Circuit.

        Parameters
        ----------
        cbit_num : int
            The Cbits number you need to use in circuit.

        Returns
        -------
        List[ClassicalCondition]

        Examples
        --------
        
        >>> c = qm.cAlloc_many(6)

        """
        return super().cAlloc_many(cbit_num)

    def real_chip_measure(self, prog : Union[List[str], List[QProg], str, QProg], shot = 1000, chip_id = None, 
                        is_amend = True, is_mapping = True, is_optimization = True, 
                        specified_block = [], describe = '') -> list:
        """Using sync way to compute your Quantum Program  .

        Parameters
        ----------
        prog : Union[List[str], List[QProg], str, QProg]
            The quantum program you want to compute.
        shot : int
            Repeate run quantum program times.
        chip_id : int
            The quantum chip ID .
        is_amend : bool
            Whether amend task result.
        is_mapping : bool
            Whether mapping logical Qubit to Physical Qubit.
        is_optimization : bool
            Whether optimize your quantum program.
        specified_block : List[int]
            Your specifed Qubit block .
        describe : str
            The detailed infomation to describe your quantum program, such as which kind of algorithm, what can this program compute.

        Returns
        -------
        list
            a list of every single quantum program

        Examples
        --------
        
        >>> result = qm.real_chip_measure(prog_list, 1000, chip_id=1, is_mapping=True, describe="test1")
        >>> print(result)
        [{'00': 0.2456881582421773, '01': 0.2495193504871486, '10': 0.25044435129147546, '11': 0.25434813997919875}, {'00': 0.2456881582421773, '01': 0.2495193504871486, '10': 0.25044435129147546, '11': 0.25434813997919875}]

        """
        proglist = self._get_prog(prog)
        req_str = self._build_task_msg(proglist, shot, chip_id, is_amend, is_mapping, is_optimization, specified_block, describe)
        url = self.PilotURL + '/task/realQuantum/run'
        resp = []
        send_ok = self._send_request(url, req_str, resp)
        if not send_ok:
            result = ['{"errCode": 3, "errInfo": "Error: Send request failed!"}']
            print(result[0])
            return result
        else:
            parsed_data = json.loads(resp[0])
            if 'taskId' in parsed_data:
                task_id = parsed_data['taskId']
            else:
                print('The taskId key is not present in the JSON data.')
            task_resp = self._tcp_recv(self.PilotIp, int(self.PilotPort), task_id)
            if task_resp[0]:
                err_info = json.loads(task_resp[1])
                result = self._parser_sync_result(task_resp[1])
                return result[0]
            else:
                while True:
                    query_result = self.query_task_state(self, task_id)               
                    if query_result[0] == '3':
                        pass
                    elif query_result[0] == '4' or query_result[0] == '35':
                        print(f"state: {query_result[0]}")
                        print(f"errCode: {query_result[2]}")
                        print(f"errInfo: {query_result[3]}")
                        #print(f"Task measure failed Please measure later, errInfo:{query_result[1]}")
                        break
                    else:
                        print(f"state: {query_result[0]}")
                        time.sleep(1) #延时2秒
                        continue
                    return task_resp[1]

    def async_real_chip_measure(self, prog : Union[List[str], List[QProg], str, QProg], shot = 1000, chip_id = None, 
                        is_amend = True, is_mapping = True, is_optimization = True, 
                        specified_block = [], describe = '') -> str:
        """Using async way to compute your Quantum Program, then you need to query task result from task_id.

        Parameters
        ----------
        prog : Union[List[str], List[QProg], str, QProg]
            The quantum program you want to compute.
        shot : int
            Repeate run quantum program times.
        chip_id : int
            The quantum chip ID .
        is_amend : bool
            Whether amend task result.
        is_mapping : bool
            Whether mapping logical Qubit to Physical Qubit.
        is_optimization : bool
            Whether optimize your quantum program.
        specified_block : List[int]
            Your specifed Qubit block .
        describe : str
            The detailed infomation to describe your quantum program, such as which kind of algorithm, what can this program compute.

        Returns
        -------
        str
            your task id which can query task result

        Examples
        --------
        This interface will return a string that will be used to query the results of the quantum program you just submitted. 

        >>> task_id = qm.async_real_chip_measure(prog_list, 1000, chip_id=1, is_mapping=True, describe="test1")
        >>> print (task_id)
        54C64205E2AF45D393FB5E6279E14984

        """
        proglist = self._get_prog(prog)
        req_str = self._build_task_msg(proglist, shot, chip_id, is_amend, is_mapping, is_optimization, specified_block, describe)
        url = self.PilotURL + '/task/realQuantum/run'
        resp = []
        send_ok = self._send_request(url, req_str, resp)
        if not send_ok:
            print('Error: Send request failed!')
            return 'Error: Send request failed"}'
        else:
            print(f"Receive: {resp[0]}")
            parsed_data = json.loads(resp[0])
            if 'taskId' in parsed_data:
                task_id = parsed_data['taskId']
                return task_id
            else:
                print(f'The taskId key is not present in the JSON data. reply: {parsed_data}')
                return parsed_data
    
    def real_chip_expectation(self, prog : Union[QProg, str], hamiltonian : str, qubits : List[int] = None,
                               shot : int = None, chip_id : int = None, is_amend : bool = True, is_mapping : bool = True, 
                               is_optimization : bool = True, specified_block : List[int] = [], task_describe : str = '') -> float:
        """submit Quantum expectation task, and get the expectation result.    

        Parameters
        ----------
        prog : QProg
            The quantum program you want to compute.
        hamiltonian : 
            Hamiltonian parameters.
        qubits : 
            measurement qubit 
        shot : int
            Repeate run quantum program times.
        chip_id : int
            The quantum chip ID .
        is_amend : bool
            Whether amend task result.
        is_mapping : bool
            Whether mapping logical Qubit to Physical Qubit.
        is_optimization : bool
            Whether optimize your quantum program.
        specified_block : List[int]
            Your specifed Qubit block .
        task_describe : str
            The detailed infomation to describe your quantum program, such as which kind of algorithm, what can this program compute.

        Returns
        -------
        float
            expectation task result
        """
        return self._real_chip_expectation(prog, hamiltonian, qubits, shot, chip_id, is_amend, is_mapping, is_optimization,
                                              specified_block, task_describe)
        

    def async_real_chip_expectation(self, prog : Union[QProg, str], hamiltonian : str, qubits : List[int] = None,
                                    shot : int = None, chip_id : int = None, is_amend : bool = True, is_mapping : bool = True, 
                                    is_optimization : bool = True, specified_block : List[int] = [], task_describe : str = '') -> str:
        """async submit Quantum expectation task, and return the task id.    

        Parameters
        ----------
        prog : QProg
            The quantum program you want to compute.
        hamiltonian : 
            Hamiltonian parameters.
        qubits : 
            measurement qubit 
        shot : int
            Repeate run quantum program times.
        chip_id : int
            The quantum chip ID .
        is_amend : bool
            Whether amend task result.
        is_mapping : bool
            Whether mapping logical Qubit to Physical Qubit.
        is_optimization : bool
            Whether optimize your quantum program.
        specified_block : List[int]
            Your specifed Qubit block .
        task_describe : str
            The detailed infomation to describe your quantum program, such as which kind of algorithm, what can this program compute.

        Returns
        -------
        str
            return expectation task id, you need query task result by using task id.
        """
        
        return self._async_real_chip_expectation(prog, hamiltonian, qubits, shot, chip_id, is_amend, is_mapping, is_optimization,
                                              specified_block, task_describe)
        
    def query_task_state(self, task_id : str, file_path : str = None) -> list:
        """Query task result from task_id.

        Parameters
        ----------
        task_id : str
            The task id you want to query.
        file_path : str
            If the parameter is not None, task result will be saved to target path.

        Returns
        -------
        list
            Contains task state, task result, task error code, task error info, 
            you can decide what to do with state and error code.

        Examples
        --------
        This interface will return a result list, contains: task state, probability result, error code, error info(if error code not equal to 0)
        You can decide whether to save the results of the task to a file by entering the second parameter or not, 
        in particular, if you enter an empty string, the file will be saved in the current path

        >>> result_list = qm.query_task_state(task_id, 'D:/python_test/result/')
        >>> for i in result_list: print(i)
        ...
        3
        ['{"key":["0","1"],"value":[0.5,0.5]}']
        0

        If you enter the second parameter a path to save task result json, the json string in file will be like:
        {
            "taskId": "2258D6B6164F4F4FA8F85D1DA2F74370",
            "endTime": 1700466283544,
            "errCode": 0,
            "errInfo": "",
            "startTime": 1700466281627,
            "qProg": [
                "[\"QINIT 72\\nCREG 72\\nX q[0]\\nH q[1]\\nMEASURE q[0]",
                "c[0]\\nMEASURE q[1]",
                "c[1]\"",
                " \"QINIT 72\\nCREG 72\\nX q[0]\\nH q[1]\\nMEASURE q[0]",
                "c[0]\\nMEASURE q[1]",
                "c[1]\"]"
            ],
            "qProgLength": 6,
            "configuration": "{\"shot\":1000,\"amendFlag\":false,\"mappingFlag\":true,\"circuitOptimization\":true,\"IsProbCount\":false,\"specified_block\":[]}",
            "taskState": "3",
            "convertQProg": [
                "[[{\"RPhi\":[2,270.0,90.0,0]},{\"RPhi\":[3,0.0,180.0,0]},{\"Measure\":[[2,3],30]}],[{\"RPhi\":[2,270.0,90.0,0]},{\"RPhi\":[3,0.0,180.0,0]},{\"Measure\":[[2,3],30]}]]"
            ],
            "mappingQProg": [
                "QINIT 72\nCREG 72\nX q[0]\nH q[1]\nMEASURE q[0],c[0]\nMEASURE q[1],c[1]",
                "QINIT 72\nCREG 72\nX q[0]\nH q[1]\nMEASURE q[0],c[0]\nMEASURE q[1],c[1]"
            ],
            "mappingQubit": [
                "{\"SrcQubits\":[0,1],\"TargetCbits\":[0,1],\"MappingQubits\":[3,2]}",
                "{\"SrcQubits\":[0,1],\"TargetCbits\":[0,1],\"MappingQubits\":[3,2]}"
            ],
            "aioExecuteTime": 441,
            "queueTime": 0,
            "compileTime": 608,
            "totalTime": 1229,
            "aioCompileTime": 0,
            "aioPendingTime": 0,
            "aioMeasureTime": 0,
            "aioPostProcessTime": 0,
            "requiredCore": "0",
            "pulseTime": 60.0,
            "cirExecuteTime": 200000.0,
            "taskType": "0",
            "taskResult": [
                "{\"key\":[\"00\",\"01\",\"10\",\"11\"],\"value\":[0.017,0.5,0.017,0.466]}",
                "{\"key\":[\"00\",\"01\",\"10\",\"11\"],\"value\":[0.018,0.474,0.025,0.483]}"
            ]
        }

        """
        req_str = self._build_query_msg(task_id)
        req_url = self.PilotURL + '/task/realQuantum/query'
        resp =[]
        send_ok = self._send_request(req_url, req_str, resp)
        if not send_ok:
            print('Error: Send request failed!')
            return 'Error: Send request failed"}'
        else:
            parsed_data = json.loads(resp[0])
            if 'taskState' in parsed_data and 'taskResult' in parsed_data and 'errCode' in parsed_data and 'errInfo' in parsed_data:    
                task_state = parsed_data['taskState']
                if task_state == '3':
                    if file_path is not None:
                        if len(file_path) > 0 and file_path[-1] != "/":
                            file_path += '/'
                        
                        timestamp_milliseconds = int(time.time() * 1000)
                        # file_name = str(timestamp_milliseconds) + '.json'
                        file_name = 'result.json'
                        file_path = os.path.join(file_path, file_name)
                        print("result save path: " + file_path)

                        if len(file_path) > 15:
                            os.makedirs(os.path.dirname(file_path), exist_ok=True)
                        with open(file_path, 'w') as file:
                            file.write(resp[0])

                task_result = parsed_data['taskResult']
                err_code = parsed_data['errCode']
                err_info = parsed_data['errInfo']
                res = [task_state, task_result, err_code, err_info]
                return res
            else:
                print(f'Query task info error! reply str: {resp[0]}')

    def get_task_list_result(self, task_id : list, file_path : str = None) -> list:
        """Get task result through task id list.

        Parameters
        ----------
        task_id : list
            The list of task id you want to query.
        file_path : str
            If the parameter is not None, task result will be saved to target path.

        Returns
        -------
        list
            This list contasins several dicts of task id and task result.

        Examples
        --------
        This interface will return a list, however, this list will not necessarily contain all the tasks queried, 
        but will only return the results of the tasks that were queried to the completion of the calculation, 
        and if the save path is set, these results will also be saved to a file.
        
        >>> result_list = qm.get_task_list_result(task_id_list, 'D:/python_test/result/')
        >>> print(result_list)
        [{'task_id': '5D102BEED2714755B9B6AA082151F70E', 'task_result': ['{"key":["00","01","10","11"],"value":[0.25,0.25,0.25,0.25]}', '{"key":["00","01","10","11"],"value":[0.25,0.25,0.25,0.25]}']}, 
        {'task_id': '18C163284EE043CAA691B201A9091891', 'task_result': ['{"key":["00","01","10","11"],"value":[0.25,0.25,0.25,0.25]}', '{"key":["00","01","10","11"],"value":[0.25,0.25,0.25,0.25]}']}, 
        {'task_id': 'C929CE6E18374181A2E2297327CE6888', 'task_result': ['{"key":["00","01","10","11"],"value":[0.25,0.25,0.25,0.25]}', '{"key":["00","01","10","11"],"value":[0.25,0.25,0.25,0.25]}']}]


        """
        return_list = []
        for item in task_id:
            single_result = self.query_task_state(item, file_path)
            if single_result[0] == '3':
                return_list.append({'task_id' : item, 'task_result' : single_result[1]})

        return return_list    



    def parse_probability_result(self, result_str : list) -> list:
        """Parse async task probability result to a list contains dict.

        Parameters
        ----------
        result_str : str
            The json str contains task result key and value.

        Returns
        -------
        list

        Examples
        --------
        
        >>> result = qm.parse_probability_result(query_str)

        """
        return super().parse_probability_result(result_str)


    def quantum_chip_config_query(self, chip_ids : str) -> str:
        """Get quantum chip config
        
        Parameters
        ----------
        chip_ids : str
            the json str contains chip id, it must be int or array, -1 represents all chips

        Returns
        -------
        str
            return quantum chip configuration

        Examples
        --------
        >>> chipID_1 = {"ChipID":-1} 
        >>> chipID_2 = {"ChipID":[5,6,7]}
        >>> config_1 = qm.quantum_chip_config_query(chipID_1)
        >>> config_2 = qm.quantum_chip_config_query(chipID_2)
        >>> print(config_1)
        >>> print(config_2)
        
        """
        req_url = self.PilotURL + '/task/realQuantum/chip_config_query'
        req_str = json.dumps(chip_ids)
        
        resp =[]
        send_ok = self._send_request(req_url, req_str, resp)
        if not send_ok:
            print('Error: Send request failed!')
            exit(0)
        else:
            try:
                indent = '    '
                chip_config_query_result = str()
                parsed_data = json.loads(resp[0])
                result_len = len(parsed_data["configuration"])
                print("get {} chip configuration(s).".format(result_len))
                for i in range(result_len):
                    data_parsed = json.loads(parsed_data["configuration"][i]["data"])
                    chip_config_query_result = chip_config_query_result + "\n" + (
                        "configuration:\n"
                        + indent + "file: " + "\"" + parsed_data['configuration'][i]['file'] + "\"\n"
                        + indent + "data:\n" + indent + json.dumps(data_parsed, indent=4) + "\n"
                    )
                return chip_config_query_result
            except IndexError as e1:
                print("Cannot find configuration related to this chip ID")
                return resp[0]

        


    



