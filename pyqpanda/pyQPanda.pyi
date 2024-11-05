from typing import Any, Callable, ClassVar, Dict, Iterator, List, Optional, Tuple

from typing import Set
from typing import overload
import flags
import numpy
AGT_H: AnsatzGateType
AGT_RX: AnsatzGateType
AGT_RY: AnsatzGateType
AGT_RZ: AnsatzGateType
AGT_X: AnsatzGateType
ARBITRARY_ROTATION: SingleGateTransferType
BACKEND_CALC_ERROR: ErrorCode
BARRIER_GATE: GateType
CLUSTER_BASE: ErrorCode
CLUSTER_SIMULATE_CALC_ERR: ErrorCode
CNOT_GATE: LATEX_GATE_TYPE
CPHASE_GATE: GateType
CPU: BackendType
CPU_SINGLE_THREAD: BackendType
CP_GATE: GateType
CU_GATE: GateType
CZ_GATE: GateType
DATABASE_ERROR: ErrorCode
DOUBLE_BIT_GATE: DoubleGateTransferType
DOUBLE_CONTINUOUS: SingleGateTransferType
DOUBLE_DISCRETE: SingleGateTransferType
DOUBLE_GATE_INVALID: DoubleGateTransferType
ERR_BACKEND_CHIP_TASK_SOCKET_WRONG: ErrorCode
ERR_CHIP_OFFLINE: ErrorCode
ERR_EMPTY_PROG: ErrorCode
ERR_FIDELITY_MATRIX: ErrorCode
ERR_INVALID_URL: ErrorCode
ERR_MATE_GATE_CONFIG: ErrorCode
ERR_NOT_FOUND_APP_ID: ErrorCode
ERR_NOT_FOUND_TASK_ID: ErrorCode
ERR_OPERATOR_DB: ErrorCode
ERR_PARAMETER: ErrorCode
ERR_PARSER_SUB_TASK_RESULT: ErrorCode
ERR_PRE_ESTIMATE: ErrorCode
ERR_QCOMPILER_FAILED: ErrorCode
ERR_QPROG_LENGTH: ErrorCode
ERR_QST_PROG: ErrorCode
ERR_QUANTUM_CHIP_PROG: ErrorCode
ERR_QUBIT_SIZE: ErrorCode
ERR_QUBIT_TOPO: ErrorCode
ERR_QVM_INIT_FAILED: ErrorCode
ERR_REPEAT_MEASURE: ErrorCode
ERR_SCHEDULE_CHIP_TOPOLOGY_SUPPORTED: ErrorCode
ERR_SUB_GRAPH_OUT_OF_RANGE: ErrorCode
ERR_SYS_CALL_TIME_OUT: ErrorCode
ERR_TASK_BUF_OVERFLOW: ErrorCode
ERR_TASK_CONFIG: ErrorCode
ERR_TASK_STATUS_BUF_OVERFLOW: ErrorCode
ERR_TASK_TERMINATED: ErrorCode
ERR_TCP_INIT_FATLT: ErrorCode
ERR_TCP_SERVER_HALT: ErrorCode
ERR_UNKNOW_TASK_TYPE: ErrorCode
ERR_UNSUPPORT_BACKEND_TYPE: ErrorCode
EXCEED_MAX_CLOCK: ErrorCode
EXCEED_MAX_QUBIT: ErrorCode
GATE_NOP: GateType
GATE_UNDEFINED: GateType
GD_DIRECTION: UpdateMode
GD_VALUE: UpdateMode
GENERAL_GATE: LATEX_GATE_TYPE
GPU: BackendType
GRADIENT: OptimizerType
HADAMARD_GATE: GateType
ISWAP_GATE: GateType
ISWAP_THETA_GATE: GateType
I_GATE: GateType
JSON_FIELD_ERROR: ErrorCode
LINEAR: ComplexVertexSplitMethod
METHOD_UNDEFINED: ComplexVertexSplitMethod
MPS: BackendType
MS_GATE: GateType
NELDER_MEAD: OptimizerType
NOISE: BackendType
NO_ERROR_FOUND: ErrorCode
ORACLE_GATE: GateType
ORIGINIR_ERROR: ErrorCode
P00_GATE: GateType
P0_GATE: GateType
P11_GATE: GateType
P1_GATE: GateType
PAULI_X_GATE: GateType
PAULI_Y_GATE: GateType
PAULI_Z_GATE: GateType
PEC: em_method
POWELL: OptimizerType
P_GATE: GateType
READ_OUT: em_method
RING: ComplexVertexSplitMethod
RPHI_GATE: GateType
RXX_GATE: GateType
RX_GATE: GateType
RYY_GATE: GateType
RY_GATE: GateType
RZX_GATE: GateType
RZZ_GATE: GateType
RZ_GATE: GateType
SINGLE_CONTINUOUS_DISCRETE: SingleGateTransferType
SINGLE_GATE_INVALID: SingleGateTransferType
SQISWAP_GATE: GateType
SWAP_GATE: LATEX_GATE_TYPE
S_GATE: GateType
Simulation: ChipID
TOFFOLI_GATE: GateType
TWO_QUBIT_GATE: GateType
T_GATE: GateType
U1_GATE: GateType
U2_GATE: GateType
U3_GATE: GateType
U4_GATE: GateType
UNDEFINED_ERROR: ErrorCode
WUYUAN_1: ChipID
WUYUAN_2: ChipID
WUYUAN_3: ChipID
X_HALF_PI: GateType
Y_HALF_PI: GateType
ZNE: em_method
Z_HALF_PI: GateType
origin_72: real_chip_type
origin_wuyuan_d3: real_chip_type
origin_wuyuan_d4: real_chip_type
origin_wuyuan_d5: real_chip_type

class AbstractOptimizer:
    """
    quantum AbstractOptimizer class
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        """
        ...

    def exec(self) -> None:
        """
        Execute the optimization process.
        
        Args:
             None: This method takes no parameters.
        
        Returns:
             result: The result of the optimization process.
        """
        ...

    def getResult(self, *args, **kwargs) -> Any:
        """
        Retrieve the result of the last optimization.
        
        Args:
             None: This method takes no parameters.
        
        Returns:
             result: The result of the last optimization.
        """
        ...

    def registerFunc(self, arg0: Callable[[List[float],List[float],int,int],Tuple[str,float]], arg1: List[float]) -> None:
        """
        Register an optimization function.
        
        Args:
             func: The optimization function to be registered.
        
        Returns:
             None
        """
        ...

    def setAdaptive(self, arg0: bool) -> None:
        """
        Set whether the optimizer should use adaptive methods.
        
        Args:
             adaptive: A boolean indicating whether to enable adaptive optimization.
        
        Returns:
             None
        """
        ...

    def setCacheFile(self, arg0: str) -> None:
        """
        Set the path for the cache file used in optimization.
        
        Args:
             cache_file: A string representing the path to the cache file.
        
        Returns:
             None
        
        """
        ...

    def setDisp(self, arg0: bool) -> None:
        """
        Set the display flag for the optimizer.
        
        Args:
             disp: A boolean indicating whether to display optimization progress.
        
        Returns:
             None
        """
        ...

    def setFatol(self, arg0: float) -> None:
        """
        Set the function absolute tolerance for optimization.
        
        Args:
             fatol: The function absolute tolerance value to be set.
        
        Returns:
             None
        """
        ...

    def setMaxFCalls(self, arg0: int) -> None:
        """
        Set the maximum number of function calls allowed during optimization.
        
        Args:
             max_calls: The maximum number of function calls to be set.
        
        Returns:
             None
        """
        ...

    def setMaxIter(self, arg0: int) -> None:
        """
        Set the maximum number of iterations allowed during optimization.
        
        Args:
             max_iter: The maximum number of iterations to be set.
        
        Returns:
             None
        """
        ...

    def setRestoreFromCacheFile(self, arg0: bool) -> None:
        """
        Set whether to restore the optimization state from a cache file.
        Args:
        
             cache_file: A string representing the path to the cache file.
        
        Returns:
             None
        
        """
        ...

    def setXatol(self, arg0: float) -> None:
        """
        Set the absolute tolerance for optimization.
        
        Args:
             atol: The absolute tolerance value to be set.
        
        Returns:
             None
        """
        ...


class AdaGradOptimizer:
    """
    variational quantum AdaGradOptimizer
    """
    def __init__(self, arg0: var, arg1: float, arg2: float, arg3: float) -> None:
        """
        """
        ...

    def get_loss(self) -> float:
        """
        """
        ...

    def get_variables(self) -> List[var]:
        """
        """
        ...

    def minimize(self, arg0: float, arg1: float, arg2: float) -> Optimizer:
        """
        """
        ...

    def run(self, arg0: List[var], arg1: int) -> bool:
        """
        """
        ...


class AdamOptimizer:
    """
    variational quantum AdamOptimizer
    """
    def __init__(self, arg0: var, arg1: float, arg2: float, arg3: float, arg4: float) -> None:
        """
        """
        ...

    def get_loss(self) -> float:
        """
        """
        ...

    def get_variables(self) -> List[var]:
        """
        """
        ...

    def minimize(self, arg0: float, arg1: float, arg2: float, arg3: float) -> Optimizer:
        """
        """
        ...

    def run(self, arg0: List[var], arg1: int) -> bool:
        """
        """
        ...


class Ansatz:
    """
    quantum ansatz class
    """
    @overload
    def __init__(self) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: QGate) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: AnsatzGate) -> None:
        """
        """
        ...

    @overload
    def __init__(self, ansatz: List[AnsatzGate], thetas: List[float] = []) -> None:
        """
        """
        ...

    @overload
    def __init__(self, ansatz_circuit: Ansatz, thetas: List[float] = []) -> None:
        """
        """
        ...

    @overload
    def __init__(self, circuit: QCircuit, thetas: List[float] = []) -> None:
        """
        """
        ...

    def get_ansatz_list(self) -> List[AnsatzGate]:
        """
        """
        ...

    def get_thetas_list(self) -> List[float]:
        """
        """
        ...

    @overload
    def insert(self, gate: QGate) -> None:
        """
        """
        ...

    @overload
    def insert(self, gate: AnsatzGate) -> None:
        """
        """
        ...

    @overload
    def insert(self, gate: List[AnsatzGate]) -> None:
        """
        """
        ...

    @overload
    def insert(self, gate: QCircuit) -> None:
        """
        """
        ...

    @overload
    def insert(self, gate: Ansatz, thetas: List[float] = []) -> None:
        """
        """
        ...

    def set_thetas(self, thetas: List[float]) -> None:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: QGate) -> Ansatz:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: List[AnsatzGate]) -> Ansatz:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: QCircuit) -> Ansatz:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: AnsatzGate) -> Ansatz:
        """
        """
        ...


class AnsatzGate:
    """
    ansatz gate struct
    """
    control: int
    target: int
    theta: float
    type: AnsatzGateType
    @overload
    def __init__(self, arg0: AnsatzGateType, arg1: int) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: AnsatzGateType, arg1: int, arg2: float) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: AnsatzGateType, arg1: int, arg2: float, arg3: int) -> None:
        """
        """
        ...


class AnsatzGateType:
    """
    Quantum ansatz gate type
    
    Members:
    
      AGT_X
    
      AGT_H
    
      AGT_RX
    
      AGT_RY
    
      AGT_RZ
    """
    __members__: ClassVar[dict] = ...  # read-only
    AGT_H: ClassVar[AnsatzGateType] = ...
    AGT_RX: ClassVar[AnsatzGateType] = ...
    AGT_RY: ClassVar[AnsatzGateType] = ...
    AGT_RZ: ClassVar[AnsatzGateType] = ...
    AGT_X: ClassVar[AnsatzGateType] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None:
        """
        """
        ...

    def __eq__(self, other: object) -> bool:
        """
        """
        ...

    def __getstate__(self) -> int:
        """
        """
        ...

    def __hash__(self) -> int:
        """
        """
        ...

    def __index__(self) -> int:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other: object) -> bool:
        """
        """
        ...

    def __setstate__(self, state: int) -> None:
        """
        """
        ...

    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class BackendType:
    """
    Quantum machine backend type
    
    Members:
    
      CPU
    
      GPU
    
      CPU_SINGLE_THREAD
    
      NOISE
    
      MPS
    """
    __members__: ClassVar[dict] = ...  # read-only
    CPU: ClassVar[BackendType] = ...
    CPU_SINGLE_THREAD: ClassVar[BackendType] = ...
    GPU: ClassVar[BackendType] = ...
    MPS: ClassVar[BackendType] = ...
    NOISE: ClassVar[BackendType] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None:
        """
        """
        ...

    def __eq__(self, other: object) -> bool:
        """
        """
        ...

    def __getstate__(self) -> int:
        """
        """
        ...

    def __hash__(self) -> int:
        """
        """
        ...

    def __index__(self) -> int:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other: object) -> bool:
        """
        """
        ...

    def __setstate__(self, state: int) -> None:
        """
        """
        ...

    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class CBit:
    """
    quantum classical bit
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        """
        ...

    def getName(self) -> str:
        """
        Retrieve the name of the classical bit.
        
        Args:
             None
        
        Returns:
             The name of the CBit as a string.
        
        """
        ...


class CPUQVM(QuantumMachine):
    """
    quantum machine cpu
    """
    def __init__(self) -> None:
        """
        """
        ...

    def get_prob_dict(self, qubit_list: QVec, select_max: int = -1) -> Dict[str,float]:
        """
        Get a dictionary of probabilities for the specified qubits.
        
        Args:
             qubit_list: List of qubits to measure.
        
             select_max: int, optional, maximum number of entries to return (default: -1).
        
        Returns:
             Dictionary of probabilities as a reference.
        
        """
        ...

    def get_prob_list(self, qubit_list: QVec, select_max: int = -1) -> List[float]:
        """
        Get a list of probabilities for the specified qubits.
        
        Args:
             qubit_list: List of qubits to measure.
        
             select_max: int, optional, maximum number of probabilities to return (default: -1).
        
        Returns:
             List of probabilities as a reference.
        
        """
        ...

    def get_prob_tuple_list(self, qubit_list: QVec, select_max: int = -1) -> List[Tuple[int,float]]:
        """
        Get a list of probability tuples for the specified qubits.
        
        Args:
             qubit_list: List of qubits to measure.
        
             select_max: int, optional, maximum number of tuples to return (default: -1).
        
        Returns:
             List of probability tuples as a reference.
        
        """
        ...

    @overload
    def init_qvm(self, arg0: bool) -> None:
        """
        Initialize the Quantum Virtual Machine (QVM).
        
        This function sets up the QVM for execution. The initialization can
        
        include options such as enabling or disabling logging for debugging.
        
        Args:
             enable_logging: A boolean flag to enable logging during the execution.
        
        Returns:
             None.
        
        
        """
        ...

    @overload
    def init_qvm(self) -> None:
        """
        Initialize the quantum virtual machine (QVM).
        
        This method sets up the necessary environment for the QVM to execute quantum programs.
        
        Returns:
             None: This method does not return a value.
        
        """
        ...

    def pmeasure(self, qubit_list: QVec, select_max: int = -1) -> List[Tuple[int,float]]:
        """
        Get the probability distribution over qubits.
        
        Args:
             qubit_list: List of qubits to measure.
        
             select_max: int, optional, maximum number of results to select (default: -1).
        
        Returns:
             Probability distribution as a reference.
        
        """
        ...

    def pmeasure_no_index(self, qubit_list: QVec) -> List[float]:
        """
        Get the probability distribution over qubits without index.
        
        Args:
             qubit_list: List of qubits to measure.
        
        Returns:
             Probability distribution as a reference.
        
        """
        ...

    @overload
    def prob_run_dict(self, program: QProg, qubit_list: QVec, select_max: int = -1) -> Dict[str,float]:
        """
        Execute a quantum program and retrieve a dictionary of probabilities for the specified qubits.
        
        Args:
             program: The quantum program to execute.
        
             qubit_list: List of qubits to measure.
        
             select_max: int, optional, maximum number of entries in the dictionary to return (default: -1).
        
        Returns:
             Dictionary of probabilities.
        
        
        """
        ...

    @overload
    def prob_run_dict(self, program: QProg, qubit_addr_list: List[int], select_max: int = -1) -> Dict[str,float]:
        """
        Execute a quantum program and retrieve a dictionary of probabilities using qubit addresses.
        
        Args:
             program: The quantum program to execute.
        
             qubit_addr_list: List of qubit addresses to measure.
        
             select_max: int, optional, maximum number of entries in the dictionary to return (default: -1).
        
        Returns:
             Dictionary of probabilities.
        
        """
        ...

    @overload
    def prob_run_list(self, program: QProg, qubit_list: QVec, select_max: int = -1) -> List[float]:
        """
        Execute a quantum program and retrieve a list of probabilities for the specified qubits.
        
        Args:
             program: The quantum program to execute.
        
             qubit_list: List of qubits to measure.
        
             select_max: int, optional, maximum number of probabilities to return (default: -1).
        
        Returns:
             List of probabilities.
        
        
        """
        ...

    @overload
    def prob_run_list(self, program: QProg, qubit_addr_list: List[int], select_max: int = -1) -> List[float]:
        """
        Execute a quantum program and retrieve a list of probabilities using qubit addresses.
        
        Args:
             program: The quantum program to execute.
        
             qubit_addr_list: List of qubit addresses to measure.
        
             select_max: int, optional, maximum number of probabilities to return (default: -1).
        
        Returns:
             List of probabilities.
        
        """
        ...

    @overload
    def prob_run_tuple_list(self, program: QProg, qubit_list: QVec, select_max: int = -1) -> List[Tuple[int,float]]:
        """
        Execute a quantum program and get a list of probability tuples.
        
        Args:
             program: The quantum program to execute.
        
             qubit_list: List of qubits to measure.
        
             select_max: int, optional, maximum number of tuples to return (default: -1).
        
        Returns:
             List of probability tuples.
        
        
        """
        ...

    @overload
    def prob_run_tuple_list(self, program: QProg, qubit_addr_list: List[int], select_max: int = -1) -> List[Tuple[int,float]]:
        """
        Execute a quantum program and get a list of probability tuples using qubit addresses.
        
        Args:
             program: The quantum program to execute.
        
             qubit_addr_list: List of qubit addresses to measure.
        
             select_max: int, optional, maximum number of tuples to return (default: -1).
        
        Returns:
             List of probability tuples.
        
        """
        ...

    def quick_measure(self, qubit_list: QVec, shots: int) -> Dict[str,int]:
        """
        Perform a quick measurement on the specified qubits.
        
        Args:
             qubit_list: List of qubits to measure.
        
             shots: Number of measurement shots to perform.
        
        Returns:
             Reference to the measurement results.
        
        """
        ...

    def set_max_threads(self, size: int) -> None:
        """
        Set the maximum number of threads for the CPU quantum virtual machine (QVM).
        
        Args:
             size: The maximum number of threads to use.
        
        Returns:
             None: This method does not return a value.
        
        """
        ...


class CPUSingleThreadQVM(QuantumMachine):
    """
    quantum machine class for cpu single thread
    """
    def __init__(self) -> None:
        """
        """
        ...

    def get_prob_dict(self, qubit_list: QVec, select_max: int = -1) -> Dict[str,float]:
        """
        Get a dictionary of probabilities for the specified qubits.
        
        Args:
             qubit_list: List of qubits to measure.
        
             select_max: int, optional, maximum number of entries to return (default: -1).
        
        Returns:
             Dictionary of probabilities as a reference.
        
        """
        ...

    def get_prob_list(self, qubit_list: QVec, select_max: int = -1) -> List[float]:
        """
        Get a list of probabilities for the specified qubits.
        
        Args:
             qubit_list: List of qubits to measure.
        
             select_max: int, optional, maximum number of probabilities to return (default: -1).
        
        Returns:
             List of probabilities as a reference.
        
        """
        ...

    def get_prob_tuple_list(self, qubit_list: QVec, select_max: int = -1) -> List[Tuple[int,float]]:
        """
        Get a list of probability tuples for the specified qubits.
        
        Args:
             qubit_list: List of qubits to measure.
        
             select_max: int, optional, maximum number of tuples to return (default: -1).
        
        Returns:
             List of probability tuples as a reference.
        
        """
        ...

    def pmeasure(self, qubit_list: QVec, select_max: int = -1) -> List[Tuple[int,float]]:
        """
        Get the probability distribution over qubits.
        
        Args:
             qubit_list: List of qubits to measure.
        
             select_max: int, optional, maximum number of results to select (default: -1).
        
        Returns:
             Probability distribution as a reference.
        
        """
        ...

    def pmeasure_no_index(self, qubit_list: QVec) -> List[float]:
        """
        Get the probability distribution over qubits without index.
        
        Args:
             qubit_list: List of qubits to measure.
        
        Returns:
             Probability distribution as a reference.
        
        """
        ...

    @overload
    def prob_run_dict(self, program: QProg, qubit_list: QVec, select_max: int = -1) -> Dict[str,float]:
        """
        Execute a quantum program and retrieve a dictionary of probabilities for the specified qubits.
        
        Args:
             program: The quantum program to execute.
        
             qubit_list: List of qubits to measure.
        
             select_max: int, optional, maximum number of entries in the dictionary to return (default: -1).
        
        Returns:
             Dictionary of probabilities.
        
        
        """
        ...

    @overload
    def prob_run_dict(self, program: QProg, qubit_addr_list: List[int], select_max: int = -1) -> Dict[str,float]:
        """
        Execute a quantum program and retrieve a dictionary of probabilities using qubit addresses.
        
        Args:
             program: The quantum program to execute.
        
             qubit_addr_list: List of qubit addresses to measure.
        
             select_max: int, optional, maximum number of entries in the dictionary to return (default: -1).
        
        Returns:
             Dictionary of probabilities.
        
        """
        ...

    @overload
    def prob_run_list(self, program: QProg, qubit_list: QVec, select_max: int = -1) -> List[float]:
        """
        Execute a quantum program and retrieve a list of probabilities for the specified qubits.
        
        Args:
             program: The quantum program to execute.
        
             qubit_list: List of qubits to measure.
        
             select_max: int, optional, maximum number of probabilities to return (default: -1).
        
        Returns:
             List of probabilities.
        
        
        """
        ...

    @overload
    def prob_run_list(self, program: QProg, qubit_addr_list: List[int], select_max: int = -1) -> List[float]:
        """
        Execute a quantum program and retrieve a list of probabilities using qubit addresses.
        
        Args:
             program: The quantum program to execute.
        
             qubit_addr_list: List of qubit addresses to measure.
        
             select_max: int, optional, maximum number of probabilities to return (default: -1).
        
        Returns:
             List of probabilities.
        
        """
        ...

    @overload
    def prob_run_tuple_list(self, program: QProg, qubit_list: QVec, select_max: int = -1) -> List[Tuple[int,float]]:
        """
        Execute a quantum program and get a list of probability tuples.
        
        Args:
             program: The quantum program to execute.
        
             qubit_list: List of qubits to measure.
        
             select_max: int, optional, maximum number of tuples to return (default: -1).
        
        Returns:
             List of probability tuples.
        
        
        """
        ...

    @overload
    def prob_run_tuple_list(self, program: QProg, qubit_addr_list: List[int], select_max: int = -1) -> List[Tuple[int,float]]:
        """
        Execute a quantum program and get a list of probability tuples using qubit addresses.
        
        Args:
             program: The quantum program to execute.
        
             qubit_addr_list: List of qubit addresses to measure.
        
             select_max: int, optional, maximum number of tuples to return (default: -1).
        
        Returns:
             List of probability tuples.
        
        """
        ...

    def quick_measure(self, qubit_list: QVec, shots: int) -> Dict[str,int]:
        """
        Perform a quick measurement on the specified qubits.
        
        Args:
             qubit_list: List of qubits to measure.
        
             shots: Number of measurement shots to perform.
        
        Returns:
             Reference to the measurement results.
        
        """
        ...


class ChipID:
    """
    origin quantum real chip type
    
    Members:
    
      Simulation
    
      WUYUAN_1
    
      WUYUAN_2
    
      WUYUAN_3
    """
    __members__: ClassVar[dict] = ...  # read-only
    Simulation: ClassVar[ChipID] = ...
    WUYUAN_1: ClassVar[ChipID] = ...
    WUYUAN_2: ClassVar[ChipID] = ...
    WUYUAN_3: ClassVar[ChipID] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None:
        """
        """
        ...

    def __eq__(self, other: object) -> bool:
        """
        """
        ...

    def __getstate__(self) -> int:
        """
        """
        ...

    def __hash__(self) -> int:
        """
        """
        ...

    def __index__(self) -> int:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other: object) -> bool:
        """
        """
        ...

    def __setstate__(self, state: int) -> None:
        """
        """
        ...

    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class ClassicalCondition:
    """
    Classical condition class  Proxy class of cexpr class
    """
    __hash__: ClassVar[None] = ...
    def __init__(self, *args, **kwargs) -> None:
        """
        """
        ...

    @overload
    def c_and(self, arg0: int) -> ClassicalCondition:
        """
        Perform a logical AND operation with a classical bit.
        
        Args:
             cbit: The classical bit size to perform AND with.
        
        Returns:
             The result of the AND operation.
        
        
        """
        ...

    @overload
    def c_and(self, arg0: ClassicalCondition) -> ClassicalCondition:
        """
        Perform a logical AND operation with another ClassicalCondition.
        
        Args:
             other: Another ClassicalCondition to perform AND with.
        
        Returns:
             The result of the AND operation.
        
        """
        ...

    def c_not(self) -> ClassicalCondition:
        """
        Perform a logical NOT operation on the classical condition.
        
        Args:
             None
        
        Returns:
             The result of the NOT operation.
        
        """
        ...

    @overload
    def c_or(self, arg0: int) -> ClassicalCondition:
        """
        Perform a logical OR operation with a classical bit.
        
        Args:
             cbit: The classical bit size to perform OR with.
        
        Returns:
             The result of the OR operation.
        
        
        """
        ...

    @overload
    def c_or(self, arg0: ClassicalCondition) -> ClassicalCondition:
        """
        Perform a logical OR operation with another ClassicalCondition.
        
        Args:
             other: Another ClassicalCondition to perform OR with.
        
        Returns:
             The result of the OR operation.
        
        """
        ...

    def get_val(self) -> int:
        """
        Retrieve the current value of the classical condition.
        
        Args:
             None
        
        Returns:
             The value of the ClassicalCondition.
        
        """
        ...

    def set_val(self, arg0: int) -> None:
        """
        Set a new value for the classical condition.
        
        Args:
             value: The new value to set.
        
        Returns:
             None
        
        """
        ...

    @overload
    def __add__(self, arg0: ClassicalCondition) -> ClassicalCondition:
        """
        """
        ...

    @overload
    def __add__(self, arg0: int) -> ClassicalCondition:
        """
        """
        ...

    @overload
    def __eq__(self, arg0: ClassicalCondition) -> ClassicalCondition:
        """
        """
        ...

    @overload
    def __eq__(self, arg0: int) -> ClassicalCondition:
        """
        """
        ...

    @overload
    def __eq__(self, arg0: int) -> ClassicalCondition:
        """
        """
        ...

    @overload
    def __ge__(self, arg0: int) -> ClassicalCondition:
        """
        """
        ...

    @overload
    def __ge__(self, arg0: ClassicalCondition) -> ClassicalCondition:
        """
        """
        ...

    @overload
    def __ge__(self, arg0: int) -> ClassicalCondition:
        """
        """
        ...

    @overload
    def __gt__(self, arg0: int) -> ClassicalCondition:
        """
        """
        ...

    @overload
    def __gt__(self, arg0: ClassicalCondition) -> ClassicalCondition:
        """
        """
        ...

    @overload
    def __gt__(self, arg0: int) -> ClassicalCondition:
        """
        """
        ...

    @overload
    def __le__(self, arg0: ClassicalCondition) -> ClassicalCondition:
        """
        """
        ...

    @overload
    def __le__(self, arg0: int) -> ClassicalCondition:
        """
        """
        ...

    @overload
    def __le__(self, arg0: int) -> ClassicalCondition:
        """
        """
        ...

    @overload
    def __lt__(self, arg0: ClassicalCondition) -> ClassicalCondition:
        """
        """
        ...

    @overload
    def __lt__(self, arg0: int) -> ClassicalCondition:
        """
        """
        ...

    @overload
    def __lt__(self, arg0: int) -> ClassicalCondition:
        """
        """
        ...

    @overload
    def __mul__(self, arg0: ClassicalCondition) -> ClassicalCondition:
        """
        """
        ...

    @overload
    def __mul__(self, arg0: int) -> ClassicalCondition:
        """
        """
        ...

    def __radd__(self, arg0: int) -> ClassicalCondition:
        """
        """
        ...

    def __rmul__(self, arg0: int) -> ClassicalCondition:
        """
        """
        ...

    def __rsub__(self, arg0: int) -> ClassicalCondition:
        """
        """
        ...

    def __rtruediv__(self, arg0: int) -> ClassicalCondition:
        """
        """
        ...

    @overload
    def __sub__(self, arg0: ClassicalCondition) -> ClassicalCondition:
        """
        """
        ...

    @overload
    def __sub__(self, arg0: int) -> ClassicalCondition:
        """
        """
        ...

    @overload
    def __truediv__(self, arg0: ClassicalCondition) -> ClassicalCondition:
        """
        """
        ...

    @overload
    def __truediv__(self, arg0: int) -> ClassicalCondition:
        """
        """
        ...


class ClassicalProg:
    """
    quantum ClassicalProg
    """
    def __init__(self, arg0: ClassicalCondition) -> None:
        """
        """
        ...


class CommProtocolConfig:
    """
    """
    circuits_num: int
    open_error_mitigation: bool
    open_mapping: bool
    optimization_level: int
    shots: int
    def __init__(self) -> None:
        """
        """
        ...


class ComplexVertexSplitMethod:
    """
    quantum complex vertex split method
    
    Members:
    
      METHOD_UNDEFINED
    
      LINEAR
    
      RING
    """
    __members__: ClassVar[dict] = ...  # read-only
    LINEAR: ClassVar[ComplexVertexSplitMethod] = ...
    METHOD_UNDEFINED: ClassVar[ComplexVertexSplitMethod] = ...
    RING: ClassVar[ComplexVertexSplitMethod] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None:
        """
        """
        ...

    def __eq__(self, other: object) -> bool:
        """
        """
        ...

    def __getstate__(self) -> int:
        """
        """
        ...

    def __hash__(self) -> int:
        """
        """
        ...

    def __index__(self) -> int:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other: object) -> bool:
        """
        """
        ...

    def __setstate__(self, state: int) -> None:
        """
        """
        ...

    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class DAGNodeType:
    """
    Quantum dag node type
    
    Members:
    
      NUKNOW_SEQ_NODE_TYPE
    
      MAX_GATE_TYPE
    
      MEASURE
    
      QUBIT
    
      RESET
    """
    __members__: ClassVar[dict] = ...  # read-only
    MAX_GATE_TYPE: ClassVar[DAGNodeType] = ...
    MEASURE: ClassVar[DAGNodeType] = ...
    NUKNOW_SEQ_NODE_TYPE: ClassVar[DAGNodeType] = ...
    QUBIT: ClassVar[DAGNodeType] = ...
    RESET: ClassVar[DAGNodeType] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None:
        """
        """
        ...

    def __eq__(self, other: object) -> bool:
        """
        """
        ...

    def __getstate__(self) -> int:
        """
        """
        ...

    def __hash__(self) -> int:
        """
        """
        ...

    def __index__(self) -> int:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other: object) -> bool:
        """
        """
        ...

    def __setstate__(self, state: int) -> None:
        """
        """
        ...

    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class DecompositionMode:
    """
    Quantum matrix decomposition mode
    
    Members:
    
      QR
    
      HOUSEHOLDER_QR
    
      QSDecomposition
    
      CSDecomposition
    """
    __members__: ClassVar[dict] = ...  # read-only
    CSDecomposition: ClassVar[DecompositionMode] = ...
    HOUSEHOLDER_QR: ClassVar[DecompositionMode] = ...
    QR: ClassVar[DecompositionMode] = ...
    QSDecomposition: ClassVar[DecompositionMode] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None:
        """
        """
        ...

    def __eq__(self, other: object) -> bool:
        """
        """
        ...

    def __getstate__(self) -> int:
        """
        """
        ...

    def __hash__(self) -> int:
        """
        """
        ...

    def __index__(self) -> int:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other: object) -> bool:
        """
        """
        ...

    def __setstate__(self, state: int) -> None:
        """
        """
        ...

    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class DensityMatrixSimulator(QuantumMachine):
    """
    simulator for density matrix
    """
    def __init__(self) -> None:
        """
        """
        ...

    def get_density_matrix(self, prog: QProg) -> numpy.ndarray[numpy.complex128[m,n]]:
        """
        Run quantum program and get the full density matrix.
        
        Args:
             prog: The quantum program to execute.
        
        Returns:
             The full density matrix.
        
        """
        ...

    @overload
    def get_expectation(self, prog: QProg, hamiltonian: List[Tuple[Dict[int,str],float]], qubits: QVec) -> float:
        """
        Run the quantum program and calculate the Hamiltonian expectation for the specified qubits.
        
        Args:
             prog: The quantum program to execute.
        
             hamiltonian: The QHamiltonian to use for the expectation value.
        
             qubits: The selected qubits for measurement.
        
        Returns:
             The Hamiltonian expectation for the specified qubits.
        
        
        """
        ...

    @overload
    def get_expectation(self, prog: QProg, hamiltonian: List[Tuple[Dict[int,str],float]], qubits: List[int]) -> float:
        """
        Run the quantum program and calculate the Hamiltonian expectation for the specified qubits.
        
        Args:
             prog: The quantum program to execute.
        
             hamiltonian: The QHamiltonian to use for the expectation value.
        
             qubits: The selected qubits for measurement.
        
        Returns:
             The Hamiltonian expectation for the specified qubits.
        
        """
        ...

    @overload
    def get_probabilities(self, prog: QProg) -> List[float]:
        """
        Run the quantum program and get the probabilities for all indices.
        
        Args:
             prog: The quantum program to execute.
        
        Returns:
             The probabilities result of the quantum program.
        
        
        """
        ...

    @overload
    def get_probabilities(self, prog: QProg, qubits: QVec) -> List[float]:
        """
        Run the quantum program and get the probabilities for all indices for the specified qubits.
        
        Args:
             prog: The quantum program to execute.
        
             qubits: The selected qubits for measurement.
        
        Returns:
             The probabilities result of the quantum program.
        
        
        """
        ...

    @overload
    def get_probabilities(self, prog: QProg, qubits: List[int]) -> List[float]:
        """
        Run the quantum program and get the probabilities for all indices for the specified qubits.
        
        Args:
             prog: The quantum program to execute.
        
             qubits: The selected qubits for measurement.
        
        Returns:
             The probabilities result of the quantum program.
        
        
        """
        ...

    @overload
    def get_probabilities(self, prog: QProg, indices: List[str]) -> List[float]:
        """
        Run the quantum program and get the probabilities for the specified binary indices.
        
        Args:
             prog: The quantum program to execute.
        
             indices: The selected binary indices for measurement.
        
        Returns:
             The probabilities result of the quantum program.
        
        """
        ...

    @overload
    def get_probability(self, prog: QProg, index: int) -> float:
        """
        Run the quantum program and get the probability for the specified index.
        
        Args:
             prog: The quantum program to execute.
        
             index: The measurement index in [0, 2^N      1].
        
        Returns:
             The probability result of the quantum program.
        
        
        """
        ...

    @overload
    def get_probability(self, prog: QProg, index: str) -> float:
        """
        Run the quantum program and get the probability for the specified index.
        
        Args:
             prog: The quantum program to execute.
        
             index: The measurement index in [0, 2^N      1].
        
        Returns:
             The probability result of the quantum program.
        """
        ...

    @overload
    def get_reduced_density_matrix(self, prog: QProg, qubits: QVec) -> numpy.ndarray[numpy.complex128[m,n]]:
        """
        Run quantum program and get the density matrix for current qubits.
        
        Args:
             prog: The quantum program to execute.
        
             qubits: The selected qubits from the quantum program.
        
        Returns:
             The density matrix for the specified qubits.
        
        
        """
        ...

    @overload
    def get_reduced_density_matrix(self, prog: QProg, qubits: List[int]) -> numpy.ndarray[numpy.complex128[m,n]]:
        """
        Run quantum program and get the density matrix for current qubits.
        
        Args:
             prog: The quantum program to execute.
        
             qubits: The selected qubits from the quantum program.
        
        Returns:
             The density matrix for the specified qubits.
        
        """
        ...

    def init_qvm(self, is_double_precision: bool = True) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: numpy.ndarray[numpy.complex128[m,n]]) -> None:
        """
        Set the noise model for the density matrix simulator.
        
        Args:
             noise_model: The noise model represented as a complex matrix.
        
        Returns:
             None.
        
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: numpy.ndarray[numpy.complex128[m,n]], arg1: List[GateType]) -> None:
        """
        Set the noise model for the density matrix simulator with specific gate types.
        
        Args:
             noise_model: The noise model represented as a complex matrix.
        
             gate_types: A vector of gate types to which the noise model applies.
        
        Returns:
             None.
        
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: List[numpy.ndarray[numpy.complex128[m,n]]]) -> None:
        """
        Set multiple noise models for the density matrix simulator.
        
        Args:
             noise_models: A vector of noise models, each represented as a complex matrix.
        
        Returns:
             None.
        
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: List[numpy.ndarray[numpy.complex128[m,n]]], arg1: List[GateType]) -> None:
        """
        Set multiple noise models for the density matrix simulator with specific gate types.
        
        Args:
             noise_models: A vector of noise models, each represented as a complex matrix.
        
             gate_types: A vector of gate types to which the noise models apply.
        
        Returns:
             None.
        
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float) -> None:
        """
        Set a specific noise model for the density matrix simulator with a given gate type and probability.
        
        Args:
             noise_model: The noise model to apply.
        
             gate_type: The specific gate type associated with the noise model.
        
             probability: The probability of the noise occurring.
        
        Returns:
             None.
        
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: List[GateType], arg2: float) -> None:
        """
        Set a specific noise model for the density matrix simulator with multiple gate types and a given probability.
        
        Args:
             noise_model: The noise model to apply.
        
             gate_types: A vector of gate types associated with the noise model.
        
             probability: The probability of the noise occurring.
        
        Returns:
             None.
        
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float, arg3: QVec) -> None:
        """
        Set a specific noise model for the density matrix simulator with a given gate type, probability, and target qubits.
        
        Args:
             noise_model: The noise model to apply.
        
             gate_type: The specific gate type associated with the noise model.
        
             probability: The probability of the noise occurring.
        
             qubits: The target qubits affected by the noise model.
        
        Returns:
             None.
        
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: List[GateType], arg2: float, arg3: QVec) -> None:
        """
        Set a specific noise model for the density matrix simulator with multiple gate types, a given probability, and target qubits.
        
        Args:
             noise_model: The noise model to apply.
        
             gate_types: A vector of gate types associated with the noise model.
        
             probability: The probability of the noise occurring.
        
             qubits: The target qubits affected by the noise model.
        
        Returns:
             None.
        
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float, arg3: List[QVec]) -> None:
        """
        Set a specific noise model for the density matrix simulator with a given gate type, probability, and groups of target qubits.
        
        Args:
             noise_model: The noise model to apply.
        
             gate_type: The specific gate type associated with the noise model.
        
             probability: The probability of the noise occurring.
        
             qubit_groups: A vector of QVecs representing groups of target qubits affected by the noise model.
        
        Returns:
             None.
        
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float, arg3: float, arg4: float) -> None:
        """
        Set a specific noise model for the density matrix simulator with a given gate type, probability, duration, and temperature.
        
        Args:
             noise_model: The noise model to apply.
        
             gate_type: The specific gate type associated with the noise model.
        
             probability: The probability of the noise occurring.
        
             duration: The duration for which the noise model is applied.
        
             temperature: The temperature affecting the noise characteristics.
        
        Returns:
             None.
        
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: List[GateType], arg2: float, arg3: float, arg4: float) -> None:
        """
        Set a specific noise model for the density matrix simulator with multiple gate types, a given probability, duration, and temperature.
        
        Args:
             noise_model: The noise model to apply.
        
             gate_types: A vector of gate types associated with the noise model.
        
             probability: The probability of the noise occurring.
        
             duration: The duration for which the noise model is applied.
        
             temperature: The temperature affecting the noise characteristics.
        
        Returns:
             None.
        
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float, arg3: float, arg4: float, arg5: QVec) -> None:
        """
        Set a specific noise model for the density matrix simulator with a given gate type, probability, duration, temperature, and a target qubit.
        
        Args:
             noise_model: The noise model to apply.
        
             gate_type: The specific gate type associated with the noise model.
        
             probability: The probability of the noise occurring.
        
             duration: The duration for which the noise model is applied.
        
             temperature: The temperature affecting the noise characteristics.
        
             target_qubit: The specific qubit targeted by the noise model.
        
        Returns:
             None.
        
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: List[GateType], arg2: float, arg3: float, arg4: float, arg5: QVec) -> None:
        """
        Set a specific noise model for the density matrix simulator with multiple gate types, probability, duration, temperature, and a target qubit.
        
        Args:
             noise_model: The noise model to apply.
        
             gate_types: A vector of gate types associated with the noise model.
        
             probability: The probability of the noise occurring.
        
             duration: The duration for which the noise model is applied.
        
             temperature: The temperature affecting the noise characteristics.
        
             target_qubit: The specific qubit targeted by the noise model.
        
        Returns:
             None.
        
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float, arg3: float, arg4: float, arg5: List[QVec]) -> None:
        """
        Set a specific noise model for the density matrix simulator with a given gate type, probability, duration, temperature, and multiple target qubits.
        
        Args:
             noise_model: The noise model to apply.
        
             gate_type: The specific gate type associated with the noise model.
        
             probability: The probability of the noise occurring.
        
             duration: The duration for which the noise model is applied.
        
             temperature: The temperature affecting the noise characteristics.
        
             target_qubits: A vector of qubits targeted by the noise model.
        
        Returns:
             None.
        
        """
        ...


class DoubleGateTransferType:
    """
    Quantum double gate transfer type
    
    Members:
    
      DOUBLE_GATE_INVALID
    
      DOUBLE_BIT_GATE
    """
    __members__: ClassVar[dict] = ...  # read-only
    DOUBLE_BIT_GATE: ClassVar[DoubleGateTransferType] = ...
    DOUBLE_GATE_INVALID: ClassVar[DoubleGateTransferType] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None:
        """
        """
        ...

    def __eq__(self, other: object) -> bool:
        """
        """
        ...

    def __getstate__(self) -> int:
        """
        """
        ...

    def __hash__(self) -> int:
        """
        """
        ...

    def __index__(self) -> int:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other: object) -> bool:
        """
        """
        ...

    def __setstate__(self, state: int) -> None:
        """
        """
        ...

    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class Encode:
    """
    quantum amplitude encode
    """
    def __init__(self) -> None:
        """
        """
        ...

    @overload
    def amplitude_encode(self, qubit: QVec, data: List[float]) -> None:
        """
        Perform amplitude encoding on the given qubits.
        
        Args:
             qubit: The quantum vector to be encoded.
        
             data: The classical data to be encoded.
        
        Returns:
             An encoded quantum state.
        
        
        """
        ...

    @overload
    def amplitude_encode(self, qubit: QVec, data: List[complex]) -> None:
        """
        Perform amplitude encoding using complex numbers on the given qubits.
        
        Args:
             qubit: The quantum vector to be encoded.
        
             data: The classical complex data to be encoded.
        
        Returns:
             An encoded quantum state.
        
        """
        ...

    @overload
    def amplitude_encode_recursive(self, qubit: QVec, data: List[float]) -> None:
        """
        Perform recursive amplitude encoding on the given qubits.
        
        Args:
             qubit: The quantum vector to be encoded.
        
             data: The classical data to be encoded.
        
        Returns:
             An encoded quantum state.
        
        
        """
        ...

    @overload
    def amplitude_encode_recursive(self, qubit: QVec, data: List[complex]) -> None:
        """
        Encode by amplitude recursively.
        
        Args:
             QVec: qubits
        
             QStat: amplitude
        
        Returns:
             circuit
        
        """
        ...

    def angle_encode(self, qubit: QVec, data: List[float], gate_type: GateType = GateType.RY_GATE) -> None:
        """
        Encode by angle.
        
        Args:
             QVec: qubits 
        
             prob_vec: data 
        
        Returns:
             circuit.
        
        """
        ...

    @overload
    def approx_mps(self, qubit: QVec, data: List[float], layers: int = 3, sweeps: int = 100, double2float: bool = False) -> None:
        """
        Approximate Matrix Product State encoding.
        
        Args:
             QVec: qubits 
        
             std::vector<double>: input data 
        
             int: number of layers for encoding (default: 3)
        
             int: number of sweeps for optimization (default: 100)
        
             bool: flag to convert double data to float (default: false)
        
        Returns:
             Encoded circuit based on input parameters.
        
        Raises:
             run_fail: An error occurred during the encoding process.
        
        
        """
        ...

    @overload
    def approx_mps(self, qubit: QVec, data: List[complex], layers: int = 3, sweeps: int = 100) -> None:
        """
        Approximate Matrix Product State encoding.
        
        Args:
             QVec: qubits 
        
             std::vector<qcomplex_t>: input data 
        
             int: number of layers (default: 3)
        
             int: number of steps (default: 100)
        
        Returns:
             Encoded circuit.
        
        """
        ...

    def basic_encode(self, qubit: QVec, data: str) -> None:
        """
        Basic encoding.
        
        Args:
             QVec: qubits 
        
             string: data 
        
        Returns:
             circuit
        
        """
        ...

    def bid_amplitude_encode(self, qubit: QVec, data: List[float], split: int = 0) -> None:
        """
        Encode by bid.
        
        Args:
             QVec: qubits 
        
             QStat: amplitude 
        
             split: int 
        
        Returns:
             circuit
        
        """
        ...

    def dc_amplitude_encode(self, qubit: QVec, data: List[float]) -> None:
        """
        Encode by DC amplitude.
        
        Args:
             QVec: qubits 
        
             QStat: amplitude 
        
        Returns:
             circuit
        
        """
        ...

    def dense_angle_encode(self, qubit: QVec, data: List[float]) -> None:
        """
        Encode by dense angle.
        
        Args:
             QVec: qubits 
        
             prob_vec: data 
        
        Returns:
             circuit
        
        """
        ...

    @overload
    def ds_quantum_state_preparation(self, qubit: QVec, data: Dict[str,float]) -> None:
        """
        Prepare a quantum state.
        
        Args:
             QVec: qubits 
        
             std::map<std::string, double>: state parameters 
        
        Returns:
             circuit
        
        
        """
        ...

    @overload
    def ds_quantum_state_preparation(self, qubit: QVec, data: Dict[str,complex]) -> None:
        """
        Prepare a quantum state.
        
        Args:
             QVec: qubits 
        
             std::map<std::string, std::complex<double>>: state parameters 
        
        Returns:
             circuit
        
        
        """
        ...

    @overload
    def ds_quantum_state_preparation(self, qubit: QVec, data: List[float]) -> None:
        """
        Prepare a quantum state.
        
        Args:
             QVec: qubits 
        
             std::vector<double>: state parameters 
        
        Returns:
             circuit
        
        
        """
        ...

    @overload
    def ds_quantum_state_preparation(self, qubit: QVec, data: List[complex]) -> None:
        """
        Prepare a quantum state.
        
        Args:
             QVec: qubits 
        
             std::vector<std::complex<double>>: state parameters 
        
        Returns:
             circuit
        
        """
        ...

    @overload
    def efficient_sparse(self, qubit: QVec, data: Dict[str,float]) -> None:
        """
        Perform an efficient sparse operation.
        
        Args:
             QVec: qubits 
        
             std::map<std::string, double>: parameters for the operation 
        
        Returns:
             circuit
        
        
        """
        ...

    @overload
    def efficient_sparse(self, qubit: QVec, data: Dict[str,complex]) -> None:
        """
        Perform an efficient sparse operation.
        
        Args:
             QVec: qubits 
        
             std::map<std::string, std::complex<double>>: parameters for the operation 
        
        Returns:
             circuit
        
        
        """
        ...

    @overload
    def efficient_sparse(self, qubit: QVec, data: List[float]) -> None:
        """
        Perform an efficient sparse operation.
        
        Args:
             QVec: qubits 
        
             std::vector<double>: parameters for the operation 
        
        Returns:
             circuit
        
        
        """
        ...

    @overload
    def efficient_sparse(self, qubit: QVec, data: List[complex]) -> None:
        """
        Perform an efficient sparse operation.
        
        Args:
             QVec: qubits 
        
             std::vector<std::complex<double>>: parameters for the operation 
        
        Returns:
             circuit
        
        """
        ...

    def get_circuit(self) -> QCircuit:
        """
        Retrieve the circuit from the encoder.
        
        Returns:
             The corresponding circuit object.
        
        """
        ...

    @overload
    def get_fidelity(self, data: List[float]) -> float:
        """
        Calculate the fidelity based on the provided data.
        
        Args:
             data: A vector of doubles representing the input data.
        
        Returns:
             The calculated fidelity value.
        
        
        """
        ...

    @overload
    def get_fidelity(self, data: List[complex]) -> float:
        """
        Calculate the fidelity based on the provided complex data.
        
        Args:
             data: A vector of qcomplex_t representing the input data.
        
        Returns:
             The calculated fidelity value.
        
        
        """
        ...

    @overload
    def get_fidelity(self, data: List[float]) -> float:
        """
        Calculate the fidelity based on the provided float data.
        
        Args:
             data: A vector of floats representing the input data.
        
        Returns:
             The calculated fidelity value.
        
        """
        ...

    def get_out_qubits(self) -> QVec:
        """
        Retrieve the output qubits from the encoder.
        
        Returns:
             A vector of output qubits.
        
        """
        ...

    def iqp_encode(self, qubit: QVec, data: List[float], control_list: List[Tuple[int,int]] = [], bool_inverse: bool = False, repeats: int = 1) -> None:
        """
        Encode by IQP.
        
        Args:
             QVec: qubits 
        
             prob_vec: data 
        
             list: control_list 
        
             bool: bool_inverse 
        
             int: repeats 
        
        Returns:
             circuit.
        
        """
        ...

    def schmidt_encode(self, qubit: QVec, data: List[float], cutoff: float) -> None:
        """
        Encode by schmidt.
        
        Args:
             QVec: qubits 
        
             QStat: amplitude 
        
             double: cutoff 
        
        Returns:
             circuit
        
        """
        ...

    @overload
    def sparse_isometry(self, qubit: QVec, data: Dict[str,float]) -> None:
        """
        Perform a sparse isometry operation.
        
        Args:
             QVec: qubits 
        
             std::map<std::string, double>: parameters for the isometry 
        
        Returns:
             circuit
        
        
        """
        ...

    @overload
    def sparse_isometry(self, qubit: QVec, data: Dict[str,complex]) -> None:
        """
        Perform a sparse isometry operation.
        
        Args:
             QVec: qubits 
        
             std::map<std::string, std::complex<double>>: parameters for the isometry 
        
        Returns:
             circuit
        
        
        """
        ...

    @overload
    def sparse_isometry(self, qubit: QVec, data: List[float]) -> None:
        """
        Perform a sparse isometry operation.
        
        Args:
             QVec: qubits 
        
             std::vector<double>: parameters for the isometry 
        
        Returns:
             circuit
        
        
        """
        ...

    @overload
    def sparse_isometry(self, qubit: QVec, data: List[complex]) -> None:
        """
        Perform a sparse isometry operation.
        
        Args:
             QVec: qubits 
        
             std::vector<std::complex<double>>: parameters for the isometry 
        
        Returns:
             circuit
        
        """
        ...


class ErrorCode:
    """
    pliot error code
    
    Members:
    
      NO_ERROR_FOUND
    
      DATABASE_ERROR
    
      ORIGINIR_ERROR
    
      JSON_FIELD_ERROR
    
      BACKEND_CALC_ERROR
    
      ERR_TASK_BUF_OVERFLOW
    
      EXCEED_MAX_QUBIT
    
      ERR_UNSUPPORT_BACKEND_TYPE
    
      EXCEED_MAX_CLOCK
    
      ERR_UNKNOW_TASK_TYPE
    
      ERR_QVM_INIT_FAILED
    
      ERR_QCOMPILER_FAILED
    
      ERR_PRE_ESTIMATE
    
      ERR_MATE_GATE_CONFIG
    
      ERR_FIDELITY_MATRIX
    
      ERR_QST_PROG
    
      ERR_EMPTY_PROG
    
      ERR_QUBIT_SIZE
    
      ERR_QUBIT_TOPO
    
      ERR_QUANTUM_CHIP_PROG
    
      ERR_REPEAT_MEASURE
    
      ERR_OPERATOR_DB
    
      ERR_TASK_STATUS_BUF_OVERFLOW
    
      ERR_BACKEND_CHIP_TASK_SOCKET_WRONG
    
      CLUSTER_SIMULATE_CALC_ERR
    
      ERR_SCHEDULE_CHIP_TOPOLOGY_SUPPORTED
    
      ERR_TASK_CONFIG
    
      ERR_NOT_FOUND_APP_ID
    
      ERR_NOT_FOUND_TASK_ID
    
      ERR_PARSER_SUB_TASK_RESULT
    
      ERR_SYS_CALL_TIME_OUT
    
      ERR_TASK_TERMINATED
    
      ERR_INVALID_URL
    
      ERR_PARAMETER
    
      ERR_QPROG_LENGTH
    
      ERR_CHIP_OFFLINE
    
      UNDEFINED_ERROR
    
      ERR_SUB_GRAPH_OUT_OF_RANGE
    
      ERR_TCP_INIT_FATLT
    
      ERR_TCP_SERVER_HALT
    
      CLUSTER_BASE
    """
    __members__: ClassVar[dict] = ...  # read-only
    BACKEND_CALC_ERROR: ClassVar[ErrorCode] = ...
    CLUSTER_BASE: ClassVar[ErrorCode] = ...
    CLUSTER_SIMULATE_CALC_ERR: ClassVar[ErrorCode] = ...
    DATABASE_ERROR: ClassVar[ErrorCode] = ...
    ERR_BACKEND_CHIP_TASK_SOCKET_WRONG: ClassVar[ErrorCode] = ...
    ERR_CHIP_OFFLINE: ClassVar[ErrorCode] = ...
    ERR_EMPTY_PROG: ClassVar[ErrorCode] = ...
    ERR_FIDELITY_MATRIX: ClassVar[ErrorCode] = ...
    ERR_INVALID_URL: ClassVar[ErrorCode] = ...
    ERR_MATE_GATE_CONFIG: ClassVar[ErrorCode] = ...
    ERR_NOT_FOUND_APP_ID: ClassVar[ErrorCode] = ...
    ERR_NOT_FOUND_TASK_ID: ClassVar[ErrorCode] = ...
    ERR_OPERATOR_DB: ClassVar[ErrorCode] = ...
    ERR_PARAMETER: ClassVar[ErrorCode] = ...
    ERR_PARSER_SUB_TASK_RESULT: ClassVar[ErrorCode] = ...
    ERR_PRE_ESTIMATE: ClassVar[ErrorCode] = ...
    ERR_QCOMPILER_FAILED: ClassVar[ErrorCode] = ...
    ERR_QPROG_LENGTH: ClassVar[ErrorCode] = ...
    ERR_QST_PROG: ClassVar[ErrorCode] = ...
    ERR_QUANTUM_CHIP_PROG: ClassVar[ErrorCode] = ...
    ERR_QUBIT_SIZE: ClassVar[ErrorCode] = ...
    ERR_QUBIT_TOPO: ClassVar[ErrorCode] = ...
    ERR_QVM_INIT_FAILED: ClassVar[ErrorCode] = ...
    ERR_REPEAT_MEASURE: ClassVar[ErrorCode] = ...
    ERR_SCHEDULE_CHIP_TOPOLOGY_SUPPORTED: ClassVar[ErrorCode] = ...
    ERR_SUB_GRAPH_OUT_OF_RANGE: ClassVar[ErrorCode] = ...
    ERR_SYS_CALL_TIME_OUT: ClassVar[ErrorCode] = ...
    ERR_TASK_BUF_OVERFLOW: ClassVar[ErrorCode] = ...
    ERR_TASK_CONFIG: ClassVar[ErrorCode] = ...
    ERR_TASK_STATUS_BUF_OVERFLOW: ClassVar[ErrorCode] = ...
    ERR_TASK_TERMINATED: ClassVar[ErrorCode] = ...
    ERR_TCP_INIT_FATLT: ClassVar[ErrorCode] = ...
    ERR_TCP_SERVER_HALT: ClassVar[ErrorCode] = ...
    ERR_UNKNOW_TASK_TYPE: ClassVar[ErrorCode] = ...
    ERR_UNSUPPORT_BACKEND_TYPE: ClassVar[ErrorCode] = ...
    EXCEED_MAX_CLOCK: ClassVar[ErrorCode] = ...
    EXCEED_MAX_QUBIT: ClassVar[ErrorCode] = ...
    JSON_FIELD_ERROR: ClassVar[ErrorCode] = ...
    NO_ERROR_FOUND: ClassVar[ErrorCode] = ...
    ORIGINIR_ERROR: ClassVar[ErrorCode] = ...
    UNDEFINED_ERROR: ClassVar[ErrorCode] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None:
        """
        """
        ...

    def __eq__(self, other: object) -> bool:
        """
        """
        ...

    def __getstate__(self) -> int:
        """
        """
        ...

    def __hash__(self) -> int:
        """
        """
        ...

    def __index__(self) -> int:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other: object) -> bool:
        """
        """
        ...

    def __setstate__(self, state: int) -> None:
        """
        """
        ...

    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class Fusion:
    """
    quantum fusion operation
    """
    def __init__(self) -> None:
        """
        """
        ...

    @overload
    def aggregate_operations(self, circuit: QCircuit) -> None:
        """
        Aggregate operations into the provided quantum circuit.
        
        Args:
             circuit: The quantum circuit to which operations will be added.
        
        Returns:
             A reference to the modified circuit.
        
        
        """
        ...

    @overload
    def aggregate_operations(self, qprog: QProg) -> None:
        """
        Aggregate operations into the provided quantum program.
        
        Args:
             qprog: The quantum program to which operations will be added.
        
        Returns:
             A reference to the modified program.
        
        """
        ...


class GateType:
    """
    quantum gate type
    
    Members:
    
      GATE_NOP
    
      GATE_UNDEFINED
    
      P0_GATE
    
      P1_GATE
    
      PAULI_X_GATE
    
      PAULI_Y_GATE
    
      PAULI_Z_GATE
    
      X_HALF_PI
    
      Y_HALF_PI
    
      Z_HALF_PI
    
      HADAMARD_GATE
    
      T_GATE
    
      S_GATE
    
      P_GATE
    
      CP_GATE
    
      RX_GATE
    
      RY_GATE
    
      RZ_GATE
    
      RXX_GATE
    
      RYY_GATE
    
      RZZ_GATE
    
      RZX_GATE
    
      U1_GATE
    
      U2_GATE
    
      U3_GATE
    
      U4_GATE
    
      CU_GATE
    
      CNOT_GATE
    
      CZ_GATE
    
      MS_GATE
    
      CPHASE_GATE
    
      ISWAP_THETA_GATE
    
      ISWAP_GATE
    
      SQISWAP_GATE
    
      SWAP_GATE
    
      TWO_QUBIT_GATE
    
      P00_GATE
    
      P11_GATE
    
      TOFFOLI_GATE
    
      ORACLE_GATE
    
      I_GATE
    
      BARRIER_GATE
    
      RPHI_GATE
    """
    __members__: ClassVar[dict] = ...  # read-only
    BARRIER_GATE: ClassVar[GateType] = ...
    CNOT_GATE: ClassVar[GateType] = ...
    CPHASE_GATE: ClassVar[GateType] = ...
    CP_GATE: ClassVar[GateType] = ...
    CU_GATE: ClassVar[GateType] = ...
    CZ_GATE: ClassVar[GateType] = ...
    GATE_NOP: ClassVar[GateType] = ...
    GATE_UNDEFINED: ClassVar[GateType] = ...
    HADAMARD_GATE: ClassVar[GateType] = ...
    ISWAP_GATE: ClassVar[GateType] = ...
    ISWAP_THETA_GATE: ClassVar[GateType] = ...
    I_GATE: ClassVar[GateType] = ...
    MS_GATE: ClassVar[GateType] = ...
    ORACLE_GATE: ClassVar[GateType] = ...
    P00_GATE: ClassVar[GateType] = ...
    P0_GATE: ClassVar[GateType] = ...
    P11_GATE: ClassVar[GateType] = ...
    P1_GATE: ClassVar[GateType] = ...
    PAULI_X_GATE: ClassVar[GateType] = ...
    PAULI_Y_GATE: ClassVar[GateType] = ...
    PAULI_Z_GATE: ClassVar[GateType] = ...
    P_GATE: ClassVar[GateType] = ...
    RPHI_GATE: ClassVar[GateType] = ...
    RXX_GATE: ClassVar[GateType] = ...
    RX_GATE: ClassVar[GateType] = ...
    RYY_GATE: ClassVar[GateType] = ...
    RY_GATE: ClassVar[GateType] = ...
    RZX_GATE: ClassVar[GateType] = ...
    RZZ_GATE: ClassVar[GateType] = ...
    RZ_GATE: ClassVar[GateType] = ...
    SQISWAP_GATE: ClassVar[GateType] = ...
    SWAP_GATE: ClassVar[GateType] = ...
    S_GATE: ClassVar[GateType] = ...
    TOFFOLI_GATE: ClassVar[GateType] = ...
    TWO_QUBIT_GATE: ClassVar[GateType] = ...
    T_GATE: ClassVar[GateType] = ...
    U1_GATE: ClassVar[GateType] = ...
    U2_GATE: ClassVar[GateType] = ...
    U3_GATE: ClassVar[GateType] = ...
    U4_GATE: ClassVar[GateType] = ...
    X_HALF_PI: ClassVar[GateType] = ...
    Y_HALF_PI: ClassVar[GateType] = ...
    Z_HALF_PI: ClassVar[GateType] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None:
        """
        """
        ...

    def __eq__(self, other: object) -> bool:
        """
        """
        ...

    def __getstate__(self) -> int:
        """
        """
        ...

    def __hash__(self) -> int:
        """
        """
        ...

    def __index__(self) -> int:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other: object) -> bool:
        """
        """
        ...

    def __setstate__(self, state: int) -> None:
        """
        """
        ...

    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class HHLAlg:
    """
     quantum hhl algorithm class
    """
    def __init__(self, arg0: QuantumMachine) -> None:
        """
        """
        ...

    def check_QPE_result(self) -> str:
        """
        check QPE result
        """
        ...

    def get_amplification_factor(self) -> float:
        """
        get_amplification_factor
        """
        ...

    def get_ancillary_qubit(self) -> QVec:
        """
        get_ancillary_qubit
        """
        ...

    def get_hhl_circuit(self, matrix_A: List[complex], data_b: List[float], precision_cnt: int = 0) -> QCircuit:
        """
        """
        ...

    def get_qubit_for_QFT(self) -> List[Qubit]:
        """
        get_qubit_for_QFT
        """
        ...

    def get_qubit_for_b(self) -> List[Qubit]:
        """
        get_qubit_for_b
        """
        ...

    def query_uesed_qubit_num(self) -> int:
        """
        query_uesed_qubit_num
        """
        ...


class LATEX_GATE_TYPE:
    """
    Quantum latex gate type
    
    Members:
    
      GENERAL_GATE
    
      CNOT_GATE
    
      SWAP_GATE
    """
    __members__: ClassVar[dict] = ...  # read-only
    CNOT_GATE: ClassVar[LATEX_GATE_TYPE] = ...
    GENERAL_GATE: ClassVar[LATEX_GATE_TYPE] = ...
    SWAP_GATE: ClassVar[LATEX_GATE_TYPE] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None:
        """
        """
        ...

    def __eq__(self, other: object) -> bool:
        """
        """
        ...

    def __getstate__(self) -> int:
        """
        """
        ...

    def __hash__(self) -> int:
        """
        """
        ...

    def __index__(self) -> int:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other: object) -> bool:
        """
        """
        ...

    def __setstate__(self, state: int) -> None:
        """
        """
        ...

    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class LatexMatrix:
    """
    Generate quantum circuits latex src code can be compiled on latex package 'qcircuit'
    circuits element treated as matrix element in latex syntax
    
    qcircuit package tutorial [https://physics.unm.edu/CQuIC/Qcircuit/Qtutorial.pdf]
    """
    def __init__(self) -> None:
        """
        """
        ...

    def insert_barrier(self, rows: List[int], from_col: int) -> int:
        """
        Insert a barrier into the circuit.
        
        Args:
             rows: The rows of the LaTeX matrix where the barrier is applied.
        
             from_col: Desired column position for the barrier; if space is insufficient, a suitable column will be found.
        
        Returns:
             int: Actual column number where the barrier is placed.
        
        """
        ...

    def insert_gate(self, target_rows: List[int], ctrl_rows: List[int], from_col: int, gate_type: LATEX_GATE_TYPE, gate_name: str = '', dagger: bool = False, param: str = '') -> int:
        """
        Insert a gate into the circuit.
        
        Args:
             target_rows: Gate target rows of the LaTeX matrix.
        
             ctrl_rows: Control rows for the gate.
        
             from_col: Desired column position for the gate; if space is insufficient, a suitable column will be found.
        
             gate_type: Enum type of LATEX_GATE_TYPE.
        
             gate_name: Name of the gate (default: '').
        
             dagger: Flag indicating if the gate is a dagger (default: false).
        
             param: Parameter string for the gate (default: '').
        
        Returns:
             int: Actual column number where the gate is placed.
        
        """
        ...

    def insert_measure(self, q_row: int, c_row: int, from_col: int) -> int:
        """
        Insert a measurement operation into the circuit.
        
        Args:
             q_row: The row of the qubit being measured.
        
             c_row: The row of the classical bit that will store the measurement result.
        
             from_col: The desired column position for the measurement.
        
        Returns:
             None, as the function modifies the matrix in place.
        
        """
        ...

    def insert_reset(self, q_row: int, from_col: int) -> int:
        """
        Insert a reset operation into the circuit.
        
        Args:
             q_row: The row of the qubit to be reset.
        
             from_col: The desired column position for the reset.
        
        Returns:
             None, as the function modifies the matrix in place.
        
        """
        ...

    def insert_timeseq(self, t_col: int, time_seq: int) -> None:
        """
        Insert a time sequence into the circuit.
        
        Args:
             t_col: The column position where the time sequence will be inserted.
        
             time_seq: The time sequence data to be inserted.
        
        Warning:
             This function does not check for column number validity, which may cause overwriting.
        
             Users must ensure the column number is managed correctly to avoid conflicts.
        
        """
        ...

    def set_label(self, qubit_label: Dict[int,str], cbit_label: Dict[int,str] = {}, time_seq_label: str = '', head: bool = True) -> None:
        """
        Set label at the leftmost head column or rightmost tail column.
        Labels can be reset at any time.
        
        Args:
             qubit_label: Label for the qubit wire's leftmost head label, specified in LaTeX syntax.If not given, the row will remain empty (e.g., {0: 'q_{1}', 2:'q_{2}'}).
        
             cbit_label: Classic label string, supports LaTeX formatting.
        
             time_seq_label: If given, sets the time sequence label.
        
             head: If true, appends the label at the head; if false, appends at the tail.
        
        Returns:
             None, as the function modifies the matrix in place.
        
        """
        ...

    def set_logo(self, logo: str = '') -> None:
        """
        Add a logo string.
        
        Args:
             logo: The logo string to be added. If not provided, the logo will be set to an empty string.
        
        Returns:
             None, as the function modifies the matrix in place.
        
        """
        ...

    def str(self, with_time: bool = False) -> str:
        """
        Return the final LaTeX source code representation of the matrix.
        
        Args:
             with_time: A boolean flag indicating whether to include timing information in the output.
        
        Returns:
             str: The LaTeX source code as a string. This method can be called at any time to obtain the current state of the matrix.
        
        """
        ...


class MPSQVM(QuantumMachine):
    """
    quantum matrix product state machine class
    """
    def __init__(self) -> None:
        """
        """
        ...

    @overload
    def add_single_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float) -> None:
        """
        Add a noise model to a specific gate.
        
        Args:
             noise_model: NOISE_MODEL, the type of noise model to apply.
        
             gate_type: GateType, the type of gate affected by the noise.
        
             error_rate: float, the rate of noise occurrence.
        
        Returns:
             None.
        
        
        """
        ...

    @overload
    def add_single_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float, arg3: float, arg4: float) -> None:
        """
        Add a noise model to a specific gate with multiple error rates.
        
        Args:
             noise_model: NOISE_MODEL, the type of noise model to apply.
        
             gate_type: GateType, the type of gate affected by the noise.
        
             error_rate_1: float, the first error rate.
        
             error_rate_2: float, the second error rate.
        
             error_rate_3: float, the third error rate.
        
        Returns:
             None.
        
        """
        ...

    def get_prob_dict(self, qubit_list: QVec, select_max: int = -1) -> Dict[str,float]:
        """
        Get pmeasure result as dict.
        
        Args:
             qubit_list: List of qubits for pmeasure.
        
             select_max: Maximum number of returned elements in the result tuple; should be in [-1, 1<<len(qubit_list)]. Default is -1, meaning no limit.
        
        Returns:
             Measure result of the quantum machine.
        
        """
        ...

    def get_prob_list(self, qubit_list: QVec, select_max: int = -1) -> List[float]:
        """
        Get pmeasure result as list.
        
        Args:
             qubit_list: List of qubits for pmeasure.
        
             select_max: Maximum number of returned elements in the result tuple; should be in [-1, 1<<len(qubit_list)]. Default is -1, meaning no limit.
        
        Returns:
             Measure result of the quantum machine.
        
        """
        ...

    def get_prob_tuple_list(self, qubit_list: QVec, select_max: int = -1) -> List[Tuple[int,float]]:
        """
        Get pmeasure result as list.
        
        Args:
             qubit_list: List of qubits for pmeasure.
        
             select_max: Maximum number of returned elements in the result tuple; should be in [-1, 1<<len(qubit_list)]. Default is -1, meaning no limit.
        
        Returns:
             Measure result of the quantum machine.
        
        """
        ...

    def pmeasure(self, qubit_list: QVec, select_max: int = -1) -> List[Tuple[int,float]]:
        """
        Get the probability distribution over qubits.
        
        Args:
             qubit_list: List of qubits to measure.
        
             select_max: Maximum number of returned elements in the result tuple; should be in [-1, 1<<len(qubit_list)]. Default is -1, which means no limit.
        
        Returns:
             Measure result of the quantum machine in tuple form.
        
        """
        ...

    def pmeasure_bin_index(self, program: QProg, string: str) -> complex:
        """
        Get pmeasure bin index quantum state amplitude.
        
        Args:
             string: Bin string.
        
        Returns:
             Complex: Bin amplitude.
        
        """
        ...

    def pmeasure_bin_subset(self, program: QProg, string_list: List[str]) -> List[complex]:
        """
        Get pmeasure quantum state amplitude subset.
        
        Args:
             list: List of bin state strings.
        
        Returns:
             List: Bin amplitude result list.
        
        """
        ...

    def pmeasure_dec_index(self, program: QProg, string: str) -> complex:
        """
        Get pmeasure decimal index quantum state amplitude.
        
        Args:
             string: Decimal string.
        
        Returns:
             Complex: Decimal amplitude.
        
        """
        ...

    def pmeasure_dec_subset(self, program: QProg, string_list: List[str]) -> List[complex]:
        """
        Get pmeasure quantum state amplitude subset.
        
        Args:
             list: List of decimal state strings.
        
        Returns:
             List: Decimal amplitude result list.
        
        """
        ...

    def pmeasure_no_index(self, qubit_list: QVec) -> List[float]:
        """
        Get the probability distribution over qubits.
        
        Args:
             qubit_list: List of qubits to measure.
        
        Returns:
             Measure result of the quantum machine in list form.
        
        """
        ...

    def prob_run_dict(self, program: QProg, qubit_list: QVec, select_max: int = -1) -> Dict[str,float]:
        """
        Run quantum program and get pmeasure result as dict.
        Args:
             program: Quantum program to run.
        
             qubit_list: List of qubits for pmeasure.
        
             select_max: Maximum number of returned elements in the result; should be in [-1, 1<<len(qubit_list)]. Default is -1, meaning no limit.
        Returns:
             Measure result of the quantum machine.
        
        """
        ...

    def prob_run_list(self, program: QProg, qubit_list: QVec, select_max: int = -1) -> List[float]:
        """
        Run quantum program and get pmeasure result as list.
        
        Args:
             program: Quantum program to run.
        
             qubit_list: List of qubits for pmeasure.
        
             select_max: Maximum number of returned elements in the result; should be in [-1, 1<<len(qubit_list)]. Default is -1, meaning no limit.
        
        Returns:
             Measure result of the quantum machine.
        
        """
        ...

    def prob_run_tuple_list(self, program: QProg, qubit_list: QVec, select_max: int = -1) -> List[Tuple[int,float]]:
        """
        Run quantum program and get pmeasure result as tuple list.
        
        Args:
             program: Quantum program to run.
        
             qubit_list: List of qubits for pmeasure.
        
             select_max: Maximum number of returned elements in the result tuple; should be in [-1, 1<<len(qubit_list)]. Default is -1, meaning no limit.
        
        Returns:
             Measure result of the quantum machine.
        
        """
        ...

    def quick_measure(self, qubit_list: QVec, shots: int) -> Dict[str,int]:
        """
        Quick measure.
        
        Args:
             qubit_list: List of qubits to measure.
        
             shots: The number of repetitions for the measurement operation.
        
        Returns:
             Result of the quantum program.
        
        """
        ...

    @overload
    def set_measure_error(self, arg0: NoiseModel, arg1: float) -> None:
        """
        Set the measurement error based on the specified noise model.
        
        Args:
             noise_model: The type of noise model to apply.
        
             error_rate: The rate of measurement error to be set.
        
        
        """
        ...

    @overload
    def set_measure_error(self, arg0: NoiseModel, arg1: float, arg2: float, arg3: float) -> None:
        """
        Set the measurement error with multiple error rates for the specified noise model.
        
        Args:
             noise_model: The type of noise model to apply.
        
             error_rate1: First error rate.
        
             error_rate2: Second error rate.
        
             error_rate3: Third error rate.
        
        """
        ...

    @overload
    def set_mixed_unitary_error(self, arg0: GateType, arg1: List[List[complex]], arg2: List[QVec]) -> None:
        """
        Set mixed unitary errors for the specified gate type.
        
        Args:
             gate_type: Type of gate affected by the error.
        
             unitary_errors: List of unitary error matrices.
        
             qubits: List of qubits where the errors will be applied.
        
        
        """
        ...

    @overload
    def set_mixed_unitary_error(self, arg0: GateType, arg1: List[List[complex]], arg2: List[float], arg3: List[QVec]) -> None:
        """
        Set mixed unitary errors with associated probabilities for the specified gate type.
        
        Args:
             gate_type: Type of gate affected by the error.
        
             unitary_errors: List of unitary error matrices.
        
             probabilities: Probabilities associated with each unitary error.
        
             qubits: List of qubits where the errors will be applied.
        
        
        """
        ...

    @overload
    def set_mixed_unitary_error(self, arg0: GateType, arg1: List[List[complex]]) -> None:
        """
        Set mixed unitary errors for the specified gate type.
        
        Args:
             gate_type: Type of gate affected by the error.
        
             unitary_errors: List of unitary error matrices to apply for the gate type.
        
        
        """
        ...

    @overload
    def set_mixed_unitary_error(self, arg0: GateType, arg1: List[List[complex]], arg2: List[float]) -> None:
        """
        Set mixed unitary errors with associated probabilities for the specified gate type.
        
        Args:
             gate_type: Type of gate affected by the error.
        
             unitary_errors: List of unitary error matrices.
        
             probabilities: Probabilities associated with each unitary error.
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float) -> None:
        """
        Set the noise model for the quantum simulation.
        
        Args:
             noise_model: Type of noise model (bit-flip, phase-flip, etc.).
        
             gate_type: Type of gate affected by the noise.
        
             noise_level: Level of noise to apply.
        
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float, arg3: List[QVec]) -> None:
        """
        Set the noise model for the quantum simulation with specific qubits.
        
        Args:
             noise_model: Type of noise model (bit-flip, phase-flip, etc.).
        
             gate_type: Type of gate affected by the noise.
        
             noise_level: Level of noise to apply.
        
             qubits: List of qubits to which the noise model will be applied.
        
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float, arg3: float, arg4: float) -> None:
        """
        Set the noise model for the quantum simulation with multiple noise levels.
        
        Args:
             noise_model: Type of noise model (bit-flip, phase-flip, etc.).
        
             gate_type: Type of gate affected by the noise.
        
             noise_level_1: First noise level to apply.
        
             noise_level_2: Second noise level to apply.
        
             noise_level_3: Third noise level to apply.
        
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float, arg3: float, arg4: float, arg5: List[QVec]) -> None:
        """
        Set the noise model for the quantum simulation with specific noise levels and qubits.
        
        Args:
             noise_model: Type of noise model (bit-flip, phase-flip, etc.).
        
             gate_type: Type of gate affected by the noise.
        
             noise_level_1: First noise level to apply.
        
             noise_level_2: Second noise level to apply.
        
             noise_level_3: Third noise level to apply.
        
             qubits: List of qubits to which the noise model will be applied.
        
        """
        ...

    def set_readout_error(self, readout_params: List[List[float]], qubits: QVec) -> None:
        """
        Set readout error parameters for the specified qubits.
        
        Args:
             readout_params: Parameters defining the readout errors.
        
             qubits: List of qubits to which the readout errors apply.
        
        """
        ...

    def set_reset_error(self, reset_0_param: float, reset_1_param: float) -> None:
        """
        Set the reset error for the quantum state.
        
        Args:
             reset_0_param: float, error probability for resetting qubit to 0.
        
             reset_1_param: float, error probability for resetting qubit to 1.
        
        Returns:
             None.
        
        """
        ...

    def set_rotation_error(self, param: float) -> None:
        """
        Set the rotation error parameters.
        
        Args:
             param: The parameters defining the rotation error.
        
        Returns:
             A reference to the updated instance of the class.
        
        """
        ...


class MomentumOptimizer:
    """
    variational quantum MomentumOptimizer
    """
    def __init__(self, arg0: var, arg1: float, arg2: float) -> None:
        """
        """
        ...

    def get_loss(self) -> float:
        """
        """
        ...

    def get_variables(self) -> List[var]:
        """
        """
        ...

    def minimize(self, arg0: float, arg1: float) -> Optimizer:
        """
        """
        ...

    def run(self, arg0: List[var], arg1: int) -> bool:
        """
        """
        ...


class NodeInfo:
    """
    Detailed information of a QProg node
    """
    m_cbits: List[int]
    m_control_qubits: QVec
    m_gate_type: GateType
    m_is_dagger: bool
    m_iter: NodeIter
    m_name: str
    m_node_type: NodeType
    m_params: List[float]
    m_target_qubits: QVec
    @overload
    def __init__(self) -> None:
        """
        """
        ...

    @overload
    def __init__(self, iter: NodeIter, target_qubits: QVec, control_qubits: QVec, type: int, dagger: bool) -> None:
        """
        Initialize a quantum operation with the specified parameters.
        
        Args:
             iter: The node iterator for the quantum operation.
        
             target_qubits: The target qubits involved in the operation.
        
             control_qubits: The control qubits for the operation.
        
             type: An integer representing the type of operation.
        
             dagger: A boolean indicating whether the operation is a dagger (adjoint) operation.
        
        Returns:
             None: This function initializes the quantum operation.
        
        """
        ...

    def reset(self) -> None:
        """
        Reset the NodeInfo instance to its initial state.
        This function clears any current data in the NodeInfo and prepares it for reuse.
        
        Args:
             None
        
        Returns:
             None
        
        """
        ...


class NodeIter:
    """
    quantum node iter
    """
    __hash__: ClassVar[None] = ...
    def __init__(self) -> None:
        """
        Initialize a new NodeIter instance.
        
        Args:
             None
        
        Returns:
             A new instance of NodeIter.
        
        """
        ...

    def get_next(self) -> NodeIter:
        """
        Get the next node iterator.
        
        Args:
             None
        
        Returns:
             The next NodeIter instance.
        
        """
        ...

    def get_node_type(self) -> NodeType:
        """
        Retrieve the type of the current node.
        
        Args:
             None
        
        Returns:
             The type of the node.
        
        """
        ...

    def get_pre(self) -> NodeIter:
        """
        Get the previous node iterator.
        
        Args:
             None
        
        Returns:
             The previous NodeIter instance.
        
        """
        ...

    def __eq__(self, arg0: NodeIter) -> bool:
        """
        Check equality between two NodeIter instances.
        
        Args:
             other: Another NodeIter instance.
        
        Returns:
             True if equal, false otherwise.
        
        """
        ...

    def __ne__(self, arg0: NodeIter) -> bool:
        """
        Check inequality between two NodeIter instances.
        
        Args:
             other: Another NodeIter instance.
        
        Returns:
             True if not equal, false otherwise.
        
        """
        ...


class NodeType:
    """
    quantum node type
    
    Members:
    
      NODE_UNDEFINED
    
      GATE_NODE
    
      CIRCUIT_NODE
    
      PROG_NODE
    
      MEASURE_GATE
    
      WHILE_START_NODE
    
      QIF_START_NODE
    
      CLASS_COND_NODE
    
      RESET_NODE
    """
    __members__: ClassVar[dict] = ...  # read-only
    CIRCUIT_NODE: ClassVar[NodeType] = ...
    CLASS_COND_NODE: ClassVar[NodeType] = ...
    GATE_NODE: ClassVar[NodeType] = ...
    MEASURE_GATE: ClassVar[NodeType] = ...
    NODE_UNDEFINED: ClassVar[NodeType] = ...
    PROG_NODE: ClassVar[NodeType] = ...
    QIF_START_NODE: ClassVar[NodeType] = ...
    RESET_NODE: ClassVar[NodeType] = ...
    WHILE_START_NODE: ClassVar[NodeType] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None:
        """
        """
        ...

    def __eq__(self, other: object) -> bool:
        """
        """
        ...

    def __getstate__(self) -> int:
        """
        """
        ...

    def __hash__(self) -> int:
        """
        """
        ...

    def __index__(self) -> int:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other: object) -> bool:
        """
        """
        ...

    def __setstate__(self, state: int) -> None:
        """
        """
        ...

    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class Noise:
    """
    Quantum machine for noise simulation
    """
    def __init__(self) -> None:
        """
        Initialize a new NoiseModel instance.
        
        Args:
             None
        
        Returns:
             A new NoiseModel instance.
        
        """
        ...

    @overload
    def add_mixed_unitary_error(self, gate_types: GateType, unitary_matrices: List[List[complex]], probs: List[float]) -> None:
        """
        Add mixed unitary errors to specified gate types.
        
        Args:
             gate_types: The type of gates to which the mixed unitary errors apply.
        
             unitary_matrices: A vector of unitary matrices representing the errors.
        
             probs: A vector of probabilities corresponding to each unitary matrix.
        
        Returns:
             None.
        
        
        """
        ...

    @overload
    def add_mixed_unitary_error(self, gate_types: GateType, unitary_matrices: List[List[complex]], probs: List[float], qubits: QVec) -> None:
        """
        Add mixed unitary errors to specified gate types with targeted qubits.
        
        Args:
             gate_types: The type of gates to which the mixed unitary errors apply.
        
             unitary_matrices: A vector of unitary matrices representing the errors.
        
             probs: A vector of probabilities corresponding to each unitary matrix.
        
             qubits: A vector of qubit indices that the mixed unitary errors affect.
        
        Returns:
             None.
        
        
        """
        ...

    @overload
    def add_mixed_unitary_error(self, gate_types: GateType, unitary_matrices: List[List[complex]], probs: List[float], qubits: List[QVec]) -> None:
        """
        Add mixed unitary errors to specified gate types for multiple qubits.
        
        Args:
             gate_types: The type of gates to which the mixed unitary errors apply.
        
             unitary_matrices: A vector of unitary matrices representing the errors.
        
             probs: A vector of probabilities corresponding to each unitary matrix.
        
             qubits: A vector of QVec instances indicating which qubits the errors affect.
        
        Returns:
             None.
        
        """
        ...

    @overload
    def add_noise_model(self, noise_model: NoiseModel, gate_type: GateType, prob: float) -> None:
        """
        Add a noise model to the noise simulation.
        
        Args:
             noise_model: An instance of NOISE_MODEL to be added.
        
             gate_type: The type of gate to which the noise model applies.
        
             prob: The probability of the noise occurring.
        
        Returns:
             None.
        
        
        """
        ...

    @overload
    def add_noise_model(self, noise_model: NoiseModel, gate_types: List[GateType], prob: float) -> None:
        """
        Add a noise model to multiple gate types.
        
        Args:
             noise_model: An instance of NOISE_MODEL to be added.
        
             gate_types: A vector of gate types to which the noise model applies.
        
             prob: The probability of the noise occurring.
        
        Returns:
             None.
        
        
        """
        ...

    @overload
    def add_noise_model(self, noise_model: NoiseModel, gate_type: GateType, prob: float, qubits: QVec) -> None:
        """
        Add a noise model to a specific gate with targeted qubits.
        
        Args:
             noise_model: An instance of NOISE_MODEL to be added.
        
             gate_type: The type of gate to which the noise model applies.
        
             prob: The probability of the noise occurring.
        
             qubits: A vector of qubit indices that the noise affects.
        
        Returns:
             None.
        
        
        """
        ...

    @overload
    def add_noise_model(self, noise_model: NoiseModel, gate_types: List[GateType], prob: float, qubits: QVec) -> None:
        """
        Add a noise model to multiple gate types with targeted qubits.
        
        Args:
             noise_model: An instance of NOISE_MODEL to be added.
        
             gate_types: A vector of gate types to which the noise model applies.
        
             prob: The probability of the noise occurring.
        
             qubits: A vector of qubit indices that the noise affects.
        
        Returns:
             None.
        
        
        """
        ...

    @overload
    def add_noise_model(self, noise_model: NoiseModel, gate_type: GateType, prob: float, qubits: List[QVec]) -> None:
        """
        Add a noise model to a specific gate with targeted qubits.
        
        Args:
             noise_model: An instance of NOISE_MODEL to be added.
        
             gate_type: The type of gate to which the noise model applies.
        
             prob: The probability of the noise occurring.
        
             qubits: A vector of qubit indices that the noise affects.
        
        Returns:
             None.
        
        
        """
        ...

    @overload
    def add_noise_model(self, noise_model: NoiseModel, gate_type: GateType, t1: float, t2: float, t_gate: float) -> None:
        """
        Add a noise model to a specific gate with time parameters.
        
        Args:
             noise_model: An instance of NOISE_MODEL to be added.
        
             gate_type: The type of gate to which the noise model applies.
        
             t1: The time constant for relaxation (T1).
        
             t2: The time constant for dephasing (T2).
        
             t_gate: The duration of the gate operation.
        
        Returns:
             None.
        
        
        """
        ...

    @overload
    def add_noise_model(self, noise_model: NoiseModel, gate_types: List[GateType], t1: float, t2: float, t_gate: float) -> None:
        """
        Add a noise model to multiple gate types with time parameters.
        
        Args:
             noise_model: An instance of NOISE_MODEL to be added.
        
             gate_types: A vector of gate types to which the noise model applies.
        
             t1: The time constant for relaxation (T1).
        
             t2: The time constant for dephasing (T2).
        
             t_gate: The duration of the gate operation.
        
        Returns:
             None.
        
        
        """
        ...

    @overload
    def add_noise_model(self, noise_model: NoiseModel, gate_type: GateType, t1: float, t2: float, t_gate: float, qubits: QVec) -> None:
        """
        Add a noise model to a specific gate with time parameters and targeted qubits.
        
        Args:
             noise_model: An instance of NOISE_MODEL to be added.
        
             gate_type: The type of gate to which the noise model applies.
        
             t1: The time constant for relaxation (T1).
        
             t2: The time constant for dephasing (T2).
        
             t_gate: The duration of the gate operation.
        
             qubits: A vector of qubit indices that the noise affects.
        
        Returns:
             None.
        
        
        """
        ...

    @overload
    def add_noise_model(self, noise_model: NoiseModel, gate_types: List[GateType], t1: float, t2: float, t_gate: float, qubits: QVec) -> None:
        """
        Add a noise model to multiple gate types with specified time parameters and targeted qubits.
        
        Args:
             noise_model: An instance of NOISE_MODEL to be added.
        
             gate_types: A vector of gate types to which the noise model applies.
        
             t1: The time constant for relaxation (T1).
        
             t2: The time constant for dephasing (T2).
        
             t_gate: The duration of the gate operation.
        
             qubits: A vector of qubit indices that the noise affects.
        
        Returns:
             None.
        
        
        """
        ...

    @overload
    def add_noise_model(self, noise_model: NoiseModel, gate_type: GateType, t1: float, t2: float, t_gate: float, qubits: List[QVec]) -> None:
        """
        Add a noise model to a specific gate with specified time parameters and targeted qubits.
        
        Args:
             noise_model: An instance of NOISE_MODEL to be added.
        
             gate_type: The type of gate to which the noise model applies.
        
             t1: The time constant for relaxation (T1).
        
             t2: The time constant for dephasing (T2).
        
             t_gate: The duration of the gate operation.
        
             qubits: A vector of vectors of qubit indices that the noise affects.
        
        Returns:
             None.
        
        """
        ...

    @overload
    def set_measure_error(self, noise_model: NoiseModel, prob: float, qubits: QVec = ...) -> None:
        """
        Set the measurement error for specified qubits.
        
        Args:
             noise_model: An instance of NOISE_MODEL to be used.
        
             prob: The probability of measurement error.
        
             qubits: A vector of qubit indices to which the measurement error applies. Defaults to an empty QVec.
        
        Returns:
             None.
        
        
        """
        ...

    @overload
    def set_measure_error(self, noise_model: NoiseModel, t1: float, t2: float, t_gate: float, qubits: QVec = ...) -> None:
        """
        Set the measurement error using time parameters for the specified qubits.
        
        Args:
             noise_model: An instance of NOISE_MODEL to be used.
        
             t1: The time constant for relaxation (T1).
        
             t2: The time constant for dephasing (T2).
        
             t_gate: The duration of the gate operation.
        
             qubits: A vector of qubit indices to which the measurement error applies. Defaults to an empty QVec.
        
        Returns:
             None.
        
        """
        ...

    def set_readout_error(self, prob_list: List[List[float]], qubits: QVec = ...) -> None:
        """
        Set readout errors for specified qubits.
        
        Args:
             prob_list: A list of probabilities for readout errors.
        
             qubits: A vector of qubit indices that the readout errors apply to (default is all qubits).
        
        Returns:
             None.
        
        """
        ...

    def set_reset_error(self, p0: float, p1: float, qubits: QVec) -> None:
        """
        Set reset errors for specified qubits.
        
        Args:
             p0: The probability of resetting to state |0>.
        
             p1: The probability of resetting to state |1>.
        
             qubits: A vector of qubit indices that the reset errors apply to.
        
        Returns:
             None.
        
        """
        ...

    def set_rotation_error(self, error: float) -> None:
        """
        Set rotation error for gates.
        
        Args:
             error: The error model for rotation operations.
        
        Returns:
             None.
        
        """
        ...


class NoiseModel:
    """
    noise model type
    
    Members:
    
      DAMPING_KRAUS_OPERATOR
    
      DECOHERENCE_KRAUS_OPERATOR
    
      DEPHASING_KRAUS_OPERATOR
    
      PAULI_KRAUS_MAP
    
      BITFLIP_KRAUS_OPERATOR
    
      DEPOLARIZING_KRAUS_OPERATOR
    
      BIT_PHASE_FLIP_OPRATOR
    
      PHASE_DAMPING_OPRATOR
    """
    __members__: ClassVar[dict] = ...  # read-only
    BITFLIP_KRAUS_OPERATOR: ClassVar[NoiseModel] = ...
    BIT_PHASE_FLIP_OPRATOR: ClassVar[NoiseModel] = ...
    DAMPING_KRAUS_OPERATOR: ClassVar[NoiseModel] = ...
    DECOHERENCE_KRAUS_OPERATOR: ClassVar[NoiseModel] = ...
    DEPHASING_KRAUS_OPERATOR: ClassVar[NoiseModel] = ...
    DEPOLARIZING_KRAUS_OPERATOR: ClassVar[NoiseModel] = ...
    PAULI_KRAUS_MAP: ClassVar[NoiseModel] = ...
    PHASE_DAMPING_OPRATOR: ClassVar[NoiseModel] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None:
        """
        """
        ...

    def __eq__(self, other: object) -> bool:
        """
        """
        ...

    def __getstate__(self) -> int:
        """
        """
        ...

    def __hash__(self) -> int:
        """
        """
        ...

    def __index__(self) -> int:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other: object) -> bool:
        """
        """
        ...

    def __setstate__(self, state: int) -> None:
        """
        """
        ...

    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class NoiseQVM(QuantumMachine):
    """
    quantum machine class for simulate noise prog
    """
    def __init__(self) -> None:
        """
        """
        ...

    def initQVM(self, arg0: dict) -> None:
        """
        init quantum virtual machine
        """
        ...

    @overload
    def init_qvm(self, json_config: dict) -> None:
        """
        init quantum virtual machine
        
        """
        ...

    @overload
    def init_qvm(self) -> None:
        """
        init quantum virtual machine
        """
        ...

    def set_max_threads(self, size: int) -> None:
        """
        Set the maximum number of threads for the noise quantum virtual machine (NoiseQVM).
        
        Args:
             size: The maximum number of threads to utilize.
        
        Returns:
             None: This method does not return a value.
        
        """
        ...

    @overload
    def set_measure_error(self, model: NoiseModel, prob: float, qubits: QVec = ...) -> None:
        """
        Set the measurement error model in the quantum virtual machine.
        
        Args:
             model: The noise model to be applied for measurement errors.
        
             prob: A double representing the probability of measurement error.
        
             qubits: A specific qubit vector (QVec) for which the measurement error applies (default is an empty QVec).
        
        Returns:
             None, as the function configures the measurement error model in place for the specified qubit vector.
        
        
        """
        ...

    @overload
    def set_measure_error(self, model: NoiseModel, T1: float, T2: float, t_gate: float, qubits: QVec = ...) -> None:
        """
        Set the measurement error model in the quantum virtual machine with specific error parameters.
        
        Args:
             model: The noise model to be applied for measurement errors.
        
             T1: A double representing the relaxation time constant for the qubits.
        
             T2: A double representing the dephasing time constant for the qubits.
        
             t_gate: A double representing the time duration of the gate operation.
        
             qubits: A specific qubit vector (QVec) for which the measurement error applies (default is an empty QVec).
        
        Returns:
             None, as the function configures the measurement error model in place for the specified qubit vector.
        
        """
        ...

    @overload
    def set_mixed_unitary_error(self, arg0: GateType, arg1: List[List[complex]], arg2: List[float]) -> None:
        """
        Set a mixed unitary error model for a specific gate type in the quantum virtual machine.
        
        Args:
             gate_type: The type of gate for which the mixed unitary error model applies.
        
             unitary_ops: A vector of unitary operations (QStat) representing the error model.
        
             probabilities: A vector of doubles representing the probabilities associated with each unitary operation.
        
        Returns:
             None, as the function configures the mixed unitary error model in place for the specified gate type.
        
        
        """
        ...

    @overload
    def set_mixed_unitary_error(self, arg0: GateType, arg1: List[List[complex]], arg2: List[float], arg3: QVec) -> None:
        """
        Set a mixed unitary error model for a specific gate type in the quantum virtual machine with specific qubits.
        
        Args:
             gate_type: The type of gate for which the mixed unitary error model applies.
        
             unitary_ops: A vector of unitary operations (QStat) representing the error model.
        
             probabilities: A vector of doubles representing the probabilities associated with each unitary operation.
        
             qubits: A specific qubit vector (QVec) for which the mixed unitary error applies.
        
        Returns:
             None, as the function configures the mixed unitary error model in place for the specified gate type and qubits.
        
        
        """
        ...

    @overload
    def set_mixed_unitary_error(self, arg0: GateType, arg1: List[List[complex]], arg2: List[float], arg3: List[QVec]) -> None:
        """
        Set a mixed unitary error model for a specific gate type in the quantum virtual machine, targeting multiple qubits.
        
        Args:
             gate_type: The type of gate for which the mixed unitary error model applies.
        
             unitary_ops: A vector of unitary operations (QStat) representing the error model.
        
             probabilities: A vector of doubles representing the probabilities associated with each unitary operation.
        
             qubit_groups: A vector of qubit vectors (QVec) specifying the qubits affected by the error model.
        
        Returns:
             None, as the function configures the mixed unitary error model in place for the specified gate type and qubit groups.
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float) -> None:
        """
        Set the noise model for the quantum virtual machine.
        
        Args:
             noise_model: The noise model to be applied.
        
             gate_type: The type of gate for which the noise model is relevant.
        
             noise_level: A double representing the level of noise to apply.
        
        Returns:
             None, as the function configures the noise model in place.
        
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: List[GateType], arg2: float) -> None:
        """
        Set the noise model for multiple gate types in the quantum virtual machine.
        
        Args:
             noise_model: The noise model to be applied.
        
             gate_types: A vector of gate types for which the noise model is relevant.
        
             noise_level: A double representing the level of noise to apply.
        
        Returns:
             None, as the function configures the noise model in place for the specified gate types.
        
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float, arg3: QVec) -> None:
        """
        Set the noise model for a specific gate type and qubit vector in the quantum virtual machine.
        
        Args:
             noise_model: The noise model to be applied.
        
             gate_type: The type of gate for which the noise model is relevant.
        
             noise_level: A double representing the level of noise to apply.
        
             qubits: A vector of qubits (QVec) affected by the noise model.
        
        Returns:
             None, as the function configures the noise model in place for the specified gate type and qubits.
        
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: List[GateType], arg2: float, arg3: QVec) -> None:
        """
        Set the noise model for multiple gate types and a specific qubit vector in the quantum virtual machine.
        
        Args:
             noise_model: The noise model to be applied.
        
             gate_types: A vector of gate types for which the noise model is relevant.
        
             noise_level: A double representing the level of noise to apply.
        
             qubits: A vector of qubits (QVec) affected by the noise model.
        
        Returns:
             None, as the function configures the noise model in place for the specified gate types and qubits.
        
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float, arg3: List[QVec]) -> None:
        """
        Set the noise model for a specific gate type and multiple qubit vectors in the quantum virtual machine.
        
        Args:
             noise_model: The noise model to be applied.
        
             gate_type: The type of gate for which the noise model is relevant.
        
             noise_level: A double representing the level of noise to apply.
        
             qubits: A vector of qubit vectors (std::vector<QVec>) affected by the noise model.
        
        Returns:
             None, as the function configures the noise model in place for the specified gate type and qubit vectors.
        
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float, arg3: float, arg4: float) -> None:
        """
        Set the noise model for a specific gate type with multiple noise parameters in the quantum virtual machine.
        
        Args:
             noise_model: The noise model to be applied.
        
             gate_type: The type of gate for which the noise model is relevant.
        
             noise_level1: A double representing the first level of noise to apply.
        
             noise_level2: A double representing the second level of noise to apply.
        
             noise_level3: A double representing the third level of noise to apply.
        
        Returns:
             None, as the function configures the noise model in place for the specified gate type with the given noise parameters.
        
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: List[GateType], arg2: float, arg3: float, arg4: float) -> None:
        """
        Set the noise model for multiple gate types with various noise parameters in the quantum virtual machine.
        
        Args:
             noise_model: The noise model to be applied.
        
             gate_types: A vector of gate types for which the noise model is relevant.
        
             noise_level1: A double representing the first level of noise to apply.
        
             noise_level2: A double representing the second level of noise to apply.
        
             noise_level3: A double representing the third level of noise to apply.
        
        Returns:
             None, as the function configures the noise model in place for the specified gate types with the given noise parameters.
        
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float, arg3: float, arg4: float, arg5: QVec) -> None:
        """
        Set the noise model for a specific gate type with multiple noise parameters affecting a specific qubit vector in the quantum virtual machine.
        
        Args:
             noise_model: The noise model to be applied.
        
             gate_type: The type of gate for which the noise model is relevant.
        
             noise_level1: A double representing the first level of noise to apply.
        
             noise_level2: A double representing the second level of noise to apply.
        
             noise_level3: A double representing the third level of noise to apply.
        
             qubits: A specific qubit vector (QVec) affected by the noise model.
        
        Returns:
             None, as the function configures the noise model in place for the specified gate type and qubit vector.
        
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: List[GateType], arg2: float, arg3: float, arg4: float, arg5: QVec) -> None:
        """
        Set the noise model for multiple gate types with various noise parameters affecting a specific qubit vector in the quantum virtual machine.
        
        Args:
             noise_model: The noise model to be applied.
        
             gate_types: A vector of gate types for which the noise model is relevant.
        
             noise_level1: A double representing the first level of noise to apply.
        
             noise_level2: A double representing the second level of noise to apply.
        
             noise_level3: A double representing the third level of noise to apply.
        
             qubits: A specific qubit vector (QVec) affected by the noise model.
        
        Returns:
             None, as the function configures the noise model in place for the specified gate types and qubit vector.
        
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float, arg3: float, arg4: float, arg5: List[QVec]) -> None:
        """
        Set the noise model for a specific gate type with multiple noise parameters affecting a vector of qubit vectors in the quantum virtual machine.
        
        Args:
             noise_model: The noise model to be applied.
        
             gate_type: The type of gate for which the noise model is relevant.
        
             noise_level1: A double representing the first level of noise to apply.
        
             noise_level2: A double representing the second level of noise to apply.
        
             noise_level3: A double representing the third level of noise to apply.
        
             qubits_list: A vector of qubit vectors (QVec) affected by the noise model.
        
        Returns:
             None, as the function configures the noise model in place for the specified gate type and qubit vectors.
        
        """
        ...

    def set_readout_error(self, probs_list: List[List[float]], qubits: QVec = ...) -> None:
        """
        Set a readout error model for the quantum virtual machine.
        
        Args:
             probs_list: A list of probabilities for readout errors associated with each qubit.
        
             qubits: A vector of qubits (QVec) for which the readout error model applies. Defaults to all qubits if not specified.
        
        Returns:
             None, as this function configures the readout error model in place for the specified qubits.
        
        """
        ...

    def set_reset_error(self, p0: float, p1: float, qubits: QVec = ...) -> None:
        """
        Set a reset error model for the quantum virtual machine.
        
        Args:
             p0: Probability of the qubit resetting to state 0.
        
             p1: Probability of the qubit resetting to state 1.
        
             qubits: A vector of qubits (QVec) for which the reset error model applies. Defaults to all qubits if not specified.
        
        Returns:
             None, as this function configures the reset error model in place for the specified qubits.
        
        """
        ...

    def set_rotation_error(self, arg0: float) -> None:
        """
        Set a rotation error model for the quantum virtual machine.
        
        Args:
             None specified in the function signature, but typically would include error parameters for the rotation.
        
        Returns:
             None, as this function configures the rotation error model in place for the quantum operations.
        
        """
        ...


class Optimizer:
    """
    variational quantum Optimizer class
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        """
        ...

    def get_loss(self) -> float:
        """
        """
        ...

    def get_variables(self) -> List[var]:
        """
        """
        ...

    def run(self, arg0: List[var], arg1: int) -> bool:
        """
        """
        ...


class OptimizerFactory:
    """
    quantum OptimizerFactory class
    """
    def __init__(self) -> None:
        """
        """
        ...

    @overload
    def makeOptimizer(self) -> AbstractOptimizer:
        """
        Create an optimizer of the specified type.
        
        Args:
             optimizer_type: An instance of OptimizerType indicating the desired optimizer.
        
        Returns:
             An instance of the created optimizer.
        
        
        """
        ...

    @overload
    def makeOptimizer(self) -> AbstractOptimizer:
        """
        Create an optimizer using its name.
        
        Args:
             optimizer_name: A string representing the name of the desired optimizer.
        
        Returns:
             An instance of the created optimizer.
        
        """
        ...


class OptimizerMode:
    """
    variational quantum OptimizerMode
    
    Members:
    """
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None:
        """
        """
        ...

    def __eq__(self, other: object) -> bool:
        """
        """
        ...

    def __getstate__(self) -> int:
        """
        """
        ...

    def __hash__(self) -> int:
        """
        """
        ...

    def __index__(self) -> int:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other: object) -> bool:
        """
        """
        ...

    def __setstate__(self, state: int) -> None:
        """
        """
        ...

    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class OptimizerType:
    """
    quantum OptimizerType
    
    Members:
    
      NELDER_MEAD
    
      POWELL
    
      GRADIENT
    """
    __members__: ClassVar[dict] = ...  # read-only
    GRADIENT: ClassVar[OptimizerType] = ...
    NELDER_MEAD: ClassVar[OptimizerType] = ...
    POWELL: ClassVar[OptimizerType] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None:
        """
        """
        ...

    def __eq__(self, other: object) -> bool:
        """
        """
        ...

    def __ge__(self, other: object) -> bool:
        """
        """
        ...

    def __getstate__(self) -> int:
        """
        """
        ...

    def __gt__(self, other: object) -> bool:
        """
        """
        ...

    def __hash__(self) -> int:
        """
        """
        ...

    def __index__(self) -> int:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __le__(self, other: object) -> bool:
        """
        """
        ...

    def __lt__(self, other: object) -> bool:
        """
        """
        ...

    def __ne__(self, other: object) -> bool:
        """
        """
        ...

    def __setstate__(self, state: int) -> None:
        """
        """
        ...

    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class OriginCMem:
    """
    origin quantum cmem
    """
    def __init__(self) -> None:
        """
        Create an instance of OriginCMem.
        This constructor returns a singleton instance of OriginCMem.
        
        """
        ...

    @overload
    def Allocate_CBit(self) -> CBit:
        """
        Allocate a classical bit.
        This method allocates a new classical bit and returns a reference to it.
        
        
        """
        ...

    @overload
    def Allocate_CBit(self, cbit_num: int) -> CBit:
        """
        Allocate a specified number of classical bits.
        
        Args:
             cbit_num: The number of classical bits to allocate.
        
        Returns:
             A reference to the allocated classical bits.
        
        """
        ...

    def Free_CBit(self, cbit: CBit) -> None:
        """
        Free a previously allocated classical bit.
        
        Args:
             cbit: The classical bit to be freed.
        """
        ...

    @overload
    def cAlloc(self) -> CBit:
        """
        Allocate memory for classical bits.
        This method initializes or resets the memory allocation for classical bits.
        
        
        """
        ...

    @overload
    def cAlloc(self, arg0: int) -> CBit:
        """
        Allocate memory for classical bits.
        This method initializes or resets the memory allocation for classical bits.
        
        """
        ...

    def cAlloc_many(self, count: int) -> List[ClassicalCondition]:
        """
        Allocate memory for multiple classical bits.
        
        Args:
             count: The number of classical bits to allocate.
        
        """
        ...

    def cFree(self, classical_cond: ClassicalCondition) -> None:
        """
        Free the allocated memory for a classical condition.
        
        Args:
             classical_cond: The classical condition to be freed.
        
        """
        ...

    @overload
    def cFree_all(self, classical_cond_list: List[ClassicalCondition]) -> None:
        """
        Free memory for a list of classical conditions.
        
        Args:
             classical_cond_list: A vector of classical conditions to be freed.
        
        
        """
        ...

    @overload
    def cFree_all(self) -> None:
        """
        Free all allocated classical memory.
        This method releases all memory associated with classical conditions.
        
        """
        ...

    def clearAll(self) -> None:
        """
        Clear all allocated classical bits.
        This method releases all resources associated with classical bits.
        
        """
        ...

    def getIdleMem(self) -> int:
        """
        Get the amount of idle memory currently available.
        
        Returns:
             The amount of idle memory in terms of qubits.
        
        """
        ...

    def getMaxMem(self) -> int:
        """
        Get the maximum memory capacity.
        
        Returns:
             The maximum memory capacity in terms of qubits.
        """
        ...

    def get_allocate_cbits(self) -> List[ClassicalCondition]:
        """
        Retrieve allocated classical bits.
        Returns a vector of ClassicalCondition representing the allocated cbits.
        
        """
        ...

    def get_capacity(self) -> int:
        """
        Get the capacity of the memory.
        
        Returns:
             The total capacity of the memory in terms of qubits.
        
        """
        ...

    def get_cbit_by_addr(self, cbit_addr: int) -> CBit:
        """
        Get a classical bit by its address.
        
        Args:
             cbit_addr: The address of the classical bit.
        
        Returns:
             A reference to the classical bit associated with the given address
        .
        """
        ...

    def set_capacity(self, arg0: int) -> None:
        """
        Set the capacity of the memory.
        
        Args:
             capacity: The new capacity for the memory in terms of qubits.
        
        """
        ...


class OriginCollection:
    """
    A relatively free data collection class for saving data
    """
    @overload
    def __init__(self) -> None:
        """
        """
        ...

    @overload
    def __init__(self, file_name: str) -> None:
        """
        Construct a new OriginCollection by reading a JSON file.
        This function initializes the OriginCollection with data from the specified JSON file.
        
        Args:
             file_name: The path to the JSON file to read.
        
        Returns:
             An instance of OriginCollection.
        
        
        """
        ...

    @overload
    def __init__(self, arg0: OriginCollection) -> None:
        """
        Construct a new OriginCollection by copying an existing instance.
        This function creates a new OriginCollection as a copy of the provided instance.
        
        Args:
             other: The existing OriginCollection instance to copy.
        
        Returns:
             An instance of OriginCollection.
        
        """
        ...

    def getFilePath(self) -> str:
        """
        Retrieve the file path associated with the OriginCollection.
        This function returns the path to the file linked to the collection.
        
        Returns:
             A string containing the file path.
        
        """
        ...

    def getJsonString(self) -> str:
        """
        Retrieve the JSON string representation of the OriginCollection.
        This function converts the collection's data into a JSON format string.
        
        Returns:
             A string containing the JSON representation of the collection.
        
        """
        ...

    def getKeyVector(self) -> List[str]:
        """
        Retrieve the vector of keys associated with the OriginCollection.
        This function returns a vector containing all the keys in the collection.
        
        Returns:
             A vector of keys.
        
        """
        ...

    def getValue(self, key_name: str) -> List[str]:
        """
        Get the value associated with the specified key name.
        This function retrieves the value stored in the OriginCollection for the given key.
        
        Args:
             key_name: The name of the key whose value is to be retrieved.
        
        Returns:
             The value associated with the specified key.
        
        """
        ...

    @overload
    def getValueByKey(self, key_value: str) -> str:
        """
        Get the value associated with the specified key value.
        This function retrieves the value from the OriginCollection based on the provided key.
        
        Args:
             key_value: The key whose corresponding value is to be retrieved.
        
        Returns:
             The value associated with the specified key value.
        
        
        """
        ...

    @overload
    def getValueByKey(self, key_value: int) -> str:
        """
        Retrieve the value associated with a specified key.
        This function returns the value that corresponds to the given key.
        
        Args:
             key_value: The key for which to retrieve the associated value.
        
        Returns:
             The value associated with the specified key.
        
        """
        ...

    def insertValue(self, key: str, *args) -> None:
        """
        Insert values into the OriginCollection under the specified key.
        This function adds the first value associated with the provided key
        and then inserts additional values from the provided arguments.
        
        Args:
             key: The key under which to insert the values.
        
             args: A variable number of values to be inserted.
        
        Returns:
             None.
        
        """
        ...

    def open(self, file_name: str) -> bool:
        """
        Open and read the JSON file at the specified path.
        This function reads the contents of the JSON file provided.
        
        Args:
             file_name: The path to the JSON file to be read.
        
        Returns:
             None.
        
        """
        ...

    def setNames(self, *args) -> None:
        """
        Set names in the OriginCollection.
        This function accepts a variable number of name arguments and sets them in the OriginCollection.
        
        Args:
             args: A variable number of name strings to be set.
        
        Returns:
             None.
        
        """
        ...

    def write(self) -> bool:
        """
        Write the current data to a JSON file.
        This function saves the current contents to a specified JSON file.
        
        Args:
             None.
        
        Returns:
             None.
        
        """
        ...


class OriginQubitPool:
    """
    quantum qubit pool
    """
    def __init__(self) -> None:
        """
        Initialize the OriginQubitPool singleton instance.
        
        Returns:
             A reference to the existing OriginQubitPool instance.
        
        """
        ...

    def allocateQubitThroughPhyAddress(self, qubit_addr: int) -> Qubit:
        """
        Allocate a qubit using its physical address.
        
        Args:
             qubit_addr: The physical address of the qubit to allocate.
        
        Returns:
             A reference to the allocated qubit.
        
        """
        ...

    def allocateQubitThroughVirAddress(self, qubit_num: int) -> Qubit:
        """
        Allocate a qubit using its virtual address.
        
        Args:
             qubit_num: The virtual address of the qubit to allocate.
        
        Returns:
             A reference to the allocated qubit.
        
        """
        ...

    def clearAll(self) -> None:
        """
        Clear all qubits from the OriginQubitPool.
        This method removes all qubits, resetting the pool to its initial state.
        
        """
        ...

    def getIdleQubit(self) -> int:
        """
        Retrieve an idle qubit from the OriginQubitPool.
        
        Returns:
             An idle qubit if available, otherwise may return a null reference or indicate no idle qubits.
        
        """
        ...

    def getMaxQubit(self) -> int:
        """
        Retrieve the maximum qubit from the OriginQubitPool.
        
        Returns:
             The maximum qubit available in the pool.
        
        """
        ...

    def getPhysicalQubitAddr(self, qubit: Qubit) -> int:
        """
        Retrieve the physical address of a specified qubit.
        
        Args:
             qubit: The qubit for which to retrieve the physical address.
        
        Returns:
             The physical address of the specified qubit.
        
        """
        ...

    def getVirtualQubitAddress(self, qubit: Qubit) -> int:
        """
        Retrieve the virtual address of a specified qubit.
        
        Args:
             qubit: The qubit for which to retrieve the virtual address.
        
        Returns:
             The virtual address of the specified qubit.
        
        """
        ...

    def get_allocate_qubits(self) -> QVec:
        """
        Retrieve currently allocated qubits.
        
        Returns:
             A reference to the vector of currently allocated qubits.
        
        """
        ...

    def get_capacity(self) -> int:
        """
        Get the capacity of the OriginQubitPool.
        
        Returns:
             An integer representing the capacity of the pool.
        
        """
        ...

    def get_max_usedqubit_addr(self) -> int:
        """
        Retrieve the address of the maximum used qubit in the OriginQubitPool.
        
        Returns:
             The address of the maximum used qubit, or an indication if no qubits are in use.
        
        """
        ...

    def get_qubit_by_addr(self, qubit_addr: int) -> Qubit:
        """
        Retrieve a qubit from the pool using its address.
        
        Args:
             qubit_addr: The address of the qubit to retrieve.
        Returns:
             A reference to the requested qubit.
        
        """
        ...

    def qAlloc(self) -> Qubit:
        """
        Allocate a qubit.
        
        Returns:
             A reference to the allocated qubit.
        
        """
        ...

    def qAlloc_many(self, qubit_num: int) -> List[Qubit]:
        """
        Allocate a list of qubits.
        
        Args:
             qubit_num: The number of qubits to allocate.
        
        Returns:
             A reference to the vector of allocated qubits.
        
        """
        ...

    def qFree(self, arg0: Qubit) -> None:
        """
        Free a previously allocated qubit.
        
        Args:
             qubit: The qubit to be freed.
        """
        ...

    @overload
    def qFree_all(self, arg0: QVec) -> None:
        """
        Free all qubits in the specified vector.
        
        Args:
             qubits: A vector of qubits to be freed.
        
        
        """
        ...

    @overload
    def qFree_all(self) -> None:
        """
        Free all allocated qubits in the pool.
        This method releases all qubits that have been allocated previously.
        
        """
        ...

    def set_capacity(self, arg0: int) -> None:
        """
        Set the capacity of the OriginQubitPool.
        
        Args:
             capacity: An integer representing the new capacity to be set.
        
        """
        ...


class PartialAmpQVM(QuantumMachine):
    """
    quantum partial amplitude machine class
    
    """
    def __init__(self) -> None:
        """
        """
        ...

    def get_prob_dict(self, arg0: QVec) -> Dict[str,float]:
        """
        Get the measurement results as a dictionary.
        
        Args:
             qubit_list: A list of qubits to measure.
        
        Returns:
             A dictionary containing the measurement results of the quantum machine.
        
        """
        ...

    def init_qvm(self, backend_type: int = 0) -> None:
        """
        """
        ...

    def pmeasure_bin_index(self, bin_index: str) -> complex:
        """
        Get the amplitude of the quantum state for the specified bin index.
        
        Args:
             bin_index: A string representing the bin.
        
        Returns:
             A complex number representing the amplitude of the bin.
        
        """
        ...

    def pmeasure_dec_index(self, dec_index: str) -> complex:
        """
        Get the amplitude of the quantum state for the specified decimal index.
        
        Args:
             dec_index: A string representing the decimal.
        
        Returns:
             A complex number representing the amplitude of the decimal.
        
        """
        ...

    def pmeasure_subset(self, index_list: List[str]) -> Dict[str,complex]:
        """
        Get the amplitudes of the quantum state for a subset of indices.
        
        Args:
             index_list: A list of strings representing decimal states.
        
        Returns:
             A list of complex numbers representing the amplitude results.
        
        """
        ...

    def prob_run_dict(self, arg0: QProg, arg1: QVec) -> Dict[str,float]:
        """
        Run the quantum program and get the measurement results as a dictionary.
        
        Args:
             qprog: The quantum program to execute.
        
             qubit_list: A list of qubits to measure.
        
        Returns:
             A dictionary containing the measurement results of the quantum machine.
        
        """
        ...

    @overload
    def run(self, qprog: QProg, noise_model: Noise = NoiseModel()) -> None:
        """
        Run the quantum program.
        
        Args:
             qprog: The quantum program to execute.
        
             noise_model: An optional noise model (default is NoiseModel()).
        
        Returns:
             None.
        
        
        """
        ...

    @overload
    def run(self, qprog: QCircuit, noise_model: Noise = NoiseModel()) -> None:
        """
        Run the quantum program.
        
        Args:
             qprog: The quantum circuit to execute.
        
             noise_model: An optional noise model (default is NoiseModel()).
        
        Returns:
             None.
        
        """
        ...


class PhysicalQubit:
    """
    Physical Qubit abstract class
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        """
        ...

    def getQubitAddr(self) -> int:
        """
        Retrieve the address of the physical qubit.
        
        This function returns the address of the physical qubit associated with the instance.
        
        Args:
             None
        
        Returns:
             The address of the physical qubit.
        
        """
        ...


class PilotNoiseParams:
    """
    pliot noise simulate params
    """
    double_gate_param: float
    double_p2: float
    double_pgate: float
    noise_model: str
    single_gate_param: float
    single_p2: float
    single_pgate: float
    def __init__(self, *args, **kwargs) -> None:
        """
        """
        ...


class ProgCount:
    """
    """
    double_gate_layer_num: int
    double_gate_num: int
    gate_num: int
    layer_num: int
    multi_control_gate_num: int
    node_num: int
    selected_gate_nums: Dict[GateType,int]
    single_gate_layer_num: int
    single_gate_num: int
    def __init__(self) -> None:
        """
        """
        ...


class QCircuit:
    """
    quantum circuit node
    """
    @overload
    def __init__(self) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: NodeIter) -> None:
        """
        Initialize QCircuit from a node iterator.
        
        Args:
             iter (NodeIter&): The iterator pointing to the node.
        
        Returns:
             QCircuit: The initialized quantum circuit object.
        
        Raises:
             runtime_error: If the iterator is null or the node type is incorrect.
        
        """
        ...

    def begin(self) -> NodeIter:
        """
        Get an iterator to the first node in the circuit.
        
        Returns:
             Iterator: An iterator pointing to the first node.
        
        """
        ...

    def control(self, control_qubits: QVec) -> QCircuit:
        """
        Apply a control operation to the circuit.
        
        Args:
             control_qubits (list): A list of qubits that will act as control qubits.
        
        Returns:
             QCircuit: The circuit with the control operation applied.
        
        """
        ...

    def dagger(self) -> QCircuit:
        """
        Compute the adjoint (dagger) of the circuit.
        
        Returns:
             QCircuit: The adjoint of this circuit.
        
        """
        ...

    def end(self) -> NodeIter:
        """
        Get an iterator to the end of the circuit.
        
        Returns:
             Iterator: An iterator pointing to the end of the nodes.
        
        """
        ...

    def head(self) -> NodeIter:
        """
        Get an iterator to the head of the circuit.
        
        Returns:
             Iterator: An iterator pointing to the head node.
        
        """
        ...

    @overload
    def insert(self, arg0: QCircuit) -> QCircuit:
        """
        Insert another QCircuit into this circuit.
        
        Args:
             other (QCircuit): The circuit to be inserted.
        
        Returns:
             QCircuit: A reference to this circuit after insertion.
        
        
        """
        ...

    @overload
    def insert(self, arg0: QGate) -> QCircuit:
        """
        Insert a QGate into this circuit.
        
        Args:
             gate (QGate): The gate to be inserted.
        
        Returns:
             QCircuit: A reference to this circuit after the gate insertion.
        
        """
        ...

    def is_empty(self) -> bool:
        """
        Check if the circuit is empty.
        
        Returns:
             bool: True if the circuit has no gates; otherwise, False.
        
        """
        ...

    def last(self) -> NodeIter:
        """
        Get an iterator to the last node in the circuit.
        
        Returns:
             Iterator: An iterator pointing to the last node.
        
        """
        ...

    def set_control(self, control_qubits: QVec) -> None:
        """
        Set control qubits for the circuit.
        
        Args:
             control_qubits (list): A list of qubits to be set as control qubits.
        
        """
        ...

    def set_dagger(self, arg0: bool) -> None:
        """
        Set the dagger property of the circuit.
        
        This method modifies the circuit to represent its adjoint.
        
        """
        ...

    @overload
    def __lshift__(self, arg0: QCircuit) -> QCircuit:
        """
        Left shift operator for QCircuit.
        
        Args:
             other (QCircuit): The circuit to be combined with this circuit.
        
        Returns:
             QCircuit: A new circuit resulting from the left shift operation.
        
        
        """
        ...

    @overload
    def __lshift__(self, arg0: QGate) -> QCircuit:
        """
        Left shift operator for QCircuit with a QGate.
        
        Args:
             other (QGate): The gate to be added to this circuit.
        
        Returns:
             QCircuit: A new circuit resulting from the left shift operation with the gate.
        
        """
        ...


class QCircuitOPtimizerMode:
    """
    Quantum circuit optimize mode
    
    Members:
    
      Merge_H_X
    
      Merge_U3
    
      Merge_RX
    
      Merge_RY
    
      Merge_RZ
    """
    __members__: ClassVar[dict] = ...  # read-only
    Merge_H_X: ClassVar[QCircuitOPtimizerMode] = ...
    Merge_RX: ClassVar[QCircuitOPtimizerMode] = ...
    Merge_RY: ClassVar[QCircuitOPtimizerMode] = ...
    Merge_RZ: ClassVar[QCircuitOPtimizerMode] = ...
    Merge_U3: ClassVar[QCircuitOPtimizerMode] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None:
        """
        """
        ...

    def __eq__(self, other: object) -> bool:
        """
        """
        ...

    def __getstate__(self) -> int:
        """
        """
        ...

    def __hash__(self) -> int:
        """
        """
        ...

    def __index__(self) -> int:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other: object) -> bool:
        """
        """
        ...

    def __or__(self, arg0: QCircuitOPtimizerMode) -> int:
        """
        bitwise or
        """
        ...

    def __setstate__(self, state: int) -> None:
        """
        """
        ...

    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class QError:
    """
    Quantum QError Type
    
    Members:
    
      UndefineError
    
      qErrorNone
    
      qParameterError
    
      qubitError
    
      loadFileError
    
      initStateError
    
      destroyStateError
    
      setComputeUnitError
    
      runProgramError
    
      getResultError
    
      getQStateError
    """
    __members__: ClassVar[dict] = ...  # read-only
    UndefineError: ClassVar[QError] = ...
    __entries: ClassVar[dict] = ...
    destroyStateError: ClassVar[QError] = ...
    getQStateError: ClassVar[QError] = ...
    getResultError: ClassVar[QError] = ...
    initStateError: ClassVar[QError] = ...
    loadFileError: ClassVar[QError] = ...
    qErrorNone: ClassVar[QError] = ...
    qParameterError: ClassVar[QError] = ...
    qubitError: ClassVar[QError] = ...
    runProgramError: ClassVar[QError] = ...
    setComputeUnitError: ClassVar[QError] = ...
    def __init__(self, value: int) -> None:
        """
        """
        ...

    def __eq__(self, other: object) -> bool:
        """
        """
        ...

    def __getstate__(self) -> int:
        """
        """
        ...

    def __hash__(self) -> int:
        """
        """
        ...

    def __index__(self) -> int:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other: object) -> bool:
        """
        """
        ...

    def __setstate__(self, state: int) -> None:
        """
        """
        ...

    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class QGate:
    """
    quantum gate node
    """
    def __init__(self, arg0: NodeIter) -> None:
        """
        Initialize a QGate instance based on the provided iterator.
        This constructor checks the validity of the iterator and ensures it points to a valid gate node.
        
        Args:
             iter: A reference to a NodeIter that points to the node to be initialized.
        
        Returns:
             A QGate instance initialized from the gate node.
        
        """
        ...

    def control(self, control_qubits: QVec) -> QGate:
        """
        Get a controlled quantum gate based on the current QGate instance.
        This function creates a control version of the quantum gate using the specified control qubits.
        
        Args:
             control_qubits: A list of qubits that serve as control qubits for the gate.
        
        Returns:
             A new QGate instance representing the controlled gate.
        
        """
        ...

    @overload
    def dagger(self) -> QGate:
        """
        """
        ...

    @overload
    def dagger(Hermitianconjugate) -> Any:
        """
        """
        ...

    def gate_matrix(self) -> List[complex]:
        """
        Get the matrix representation of the quantum gate.
        
        Args:
             qgate: The quantum gate instance.
        
        Returns:
             QStat: The matrix representation of the quantum gate.
        
        """
        ...

    def gate_type(self) -> int:
        """
        Get the type of the quantum gate.
        
        Args:
             qgate: The quantum gate instance.
        
        Returns:
             The type of the quantum gate.
        
        """
        ...

    def get_control_qubit_num(self) -> int:
        """
        Retrieve the number of control qubits for the QGate instance.
        This function returns the count of qubits that act as control qubits for the gate.
        
        Args:
             None
        
        Returns:
             An integer representing the number of control qubits.
        
        """
        ...

    def get_control_qubits(self, control_qubits: QVec) -> int:
        """
        Get the control vector from the current quantum gate node.
        
        Args:
             control_qubits: The control qubits output vector.
        
        Returns:
             int: Size of the control qubits.
        
        """
        ...

    def get_qubits(self, qubits: QVec) -> int:
        """
        Get the qubit vector inside this quantum gate.
        
        Args:
             qubits: The qubits output vector.
        
        Returns:
             int: Size of the qubits.
        
        """
        ...

    def get_target_qubit_num(self) -> int:
        """
        Retrieve the number of target qubits for the QGate instance.
        This function returns the count of qubits that the quantum gate affects.
        
        Args:
             None
        
        Returns:
             An integer representing the number of target qubits.
        
        """
        ...

    def is_dagger(self) -> bool:
        """
        Check if the QGate instance is a dagger (Hermitian conjugate) of another gate.
        This function determines whether the current gate is the adjoint of its corresponding gate.
        
        Args:
             None
        
        Returns:
             A boolean indicating whether the current gate is a dagger.
        
        """
        ...

    def set_control(self, arg0: QVec) -> bool:
        """
        Set the control qubits for the QGate instance.
        This function specifies which qubits will act as control qubits for the gate.
        
        Args:
             control_qubits: A list of qubits that will serve as control qubits.
        
        Returns:
             None
        
        """
        ...

    def set_dagger(self, arg0: bool) -> bool:
        """
        Set the QGate instance to be a dagger (Hermitian conjugate) of another gate.
        This function configures the current gate to represent its adjoint.
        
        Args:
             None
        
        Returns:
             None
        
        """
        ...


class QITE:
    """
    quantum imaginary time evolution
    """
    def __init__(self) -> None:
        """
        """
        ...

    def exec(self, is_optimization: bool = True) -> int:
        """
        """
        ...

    def get_all_exec_result(self, reverse: bool = False, sort: bool = False) -> List[List[Tuple[int,float]]]:
        """
        """
        ...

    def get_ansatz_list(self, *args, **kwargs) -> Any:
        """
        """
        ...

    def get_ansatz_theta_list(self) -> List[List[float]]:
        """
        """
        ...

    def get_arbitary_cofficient(self, arg0: float) -> None:
        """
        """
        ...

    def get_exec_result(self, reverse: bool = False, sort: bool = False) -> List[Tuple[int,float]]:
        """
        """
        ...

    def get_result(self) -> List[Tuple[int,float]]:
        """
        """
        ...

    def set_Hamiltonian(self, arg0) -> None:
        """
        """
        ...

    def set_ansatz_gate(self, arg0) -> None:
        """
        """
        ...

    def set_convergence_factor_Q(self, arg0: float) -> None:
        """
        """
        ...

    def set_delta_tau(self, arg0: float) -> None:
        """
        """
        ...

    def set_iter_num(self, arg0: int) -> None:
        """
        """
        ...

    def set_log_file(self, arg0: str) -> None:
        """
        """
        ...

    def set_para_update_mode(self, arg0: UpdateMode) -> None:
        """
        """
        ...

    def set_pauli_matrix(self, arg0: QuantumMachine, arg1: numpy.ndarray[numpy.float64[m,n]]) -> None:
        """
        """
        ...

    def set_quantum_machine_type(self, arg0: QMachineType) -> None:
        """
        """
        ...

    def set_upthrow_num(self, arg0: int) -> None:
        """
        """
        ...


class QIfProg:
    """
    quantum if prog node
    """
    @overload
    def __init__(self, arg0: NodeIter) -> None:
        """
        Constructor for QIfProg.
        
        Args:
             iter: An iterator to a node.
        
        Raises:
             runtime_error: If the iterator is null or the node type is incorrect.
        
        
        """
        ...

    @overload
    def __init__(self, classical_cond: ClassicalCondition, true_branch_qprog: QProg) -> None:
        """
        Constructor for initializing with a classical condition and a quantum program.
        
        Args:
             classical_cond: The classical condition to evaluate.
        
             true_branch_qprog: The quantum program to execute if the condition is true.
        
        
        """
        ...

    @overload
    def __init__(self, classical_cond: ClassicalCondition, true_branch_qprog: QProg, false_branch_qprog: QProg) -> None:
        """
        Constructor for initializing with a classical condition and two quantum programs.
        
        Args:
             classical_cond: The classical condition to evaluate.
        
             true_branch_qprog: The quantum program to execute if the condition is true.
        
             false_branch_qprog: The quantum program to execute if the condition is false.
        
        """
        ...

    def get_classical_condition(self) -> ClassicalCondition:
        """
        Retrieve the classical condition associated with the quantum if program.
        
        Returns:
             The classical condition object used in the if statement.
        
        """
        ...

    def get_false_branch(self) -> QProg:
        """
        Get the quantum program corresponding to the false branch.
        
        Returns:
             QProg: The quantum program for the false branch, or an empty QProg if null.
        
        Raises:
             runtime_error: If the false branch has an incorrect node type.
        
        """
        ...

    def get_true_branch(self) -> QProg:
        """
        Get the quantum program corresponding to the true branch.
        
        Returns:
             QProg: The quantum program for the true branch.
        
        Raises:
             runtime_error: If the true branch is null or has an incorrect node type.
        
        """
        ...


class QMachineType:
    """
    Quantum machine type
    
    Members:
    
      CPU
    
      GPU
    
      CPU_SINGLE_THREAD
    
      NOISE
    """
    __members__: ClassVar[dict] = ...  # read-only
    CPU: ClassVar[QMachineType] = ...
    CPU_SINGLE_THREAD: ClassVar[QMachineType] = ...
    GPU: ClassVar[QMachineType] = ...
    NOISE: ClassVar[QMachineType] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None:
        """
        """
        ...

    def __eq__(self, other: object) -> bool:
        """
        """
        ...

    def __getstate__(self) -> int:
        """
        """
        ...

    def __hash__(self) -> int:
        """
        """
        ...

    def __index__(self) -> int:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other: object) -> bool:
        """
        """
        ...

    def __setstate__(self, state: int) -> None:
        """
        """
        ...

    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class QMeasure:
    """
    quantum measure node
    """
    def __init__(self, arg0: NodeIter) -> None:
        """
        Initialize QMeasure from a node iterator.
        
        Args:
             iter (NodeIter&): The iterator pointing to the node.
        
        Returns:
             QMeasure: The initialized measurement object.
        
        Raises:
             runtime_error: If the iterator is null or the node type is incorrect.
        
        """
        ...


class QOperator:
    """
    quantum operator class
    """
    @overload
    def __init__(self) -> None:
        """
        Initialize a new QOperator instance.
        
        Args:
             None
        
        Returns:
             A new QOperator instance.
        
        
        """
        ...

    @overload
    def __init__(self, arg0: QGate) -> None:
        """
        Initialize QOperator based on a quantum gate.
        
        Args:
             qgate: An instance of QGate.
        
        Returns:
             A new QOperator instance.
        
        
        """
        ...

    @overload
    def __init__(self, arg0: QCircuit) -> None:
        """
        Initialize QOperator based on a quantum circuit.
        
        Args:
             qcircuit: An instance of QCircuit.
        
        Returns:
             A new QOperator instance.
        
        """
        ...

    def get_matrix(self) -> List[complex]:
        """
        Retrieve the matrix representation of the QOperator.
        
        Args:
             None
        
        Returns:
             The matrix representation of the QOperator.
        
        """
        ...

    def to_instruction(self, arg0: str) -> str:
        """
        Convert the QOperator to an instruction representation.
        
        Args:
             None
        
        Returns:
             The instruction representation of the QOperator.
        
        """
        ...


class QOptimizationResult:
    """
    quantum QOptimizationResult class
    """
    fcalls: int
    fun_val: float
    iters: int
    key: str
    message: str
    para: List[float]
    def __init__(self, arg0: str, arg1: int, arg2: int, arg3: str, arg4: float, arg5: List[float]) -> None:
        """
        Initialize a QOptimizationResult instance.
        
        Args:
             message: A string containing the result message.
        
             iteration: A size_t representing the iteration count.
        
             total_iterations: A size_t representing the total iterations.
        
             status: A string indicating the optimization status.
        
             value: A double representing the optimization value.
        
             results: A vector of doubles for the optimization results.
        
        """
        ...


class QPilotOSService(QuantumMachine):
    """
    origin quantum pilot OS Machine
    """
    def __init__(self, machine_type: str = 'CPU') -> None:
        """
        """
        ...

    def build_expectation_task_msg(self, prog: QProg, hamiltonian: str, qubits: List[int] = [], shot: int = 1000, chip_id: int = 33554432, is_amend: bool = True, is_mapping: bool = True, is_optimization: bool = True, specified_block: List[int] = [], task_describe: str = '') -> str:
        """
        use C++ to build a expectation task body.
        """
        ...

    def build_init_msg(self, api_key: str) -> str:
        """
        """
        ...

    def build_qst_task_msg(self, prog: QProg, shot: int = 1000, chip_id: int = 33554432, is_amend: bool = True, is_mapping: bool = True, is_optimization: bool = True, specified_block: List[int] = [], task_describe: str = '') -> str:
        """
        use C++ to build ordinary qst task msg body
        """
        ...

    def build_query_msg(self, task_id: str) -> str:
        """
        """
        ...

    def build_task_msg(self, prog: List[QProg], shot: int, chip_id: int, is_amend: bool, is_mapping: bool, is_optimization: bool, specified_block: List[int], task_describe: str) -> str:
        """
        use c++ to build real chip measure task msg body.
        """
        ...

    @overload
    def cAlloc(self) -> ClassicalCondition:
        """
        Allocate a cbit
        
        """
        ...

    @overload
    def cAlloc(self, cbit: int) -> ClassicalCondition:
        """
        Allocate a cbit
        """
        ...

    def cAlloc_many(self, cbit_num: int) -> List[ClassicalCondition]:
        """
        Allocate a list of cbits
        """
        ...

    def cFree(self, arg0: ClassicalCondition) -> None:
        """
        Free a cbit
        """
        ...

    @overload
    def cFree_all(self, cbit_list: List[ClassicalCondition]) -> None:
        """
        Free a list of cbits
        
        """
        ...

    @overload
    def cFree_all(self) -> None:
        """
        Free all of cbits
        """
        ...

    def finalize(self) -> None:
        """
        finalize
        """
        ...

    def get_token(self, rep_json: str) -> ErrorCode:
        """
        """
        ...

    def init(self) -> None:
        """
        """
        ...

    def init_config(self, url: str, log_cout: bool) -> None:
        """
        """
        ...

    def parse_prob_counts_result(self, result_str: List[str]) -> List[Dict[str,int]]:
        """
        Parse result str to map<string, double>
        Args:
            result_str: Taeget result string
        
        Returns:
            array: vector<map<string, double>>
        Raises:
            none
        
        """
        ...

    def parse_probability_result(self, result_str: List[str]) -> List[Dict[str,float]]:
        """
        Parse result str to map<string, double>
        Args:
            result_str: Taeget result string
        
        Returns:
            array: vector<map<string, double>>
        Raises:
            none
        
        """
        ...

    def parse_task_result(self, result_str: str) -> Dict[str,float]:
        """
        Parse result str to map<string, double>
        Args:
            result_str: Taeget result string
        
        Returns:
            dict: map<string, double>
        Raises:
            none
        
        """
        ...

    def parser_expectation_result(self, json_str: str) -> list:
        """
        deprecated, use Python's json lib.
        """
        ...

    def parser_sync_result(self, json_str: str) -> list:
        """
        """
        ...

    def qAlloc(self) -> Qubit:
        """
        Allocate a qubit
        """
        ...

    def qAlloc_many(self, qubit_num: int) -> List[Qubit]:
        """
        Allocate a list of qubits
        """
        ...

    def qFree(self, qubit: Qubit) -> None:
        """
        Free a qubit
        """
        ...

    @overload
    def qFree_all(self, qubit_list: QVec) -> None:
        """
        Free a list of qubits
        
        """
        ...

    @overload
    def qFree_all(self, arg0: QVec) -> None:
        """
        Free all of qubits
        """
        ...

    def set_config(self, max_qubit: int, max_cbit: int) -> None:
        """
        set QVM max qubit and max cbit
        
        Args:
            max_qubit: quantum machine max qubit num 
            max_cbit: quantum machine max cbit num 
        
        Returns:
            none
        Raises:
            run_fail: An error occurred in set_configure
        
        """
        ...

    def tcp_recv(self, ip: str, port: int, task_id: str) -> list:
        """
        """
        ...


class QProg:
    """
    Quantum program,can construct quantum circuit,data struct is linked list
    """
    @overload
    def __init__(self) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: QProg) -> None:
        """
        Construct a program node.
        
        Args:
             quantum_prog: The quantum program reference.
        
        Returns:
             A new program node.
        
        
        """
        ...

    @overload
    def __init__(self, arg0: QCircuit) -> None:
        """
        Construct a program node from a QCircuit node.
        
        Args:
             qcircuit: The QCircuit reference.
        
        Returns:
             A new program node.
        
        
        """
        ...

    @overload
    def __init__(self, arg0: QIfProg) -> None:
        """
        Construct a program node from a QIfProg node.
        
        Args:
             qifprog: The QIfProg reference.
        
        Returns:
             A new program node.
        
        
        """
        ...

    @overload
    def __init__(self, arg0: QWhileProg) -> None:
        """
        Construct a program node from a QWhileProg node.
        
        Args:
             qwhileprog: The QWhileProg reference.
        
        Returns:
             A new program node.
        
        
        """
        ...

    @overload
    def __init__(self, arg0: QGate) -> None:
        """
        Construct a program node from a QGate node.
        
        Args:
             qgate: The QGate reference.
        
        Returns:
             A new program node.
        
        
        """
        ...

    @overload
    def __init__(self, arg0: QMeasure) -> None:
        """
        Construct a program node from a QMeasure node.
        
        Args:
             qmeasure: The QMeasure reference.
        
        Returns:
             A new program node.
        
        
        """
        ...

    @overload
    def __init__(self, arg0: QReset) -> None:
        """
        Construct a program node from a QReset node.
        
        Args:
             qreset: The QReset reference.
        
        Returns:
             A new program node.
        
        
        """
        ...

    @overload
    def __init__(self, arg0: ClassicalCondition) -> None:
        """
        Construct a program node from a ClassicalCondition node.
        
        Args:
             classical_condition: The ClassicalCondition reference.
        
        Returns:
             A new program node.
        
        
        """
        ...

    @overload
    def __init__(self, arg0: NodeIter) -> None:
        """
        Construct a program node from a node iterator.
        
        Args:
             iter: The iterator for the node.
        
        Returns:
             A new program node.
        
        """
        ...

    def begin(self) -> NodeIter:
        """
        Get an iterator to the first node in the program.
        
        Returns:
             A reference to the iterator pointing to the first node.
        
        """
        ...

    def end(self) -> NodeIter:
        """
        Get an iterator to the end of the program.
        
        Returns:
             A reference to the iterator pointing past the last node.
        
        """
        ...

    def get_max_qubit_addr(self) -> int:
        """
        """
        ...

    def get_qgate_num(self) -> int:
        """
        """
        ...

    def get_used_cbits(self, cbit_vector: List[ClassicalCondition]) -> List[ClassicalCondition]:
        """
        Get a list of classical bits used in the program.
        
        Args:
             cbit_vector: The vector to store the used classical bits.
        
        Returns:
             A reference to the updated classical bit vector.
        
        """
        ...

    def get_used_qubits(self, qubit_vector: QVec) -> QVec:
        """
        Get a list of qubits used in the program.
        
        Args:
             qubit_vector: The vector to store the used qubits.
        
        Returns:
             A reference to the updated qubit vector.
        
        """
        ...

    def head(self) -> NodeIter:
        """
        Get an iterator to the head node of the program.
        
        Returns:
             A reference to the iterator pointing to the head node.
        
        """
        ...

    @overload
    def insert(self, arg0: QProg) -> QProg:
        """
        Insert a program into the current program.
        
        Args:
             program: The program to be inserted.
        
        Returns:
             A reference to the updated program after insertion.
        
        
        """
        ...

    @overload
    def insert(self, arg0: QGate) -> QProg:
        """
        Insert a gate into the current program.
        
        Args:
             gate: The gate to be inserted.
        
        Returns:
             A reference to the updated program after insertion.
        
        
        """
        ...

    @overload
    def insert(self, arg0: QCircuit) -> QProg:
        """
        Insert a circuit into the current program.
        
        Args:
             circuit: The circuit to be inserted.
        
        Returns:
             A reference to the updated program after insertion.
        
        
        """
        ...

    @overload
    def insert(self, arg0: QIfProg) -> QProg:
        """
        Insert an if program into the current program.
        
        Args:
             if_program: The if program to be inserted.
        
        Returns:
             A reference to the updated program after insertion.
        
        
        """
        ...

    @overload
    def insert(self, arg0: QWhileProg) -> QProg:
        """
        Insert a QWhileProg into the program.
        
        Returns:
             A reference to the updated program.
        
        
        """
        ...

    @overload
    def insert(self, arg0: QMeasure) -> QProg:
        """
        Insert a QMeasure into the program.
        
        Returns:
             A reference to the updated program.
        
        
        """
        ...

    @overload
    def insert(self, arg0: QReset) -> QProg:
        """
        Insert a QReset into the program.
        
        Args:
             reset_op: The reset operation to be inserted.
        
        Returns:
             A reference to the updated program.
        
        
        """
        ...

    @overload
    def insert(self, arg0: ClassicalCondition) -> QProg:
        """
        Insert a ClassicalCondition into the program.
        
        Args:
             condition_op: The classical condition operation to be inserted.
        
        Returns:
             A reference to the updated program.
        
        """
        ...

    def is_empty(self) -> bool:
        """
        """
        ...

    def is_measure_last_pos(self) -> bool:
        """
        Check if the last operation in the program is a measurement.
        
        Returns:
             True if the last operation is a measurement, otherwise False.
        
        """
        ...

    def last(self) -> NodeIter:
        """
        Get an iterator to the last node in the program.
        
        Args:
             None
        
        Returns:
             A reference to the iterator pointing to the last node.
        
        """
        ...

    @overload
    def __lshift__(self, arg0: QProg) -> QProg:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: QGate) -> QProg:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: QCircuit) -> QProg:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: QIfProg) -> QProg:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: QWhileProg) -> QProg:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: QMeasure) -> QProg:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: QReset) -> QProg:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: ClassicalCondition) -> QProg:
        """
        """
        ...


class QProgDAG:
    """
    quantum prog dag class
    """
    def __init__(self) -> None:
        """
        """
        ...

    def get_edges(self) -> List[QProgDAGEdge]:
        """
        Retrieve the set of edges in the quantum program DAG.
        
        Returns:
             List[QProgDAGEdge]: A list of edges in the DAG.
        
        """
        ...

    def get_target_vertex(self, vertice_num: int) -> QProgDAGVertex:
        """
        Retrieve a target vertex from the quantum program DAG.
        
        Args:
             vertice_num: The index of the vertex to retrieve.
        
        Returns:
             QVertex: A reference to the specified vertex in the DAG.
        
        """
        ...

    def get_vertex_set(self) -> List[QProgDAGVertex]:
        """
        Retrieve the set of vertices in the quantum program DAG.
        
        Args:
             QVec: The set of vertices.
        
        Returns:
             QVec: A reference to the vector of vertices in the DAG.
        
        """
        ...


class QProgDAGEdge:
    """
    quantum prog dag edge
    """
    m_from: int
    m_qubit: int
    m_to: int
    def __init__(self, from_arg: int, to_arg: int, qubit_arg: int) -> None:
        """
        Initialize a quantum program DAG edge.
        
        Args:
             from_arg: The starting node of the edge.
        
             to_arg: The ending node of the edge.
        
             qubit_arg: The qubit associated with the edge.
        
        """
        ...


class QProgDAGVertex:
    """
    quantum prog dag vertex node
    """
    m_id: int
    m_layer: int
    m_pre_node: List[int]
    m_succ_node: List[int]
    m_type: DAGNodeType
    def __init__(self) -> None:
        """
        Initialize a quantum program DAG vertex.
        This vertex represents a node in the quantum program's directed acyclic graph (DAG).
        """
        ...

    def get_control_vec(self) -> QVec:
        """
        Retrieve the vector of control qubits associated with the vertex.
        """
        ...

    def get_iter(self) -> NodeIter:
        """
        Retrieve the iterator associated with the vertex.
        """
        ...

    def get_qubits_vec(self) -> QVec:
        """
        Retrieve the vector of qubits associated with the vertex.
        """
        ...

    def is_dagger(self) -> bool:
        """
        Check if the vertex is a dagger operation.
        """
        ...


class QReset:
    """
    quantum reset node
    """
    def __init__(self, arg0: NodeIter) -> None:
        """
        Initialize QReset from a node iterator.
        
        Args:
             iter (NodeIter&): The iterator pointing to the node.
        
        Returns:
             QReset: The initialized reset object.
        
        Raises:
             runtime_error: If the iterator is null or the node type is incorrect.
        
        """
        ...


class QResult:
    """
    QResult abstract class, this class contains the result of the quantum measurement
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        """
        ...

    def getResultMap(self) -> Dict[str,bool]:
        """
        """
        ...


class QVec:
    """
    Qubit vector basic class
    """
    @overload
    def __init__(self) -> None:
        """
        Default constructor for QVec.
        
        Args:
             None
        
        Returns:
             A new instance of QVec.
        
        
        """
        ...

    @overload
    def __init__(self, qubit_list: List[Qubit]) -> None:
        """
        Constructor that initializes QVec with a list of qubits.
        
        Args:
             qubit_list: A reference to a vector of pointers to Qubit instances.
        
        Returns:
             A new instance of QVec initialized with the provided qubits.
        
        
        """
        ...

    @overload
    def __init__(self, qvec: QVec) -> None:
        """
        Copy constructor for QVec.
        
        Args:
             qvec: A reference to an existing QVec instance.
        
        Returns:
             A new instance of QVec that is a copy of the provided instance.
        
        
        """
        ...

    @overload
    def __init__(self, qubit: Qubit) -> None:
        """
        Constructor that initializes QVec with a single qubit.
        
        Args:
             qubit: A pointer to a Qubit instance.
        
        Returns:
             A new instance of QVec initialized with the provided qubit.
        
        """
        ...

    def append(self, qubit: Qubit) -> None:
        """
        Add a qubit to the end of the QVec.
        
        Args:
             qubit: A pointer to the Qubit to be added.
        
        Returns:
             None.
        
        """
        ...

    def pop(self) -> None:
        """
        Remove and return the last qubit from the QVec.
        
        Args:
             None
        
        Returns:
             A pointer to the removed Qubit.
        
        """
        ...

    def to_list(self) -> List[Qubit]:
        """
        Convert the QVec to a standard vector of qubit pointers.
        
        Args:
             None
        
        Returns:
             A vector containing pointers to the qubits in the QVec.
        
        """
        ...

    @overload
    def __getitem__(self, qubit_addr: int) -> Qubit:
        """
        Retrieve a qubit by its index.
        
        Args:
             qubit_addr: The index of the qubit to retrieve.
        
        Returns:
             A reference to the Qubit at the specified index.
        
        
        """
        ...

    @overload
    def __getitem__(self, classical_cond) -> Qubit:
        """
        Retrieve a qubit based on a classical condition.
        
        Args:
             classical_cond: The classical condition to evaluate.
        
        Returns:
             A reference to the Qubit associated with the provided condition.
        
        """
        ...

    def __len__(self) -> int:
        """
        Get the number of qubits in the QVec.
        
        Args:
             None
        
        Returns:
             The count of qubits in the QVec.
        
        """
        ...


class QWhileProg:
    """
    quantum while node
    """
    @overload
    def __init__(self, arg0: NodeIter) -> None:
        """
        Initialize QWhileProg from a node iterator.
        
        Args:
             iter (NodeIter&): The iterator pointing to the node.
        
        Raises:
             runtime_error: If the iterator is null or the node type is incorrect.
        
        
        """
        ...

    @overload
    def __init__(self, arg0: ClassicalCondition, arg1: QProg) -> None:
        """
        """
        ...

    def get_classical_condition(self) -> ClassicalCondition:
        """
        Retrieve the classical condition associated with the while program.
        
        Returns:
             The classical condition object used in the while statement.
        
        """
        ...

    def get_true_branch(self) -> QProg:
        """
        Retrieve the quantum program corresponding to the true branch.
        
        Returns:
             QProg: The quantum program for the true branch.
        
        Raises:
             runtime_error: If the true branch is null or has an incorrect node type.
        
        """
        ...


class QuantumMachine:
    """
    quantum machine base class
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        """
        ...

    def allocate_qubit_through_phy_address(self, address: int) -> Qubit:
        """
        Allocate qubits through physical address.
        
        This function allocates qubits using the specified physical address.
        
        Args:
             address: The physical address of the qubit.
        
        Returns:
             The allocated qubit.
        
        """
        ...

    def allocate_qubit_through_vir_address(self, address: int) -> Qubit:
        """
        Allocate a qubit using its physical address.
        
        This function allocates a qubit based on the specified physical address.
        
        Args:
             address: The physical address of the qubit to allocate.
        
        Returns:
             A reference to the allocated Qubit.
        
        """
        ...

    def async_run(self, qprog: QProg, noise_model: Noise = NoiseModel()) -> None:
        """
        Execute the quantum program asynchronously in the background.
        
        This function runs the specified quantum program without blocking the main thread.
        
        You can check the progress using get_processed_qgate_num(), determine if the process
        
        is finished with is_async_finished(), and retrieve results with get_async_result().
        
        Args:
             qprog: The quantum program to run.
        
             noise_model: (optional) The noise model to apply (default is NoiseModel()).
        
        Returns:
             A reference indicating the status of the asynchronous operation.
        
        """
        ...

    @overload
    def cAlloc(self) -> ClassicalCondition:
        """
        Allocate a classical bit (CBit).
        
        This function must be called after init().
        
        Args:
             None
        
        Returns:
             CBit: A reference to the allocated classical bit.
        
        
        """
        ...

    @overload
    def cAlloc(self, cbit: int) -> ClassicalCondition:
        """
        Allocate a classical bit (CBit) in the QuantumMachine.
        
        This function allocates a CBit after the quantum machine has been initialized.
        
        Args:
             cbit_addr: The address of the CBit to allocate, which should be in the range [0, 29).
        
        Returns:
             Reference to the allocated CBit.
        
        """
        ...

    def cAlloc_many(self, cbit_num: int) -> List[ClassicalCondition]:
        """
        Allocate multiple classical bits (CBits).
        
        This function must be called after init().
        
        Args:
             cbit_num: The number of classical bits to allocate.
        
        Returns:
             list[CBit]: A list of allocated classical bits.
        
        """
        ...

    def cFree(self, arg0: ClassicalCondition) -> None:
        """
        Free a classical bit (CBit).
        
        This function deallocates a previously allocated classical bit.
        
        Args:
             CBit: The classical bit to be freed.
        
        Returns:
             None: This function does not return a value.
        
        """
        ...

    @overload
    def cFree_all(self, cbit_list: List[ClassicalCondition]) -> None:
        """
        Free all allocated classical bits (CBits).
        
        This function deallocates all classical bits provided in the input list.
        
        Args:
             None
        
        Returns:
             None: This function does not return a value.
        
        
        """
        ...

    @overload
    def cFree_all(self) -> None:
        """
        Free all classical bits (CBits).
        
        This function deallocates all classical bits that have been previously allocated.
        
        Args:
             None
        
        Returns:
             None: This function does not return a value.
        
        """
        ...

    def directly_run(self, qprog: QProg, noise_model: Noise = NoiseModel()) -> Dict[str,bool]:
        """
        Directly execute the quantum program.
        
        This function runs the specified quantum program immediately after the
        
        initialization (init()). It supports an optional noise model, which is
        
        currently only applicable to CPUQVM.
        
        Args:
             qprog: The quantum program to run.
        
             noise_model: (optional) The noise model to apply (default is no noise).
        
        Returns:
             A dictionary with the execution results:
                 The final qubit register state.
                 The measurement probabilities.
        
        """
        ...

    def finalize(self) -> None:
        """
        Finalize the quantum machine.
        
        Args:
             None
        
        Returns:
             None
        
        """
        ...

    def getAllocateCMem(self) -> int:
        """
        Get the list of allocated classical bits (cbits) in the QuantumMachine.
        
        This function retrieves the cbits that have been allocated for use in the quantum machine.
        
        Args:
             None
        
        Returns:
             List of allocated cbits.
        
        """
        ...

    def getAllocateQubitNum(self) -> int:
        """
        Get the list of allocated qubits in the QuantumMachine.
        
        This function retrieves the qubits that have been allocated for use in the quantum machine.
        
        Args:
             None
        
        Returns:
             List of allocated qubits.
        
        """
        ...

    def getStatus(self, *args, **kwargs) -> Any:
        """
        Get the status of the Quantum machine.
        
        This function retrieves the current status of the Quantum machine.
        
        Args:
             None
        
        Returns:
             QMachineStatus: The status of the Quantum machine.
        
        """
        ...

    def get_allocate_cbits(self) -> List[ClassicalCondition]:
        """
        Retrieve the list of allocated cbits in the QuantumMachine.
        
        This function returns a list of currently allocated cbits.
        
        Args:
             None
        
        Returns:
             A list of allocated cbits.
        
        """
        ...

    def get_allocate_cmem_num(self) -> int:
        """
        Retrieve the list of allocated cbits in the QuantumMachine.
        
        This function returns the currently allocated cbits.
        
        Args:
             None
        
        Returns:
             A list of allocated cbits.
        
        """
        ...

    def get_allocate_qubit_num(self) -> int:
        """
        Retrieve the list of allocated qubits in the QuantumMachine.
        
        This function returns the currently allocated qubits.
        
        Args:
             None
        
        Returns:
             A list of allocated qubits.
        
        """
        ...

    def get_allocate_qubits(self) -> List[Qubit]:
        """
        Retrieve the list of allocated qubits in the QuantumMachine.
        
        This function returns a list of currently allocated qubits.
        
        Args:
             None
        
        Returns:
             A list of allocated qubits.
        
        """
        ...

    def get_async_result(self) -> Dict[str,bool]:
        """
        Retrieve the result of the asynchronous quantum program execution.
        
        This function blocks the current code until the asynchronous process initiated
        
        by async_run() is complete, then returns the results.
        
        Returns:
             The result of the asynchronous execution.
        
        """
        ...

    @overload
    def get_expectation(self, qprog: QProg, hamiltonian: List[Tuple[Dict[int,str],float]], qubit_list: QVec) -> float:
        """
        Calculate the expectation value of the given Hamiltonian.
        
        This function computes the expectation value based on the provided quantum program,
        
        Hamiltonian, and list of qubits to measure.
        
        Args:
             qprog: The quantum program to execute.
        
             hamiltonian: The Hamiltonian for which the expectation is calculated.
        
             qubit_list: A list of qubits to measure.
        
        Returns:
             A double representing the expectation value of the current Hamiltonian.
        
        
        """
        ...

    @overload
    def get_expectation(self, qprog: QProg, hamiltonian: List[Tuple[Dict[int,str],float]], qubit_list: QVec, shots: int) -> float:
        """
        Calculate the expectation value of the given Hamiltonian with specified measurement shots.
        
        This function computes the expectation value based on the provided quantum program,
        
        Hamiltonian, list of qubits to measure, and the number of measurement shots.
        
        Args:
             qprog: The quantum program to execute.
        
             hamiltonian: The Hamiltonian for which the expectation is calculated.
        
             qubit_list: A list of qubits to measure.
        
             shots: The number of measurement shots to perform.
        
        Returns:
             A double representing the expectation value of the current Hamiltonian.
        
        """
        ...

    def get_gate_time_map(self) -> Dict[GateType,int]:
        """
        Retrieve the gate time mapping for the QuantumMachine.
        
        This function returns a map of gates to their corresponding execution times.
        
        Args:
             None
        
        Returns:
             A reference to the gate time map.
        
        """
        ...

    def get_processed_qgate_num(self) -> int:
        """
        Retrieve the number of processed quantum gates.
        
        This function returns the total count of quantum gates that have been processed
        
        by the QuantumMachine.
        
        Returns:
             An integer representing the number of processed quantum gates.
        
        """
        ...

    def get_qstate(self) -> List[complex]:
        """
        Get the status of the quantum machine.
        
        Args:
             None
        
        Returns:
             QMachineStatus: The current status of the quantum machine.
        
        """
        ...

    def get_status(self, *args, **kwargs) -> Any:
        """
        Retrieve the status of the QuantumMachine.
        
        This function returns the current status of the quantum machine.
        
        Args:
             None
        
        Returns:
             The status of the Quantum machine, represented as a QMachineStatus.
        
        """
        ...

    def initQVM(self) -> None:
        """
        Initialize the global unique quantum machine in the background.
        
        This function sets up the quantum machine based on the specified type.
        
        Args:
             machine_type: The type of quantum machine to initialize, as defined in pyQPanda.QMachineType.
        
        Returns:
             bool: True if the initialization is successful, otherwise false.
        
        """
        ...

    def init_qvm(self) -> None:
        """
        Initialize the global unique quantum machine in the background.
        
        This function sets up the quantum machine based on the specified type.
        
        Args:
             machine_type: The type of quantum machine to initialize, as defined in pyQPanda.QMachineType.
        
        Returns:
             bool: True if the initialization is successful, otherwise false.
        
        """
        ...

    def init_sparse_state(self, *args, **kwargs) -> Any:
        """
        Initialize a sparse quantum state for the QuantumMachine.
        
        This function sets the initial sparse state of the quantum machine.
        
        Args:
             state: A map representing the sparse state, where keys are state identifiers and values are qcomplex_t. Defaults to an empty map.
        
             qlist: The list of qubits to which the sparse state will be applied, represented as a QVec object. Defaults to QVec().
        
        Returns:
             Reference to the updated quantum machine.
        
        """
        ...

    def init_state(self, state: List[complex] = QStat(), qlist: QVec = QVec()) -> None:
        """
        Initialize the quantum state of the QuantumMachine.
        
        This function sets the initial state of the quantum machine.
        
        Args:
             state: The initial quantum state, represented as a QStat object. Defaults to QStat().
        
             qlist: The list of qubits to which the state will be applied, represented as a QVec object. Defaults to QVec().
        
        Returns:
             Reference to the updated quantum machine.
        
        """
        ...

    def is_async_finished(self) -> bool:
        """
        Check if the asynchronous quantum program execution is complete.
        
        This function returns a boolean indicating whether the asynchronous process
        
        initiated by async_run() has finished.
        
        Returns:
             True if the process is complete, False otherwise.
        
        """
        ...

    def qAlloc(self) -> Qubit:
        """
        Allocate a qubit.
        
        This function must be called after init().
        
        Args:
             qubit_addr: The physical address of the qubit, should be in the range [0, 29).
        
        """
        ...

    def qAlloc_many(self, qubit_num: int) -> List[Qubit]:
        """
        Allocate multiple qubits.
        
        This function must be called after init().
        
        Args:
             qubit_num: The number of qubits to allocate.
        
        Returns:
             list[Qubit]: A list of allocated qubits.
        
        """
        ...

    def qFree(self, qubit: Qubit) -> None:
        """
        Free a qubit.
        
        This function deallocates a previously allocated qubit.
        
        Args:
             qubit: The Qubit to be freed.
        
        Returns:
             None: This function does not return a value.
        
        """
        ...

    @overload
    def qFree_all(self, qubit_list: QVec) -> None:
        """
        Free all allocated qubits.
        
        This function deallocates all qubits that have been previously allocated.
        
        Args:
             None
        
        Returns:
             None: This function does not return a value.
        
        
        """
        ...

    @overload
    def qFree_all(self, arg0: QVec) -> None:
        """
        Free all qubits.
        
        This function deallocates all qubits provided in the input vector.
        
        Args:
             None
        
        Returns:
             None: This function does not return a value.
        
        """
        ...

    @overload
    def run_with_configuration(self, qprog: QProg, cbit_list: List[ClassicalCondition], data: dict, noise_model: Noise = NoiseModel()) -> Dict[str,int]:
        """
        Execute the quantum program with a specified configuration.
        
        This function runs the quantum program using the provided classical bits,
        
        parameters, and an optional noise model. It supports multiple shots for
        
        repeated execution.
        
        Args:
             qprog: The quantum program to execute.
        
             cbit_list: The list of classical bits.
        
             data: Parameters for the execution in dictionary form.
        
             noise_model: (optional) The noise model to apply (default is no noise).
        
        Returns:
             The execution results over the specified shots, including:
                 The final qubit register state.
                 The count of hits for each outcome.
        
        
        """
        ...

    @overload
    def run_with_configuration(self, qprog: QProg, cbit_list: List[ClassicalCondition], shot: int, noise_model: Noise = NoiseModel()) -> Dict[str,int]:
        """
        Execute the quantum program with a specified configuration.
        
        This function runs the quantum program using the provided classical bits,
        
        parameters, and an optional noise model. It supports multiple shots for
        
        repeated execution.
        
        Args:
             qprog: The quantum program to execute.
        
             cbit_list: The list of classical bits.
        
             shot: The number of times to repeat the execution.
        
             noise_model: (optional) The noise model to apply (default is no noise).
        
        Note: Noise models currently only work on CPUQVM.
        
        Returns:
             A tuple containing the results of the quantum program execution:
                 The final qubit register state.
                 The count of hits for each outcome.
        
        
        """
        ...

    @overload
    def run_with_configuration(self, qprog: QProg, shot: int, noise_model: Noise = NoiseModel()) -> Dict[str,int]:
        """
        Execute the quantum program with a specified configuration.
        
        This function runs the quantum program using the provided quantum program,
        
        number of shots, and an optional noise model. It supports multiple shots
        
        for repeated execution.
        
        Args:
             qprog: The quantum program to execute.
        
             shot: The number of times to repeat the execution.
        
             noise_model: (optional) The noise model to apply (default is no noise).
        
        Returns:
             The execution results over the specified shots, including:
                 The final qubit register state.
                 The count of hits for each outcome.
        
        
        """
        ...

    @overload
    def run_with_configuration(self, qprog: QProg, cbit_list: List[int], shot: int, noise_model: Noise = NoiseModel()) -> Dict[str,int]:
        """
        Execute the quantum program with a specified configuration.
        
        This function runs the quantum program using the provided classical bits,
        
        the number of shots for repeated execution, and an optional noise model.
        
        Args:
             qprog: The quantum program to execute.
        
             cbit_list: The list of classical bits.
        
             shot: The number of times to repeat the execution.
        
             noise_model: (optional) The noise model to apply (default is no noise). Note: Noise models currently work only on CPUQVM.
        
        Returns:
             A tuple containing the execution results over the specified shots:
                 The final qubit register state.
                 The count of hits for each outcome.
        
        """
        ...

    def set_configure(self, max_qubit: int, max_cbit: int) -> None:
        """
        Set the maximum qubit and cbit numbers for the QVM.
        
        Args:
             max_qubit: Maximum number of qubits in the quantum machine.
        
             max_cbit: Maximum number of cbits in the quantum machine.
        
        Returns:
             None
        
        """
        ...


class QuantumStateTomography:
    """
    quantum state tomography class
    """
    def __init__(self) -> None:
        """
        """
        ...

    def caculate_tomography_density(self) -> List[List[complex]]:
        """
        Calculate the tomography density.
        
        Returns:
             A reference to the calculated density matrix.
        
        """
        ...

    @overload
    def combine_qprogs(self, circuit: QProg, qlist: QVec) -> List[QProg]:
        """
        Return a list of quantum state tomography quantum programs.
        
        Args:
             circuit: The quantum circuit to be combined.
        
             qlist: The list of qubits involved.
        
        Returns:
             A reference to the combined quantum programs.
        
        
        """
        ...

    @overload
    def combine_qprogs(self, circuit: QCircuit, qlist: QVec) -> List[QProg]:
        """
        Return a list of quantum state tomography quantum programs.
        
        Args:
             circuit: The quantum circuit to be combined.
        
             qlist: The list of qubits involved.
        
        Returns:
             A reference to the combined quantum programs.
        
        
        """
        ...

    @overload
    def combine_qprogs(self, circuit: QProg, qlist: List[int]) -> List[QProg]:
        """
        Return a list of quantum state tomography quantum programs.
        
        Args:
             circuit: The quantum circuit to be combined.
        
             qlist: A vector of indices representing the qubits involved.
        
        Returns:
             A reference to the combined quantum programs.
        
        
        """
        ...

    @overload
    def combine_qprogs(self, circuit: QCircuit, qlist: List[int]) -> List[QProg]:
        """
        Return a list of quantum state tomography quantum programs.
        
        Args:
             circuit: The quantum circuit to be combined.
        
             qlist: A vector of indices representing the qubits involved.
        
        Returns:
             A reference to the combined quantum programs.
        
        """
        ...

    def exec(self, qm, shots: int) -> List[List[complex]]:
        """
        Run state tomography quantum programs.
        
        Args:
             qm: The quantum machine to execute the programs on.
        
             shots: The number of shots for the execution.
        
        Returns:
             A reference to the execution results.
        
        """
        ...

    def set_qprog_results(self, qlist: int, results: List[Dict[str,float]]) -> None:
        """
        Set the results of combined quantum programs.
        
        Args:
             qlist: The index of the qubit list.
        
             results: A vector of maps containing the result data.
        
        Returns:
             A reference to the updated state.
        
        Raises:
             run_fail: An error occurred while setting the results.
        
        """
        ...


class Qubit:
    """
    Qubit abstract class
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        """
        ...

    def getPhysicalQubitPtr(self) -> PhysicalQubit:
        """
        Retrieve a pointer to the associated physical qubit.
        
        This function returns a pointer to the physical qubit that corresponds to this qubit instance.
        
        Args:
             None
        
        Returns:
             A pointer to the associated physical qubit.
        
        """
        ...

    def get_phy_addr(self) -> int:
        """
        Retrieve the physical address of the qubit.
        
        This function returns the physical address associated with this qubit instance.
        
        Args:
             None
        
        Returns:
             The physical address of the qubit.
        
        """
        ...


class RMSPropOptimizer:
    """
    variational quantum RMSPropOptimizer
    """
    def __init__(self, arg0: var, arg1: float, arg2: float, arg3: float) -> None:
        """
        """
        ...

    def get_loss(self) -> float:
        """
        """
        ...

    def get_variables(self) -> List[var]:
        """
        """
        ...

    def minimize(self, arg0: float, arg1: float, arg2: float) -> Optimizer:
        """
        """
        ...

    def run(self, arg0: List[var], arg1: int) -> bool:
        """
        """
        ...


class SingleAmpQVM(QuantumMachine):
    """
    quantum single amplitude machine class
    """
    def __init__(self) -> None:
        """
        """
        ...

    @overload
    def get_prob_dict(self, arg0: QVec) -> Dict[str,float]:
        """
        Get the pmeasure result as a dictionary.
        
        Args:
             qubit_list: A list of qubits for pmeasure.
        
        Returns:
             A dictionary containing the measurement results of the quantum machine.
        
        
        """
        ...

    @overload
    def get_prob_dict(self, arg0: List[int]) -> Dict[str,float]:
        """
        Get the pmeasure result as a dictionary.
        
        Args:
             qubit_list: A list of qubits for pmeasure.
        
        Returns:
             A dictionary containing the measurement results of the quantum machine.
        
        """
        ...

    def get_quick_map_vertice(self, arg0: List[Tuple[int,int]]) -> None:
        """
        Get the quick map vertices.
        
        Returns:
             A reference to the quick map vertices.
        
        """
        ...

    def get_sequence(self, arg0: List[int], arg1: List[List[Tuple[int,bool]]]) -> int:
        """
        Get the program sequence.
        
        Returns:
             A reference to the current program sequence.
        
        """
        ...

    def pmeasure_bin_amplitude(self, arg0: str) -> complex:
        """
        Measure the bin amplitude of the quantum state.
        
        Args:
             bin_string: A string representing the bin.
        
        Returns:
             A complex number representing the bin amplitude.
        
        """
        ...

    def pmeasure_bin_index(self, arg0: str) -> float:
        """
        Measure the bin index of the quantum state amplitude.
        
        Args:
             bin_string: A string representing the bin.
        
        Returns:
             A double representing the amplitude probability of the bin.
        
        """
        ...

    def pmeasure_dec_amplitude(self, arg0: str) -> complex:
        """
        Measure the dec amplitude of the quantum state.
        
        Args:
             dec_string: A string representing the dec.
        
        Returns:
             A complex number representing the dec amplitude.
        
        """
        ...

    def pmeasure_dec_index(self, arg0: str) -> float:
        """
        Measure the dec index of the quantum state amplitude.
        
        Args:
             dec_string: A string representing the dec.
        
        Returns:
             A double representing the amplitude probability of the dec.
        
        """
        ...

    @overload
    def prob_run_dict(self, arg0: QProg, arg1: QVec) -> Dict[str,float]:
        """
        Run the quantum program and get the pmeasure result as a dictionary.
        
        Args:
             qprog: The quantum program to run.
        
             qubit_list: A list of qubits for pmeasure.
        
        Returns:
             A dictionary containing the measurement results of the quantum machine.
        
        
        """
        ...

    @overload
    def prob_run_dict(self, arg0: QProg, arg1: List[int]) -> Dict[str,float]:
        """
        Run the quantum program and get the pmeasure result as a dictionary.
        
        Args:
             qprog: The quantum program to run.
        
             qubit_list: A list of qubits for pmeasure.
        
        Returns:
             A dictionary containing the measurement results of the quantum machine.
        
        """
        ...

    @overload
    def run(self, prog: QProg, qv: QVec, max_rank: int = 30, alloted_time: int = 5) -> None:
        """
        Run the quantum program.
        
        Args:
             prog: A quantum program (QProg) to be executed.
        
             qv: A list of qubits (QVec) involved in the program.
        
             max_rank: The maximum rank to consider during execution (default is 30).
        
             alloted_time: The time allocated for execution (default is 5 seconds).
        
        Returns:
             None, as the function executes the program in place.
        
        
        """
        ...

    @overload
    def run(self, arg0: QProg, arg1: QVec, arg2: int, arg3: List[List[Tuple[int,bool]]]) -> None:
        """
        Run the quantum program.
        
        Args:
             prog: A quantum program (QProg) to be executed.
        
             qv: A list of qubits (QVec) involved in the program.
        
             max_rank: The maximum rank to consider during execution.
        
             sequences: A list of sequences (std::vector<qprog_sequence_t>).
        
        Returns:
             None, as the function executes the program in place.
        
        """
        ...


class SingleGateTransferType:
    """
    Quantum single gate transfer type
    
    Members:
    
      SINGLE_GATE_INVALID
    
      ARBITRARY_ROTATION
    
      DOUBLE_CONTINUOUS
    
      SINGLE_CONTINUOUS_DISCRETE
    
      DOUBLE_DISCRETE
    """
    __members__: ClassVar[dict] = ...  # read-only
    ARBITRARY_ROTATION: ClassVar[SingleGateTransferType] = ...
    DOUBLE_CONTINUOUS: ClassVar[SingleGateTransferType] = ...
    DOUBLE_DISCRETE: ClassVar[SingleGateTransferType] = ...
    SINGLE_CONTINUOUS_DISCRETE: ClassVar[SingleGateTransferType] = ...
    SINGLE_GATE_INVALID: ClassVar[SingleGateTransferType] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None:
        """
        """
        ...

    def __eq__(self, other: object) -> bool:
        """
        """
        ...

    def __getstate__(self) -> int:
        """
        """
        ...

    def __hash__(self) -> int:
        """
        """
        ...

    def __index__(self) -> int:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other: object) -> bool:
        """
        """
        ...

    def __setstate__(self, state: int) -> None:
        """
        """
        ...

    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class SparseQVM(QuantumMachine):
    """
    quantum sparse machine class
    
    """
    def __init__(self) -> None:
        """
        """
        ...

    def directlyRun(self, arg0: QProg) -> Dict[str,bool]:
        """
        Run the quantum program and get the measurement results as a dictionary.
        
        Args:
             qprog: The quantum program to execute.
        
        Returns:
             Dict[str, bool]: The result of the quantum program execution in one shot.
        
        """
        ...

    def directly_run(self, arg0: QProg) -> Dict[str,bool]:
        """
        Run the quantum program and get the measurement results as a dictionary.
        
        Args:
             qprog: The quantum program to execute.
        
        Returns:
             The measurement results of the quantum machine.
        
        """
        ...

    def init_qvm(self) -> None:
        """
        init quantum virtual machine
        """
        ...

    def prob_run_dict(self, arg0: QProg) -> Dict[str,float]:
        """
        Run the quantum program and get the measurement results as a dictionary.
        
        Args:
             qprog: The quantum program to execute.
        
        Returns:
             A dictionary containing the measurement results of the quantum machine.
        
        """
        ...

    def run_with_configuration(self, arg0: QProg, arg1: List[ClassicalCondition], arg2: int) -> Dict[str,int]:
        """
        Run the quantum program with the specified configuration and get the measurement results as a dictionary.
        
        Args:
             qprog: The quantum program to execute.
        
             cbits: The quantum classical bits.
        
             shots: The number of sample shots.
        
        Returns:
             The measurement results of the quantum machine.
        
        """
        ...


class Stabilizer(QuantumMachine):
    """
    simulator for basic clifford simulator
    """
    def __init__(self) -> None:
        """
        """
        ...

    def init_qvm(self) -> None:
        """
        init quantum virtual machine
        """
        ...

    def prob_run_dict(self, qprog: QProg, qubits: QVec, select_max: int = -1) -> Dict[str,float]:
        """
        Run quantum program and get probabilities.
        
        Args:
             qprog: Quantum program to execute.
        
             qubits: Qubits to be measured for probabilities.
        
             select_max: Optional, selects the maximum number of probabilities to return.
        
        Returns:
             Probabilities result of the quantum program.
        
        """
        ...

    def run_with_configuration(self, qprog: QProg, shot: int) -> Dict[str,int]:
        """
        Run quantum program and get shots result.
        
        Args:
             qprog: Quantum program to execute.
        
             shot: Number of measurement shots.
        
        Returns:
             Shots result of the quantum program.
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float) -> None:
        """
        Set a noise model for the Stabilizer simulator with a specific gate type and probability.
        
        Args:
             noise_model: The noise model to apply (e.g., bit-flip, phase-flip, etc.).
        
             gate_type: The specific gate type associated with the noise model.
        
             probability: The probability of the noise occurring.
        
        Returns:
             None.
        
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: List[GateType], arg2: float) -> None:
        """
        Set a noise model for the Stabilizer simulator with multiple gate types and a specified probability.
        
        Args:
             noise_model: The noise model to apply (e.g., bit-flip, phase-flip, etc.).
        
             gate_types: A vector of gate types associated with the noise model.
        
             probability: The probability of the noise occurring.
        
        Returns:
             None.
        
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float, arg3: QVec) -> None:
        """
        Set a noise model for the Stabilizer simulator with a specific gate type, probability, and targeted qubits.
        
        Args:
             noise_model: The noise model to apply (e.g., bit-flip, phase-flip, etc.).
        
             gate_type: The specific gate type associated with the noise model.
        
             probability: The probability of the noise occurring.
        
             target_qubits: The qubits targeted by the noise model.
        
        Returns:
             None.
        
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: List[GateType], arg2: float, arg3: QVec) -> None:
        """
        Set a noise model for the Stabilizer simulator with multiple gate types, a specified probability, and targeted qubits.
        
        Args:
             noise_model: The noise model to apply (e.g., bit-flip, phase-flip, etc.).
        
             gate_types: A vector of gate types associated with the noise model.
        
             probability: The probability of the noise occurring.
        
             target_qubits: The qubits targeted by the noise model.
        
        Returns:
             None.
        
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float, arg3: List[QVec]) -> None:
        """
        Set a noise model for the Stabilizer simulator with a specific gate type, probability, and multiple targeted qubits.
        
        Args:
             noise_model: The noise model to apply (e.g., bit-flip, phase-flip, etc.).
        
             gate_type: The specific gate type associated with the noise model.
        
             probability: The probability of the noise occurring.
        
             target_qubits: A vector of qubit vectors targeted by the noise model.
        
        Returns:
             None.
        
        """
        ...


class UpdateMode:
    """
    quantum imaginary time evolution update mode
    
    Members:
    
      GD_VALUE
    
      GD_DIRECTION
    """
    __members__: ClassVar[dict] = ...  # read-only
    GD_DIRECTION: ClassVar[UpdateMode] = ...
    GD_VALUE: ClassVar[UpdateMode] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None:
        """
        """
        ...

    def __eq__(self, other: object) -> bool:
        """
        """
        ...

    def __ge__(self, other: object) -> bool:
        """
        """
        ...

    def __getstate__(self) -> int:
        """
        """
        ...

    def __gt__(self, other: object) -> bool:
        """
        """
        ...

    def __hash__(self) -> int:
        """
        """
        ...

    def __index__(self) -> int:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __le__(self, other: object) -> bool:
        """
        """
        ...

    def __lt__(self, other: object) -> bool:
        """
        """
        ...

    def __ne__(self, other: object) -> bool:
        """
        """
        ...

    def __setstate__(self, state: int) -> None:
        """
        """
        ...

    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class VanillaGradientDescentOptimizer:
    """
    variational quantum VanillaGradientDescentOptimizer
    """
    def __init__(self, arg0: var, arg1: float, arg2: float, arg3: OptimizerMode) -> None:
        """
        """
        ...

    def get_loss(self) -> float:
        """
        """
        ...

    def get_variables(self) -> List[var]:
        """
        """
        ...

    def minimize(self, arg0: float, arg1: float) -> Optimizer:
        """
        """
        ...

    def run(self, arg0: List[var], arg1: int) -> bool:
        """
        """
        ...


class VariationalQuantumCircuit:
    """
    variational quantum CIRCUIT class
    """
    @overload
    def __init__(self) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: QCircuit) -> None:
        """
        """
        ...

    def control(self, arg0: QVec) -> VariationalQuantumCircuit:
        """
        """
        ...

    def dagger(self) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def feed(self) -> QCircuit:
        """
        """
        ...

    @overload
    def feed(self, arg0) -> QCircuit:
        """
        """
        ...

    def get_control_qubit(self) -> QVec:
        """
        """
        ...

    @overload
    def insert(self, arg0: VariationalQuantumGate_I) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def insert(self, arg0: VariationalQuantumGate_H) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def insert(self, arg0: VariationalQuantumGate_X) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def insert(self, arg0: VariationalQuantumGate_Y) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def insert(self, arg0: VariationalQuantumGate_T) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def insert(self, arg0: VariationalQuantumGate_S) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def insert(self, arg0: VariationalQuantumGate_Z) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def insert(self, arg0: VariationalQuantumGate_X1) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def insert(self, arg0: VariationalQuantumGate_Y1) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def insert(self, arg0: VariationalQuantumGate_Z1) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def insert(self, arg0: VariationalQuantumGate_U1) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def insert(self, arg0: VariationalQuantumGate_U2) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def insert(self, arg0: VariationalQuantumGate_U3) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def insert(self, arg0: VariationalQuantumGate_U4) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def insert(self, arg0: VariationalQuantumGate_RX) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def insert(self, arg0: VariationalQuantumGate_RY) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def insert(self, arg0: VariationalQuantumGate_RZ) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def insert(self, arg0: VariationalQuantumGate_CNOT) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def insert(self, arg0: VariationalQuantumGate_CR) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def insert(self, arg0: VariationalQuantumGate_CZ) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def insert(self, arg0: VariationalQuantumGate_CRX) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def insert(self, arg0: VariationalQuantumGate_CRY) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def insert(self, arg0: VariationalQuantumGate_CRZ) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def insert(self, arg0: VariationalQuantumGate_SWAP) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def insert(self, arg0: VariationalQuantumGate_iSWAP) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def insert(self, arg0: VariationalQuantumGate_SqiSWAP) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def insert(self, arg0: VariationalQuantumCircuit) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def insert(self, arg0: QCircuit) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def insert(self, arg0: QGate) -> VariationalQuantumCircuit:
        """
        """
        ...

    def is_dagger(self) -> bool:
        """
        """
        ...

    def set_control(self, arg0: QVec) -> bool:
        """
        """
        ...

    def set_dagger(self, arg0: bool) -> bool:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: VariationalQuantumGate_I) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: VariationalQuantumGate_H) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: VariationalQuantumGate_X) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: VariationalQuantumGate_Y) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: VariationalQuantumGate_T) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: VariationalQuantumGate_S) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: VariationalQuantumGate_Z) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: VariationalQuantumGate_X1) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: VariationalQuantumGate_Y1) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: VariationalQuantumGate_Z1) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: VariationalQuantumGate_U1) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: VariationalQuantumGate_U2) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: VariationalQuantumGate_U3) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: VariationalQuantumGate_U4) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: VariationalQuantumGate_RX) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: VariationalQuantumGate_RY) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: VariationalQuantumGate_RZ) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: VariationalQuantumGate_CNOT) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: VariationalQuantumGate_CR) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: VariationalQuantumGate_CZ) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: VariationalQuantumGate_CRX) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: VariationalQuantumGate_CRY) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: VariationalQuantumGate_CRZ) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: VariationalQuantumGate_SWAP) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: VariationalQuantumGate_iSWAP) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: VariationalQuantumGate_SqiSWAP) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: VariationalQuantumCircuit) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: QCircuit) -> VariationalQuantumCircuit:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: QGate) -> VariationalQuantumCircuit:
        """
        """
        ...


class VariationalQuantumGate:
    """
    variational quantum gate base class
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        """
        ...

    def feed(self, arg0: Dict[int,float]) -> QGate:
        """
        """
        ...

    def get_constants(self) -> List[float]:
        """
        """
        ...

    def get_control_qubit(self) -> QVec:
        """
        """
        ...

    def get_vars(self) -> List[var]:
        """
        """
        ...

    def is_dagger(self) -> bool:
        """
        """
        ...

    def set_control(self, arg0: QVec) -> bool:
        """
        """
        ...

    def set_dagger(self, arg0: bool) -> bool:
        """
        """
        ...


class VariationalQuantumGate_CNOT(VariationalQuantumGate):
    """
    variational quantum CNOT gate class
    """
    def __init__(self, arg0: Qubit, arg1: Qubit) -> None:
        """
        """
        ...

    def control(self, arg0: QVec) -> VariationalQuantumGate_CNOT:
        """
        """
        ...

    def dagger(self) -> VariationalQuantumGate_CNOT:
        """
        """
        ...


class VariationalQuantumGate_CR(VariationalQuantumGate):
    """
    variational quantum CR gate class
    """
    @overload
    def __init__(self, arg0: Qubit, arg1: Qubit, arg2: float) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: Qubit, arg1: Qubit, arg2: var) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: VariationalQuantumGate_CR) -> None:
        """
        """
        ...

    def control(self, arg0: QVec) -> VariationalQuantumGate_CR:
        """
        """
        ...

    def dagger(self) -> VariationalQuantumGate_CR:
        """
        """
        ...


class VariationalQuantumGate_CRX(VariationalQuantumGate):
    """
    variational quantum CRX gate class
    """
    @overload
    def __init__(self, arg0: Qubit, arg1: QVec, arg2: float) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: Qubit, arg1: QVec, arg2: var) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: VariationalQuantumGate_CRX) -> None:
        """
        """
        ...

    def control(self, arg0: QVec) -> VariationalQuantumGate_CRX:
        """
        """
        ...

    def dagger(self) -> VariationalQuantumGate_CRX:
        """
        """
        ...


class VariationalQuantumGate_CRY(VariationalQuantumGate):
    """
    variational quantum CRY gate class
    """
    @overload
    def __init__(self, arg0: Qubit, arg1: QVec, arg2: float) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: Qubit, arg1: QVec, arg2: var) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: VariationalQuantumGate_CRY) -> None:
        """
        """
        ...

    def control(self, arg0: QVec) -> VariationalQuantumGate_CRY:
        """
        """
        ...

    def dagger(self) -> VariationalQuantumGate_CRY:
        """
        """
        ...


class VariationalQuantumGate_CRZ(VariationalQuantumGate):
    """
    variational quantum CRZ gate class
    """
    @overload
    def __init__(self, arg0: Qubit, arg1: QVec, arg2: float) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: Qubit, arg1: QVec, arg2: var) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: VariationalQuantumGate_CRZ) -> None:
        """
        """
        ...

    def control(self, arg0: QVec) -> VariationalQuantumGate_CRZ:
        """
        """
        ...

    def dagger(self) -> VariationalQuantumGate_CRZ:
        """
        """
        ...


class VariationalQuantumGate_CU(VariationalQuantumGate):
    """
    variational quantum CU gate class
    """
    @overload
    def __init__(self, arg0: Qubit, arg1: Qubit, arg2: float, arg3: float, arg4: float, arg5: float) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: Qubit, arg1: Qubit, arg2: var, arg3: var, arg4: var, arg5: var) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: VariationalQuantumGate_CU) -> None:
        """
        """
        ...

    def control(self, arg0: QVec) -> VariationalQuantumGate_CU:
        """
        """
        ...

    def dagger(self) -> VariationalQuantumGate_CU:
        """
        """
        ...


class VariationalQuantumGate_CZ(VariationalQuantumGate):
    """
    variational quantum CZ gate class
    """
    def __init__(self, arg0: Qubit, arg1: Qubit) -> None:
        """
        """
        ...

    def control(self, arg0: QVec) -> VariationalQuantumGate_CZ:
        """
        """
        ...

    def dagger(self) -> VariationalQuantumGate_CZ:
        """
        """
        ...


class VariationalQuantumGate_H(VariationalQuantumGate):
    """
    variational quantum  H gate class
    """
    def __init__(self, arg0: Qubit) -> None:
        """
        """
        ...

    def control(self, arg0: QVec) -> VariationalQuantumGate_H:
        """
        """
        ...

    def dagger(self) -> VariationalQuantumGate_H:
        """
        """
        ...


class VariationalQuantumGate_I(VariationalQuantumGate):
    """
    variational quantum  I gate class
    """
    def __init__(self, arg0: Qubit) -> None:
        """
        """
        ...

    def control(self, arg0: QVec) -> VariationalQuantumGate_I:
        """
        """
        ...

    def dagger(self) -> VariationalQuantumGate_I:
        """
        """
        ...


class VariationalQuantumGate_RX(VariationalQuantumGate):
    """
    variational quantum RX gate class
    """
    @overload
    def __init__(self, arg0: Qubit, arg1: var) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: Qubit, arg1: float) -> None:
        """
        """
        ...

    def control(self, arg0: QVec) -> VariationalQuantumGate_RX:
        """
        """
        ...

    def dagger(self) -> VariationalQuantumGate_RX:
        """
        """
        ...


class VariationalQuantumGate_RY(VariationalQuantumGate):
    """
    variational quantum RY gate class
    """
    @overload
    def __init__(self, arg0: Qubit, arg1: var) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: Qubit, arg1: float) -> None:
        """
        """
        ...

    def control(self, arg0: QVec) -> VariationalQuantumGate_RY:
        """
        """
        ...

    def dagger(self) -> VariationalQuantumGate_RY:
        """
        """
        ...


class VariationalQuantumGate_RZ(VariationalQuantumGate):
    """
    variational quantum RZ gate class
    """
    @overload
    def __init__(self, arg0: Qubit, arg1: var) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: Qubit, arg1: float) -> None:
        """
        """
        ...

    def control(self, arg0: QVec) -> VariationalQuantumGate_RZ:
        """
        """
        ...

    def dagger(self) -> VariationalQuantumGate_RZ:
        """
        """
        ...


class VariationalQuantumGate_S(VariationalQuantumGate):
    """
    variational quantum S gate class
    """
    def __init__(self, arg0: Qubit) -> None:
        """
        """
        ...

    def control(self, arg0: QVec) -> VariationalQuantumGate_S:
        """
        """
        ...

    def dagger(self) -> VariationalQuantumGate_S:
        """
        """
        ...


class VariationalQuantumGate_SWAP(VariationalQuantumGate):
    """
    variational quantum SWAP gate class
    """
    def __init__(self, arg0: Qubit, arg1: Qubit) -> None:
        """
        """
        ...

    def control(self, arg0: QVec) -> VariationalQuantumGate_SWAP:
        """
        """
        ...

    def dagger(self) -> VariationalQuantumGate_SWAP:
        """
        """
        ...


class VariationalQuantumGate_SqiSWAP(VariationalQuantumGate):
    """
    variational quantum SqiSWAP gate class
    """
    def __init__(self, arg0: Qubit, arg1: Qubit) -> None:
        """
        """
        ...

    def control(self, arg0: QVec) -> VariationalQuantumGate_SqiSWAP:
        """
        """
        ...

    def dagger(self) -> VariationalQuantumGate_SqiSWAP:
        """
        """
        ...


class VariationalQuantumGate_T(VariationalQuantumGate):
    """
    variational quantum T gate class
    """
    def __init__(self, arg0: Qubit) -> None:
        """
        """
        ...

    def control(self, arg0: QVec) -> VariationalQuantumGate_T:
        """
        """
        ...

    def dagger(self) -> VariationalQuantumGate_T:
        """
        """
        ...


class VariationalQuantumGate_U1(VariationalQuantumGate):
    """
    variational quantum U1 gate class
    """
    @overload
    def __init__(self, arg0: Qubit, arg1: var) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: Qubit, arg1: float) -> None:
        """
        """
        ...

    def control(self, arg0: QVec) -> VariationalQuantumGate_U1:
        """
        """
        ...

    def dagger(self) -> VariationalQuantumGate_U1:
        """
        """
        ...


class VariationalQuantumGate_U2(VariationalQuantumGate):
    """
    variational quantum U2 gate class
    """
    @overload
    def __init__(self, arg0: Qubit, arg1: var, arg2: var) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: Qubit, arg1: float, arg2: float) -> None:
        """
        """
        ...

    def control(self, arg0: QVec) -> VariationalQuantumGate_U2:
        """
        """
        ...

    def dagger(self) -> VariationalQuantumGate_U2:
        """
        """
        ...


class VariationalQuantumGate_U3(VariationalQuantumGate):
    """
    variational quantum U3 gate class
    """
    @overload
    def __init__(self, arg0: Qubit, arg1: var, arg2: var, arg3: var) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: Qubit, arg1: float, arg2: float, arg3: float) -> None:
        """
        """
        ...

    def control(self, arg0: QVec) -> VariationalQuantumGate_U3:
        """
        """
        ...

    def dagger(self) -> VariationalQuantumGate_U3:
        """
        """
        ...


class VariationalQuantumGate_U4(VariationalQuantumGate):
    """
    variational quantum U4 gate class
    """
    @overload
    def __init__(self, arg0: Qubit, arg1: var, arg2: var, arg3: var, arg4: var) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: Qubit, arg1: float, arg2: float, arg3: float, arg4: float) -> None:
        """
        """
        ...

    def control(self, arg0: QVec) -> VariationalQuantumGate_U4:
        """
        """
        ...

    def dagger(self) -> VariationalQuantumGate_U4:
        """
        """
        ...


class VariationalQuantumGate_X(VariationalQuantumGate):
    """
    variational quantum X gate class
    """
    def __init__(self, arg0: Qubit) -> None:
        """
        """
        ...

    def control(self, arg0: QVec) -> VariationalQuantumGate_X:
        """
        """
        ...

    def dagger(self) -> VariationalQuantumGate_X:
        """
        """
        ...


class VariationalQuantumGate_X1(VariationalQuantumGate):
    """
    variational quantum X1 gate class
    """
    def __init__(self, arg0: Qubit) -> None:
        """
        """
        ...

    def control(self, arg0: QVec) -> VariationalQuantumGate_X1:
        """
        """
        ...

    def dagger(self) -> VariationalQuantumGate_X1:
        """
        """
        ...


class VariationalQuantumGate_Y(VariationalQuantumGate):
    """
    variational quantum Y gate class
    """
    def __init__(self, arg0: Qubit) -> None:
        """
        """
        ...

    def control(self, arg0: QVec) -> VariationalQuantumGate_Y:
        """
        """
        ...

    def dagger(self) -> VariationalQuantumGate_Y:
        """
        """
        ...


class VariationalQuantumGate_Y1(VariationalQuantumGate):
    """
    variational quantum Y1 gate class
    """
    def __init__(self, arg0: Qubit) -> None:
        """
        """
        ...

    def control(self, arg0: QVec) -> VariationalQuantumGate_Y1:
        """
        """
        ...

    def dagger(self) -> VariationalQuantumGate_Y1:
        """
        """
        ...


class VariationalQuantumGate_Z(VariationalQuantumGate):
    """
    variational quantum Z gate class
    """
    def __init__(self, arg0: Qubit) -> None:
        """
        """
        ...

    def control(self, arg0: QVec) -> VariationalQuantumGate_Z:
        """
        """
        ...

    def dagger(self) -> VariationalQuantumGate_Z:
        """
        """
        ...


class VariationalQuantumGate_Z1(VariationalQuantumGate):
    """
    variational quantum Z1 gate class
    """
    def __init__(self, arg0: Qubit) -> None:
        """
        """
        ...

    def control(self, arg0: QVec) -> VariationalQuantumGate_Z1:
        """
        """
        ...

    def dagger(self) -> VariationalQuantumGate_Z1:
        """
        """
        ...


class VariationalQuantumGate_iSWAP(VariationalQuantumGate):
    """
    variational quantum iSWAP gate class
    """
    def __init__(self, arg0: Qubit, arg1: Qubit) -> None:
        """
        """
        ...

    def control(self, arg0: QVec) -> VariationalQuantumGate_iSWAP:
        """
        """
        ...

    def dagger(self) -> VariationalQuantumGate_iSWAP:
        """
        """
        ...


class em_method:
    """
    origin quantum real chip error_mitigation type
    
    Members:
    
      ZNE
    
      PEC
    
      READ_OUT
    """
    __members__: ClassVar[dict] = ...  # read-only
    PEC: ClassVar[em_method] = ...
    READ_OUT: ClassVar[em_method] = ...
    ZNE: ClassVar[em_method] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None:
        """
        """
        ...

    def __eq__(self, other: object) -> bool:
        """
        """
        ...

    def __getstate__(self) -> int:
        """
        """
        ...

    def __hash__(self) -> int:
        """
        """
        ...

    def __index__(self) -> int:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other: object) -> bool:
        """
        """
        ...

    def __setstate__(self, state: int) -> None:
        """
        """
        ...

    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class expression:
    """
    variational quantum expression class
    """
    def __init__(self, arg0: var) -> None:
        """
        """
        ...

    @overload
    def backprop(self, arg0: Dict[var,numpy.ndarray[numpy.float64[m,n]]]) -> None:
        """
        """
        ...

    @overload
    def backprop(self, arg0: Dict[var,numpy.ndarray[numpy.float64[m,n]]], arg1: List[var]) -> None:
        """
        """
        ...

    def find_leaves(self) -> List[var]:
        """
        """
        ...

    def find_non_consts(self, arg0: List[var]) -> List[var]:
        """
        """
        ...

    def get_root(self) -> var:
        """
        """
        ...

    @overload
    def propagate(self) -> numpy.ndarray[numpy.float64[m,n]]:
        """
        """
        ...

    @overload
    def propagate(self, arg0: List[var]) -> numpy.ndarray[numpy.float64[m,n]]:
        """
        """
        ...


class hadamard_circuit(QCircuit):
    """
    hadamard circuit class
    """
    def __init__(self, arg0: QVec) -> None:
        """
        """
        ...


class real_chip_type:
    """
    origin quantum real chip type enum
    
    Members:
    
      origin_wuyuan_d3
    
      origin_wuyuan_d4
    
      origin_wuyuan_d5
    
      origin_72
    """
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    origin_72: ClassVar[real_chip_type] = ...
    origin_wuyuan_d3: ClassVar[real_chip_type] = ...
    origin_wuyuan_d4: ClassVar[real_chip_type] = ...
    origin_wuyuan_d5: ClassVar[real_chip_type] = ...
    def __init__(self, value: int) -> None:
        """
        """
        ...

    def __eq__(self, other: object) -> bool:
        """
        """
        ...

    def __getstate__(self) -> int:
        """
        """
        ...

    def __hash__(self) -> int:
        """
        """
        ...

    def __index__(self) -> int:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other: object) -> bool:
        """
        """
        ...

    def __setstate__(self, state: int) -> None:
        """
        """
        ...

    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class var:
    """
    quantum variational class
    """
    @overload
    def __init__(self, arg0: float) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: numpy.ndarray[numpy.float64[m,n],flags.writeable]) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: float, arg1: bool) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: numpy.ndarray[numpy.float64[m,n],flags.writeable], arg1: bool) -> None:
        """
        """
        ...

    def clone(self) -> var:
        """
        """
        ...

    def get_value(self) -> numpy.ndarray[numpy.float64[m,n]]:
        """
        """
        ...

    @overload
    def set_value(self, arg0: numpy.ndarray[numpy.float64[m,n]]) -> None:
        """
        """
        ...

    @overload
    def set_value(self, arg0: float) -> None:
        """
        """
        ...

    @overload
    def __add__(self, arg0: var) -> var:
        """
        """
        ...

    @overload
    def __add__(self, arg0: float) -> var:
        """
        """
        ...

    @overload
    def __eq__(self, arg0: var) -> bool:
        """
        """
        ...

    @overload
    def __eq__(self, arg0: var) -> bool:
        """
        """
        ...

    def __getitem__(self, arg0: int) -> var:
        """
        """
        ...

    def __hash__(self) -> int:
        """
        """
        ...

    @overload
    def __mul__(self, arg0: var) -> var:
        """
        """
        ...

    @overload
    def __mul__(self, arg0: float) -> var:
        """
        """
        ...

    def __radd__(self, arg0: float) -> var:
        """
        """
        ...

    def __rmul__(self, arg0: float) -> var:
        """
        """
        ...

    def __rsub__(self, arg0: float) -> var:
        """
        """
        ...

    def __rtruediv__(self, arg0: float) -> var:
        """
        """
        ...

    @overload
    def __sub__(self, arg0: var) -> var:
        """
        """
        ...

    @overload
    def __sub__(self, arg0: float) -> var:
        """
        """
        ...

    @overload
    def __truediv__(self, arg0: var) -> var:
        """
        """
        ...

    @overload
    def __truediv__(self, arg0: float) -> var:
        """
        """
        ...


@overload
def BARRIER(qubit: Qubit) -> QGate:
    """
    Create a BARRIER gate for a specified qubit.
    
    Args:
        qubit: the qubit to which the BARRIER will be applied.
    
    Returns:
        A BARRIER node representing the operation.
    
    
    """
    ...

@overload
def BARRIER(qubit_list: int) -> QGate:
    """
    Create a BARRIER gate for a list of qubits.
    
    Args:
        qubit_list: integer representing the qubits to which the BARRIER will be applied.
    
    Returns:
        A BARRIER node representing the operation.
    
    
    """
    ...

@overload
def BARRIER(qubit_list: QVec) -> QGate:
    """
    Create a BARRIER gate for a list of qubits.
    
    Args:
        qubit_list: a list of qubits to which the BARRIER will be applied.
    
    Returns:
        A BARRIER node representing the operation.
    
    
    """
    ...

@overload
def BARRIER(qubit_addr_list: List[int]) -> QGate:
    """
    Create a BARRIER gate for a list of qubit addresses.
    
    Args:
        qubit_addr_list: a list of integers representing the addresses of the qubits.
    
    Returns:
        A BARRIER node representing the operation.
    
    """
    ...

@overload
def CNOT(control_qubit: Qubit, target_qubit: Qubit) -> QGate:
    """
    Returns:
        a CNOT gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def CNOT(control_qubit_list: QVec, target_qubit_list: QVec) -> QCircuit:
    """
    Returns:
        a CNOT gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def CNOT(control_qubit_addr: int, target_qubit_addr: int) -> QGate:
    """
    """
    ...

@overload
def CNOT(control_qubit_addr_list: List[int], target_qubit_addr_list: List[int]) -> QCircuit:
    """
    Returns:
        a CNOT gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    """
    ...

@overload
def CP(control_qubit: Qubit, target_qubit: Qubit, theta_angle: float) -> QGate:
    """
    Returns:
        a CP gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def CP(control_qubit_list: QVec, target_qubit_list: QVec, theta_angle: float) -> QCircuit:
    """
    Returns:
        a CP gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def CP(control_qubit_addr: int, target_qubit_addr: int, theta_angle: float) -> QGate:
    """
    Returns:
        a CP gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def CP(control_qubit_addr_list: List[int], target_qubit_addr_list: List[int], theta_angle: float) -> QCircuit:
    """
    Returns:
        a CP gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    """
    ...

@overload
def CR(control_qubit: Qubit, target_qubit: Qubit, theta_angle: float) -> QGate:
    """
    Returns:
        a CR gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def CR(control_qubit_list: QVec, target_qubit_list: QVec, theta_angle: float) -> QCircuit:
    """
    Returns:
        a CR gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def CR(control_qubit_addr: int, target_qubit_addr: int, theta_angle: float) -> QGate:
    """
    Returns:
        a CR gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def CR(control_qubit_addr_list: List[int], target_qubit_addr_list: List[int], theta_angle: float) -> QCircuit:
    """
    Returns:
        a CR gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    """
    ...

@overload
def CU(alpha_angle: float, beta_angle: float, gamma_angle: float, delta_angle: float, control_qubit: Qubit, target_qubit: Qubit) -> QGate:
    """
    Create a CU gate.
    
    Args:
        alpha_angle: the alpha angle for the CU gate.
    
        beta_angle: the beta angle for the CU gate.
    
        gamma_angle: the gamma angle for the CU gate.
    
        delta_angle: the delta angle for the CU gate.
    
        control_qubit: the qubit that controls the operation.
    
        target_qubit: the qubit that is affected by the control qubit.
    
    Returns:
        A CU node representing the operation.
    
    """
    ...

@overload
def CU(alpha_angle: float, beta_angle: float, gamma_angle: float, delta_angle: float, control_qubit_list: QVec, target_qubi_list: QVec) -> QCircuit:
    """
    Create a CU gate.
    
    Args:
        alpha_angle (double): U4 gate alpha angle.
    
        beta_angle (double): U4 gate beta angle.
    
        gamma_angle (double): U4 gate gamma angle.
    
        delta_angle (double): U4 gate delta angle.
    
        control_qubit_list (const QVec &): List of control qubits.
    
        target_qubit_list (const QVec &): List of target qubits.
    
    Returns:
        A CU node representing the operation.
    
    
    """
    ...

@overload
def CU(matrix: List[complex], control_qubit: Qubit, target_qubit: Qubit) -> QGate:
    """
    Create a CU gate.
    
    Args:
        matrix (QStat &): The CU gate matrix.
    
        control_qubit (Qubit *): The control qubit.
    
        target_qubit (Qubit *): The target qubit.
    
    Returns:
        A CU node representing the operation.
    
    
    """
    ...

@overload
def CU(matrix: List[complex], control_qubit_list: QVec, target_qubit_list: QVec) -> QCircuit:
    """
    Create a CU gate.
    
    Args:
        matrix (QStat &): The CU gate matrix.
    
        control_qubit_list (const QVec &): List of control qubits.
    
        target_qubit_list (const QVec &): List of target qubits.
    
    Returns:
        A CU node representing the operation.
    
    
    """
    ...

@overload
def CU(control_qubit: Qubit, target_qubit: Qubit, alpha_angle: float, beta_angle: float, gamma_angle: float, delta_angle: float) -> QGate:
    """
    Create a CU gate.
    
    Args:
        control_qubit (Qubit *): The control qubit.
    
        target_qubit (Qubit *): The target qubit.
    
        alpha_angle (double): U4 gate alpha angle.
    
        beta_angle (double): U4 gate beta angle.
    
        gamma_angle (double): U4 gate gamma angle.
    
        delta_angle (double): U4 gate delta angle.
    
    Returns:
        A CU node representing the operation.
    
    
    """
    ...

@overload
def CU(control_qubit_list: QVec, target_qubit_list: QVec, alpha_angle: float, beta_angle: float, gamma_angle: float, delta_angle: float) -> QCircuit:
    """
    Create a CU gate.
    
    Args:
        control_qubit_list (QVec): Control qubit list.
    
        target_qubit_list (QVec): Target qubit list.
    
        alpha_angle (double): U4 gate alpha angle.
    
        beta_angle (double): U4 gate beta angle.
    
        gamma_angle (double): U4 gate gamma angle.
    
        delta_angle (double): U4 gate delta angle.
    
    Returns:
        CU node representing the operation.
    
    
    """
    ...

@overload
def CU(control_qubit_addr: int, target_qubit_addr: int, alpha_angle: float, beta_angle: float, gamma_angle: float, delta_angle: float) -> QGate:
    """
    Create a CU gate.
    
    Args:
        control_qubit_addr (int): Address of the control qubit.
    
        target_qubit_addr (int): Address of the target qubit.
    
        alpha_angle (double): U4 gate alpha angle.
    
        beta_angle (double): U4 gate beta angle.
    
        gamma_angle (double): U4 gate gamma angle.
    
        delta_angle (double): U4 gate delta angle.
    
    Returns:
        A CU node representing the operation.
    
    
    """
    ...

@overload
def CU(control_qubit_addr_list: List[int], target_qubit_addr_list: List[int], alpha_angle: float, beta_angle: float, gamma_angle: float, delta_angle: float) -> QCircuit:
    """
    Create a CU gate.
    
    Args:
        control_qubit_addr_list (std::vector<int>): List of control qubit addresses.
    
        target_qubit_addr_list (std::vector<int>): List of target qubit addresses.
    
        alpha_angle (double): U4 gate alpha angle.
    
        beta_angle (double): U4 gate beta angle.
    
        gamma_angle (double): U4 gate gamma angle.
    
        delta_angle (double): U4 gate delta angle.
    
    Returns:
        A CU node representing the operation.
    
    
    """
    ...

@overload
def CU(control_qubit: Qubit, target_qubit: Qubit, matrix: List[complex]) -> QGate:
    """
    Create a CU gate.
    
    Args:
        control_qubit (Qubit *): The control qubit.
    
        target_qubit (Qubit *): The target qubit.
    
        matrix (QStat &): The CU gate matrix.
    
    Returns:
        A CU node representing the operation.
    
    
    """
    ...

@overload
def CU(control_qubit_list: QVec, target_qubit_list: QVec, matrix: List[complex]) -> QCircuit:
    """
    Create a CU gate.
    
    Args:
        control_qubit_list (const QVec &): List of control qubits.
    
        target_qubit_list (const QVec &): List of target qubits.
    
        matrix (QStat &): The CU gate matrix.
    
    Returns:
        A CU node representing the operation.
    
    
    """
    ...

@overload
def CU(control_qubit_addr: int, target_qubit_addr: int, matrix: List[complex]) -> QGate:
    """
    Create a CU gate.
    
    Args:
        control_qubit_addr (int): Address of the control qubit.
    
        target_qubit_addr (int): Address of the target qubit.
    
        matrix (QStat &): The CU gate matrix.
    
    Returns:
        A CU node representing the operation.
    
    
    """
    ...

@overload
def CU(control_qubit_addr_list: List[int], target_qubit_addr_list: List[int], matrix: List[complex]) -> QCircuit:
    """
    Create a CU gate.
    
    Args:
        control_qubit_addr_list (const std::vector<int> &): List of control qubit addresses.
    
        target_qubit_addr_list (const std::vector<int> &): List of target qubit addresses.
    
        matrix (QStat &): The CU gate matrix.
    
    Returns:
        A CU node representing the operation.
    
    """
    ...

@overload
def CZ(control_qubit: Qubit, target_qubit: Qubit) -> QGate:
    """
    Returns:
        a CZ gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def CZ(control_qubit_list: QVec, target_qubit_list: QVec) -> QCircuit:
    """
    Returns:
        a CZ gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def CZ(control_qubit_addr: int, target_qubit_addr: int) -> QGate:
    """
    """
    ...

@overload
def CZ(control_qubit_addr_list: List[int], target_qubit_addr_list: List[int]) -> QCircuit:
    """
    Returns:
        a CZ gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    """
    ...

def CreateEmptyCircuit() -> QCircuit:
    """
    Create an empty QCircuit container.
    
    Args:
        none
    
    Returns:
        result: An empty QCircuit.
    
    """
    ...

def CreateEmptyQProg() -> QProg:
    """
    Create an empty QProg container.
    
    Args:
        none
    
    Returns:
        an empty QProg.
    
    """
    ...

@overload
def CreateIfProg(classical_condition: ClassicalCondition, true_node: QProg) -> QIfProg:
    """
    Create an IfProg that executes a quantum operation if a classical condition is true.
    
    Args:
        classical_condition: A classical condition representing the if condition.
    
        true_node: The quantum operations to execute if the condition is true.
    
    Returns:
        IfProg: The program that performs the specified operations if the condition is true.
    
    
    """
    ...

@overload
def CreateIfProg(classical_condition: ClassicalCondition, true_node: QProg, false_node: QProg) -> QIfProg:
    """
    Create an IfProg that executes one of two quantum operations based on a classical condition.
    
    Args:
        classical_condition: A classical condition representing the if condition.
    
        true_node: The quantum operations to execute if the condition is true.
    
        false_node: The quantum operations to execute if the condition is false.
    
    Returns:
        IfProg: The program that performs the specified operations based on the condition.
    
    """
    ...

def CreateWhileProg(classical_condition: ClassicalCondition, true_node: QProg) -> QWhileProg:
    """
    Create a WhileProg that executes while a classical condition is true.
    
    Args:
        classical_condition: A classical condition representing the while-loop condition.
    
        true_node: The quantum operations to execute while the condition is true.
    
    Returns:
        WhileProg: The program that performs the specified operations while the condition holds.
    
    """
    ...

def Grover(*args, **kwargs) -> Any:
    """
    Quantum grover circuit
    
    Args:
        qvec: qubit list
        Classical_condition: quantum Classical condition
        QuantumMachine: quantum machine
    
    Returns:
        result : Grover circuit
    Raises:
        run_fail: An error occurred in Grover
    
    """
    ...

@overload
def Grover_search(list: List[int], Classical_condition: ClassicalCondition, QuantumMachine: QuantumMachine, repeat: int = 2) -> list:
    """
    Use Grover algorithm to search target data, return QProg and search_result
    
    Args:
        list: data list
        Classical_condition: quantum Classical condition
        QuantumMachine: quantum machine
        repeat: search repeat times
    
    Returns:
        result : Grover search result
    Raises:
        run_fail: An error occurred in Grover
    
    
    """
    ...

@overload
def Grover_search(list: List[str], Classical_condition: str, QuantumMachine: QuantumMachine, data: int = 2) -> list:
    """
    use Grover algorithm to search target data, return QProg and search_result
    """
    ...

@overload
def H(qubit: Qubit) -> QGate:
    """
    Create a H gate
    
    Args:
        qubit : quantum gate operate qubit
    
    Returns:
        a H gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def H(qubit_list: QVec) -> QCircuit:
    """
    Create a H gate
    
    Args:
        qubit_list: quantum gate operate qubits list
    
    Returns:
        a H gate node
    Raises:
        run_fail: An error occurred construct in gate node
    
    
    """
    ...

@overload
def H(qubit_addr: int) -> QGate:
    """
    Create a H gate
    
    Args:
        qubit_addr: quantum gate operate qubits addr
    
    Returns:
        a H gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def H(qubit_addr_list: List[int]) -> QCircuit:
    """
    Create a H gate
    
    Args:
        qubit_list_addr: quantum gate  qubits list addr
    
    Returns:
        a H gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    """
    ...

def HHL_solve_linear_equations(matrix_A: List[complex], data_b: List[float], precision_cnt: int = 0) -> List[complex]:
    """
    Use HHL algorithm to solve the target linear systems of equations : Ax = b
    
    Args:
        matrix_A: a unitary matrix or Hermitian N*N matrix with N = 2 ^ n
    
        data_b: a given vector
    
        precision_cnt: The count of digits after the decimal point
                       default is 0, indicates that there are only integer solutions.
    
    Returns:
        QStat The solution of equation, i.e.x for Ax = b
    
    Notes:
        The higher the precision is, the more qubit number and circuit - depth will be,
        for example: 1 - bit precision, 4 additional qubits are required,
        for 2 - bit precision, we need 7 additional qubits, and so on.
    """
    ...

@overload
def I(qubit: Qubit) -> QGate:
    """
    Create a I gate
    
    Args:
        qubit : quantum gate operate qubit
    
    Returns:
        a I gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def I(qubit_list: QVec) -> QCircuit:
    """
    Create a I gate
    
    Args:
        qubit_list: quantum gate operate qubits list
    
    Returns:
        a I gate node
    Raises:
        run_fail: An error occurred construct in gate node
    
    
    """
    ...

@overload
def I(qubit_addr: int) -> QGate:
    """
    Create a I gate
    
    Args:
        qubit_addr: quantum gate operate qubits addr
    
    Returns:
        a I gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def I(qubit_addr_list: List[int]) -> QCircuit:
    """
    Create a I gate
    
    Args:
        qubit_list_addr: quantum gate  qubits list addr
    
    Returns:
        a I gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    """
    ...

def MAJ(arg0: Qubit, arg1: Qubit, arg2: Qubit) -> QCircuit:
    """
    Quantum adder MAJ module
    """
    ...

def MAJ2(arg0: QVec, arg1: QVec, arg2: Qubit) -> QCircuit:
    """
    Quantum adder MAJ2 module
    """
    ...

@overload
def MS(first_qubit: Qubit, second_qubit: Qubit) -> QGate:
    """
    Returns:
        a MS gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def MS(first_qubit_list: QVec, second_qubit_list: QVec) -> QCircuit:
    """
    Returns:
        a MS gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def MS(first_qubit_addr: int, second_qubit_addr: int) -> QGate:
    """
    """
    ...

@overload
def MS(first_qubit_addr_list: List[int], second_qubit_addr_list: List[int]) -> QCircuit:
    """
    Returns:
        a MS gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    """
    ...

@overload
def Measure(qubit: Qubit, cbit: ClassicalCondition) -> QMeasure:
    """
    Create a measure node.
    
    Args:
        qubit: the qubit to be measured.
    
        cbit: classical bit that stores the quantum measurement result.
    
    Returns:
        a quantum measure node.
    
    
    """
    ...

@overload
def Measure(qubit: Qubit, cbit: CBit) -> QMeasure:
    """
    Create a measure node.
    
    Args:
        qubit: the qubit to be measured.
    
        cbit: classical bit that stores the quantum measurement result.
    
    Returns:
        a quantum measure node.
    
    
    """
    ...

@overload
def Measure(qubit_addr: int, cbit_addr: int) -> QMeasure:
    """
    Create a measure node.
    
    Args:
        qubit_addr: address of the qubit to be measured.
    
        cbit_addr: address of the classical bit that stores the quantum measurement result.
    
    Returns:
        a quantum measure node.
    
    """
    ...

@overload
def OBMT_mapping(prog: QProg, quantum_machine: QuantumMachine, b_optimization: bool = False, max_partial: int = 4294967295, max_children: int = 4294967295, config_data: str = 'QPandaConfig.json') -> QProg:
    """
    OPT_BMT mapping
    
    Args:
        prog: the target prog
    
        quantum_machine: quantum machine
    
        b_optimization: whether open the optimization
    
        max_partial: Limits the max number of partial solutions per step, There is no limit by default
    
        max_children: Limits the max number of candidate - solutions per double gate, There is no limit by default
    
        config_data: config data, @See JsonConfigParam::load_config()
    
    Returns:
        mapped quantum program
    
    """
    ...

@overload
def OBMT_mapping(prog: QProg, quantum_machine: QuantumMachine, b_optimization: bool, arch_matrix: numpy.ndarray[numpy.float64[m,n]]) -> QProg:
    """
    OPT_BMT mapping
    
    Args:
        prog: the target prog
    
        quantum_machine: quantum machine
    
        b_optimization: whether open the optimization
    
        arch_matrix: arch graph matrix
    
    Returns:
        mapped quantum program
    """
    ...

@overload
def P(qubit: Qubit, angle: float) -> QGate:
    """
    Returns:
        a P gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def P(qubit_list: QVec, angle: float) -> QCircuit:
    """
    Create a P gate
    Args:
        qubit_list: quantum gate operate qubits list
        args : quantum gate angles
    
    Returns:
        a P gate node
    Raises:
        run_fail: An error occurred construct in gate node
    
    
    """
    ...

@overload
def P(qubit_addr: int, angle: float) -> QGate:
    """
    Create a P gate
    Args:
        qubit_addr: quantum gate operate qubits addr
        args : quantum gate angles
    
    Returns:
        a P gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def P(qubit_addr_list: List[int], angle: float) -> QCircuit:
    """
    Create a P gate
    Args:
        qubit_list_addr: quantum gate  qubits list addr
        args : quantum gate angles
    
    Returns:
        a P gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    """
    ...

def PMeasure(arg0: QVec, arg1: int) -> List[Tuple[int,float]]:
    """
    Deprecated, use pmeasure instead.
    
    Args:
        QVec: pmeasure qubits list.
    
        select_num: result select num.
    
    Returns:
        result: pmeasure qubits result.
    
    """
    ...

def PMeasure_no_index(arg0: QVec) -> List[float]:
    """
    Deprecated, use pmeasure_no_index instead.
    
    Args:
        QVec: pmeasure qubits list.
    
    Returns:
        result: pmeasure qubits result.
    
    """
    ...

def QAdd(arg0: QVec, arg1: QVec, arg2: QVec) -> QCircuit:
    """
    Quantum adder that supports signed operations, but ignore carry
    """
    ...

def QAdder(arg0: QVec, arg1: QVec, arg2: Qubit, arg3: Qubit) -> QCircuit:
    """
    Quantum adder with carry
    """
    ...

def QAdderIgnoreCarry(arg0: QVec, arg1: QVec, arg2: Qubit) -> QCircuit:
    """
    
    Args:
    
        QVec: qubits list a
        QVec: qubits list b
        QVec: qubits list c
        Qubit: qubit
    
    Returns:
    
        result : circuit 
    
    Raises:
        run_fail: An error occurred in QAdderIgnoreCarry
    
    """
    ...

def QComplement(arg0: QVec, arg1: QVec) -> QCircuit:
    """
    Convert quantum state to binary complement representation
    """
    ...

def QDiv(arg0: QVec, arg1: QVec, arg2: QVec, arg3: QVec, arg4: ClassicalCondition) -> QProg:
    """
    Quantum division
    """
    ...

def QDivWithAccuracy(arg0: QVec, arg1: QVec, arg2: QVec, arg3: QVec, arg4: QVec, arg5: List[ClassicalCondition]) -> QProg:
    """
    
    Args:
    
        QVec: qubits list a
        QVec: qubits list b
        QVec: qubits list c
        QVec: qubits list k
        QVec: qubits list f
        QVec: qubits list s
        list: ClassicalCondition list
    
    Returns:
    
        result : circuit 
    
    Raises:
        run_fail: An error occurred in QDivWithAccuracy
    
    """
    ...

def QDivider(a: QVec, b: QVec, c: QVec, k: QVec, t: ClassicalCondition) -> QProg:
    """
    Quantum division, only supports positive division, and the highest position of a and b and c is sign bit
    """
    ...

def QDividerWithAccuracy(a: QVec, b: QVec, c: QVec, k: QVec, f: QVec, s: List[ClassicalCondition]) -> QProg:
    """
    
    Args:
    
        QVec: qubits list a
        QVec: qubits list b
        QVec: qubits list c
        QVec: qubits list k
        QVec: qubits list f
        QVec: qubits list s
        list: ClassicalCondition list
    
    Returns:
    
        result : circuit 
    
    Raises:
        run_fail: An error occurred in QDividerWithAccuracy
    
    """
    ...

@overload
def QDouble(first_qubit: Qubit, second_qubit: Qubit, matrix: List[complex]) -> QGate:
    """
    Returns:
        a QDouble gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def QDouble(first_qubit_list: QVec, second_qubit_list: QVec, matrix: List[complex]) -> QCircuit:
    """
    Returns:
        a QDouble gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def QDouble(first_qubit_addr: int, second_qubit_addr: int, matrix: List[complex]) -> QGate:
    """
    Returns:
        a QDouble gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def QDouble(first_qubit_addr_list: List[int], second_qubit_addr_list: List[int], matrix: List[complex]) -> QCircuit:
    """
    Returns:
        a QDouble gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    """
    ...

def QFT(qubits: QVec) -> QCircuit:
    """
    Build QFT quantum circuit
    
    Args:
        qvec: qubit list
    
    Returns:
        result : qft circuit
    Raises:
        run_fail: An error occurred in QFT
    
    """
    ...

def QMul(arg0: QVec, arg1: QVec, arg2: QVec, arg3: QVec) -> QCircuit:
    """
    Quantum multiplication
    """
    ...

def QMultiplier(arg0: QVec, arg1: QVec, arg2: QVec, arg3: QVec) -> QCircuit:
    """
    Quantum multiplication, only supports positive multiplication
    """
    ...

def QOracle(qubit_list: QVec, matrix: numpy.ndarray[numpy.complex128[m,n]], tol: float = 1e-10) -> QGate:
    """
    Generate QOracle Gate.
    
    Args:
        qubit_list: gate in qubit list.
    
        matrix: gate operator matrix.
    
    Returns:
        Oracle gate.
    
    """
    ...

def QPE(control_qubits: QVec, target_qubits: QVec, matrix: List[complex], b_estimate_eigenvalue: bool = False) -> QCircuit:
    """
    Quantum phase estimation
    
    Args:
        control_qubits: control qubit list
        target_qubits: target qubit list
        matrix: matrix
    
    Returns:
        result : QPE circuit
    Raises:
        run_fail: An error occurred in QPE
    
    """
    ...

def QSub(arg0: QVec, arg1: QVec, arg2: QVec) -> QCircuit:
    """
    Quantum subtraction
    """
    ...

@overload
def RX(qubit: Qubit, angle: float) -> QGate:
    """
    Returns:
        a RX gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def RX(qubit_list: QVec, angle: float) -> QCircuit:
    """
    Create a RX gate
    Args:
        qubit_list: quantum gate operate qubits list
        args : quantum gate angles
    
    Returns:
        a RX gate node
    Raises:
        run_fail: An error occurred construct in gate node
    
    
    """
    ...

@overload
def RX(qubit_addr: int, angle: float) -> QGate:
    """
    Create a RX gate
    Args:
        qubit_addr: quantum gate operate qubits addr
        args : quantum gate angles
    
    Returns:
        a RX gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def RX(qubit_addr_list: List[int], angle: float) -> QCircuit:
    """
    Create a RX gate
    Args:
        qubit_list_addr: quantum gate  qubits list addr
        args : quantum gate angles
    
    Returns:
        a RX gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    """
    ...

@overload
def RXX(control_qubit: Qubit, target_qubit: Qubit, alpha_angle: float) -> QGate:
    """
    Create a RXX gate
    
    Args:
        Qubit : control qubit
        Qubit : target qubit
        double: gate rotation angle theta
    
    Returns:
        a RXX gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def RXX(control_qubit_list: QVec, target_qubit_list: QVec, alpha_angle: float) -> QCircuit:
    """
    Create a RXX gate
    
    Args:
        control_qubit_list : control qubit list
        target_qubit_list : target qubit list
        double: gate rotation angle theta
    
    Returns:
        a RXX gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def RXX(control_qubit_addr: int, target_qubit_addr: int, alpha_angle: float) -> QGate:
    """
    Create a RXX gate
    
    Args:
        qubit addr : control qubit addr 
        qubit addr : target qubit addr 
        double: gate rotation angle theta
    
    Returns:
        a RXX gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def RXX(control_qubit_addr_list: List[int], target_qubit_addr_list: List[int], alpha_angle: float) -> QCircuit:
    """
    Create a RXX gate
    
    Args:
        qubit addr list : control qubit addr list
        qubit addr list : target qubit addr list
        double: gate rotation angle theta
    
    Returns:
        a RXX gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    """
    ...

@overload
def RY(qubit: Qubit, angle: float) -> QGate:
    """
    Returns:
        a RY gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def RY(qubit_list: QVec, angle: float) -> QCircuit:
    """
    Create a RY gate
    Args:
        qubit_list: quantum gate operate qubits list
        args : quantum gate angles
    
    Returns:
        a RY gate node
    Raises:
        run_fail: An error occurred construct in gate node
    
    
    """
    ...

@overload
def RY(qubit_addr: int, angle: float) -> QGate:
    """
    Create a RY gate
    Args:
        qubit_addr: quantum gate operate qubits addr
        args : quantum gate angles
    
    Returns:
        a RY gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def RY(qubit_addr_list: List[int], angle: float) -> QCircuit:
    """
    Create a RY gate
    Args:
        qubit_list_addr: quantum gate  qubits list addr
        args : quantum gate angles
    
    Returns:
        a RY gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    """
    ...

@overload
def RYY(control_qubit: Qubit, target_qubit: Qubit, alpha_angle: float) -> QGate:
    """
    Create a RYY gate
    
    Args:
        Qubit : control qubit
        Qubit : target qubit
        double: gate rotation angle theta
    
    Returns:
        a RYY gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def RYY(control_qubit_list: QVec, target_qubit_list: QVec, alpha_angle: float) -> QCircuit:
    """
    Create a RYY gate
    
    Args:
        control_qubit_list : control qubit list
        target_qubit_list : target qubit list
        double: gate rotation angle theta
    
    Returns:
        a RYY gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def RYY(control_qubit_addr: int, target_qubit_addr: int, alpha_angle: float) -> QGate:
    """
    Create a RYY gate
    
    Args:
        qubit addr : control qubit addr 
        qubit addr : target qubit addr 
        double: gate rotation angle theta
    
    Returns:
        a RYY gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def RYY(control_qubit_addr_list: List[int], target_qubit_addr_list: List[int], alpha_angle: float) -> QCircuit:
    """
    Create a RYY gate
    
    Args:
        qubit addr list : control qubit addr list
        qubit addr list : target qubit addr list
        double: gate rotation angle theta
    
    Returns:
        a RYY gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    """
    ...

@overload
def RZ(qubit: Qubit, angle: float) -> QGate:
    """
    Returns:
        a RZ gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def RZ(qubit_list: QVec, angle: float) -> QCircuit:
    """
    Create a RZ gate
    Args:
        qubit_list: quantum gate operate qubits list
        args : quantum gate angles
    
    Returns:
        a RZ gate node
    Raises:
        run_fail: An error occurred construct in gate node
    
    
    """
    ...

@overload
def RZ(qubit_addr: int, angle: float) -> QGate:
    """
    Create a RZ gate
    Args:
        qubit_addr: quantum gate operate qubits addr
        args : quantum gate angles
    
    Returns:
        a RZ gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def RZ(qubit_addr_list: List[int], angle: float) -> QCircuit:
    """
    Create a RZ gate
    Args:
        qubit_list_addr: quantum gate  qubits list addr
        args : quantum gate angles
    
    Returns:
        a RZ gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    """
    ...

@overload
def RZX(control_qubit: Qubit, target_qubit: Qubit, alpha_angle: float) -> QGate:
    """
    Create a RZX gate
    
    Args:
        Qubit : control qubit
        Qubit : target qubit
        double: gate rotation angle theta
    
    Returns:
        a RZX gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def RZX(control_qubit_list: QVec, target_qubit_list: QVec, alpha_angle: float) -> QCircuit:
    """
    Create a RZX gate
    
    Args:
        control_qubit_list : control qubit list
        target_qubit_list : target qubit list
        double: gate rotation angle theta
    
    Returns:
        a RZX gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def RZX(control_qubit_addr: int, target_qubit_addr: int, alpha_angle: float) -> QGate:
    """
    Create a RZX gate
    
    Args:
        qubit addr : control qubit addr 
        qubit addr : target qubit addr 
        double: gate rotation angle theta
    
    Returns:
        a RZX gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def RZX(control_qubit_addr_list: List[int], target_qubit_addr_list: List[int], alpha_angle: float) -> QCircuit:
    """
    Create a RZX gate
    
    Args:
        qubit addr list : control qubit addr list
        qubit addr list : target qubit addr list
        double: gate rotation angle theta
    
    Returns:
        a RZX gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    """
    ...

@overload
def RZZ(control_qubit: Qubit, target_qubit: Qubit, alpha_angle: float) -> QGate:
    """
    Create a RZZ gate
    
    Args:
        Qubit : control qubit
        Qubit : target qubit
        double: gate rotation angle theta
    
    Returns:
        a RZZ gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def RZZ(control_qubit_list: QVec, target_qubit_list: QVec, alpha_angle: float) -> QCircuit:
    """
    Create a RZZ gate
    
    Args:
        control_qubit_list : control qubit list
        target_qubit_list : target qubit list
        double: gate rotation angle theta
    
    Returns:
        a RZZ gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def RZZ(control_qubit_addr: int, target_qubit_addr: int, alpha_angle: float) -> QGate:
    """
    Create a RZZ gate
    
    Args:
        qubit addr : control qubit addr 
        qubit addr : target qubit addr 
        double: gate rotation angle theta
    
    Returns:
        a RZZ gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def RZZ(control_qubit_addr_list: List[int], target_qubit_addr_list: List[int], alpha_angle: float) -> QCircuit:
    """
    Create a RZZ gate
    
    Args:
        qubit addr list : control qubit addr list
        qubit addr list : target qubit addr list
        double: gate rotation angle theta
    
    Returns:
        a RZZ gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    """
    ...

@overload
def Reset(qubit: Qubit) -> QReset:
    """
    Create a Reset node.
    
    Args:
        qubit (Qubit *): The qubit to be reset.
    
    Returns:
        A Reset node representing the operation.
    
    
    """
    ...

@overload
def Reset(qubit_addr: int) -> QReset:
    """
    Create a Reset node.
    
    Args:
        qubit_addr (int): Address of the qubit to be reset.
    
    Returns:
        A Reset node representing the operation.
    
    """
    ...

@overload
def S(qubit: Qubit) -> QGate:
    """
    Create a S gate
    
    Args:
        qubit : quantum gate operate qubit
    
    Returns:
        a S gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def S(qubit_list: QVec) -> QCircuit:
    """
    Create a S gate
    
    Args:
        qubit_list: quantum gate operate qubits list
    
    Returns:
        a S gate node
    Raises:
        run_fail: An error occurred construct in gate node
    
    
    """
    ...

@overload
def S(qubit_addr: int) -> QGate:
    """
    Create a S gate
    
    Args:
        qubit_addr: quantum gate operate qubits addr
    
    Returns:
        a S gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def S(qubit_addr_list: List[int]) -> QCircuit:
    """
    Create a S gate
    
    Args:
        qubit_list_addr: quantum gate  qubits list addr
    
    Returns:
        a S gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    """
    ...

@overload
def SWAP(first_qubit: Qubit, second_qubit: Qubit) -> QGate:
    """
    Returns:
        a SWAP gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def SWAP(first_qubit_list: QVec, second_qubit_list: QVec) -> QCircuit:
    """
    Returns:
        a SWAP gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def SWAP(first_qubit_addr: int, second_qubit_addr: int) -> QGate:
    """
    """
    ...

@overload
def SWAP(first_qubit_addr_list: List[int], second_qubit_addr_list: List[int]) -> QCircuit:
    """
    Returns:
        a SWAP gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    """
    ...

def Shor_factorization(arg0: int) -> Tuple[bool,Tuple[int,int]]:
    """
    Use Shor factorize integer num
    
    Args:
        int: target integer num
        result: Shor result
    
    Returns:
        result : Shor_factorization search result
    Raises:
        run_fail: An error occurred in Shor_factorization
    
    """
    ...

@overload
def SqiSWAP(first_qubit: Qubit, second_qubit: Qubit) -> QGate:
    """
    Returns:
        a SqiSWAP gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def SqiSWAP(first_qubit_list: QVec, second_qubit_list: QVec) -> QCircuit:
    """
    Returns:
        a SqiSWAP gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def SqiSWAP(first_qubit_addr: int, second_qubit_addr: int) -> QGate:
    """
    """
    ...

@overload
def SqiSWAP(first_qubit_addr_list: List[int], second_qubit_addr_list: List[int]) -> QCircuit:
    """
    Returns:
        a SqiSWAP gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    """
    ...

@overload
def T(qubit: Qubit) -> QGate:
    """
    Create a T gate
    
    Args:
        qubit : quantum gate operate qubit
    
    Returns:
        a T gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def T(qubit_list: QVec) -> QCircuit:
    """
    Create a T gate
    
    Args:
        qubit_list: quantum gate operate qubits list
    
    Returns:
        a T gate node
    Raises:
        run_fail: An error occurred construct in gate node
    
    
    """
    ...

@overload
def T(qubit_addr: int) -> QGate:
    """
    Create a T gate
    
    Args:
        qubit_addr: quantum gate operate qubits addr
    
    Returns:
        a T gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def T(qubit_addr_list: List[int]) -> QCircuit:
    """
    Create a T gate
    
    Args:
        qubit_list_addr: quantum gate  qubits list addr
    
    Returns:
        a T gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    """
    ...

@overload
def Toffoli(control_qubit_first: Qubit, control_qubit_second: Qubit, target_qubit: Qubit) -> QGate:
    """
    Create a Toffoli gate.
    
    Args:
        control_qubit_first (Qubit *): First control qubit.
    
        control_qubit_second (Qubit *): Second control qubit.
    
        target_qubit (Qubit *): Target qubit.
    
    Returns:
        A Toffoli node representing the operation.
    
    
    """
    ...

@overload
def Toffoli(control_qubit_addr_first: int, control_qubit_addr_second: int, target_qubit_addr: int) -> QGate:
    """
    Create a Toffoli gate.
    
    Args:
        control_qubit_addr_first (int): Address of the first control qubit.
    
        control_qubit_addr_second (int): Address of the second control qubit.
    
        target_qubit_addr (int): Address of the target qubit.
    
    Returns:
        A Toffoli node representing the operation.
    
    """
    ...

@overload
def U1(qubit: Qubit, angle: float) -> QGate:
    """
    Returns:
        a U1 gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def U1(qubit_list: QVec, angle: float) -> QCircuit:
    """
    Create a U1 gate
    Args:
        qubit_list: quantum gate operate qubits list
        args : quantum gate angles
    
    Returns:
        a U1 gate node
    Raises:
        run_fail: An error occurred construct in gate node
    
    
    """
    ...

@overload
def U1(qubit_addr: int, angle: float) -> QGate:
    """
    Create a U1 gate
    Args:
        qubit_addr: quantum gate operate qubits addr
        args : quantum gate angles
    
    Returns:
        a U1 gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def U1(qubit_addr_list: List[int], angle: float) -> QCircuit:
    """
    Create a U1 gate
    Args:
        qubit_list_addr: quantum gate  qubits list addr
        args : quantum gate angles
    
    Returns:
        a U1 gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    """
    ...

@overload
def U2(qubit: Qubit, phi_angle: float, lambda_angle: float) -> QGate:
    """
    Returns:
        a U2 gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def U2(qubit_list: QVec, phi_angle: float, lambda_angle: float) -> QCircuit:
    """
    Create a U2 gate
    Args:
        qubit_list: quantum gate operate qubits list
        args : quantum gate angles
    
    Returns:
        a U2 gate node
    Raises:
        run_fail: An error occurred construct in gate node
    
    
    """
    ...

@overload
def U2(qubit_addr: int, phi_angle: float, lambda_angle: float) -> QGate:
    """
    Create a U2 gate
    Args:
        qubit_addr: quantum gate operate qubits addr
        args : quantum gate angles
    
    Returns:
        a U2 gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def U2(qubit_addr_list: List[int], phi_angle: float, lambda_angle: float) -> QCircuit:
    """
    Create a U2 gate
    Args:
        qubit_list_addr: quantum gate  qubits list addr
        args : quantum gate angles
    
    Returns:
        a U2 gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    """
    ...

@overload
def U3(qubit: Qubit, theta_angle: float, phi_angle: float, lambda_angle: float) -> QGate:
    """
    Returns:
        a U3 gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def U3(qubit_list: QVec, theta_angle: float, phi_angle: float, lambda_angle: float) -> QCircuit:
    """
    Create a U3 gate
    Args:
        qubit_list: quantum gate operate qubits list
        args : quantum gate angles
    
    Returns:
        a U3 gate node
    Raises:
        run_fail: An error occurred construct in gate node
    
    
    """
    ...

@overload
def U3(qubit_addr: int, theta_angle: float, phi_angle: float, lambda_angle: float) -> QGate:
    """
    Create a U3 gate
    Args:
        qubit_addr: quantum gate operate qubits addr
        args : quantum gate angles
    
    Returns:
        a U3 gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def U3(qubit_addr_list: List[int], theta_angle: float, phi_angle: float, lambda_angle: float) -> QCircuit:
    """
    Create a U3 gate
    Args:
        qubit_list_addr: quantum gate  qubits list addr
        args : quantum gate angles
    
    Returns:
        a U3 gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    """
    ...

@overload
def U4(matrix: List[complex], qubit: Qubit) -> QGate:
    """
    Create a U4 gate.
    
    Args:
        matrix: the U4 gate matrix to be applied.
    
        qubit: the target qubit for the U4 gate.
    
    Returns:
        A U4 node representing the operation.
    
    
    """
    ...

@overload
def U4(alpha_angle: float, beta_angle: float, gamma_angle: float, delta_angle: float, qubit: Qubit) -> QGate:
    """
    Create a U4 gate.
    
    Args:
        alpha_angle: the alpha angle for the U4 gate.
    
        beta_angle: the beta angle for the U4 gate.
    
        gamma_angle: the gamma angle for the U4 gate.
    
        delta_angle: the delta angle for the U4 gate.
    
        qubit: the target qubit for the U4 gate.
    
    Returns:
        A U4 node representing the operation.
    
    
    """
    ...

@overload
def U4(qubit: Qubit, matrix: List[complex]) -> QGate:
    """
    Create a U4 gate.
    
    Args:
        qubit: the target qubit for the U4 gate.
    
        matrix: the U4 gate matrix to be applied.
    
    Returns:
        A U4 node representing the operation.
    
    
    """
    ...

@overload
def U4(qubit_list: QVec, matrix: List[complex]) -> QCircuit:
    """
    Create a U4 gate.
    
    Args:
        qubit_list: the list of target qubits for the U4 gate.
    
        matrix: the U4 gate matrix to be applied.
    
    Returns:
        A U4 node representing the operation.
    
    
    """
    ...

@overload
def U4(qubit_addr: int, matrix: List[complex]) -> QGate:
    """
    Create a U4 gate.
    
    Args:
        qubit_addr: the address of the target qubit for the U4 gate.
    
        matrix: the U4 gate matrix to be applied.
    
    Returns:
        A U4 node representing the operation.
    
    
    """
    ...

@overload
def U4(qubit_addr_list: List[int], matrix: List[complex]) -> QCircuit:
    """
    Create a U4 gate.
    
    Args:
        qubit_addr_list: the list of addresses for the target qubits of the U4 gate.
    
        matrix: the U4 gate matrix to be applied.
    
    Returns:
        A U4 node representing the operation.
    
    
    """
    ...

@overload
def U4(qubit: Qubit, alpha_anlge: float, beta_anlge: float, gamma_anlge: float, delta_anlge: float) -> QGate:
    """
    Create a U4 gate.
    
    Args:
        qubit: the target qubit for the U4 gate.
    
        alpha_angle: the alpha angle for the U4 gate.
    
        beta_angle: the beta angle for the U4 gate.
    
        gamma_angle: the gamma angle for the U4 gate.
    
        delta_angle: the delta angle for the U4 gate.
    
    Returns:
        A U4 node representing the operation.
    
    
    """
    ...

@overload
def U4(qubit_list: QVec, alpha_angle: float, beta_angle: float, gamma_angle: float, delta_angle: float) -> QCircuit:
    """
    Create a U4 gate.
    
    
    Args:
        qubit_list: the list of target qubits for the U4 gate.
    
        alpha_angle: the alpha angle for the U4 gate.
    
        beta_angle: the beta angle for the U4 gate.
    
        gamma_angle: the gamma angle for the U4 gate.
    
        delta_angle: the delta angle for the U4 gate.
    
    Returns:
        A U4 node representing the operation.
    
    """
    ...

@overload
def U4(qubit_addr: int, alpha_anlge: float, beta_anlge: float, gamma_anlge: float, delta_anlge: float) -> QGate:
    """
    Create a U4 gate.
    
    Args:
        qubit_addr: the address of the target qubit for the U4 gate.
    
        alpha_angle: the alpha angle for the U4 gate.
    
        beta_angle: the beta angle for the U4 gate.
    
        gamma_angle: the gamma angle for the U4 gate.
    
        delta_angle: the delta angle for the U4 gate.
    
    Returns:
        A U4 node representing the operation.
    
    """
    ...

@overload
def U4(qubit_addr_list: List[int], alpha_anlge: float, beta_anlge: float, gamma_anlge: float, delta_anlge: float) -> QCircuit:
    """
    Create a U4 gate.
    
    Args:
        qubit_addr_list: the list of addresses of target qubits for the U4 gate.
    
        alpha_angle: the alpha angle for the U4 gate.
    
        beta_angle: the beta angle for the U4 gate.
    
        gamma_angle: the gamma angle for the U4 gate.
    
        delta_angle: the delta angle for the U4 gate.
    
    Returns:
        A U4 node representing the operation.
    """
    ...

def UMA(arg0: Qubit, arg1: Qubit, arg2: Qubit) -> QCircuit:
    """
    Quantum adder UMA module
    """
    ...

def VQG_CNOT_batch(*args, **kwargs) -> Any:
    """
    variational quantum CNOT batch gates
    """
    ...

def VQG_CU_batch(*args, **kwargs) -> Any:
    """
    variational quantum CU batch gates
    """
    ...

def VQG_CZ_batch(*args, **kwargs) -> Any:
    """
    variational quantum CZ batch gates
    """
    ...

def VQG_H_batch(*args, **kwargs) -> Any:
    """
    variational quantum H batch gates
    """
    ...

def VQG_I_batch(*args, **kwargs) -> Any:
    """
    variational quantum I batch gates
    """
    ...

def VQG_SWAP_batch(*args, **kwargs) -> Any:
    """
    variational quantum SWAP batch gates
    """
    ...

def VQG_S_batch(*args, **kwargs) -> Any:
    """
    variational quantum S batch gates
    """
    ...

def VQG_SqiSWAP_batch(*args, **kwargs) -> Any:
    """
    variational quantum SqiSWAP batch gates
    """
    ...

def VQG_T_batch(*args, **kwargs) -> Any:
    """
    variational quantum T batch gates
    """
    ...

def VQG_U1_batch(*args, **kwargs) -> Any:
    """
    variational quantum U1 batch gates
    """
    ...

def VQG_U2_batch(*args, **kwargs) -> Any:
    """
    variational quantum U2 batch gates
    """
    ...

def VQG_U3_batch(*args, **kwargs) -> Any:
    """
    variational quantum U3 batch gates
    """
    ...

def VQG_U4_batch(*args, **kwargs) -> Any:
    """
    variational quantum U4 batch gates
    """
    ...

def VQG_X1_batch(*args, **kwargs) -> Any:
    """
    variational quantum X1 batch gates
    """
    ...

def VQG_X_batch(*args, **kwargs) -> Any:
    """
    variational quantum X batch gates
    """
    ...

def VQG_Y1_batch(*args, **kwargs) -> Any:
    """
    variational quantum Y1 batch gates
    """
    ...

def VQG_Y_batch(*args, **kwargs) -> Any:
    """
    variational quantum Y batch gates
    """
    ...

def VQG_Z1_batch(*args, **kwargs) -> Any:
    """
    variational quantum Z1 batch gates
    """
    ...

def VQG_Z_batch(*args, **kwargs) -> Any:
    """
    variational quantum Z batch gates
    """
    ...

def VQG_iSWAP_batch(*args, **kwargs) -> Any:
    """
    variational quantum iSWAP batch gates
    """
    ...

@overload
def X(qubit: Qubit) -> QGate:
    """
    Create a X gate
    
    Args:
        qubit : quantum gate operate qubit
    
    Returns:
        a X gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def X(qubit_list: QVec) -> QCircuit:
    """
    Create a X gate
    
    Args:
        qubit_list: quantum gate operate qubits list
    
    Returns:
        a X gate node
    Raises:
        run_fail: An error occurred construct in gate node
    
    
    """
    ...

@overload
def X(qubit_addr: int) -> QGate:
    """
    Create a X gate
    
    Args:
        qubit_addr: quantum gate operate qubits addr
    
    Returns:
        a X gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def X(qubit_addr_list: List[int]) -> QCircuit:
    """
    Create a X gate
    
    Args:
        qubit_list_addr: quantum gate  qubits list addr
    
    Returns:
        a X gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    """
    ...

@overload
def X1(qubit: Qubit) -> QGate:
    """
    Create a X1 gate
    
    Args:
        qubit : quantum gate operate qubit
    
    Returns:
        a X1 gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def X1(qubit_list: QVec) -> QCircuit:
    """
    Create a X1 gate
    
    Args:
        qubit_list: quantum gate operate qubits list
    
    Returns:
        a X1 gate node
    Raises:
        run_fail: An error occurred construct in gate node
    
    
    """
    ...

@overload
def X1(qubit_addr: int) -> QGate:
    """
    Create a X1 gate
    
    Args:
        qubit_addr: quantum gate operate qubits addr
    
    Returns:
        a X1 gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def X1(qubit_addr_list: List[int]) -> QCircuit:
    """
    Create a X1 gate
    
    Args:
        qubit_list_addr: quantum gate  qubits list addr
    
    Returns:
        a X1 gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    """
    ...

@overload
def Y(qubit: Qubit) -> QGate:
    """
    Create a Y gate
    
    Args:
        qubit : quantum gate operate qubit
    
    Returns:
        a Y gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def Y(qubit_list: QVec) -> QCircuit:
    """
    Create a Y gate
    
    Args:
        qubit_list: quantum gate operate qubits list
    
    Returns:
        a Y gate node
    Raises:
        run_fail: An error occurred construct in gate node
    
    
    """
    ...

@overload
def Y(qubit_addr: int) -> QGate:
    """
    Create a Y gate
    
    Args:
        qubit_addr: quantum gate operate qubits addr
    
    Returns:
        a Y gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def Y(qubit_addr_list: List[int]) -> QCircuit:
    """
    Create a Y gate
    
    Args:
        qubit_list_addr: quantum gate  qubits list addr
    
    Returns:
        a Y gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    """
    ...

@overload
def Y1(qubit: Qubit) -> QGate:
    """
    Create a Y1 gate
    
    Args:
        qubit : quantum gate operate qubit
    
    Returns:
        a Y1 gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def Y1(qubit_list: QVec) -> QCircuit:
    """
    Create a Y1 gate
    
    Args:
        qubit_list: quantum gate operate qubits list
    
    Returns:
        a Y1 gate node
    Raises:
        run_fail: An error occurred construct in gate node
    
    
    """
    ...

@overload
def Y1(qubit_addr: int) -> QGate:
    """
    Create a Y1 gate
    
    Args:
        qubit_addr: quantum gate operate qubits addr
    
    Returns:
        a Y1 gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def Y1(qubit_addr_list: List[int]) -> QCircuit:
    """
    Create a Y1 gate
    
    Args:
        qubit_list_addr: quantum gate  qubits list addr
    
    Returns:
        a Y1 gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    """
    ...

@overload
def Z(qubit: Qubit) -> QGate:
    """
    Create a Z gate
    
    Args:
        qubit : quantum gate operate qubit
    
    Returns:
        a Z gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def Z(qubit_list: QVec) -> QCircuit:
    """
    Create a Z gate
    
    Args:
        qubit_list: quantum gate operate qubits list
    
    Returns:
        a Z gate node
    Raises:
        run_fail: An error occurred construct in gate node
    
    
    """
    ...

@overload
def Z(qubit_addr: int) -> QGate:
    """
    Create a Z gate
    
    Args:
        qubit_addr: quantum gate operate qubits addr
    
    Returns:
        a Z gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def Z(qubit_addr_list: List[int]) -> QCircuit:
    """
    Create a Z gate
    
    Args:
        qubit_list_addr: quantum gate  qubits list addr
    
    Returns:
        a Z gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    """
    ...

@overload
def Z1(qubit: Qubit) -> QGate:
    """
    Create a Z1 gate
    
    Args:
        qubit : quantum gate operate qubit
    
    Returns:
        a Z1 gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def Z1(qubit_list: QVec) -> QCircuit:
    """
    Create a Z1 gate
    
    Args:
        qubit_list: quantum gate operate qubits list
    
    Returns:
        a Z1 gate node
    Raises:
        run_fail: An error occurred construct in gate node
    
    
    """
    ...

@overload
def Z1(qubit_addr: int) -> QGate:
    """
    Create a Z1 gate
    
    Args:
        qubit_addr: quantum gate operate qubits addr
    
    Returns:
        a Z1 gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def Z1(qubit_addr_list: List[int]) -> QCircuit:
    """
    Create a Z1 gate
    
    Args:
        qubit_list_addr: quantum gate  qubits list addr
    
    Returns:
        a Z1 gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    """
    ...

@overload
def _back(arg0: expression, arg1: Dict[var,numpy.ndarray[numpy.float64[m,n]]], arg2: List[var]) -> None:
    """
    """
    ...

@overload
def _back(arg0: expression, arg1: Dict[var,numpy.ndarray[numpy.float64[m,n]]]) -> None:
    """
    """
    ...

@overload
def _back(arg0: var, arg1: Dict[var,numpy.ndarray[numpy.float64[m,n]]]) -> None:
    """
    """
    ...

@overload
def _back(arg0: var, arg1: Dict[var,numpy.ndarray[numpy.float64[m,n]]], arg2: List[var]) -> None:
    """
    """
    ...

def accumulateProbability(probability_list: List[float]) -> List[float]:
    """
    Accumulate the probability from a probability list.
    
    Args:
        probability_list: measured result in probability list form.
    
    Returns:
        accumulated_result: accumulated result.
    
    """
    ...

def accumulate_probabilities(probability_list: List[float]) -> List[float]:
    """
    Accumulate the probability from a probability list.
    
    Args:
        probability_list: measured result in probability list form.
    
    Returns:
        accumulated_result: accumulated result.
    
    """
    ...

def accumulate_probability(probability_list: List[float]) -> List[float]:
    """
    Accumulate the probability from a probability list.
    
    Args:
        probability_list: measured result in probability list form.
    
    Returns:
        accumulated_result: accumulated result.
    
    """
    ...

def acos(arg0: var) -> var:
    """
    """
    ...

@overload
def add(arg0: ClassicalCondition, arg1: ClassicalCondition) -> ClassicalCondition:
    """
    Add two ClassicalCondition objects.
    
    Args:
        a: The first ClassicalCondition.
    
        b: The second ClassicalCondition.
    
    Returns:
        ClassicalCondition: The sum of the two conditions.
    
    
    """
    ...

@overload
def add(arg0: ClassicalCondition, arg1: int) -> ClassicalCondition:
    """
    Add a ClassicalCondition and a bit size.
    
    Args:
        a: The ClassicalCondition to which the bit size will be added.
    
        b: The bit size to be added to the ClassicalCondition.
    
    Returns:
        ClassicalCondition: The resulting ClassicalCondition after addition.
    
    
    """
    ...

@overload
def add(arg0: int, arg1: ClassicalCondition) -> ClassicalCondition:
    """
    Add a bit size and a ClassicalCondition.
    
    Args:
        a: The bit size to be added.
    
        b: The ClassicalCondition to which the bit size will be added.
    
    Returns:
        ClassicalCondition: The resulting ClassicalCondition after addition.
    
    """
    ...

def all_cut_of_graph(adjacent_matrix: List[List[float]], all_cut_list: List[float], target_value_list: List[int]) -> float:
    """
    Generate a graph representation for the max cut problem.
    
    Args:
        adjacent_matrix: The adjacency matrix for the quantum program.
    
        all_cut_list: A list of all cut graphs in the quantum program.
    
        target_value_list: A list of target cut values.
    
    Returns:
        max value: The maximum value found from the cuts.
    
    """
    ...

@overload
def amplitude_encode(qubit: QVec, data: List[float], b_need_check_normalization: bool = True) -> QCircuit:
    """
    Encode the input double data to the amplitude of qubits
    
    Args:
        qubit: quantum program qubits
        data: double data list
        b_need_check_normalization: is need to check normalization
    
    Returns:
        result circuit 
    Raises:
        run_fail: An error occurred in amplitude_encode
    
    
    """
    ...

@overload
def amplitude_encode(qubit: QVec, data: List[complex]) -> QCircuit:
    """
    Encode the input double data to the amplitude of qubits
    
    Args:
        qubit: quantum program qubits
        data: double data list
    
    Returns:
        result circuit 
    Raises:
        run_fail: An error occurred in amplitude_encode
    
    """
    ...

@overload
def apply_QGate(qubit_list: QVec, func_obj: Callable[[Qubit],QGate]) -> QCircuit:
    """
    Apply a quantum gate operation to a list of qubits.
    
    
    Args:
        qubit_list: List of qubits to which the gate will be applied.
    
        func_obj: A function object that takes a Qubit and returns a QGate.
    
    
    Returns:
        QCircuit: The resulting circuit containing the QGate operations on all qubits.
    
    
    """
    ...

@overload
def apply_QGate(qubit_addr_list: List[int], func_obj: Callable[[int],QGate]) -> QCircuit:
    """
    Apply a quantum gate operation to a list of qubit addresses.
    
    
    Args:
        qubit_addr_list: List of qubit addresses to which the gate will be applied.
    
        func_obj: A function object that takes a qubit address (int) and returns a QGate.
    
    
    Returns:
        QCircuit: The resulting circuit containing the QGate operations on all qubits.
    
    """
    ...

def asin(arg0: var) -> var:
    """
    """
    ...

@overload
def assign(arg0: ClassicalCondition, arg1: ClassicalCondition) -> ClassicalCondition:
    """
    Assign the value of one ClassicalCondition to another.
    
    Args:
        a: The ClassicalCondition to be assigned to (passed by reference).
    
        b: The ClassicalCondition to assign from.
    
    Returns:
        ClassicalCondition: The updated value of the first ClassicalCondition.
    
    
    """
    ...

@overload
def assign(arg0: ClassicalCondition, arg1: int) -> ClassicalCondition:
    """
    Assign a bit size value to a ClassicalCondition.
    
    Args:
        a: The ClassicalCondition to be updated (passed by reference).
    
        b: The bit size value to assign.
    
    Returns:
        ClassicalCondition: The updated ClassicalCondition after assignment.
    
    """
    ...

def atan(arg0: var) -> var:
    """
    """
    ...

@overload
def average_gate_fidelity(state1: numpy.ndarray[numpy.complex128[m,n]], state2: List[complex]) -> float:
    """
    Calculate the average gate fidelity between a quantum operation and a quantum state.
    
    Args:
        matrix: a quantum operation represented as a matrix.
    
        state: a single quantum state represented as a list.
    
    Returns:
        The average gate fidelity, a value in the range [0, 1].
    
    
    """
    ...

@overload
def average_gate_fidelity(state1: numpy.ndarray[numpy.complex128[m,n]], state2: numpy.ndarray[numpy.complex128[m,n]]) -> float:
    """
    Calculate the average gate fidelity between two quantum operation matrices.
    
    Args:
        matrix1: the first quantum operation represented as a matrix.
    
        matrix2: the second quantum operation represented as a matrix.
    
    Returns:
        The average gate fidelity, a value in the range [0, 1].
    
    """
    ...

def bin_to_prog(bin_data: List[int], qubit_list: QVec, cbit_list: List[ClassicalCondition], qprog: QProg) -> bool:
    """
    Parse binary data to transform into a quantum program.
    
    Args:
        bin_data: binary data that stores quantum program information.
    
        qubit_list: list of quantum qubits.
    
        cbit_list: list of classical bits.
    
        qprog: quantum program.
    
    Returns:
        prog: the parsed quantum program.
    
    """
    ...

def bind_data(arg0: int, arg1: QVec) -> QCircuit:
    """
    
    Args:
        int: classical data
        QVec: qubits list
    
    Returns:
        result : circuit 
    Raises:
        run_fail: An error occurred in bind_data
    
    """
    ...

def bind_nonnegative_data(arg0: int, arg1: QVec) -> QCircuit:
    """
    
    Args:
        int: classical data
        QVec: qubits list
    
    Returns:
        result : circuit 
    Raises:
        run_fail: An error occurred in bind_nonnegative_data
    
    """
    ...

def build_HHL_circuit(matrix_A: List[complex], data_b: List[float], qvm: QuantumMachine, precision_cnt: int = 0) -> QCircuit:
    """
    build the quantum circuit for HHL algorithm to solve the target linear systems of equations : Ax = b
    
    Args:
        matrix_A: a unitary matrix or Hermitian N*N matrix with N = 2 ^ n
    
        data_b: a given vector
    
        qvm: quantum machine
    
        precision_cnt: The count of digits after the decimal point,
                       default is 0, indicates that there are only integer solutions
    
    Returns:
        QCircuit The whole quantum circuit for HHL algorithm
    
    Notes:
        The higher the precision is, the more qubit number and circuit - depth will be,
        for example: 1 - bit precision, 4 additional qubits are required,
        for 2 - bit precision, we need 7 additional qubits, and so on.
        The final solution = (HHL result) * (normalization factor for b) * (1 << ceil(log2(pow(10, precision_cnt))))
    """
    ...

@overload
def cAlloc() -> ClassicalCondition:
    """
    Allocate a CBit
    After init()
    
    Args:
        none
    
    Returns:
        classic result cbit
    
    
    """
    ...

@overload
def cAlloc(cbit_addr: int) -> ClassicalCondition:
    """
    Allocate a CBit
    After init()
    
    Args:
        cbit_addr: cbit address, should be in [0,29).
    
    Returns:
        classic result cbit
    
    """
    ...

def cAlloc_many(cbit_num: int) -> List[ClassicalCondition]:
    """
    Allocate several CBits
    After init()
    
    Args:
        cbit_num: numbers of cbit want to be created.
    
    Returns:
        list of cbit
    
    """
    ...

def cFree(cbit: ClassicalCondition) -> None:
    """
    Free a CBit
    
    Args:
        CBit: The CBit to be freed.
    
    Returns:
        none
    
    """
    ...

@overload
def cFree_all() -> None:
    """
    Free all CBits
    
    Args:
        none
    
    Returns:
        none
    
    
    """
    ...

@overload
def cFree_all(cbit_list: List[ClassicalCondition]) -> None:
    """
    Free all CBits
    
    Args:
        cbit_list: a list of cbits.
    
    Returns:
        none
    
    """
    ...

def cast_qprog_qcircuit(qprog: QProg) -> QCircuit:
    """
    Cast a quantum program into a quantum circuit.
    
    Args:
        qprog: The quantum program to be cast.
    
    Returns:
        QCircuit: The resulting quantum circuit.
    
    """
    ...

def cast_qprog_qgate(qprog: QProg) -> QGate:
    """
    Cast a quantum program into a quantum gate.
    
    Args:
        qprog: The quantum program to be cast.
    
    Returns:
        None: This function does not return a value.
    
    """
    ...

def cast_qprog_qmeasure(qprog: QProg) -> QMeasure:
    """
    Cast a quantum program into a quantum measurement.
    
    Args:
        qprog: The quantum program to be cast.
    
    Returns:
        None: This function does not return a value.
    
    """
    ...

def circuit_layer(qprog: QProg) -> list:
    """
    Quantum circuit layering.
    
    Args:
        QProg: Quantum program.
    
    Returns:
        A list containing layer information and qubits/cbits in use.
    
    """
    ...

def circuit_optimizer(qprog: QProg, optimizer_cir_vec: List[Tuple[QCircuit,QCircuit]] = [], mode_list: List[QCircuitOPtimizerMode] = []) -> QProg:
    """
    Optimize a quantum circuit.
    
    Args:
        qprog: the quantum program to optimize.
    
        optimizer_cir_vec: a list of quantum circuits for optimization.
    
        mode_list: a list of optimization modes.
    
    Returns:
        the updated quantum program after optimization.
    
    """
    ...

def circuit_optimizer_by_config(qprog: QProg, config_file: str = 'QPandaConfig.json', mode_list: List[QCircuitOPtimizerMode] = []) -> QProg:
    """
    Optimize a quantum circuit using configuration data.
    
    Args:
        qprog: the quantum program to optimize.
    
        config_file: configuration data for optimization.
    
        mode_list: a list of optimization modes.
    
    Returns:
        the updated quantum program after optimization.
    
    """
    ...

def comm_protocol_decode(encode_data: bytes, machine: QuantumMachine) -> Tuple[List[QProg],CommProtocolConfig]:
    """
    Decode binary data into a list of quantum programs using the communication protocol.
    
    Args:
        encode_data: The encoded binary data representing quantum programs.
    
        machine: A pointer to the QuantumMachine used for decoding.
    
    Returns:
        tuple: A tuple containing the decoded program list and the communication protocol configuration.
    
    """
    ...

@overload
def comm_protocol_encode(prog: QProg, config: CommProtocolConfig = ...) -> bytes:
    """
    Encode the communication protocol data into binary format.
    
    Args:
        prog: The quantum program to be encoded.
    
        config: The configuration for the communication protocol. Defaults to an empty configuration.
    
    Returns:
        bytes: The encoded binary data representing the communication protocol.
    
    
    """
    ...

@overload
def comm_protocol_encode(prog_list: List[QProg], config: CommProtocolConfig = ...) -> bytes:
    """
    Encode a list of quantum programs into binary communication protocol data.
    
    Args:
        prog_list: A list of quantum programs to be encoded.
    
        config: The configuration for the communication protocol. Defaults to an empty configuration.
    
    Returns:
        bytes: The encoded binary data representing the communication protocol.
    
    """
    ...

def constModAdd(arg0: QVec, arg1: int, arg2: int, arg3: QVec, arg4: QVec) -> QCircuit:
    """
    
    Args:
       QVec qvec
       int base
       int module_Num
       QVec qvec1
       QVec qvec2
    
    Returns:
        result circuit 
    Raises:
        run_fail: An error occurred in constModAdd
    
    """
    ...

def constModExp(arg0: QVec, arg1: QVec, arg2: int, arg3: int, arg4: QVec, arg5: QVec, arg6: QVec) -> QCircuit:
    """
    
    Args:
       QVec qvec
       int base
       int module_Num
       QVec qvec1
       QVec qvec2
    
    Returns:
        result circuit 
    Raises:
        run_fail: An error occurred in constModExp
    
    """
    ...

def constModMul(arg0: QVec, arg1: int, arg2: int, arg3: QVec, arg4: QVec, arg5: QVec) -> QCircuit:
    """
    
    Args:
       QVec qvec
       int base
       int module_Num
       QVec qvec1
       QVec qvec2
    
    Returns:
        result circuit 
    Raises:
        run_fail: An error occurred in constModMul
    
    """
    ...

def convert_binary_data_to_qprog(machine: QuantumMachine, data: List[int]) -> QProg:
    """
    Parse binary data into a quantum program.
    
    Args:
        machine: The quantum machine used for execution.
    
        data: The binary data representing the quantum program.
    
    Returns:
        QProg: The generated quantum program.
    
    """
    ...

def convert_originir_str_to_qprog(originir_str: str, machine: QuantumMachine) -> list:
    """
    Transform OriginIR string into QProg.
    
    Args:
        originir_str: OriginIR string.
    
        machine: initialized quantum machine.
    
    Returns:
        A list containing QProg, qubit_list, and cbit_list.
    
    """
    ...

def convert_originir_to_qprog(file_path: str, machine: QuantumMachine) -> list:
    """
    Read an OriginIR file and transform it into QProg.
    
    Args:
        file_path: OriginIR file path.
    
        machine: initialized quantum machine.
    
    Returns:
        A list containing QProg, qubit_list, and cbit_list.
    
    """
    ...

def convert_qasm_string_to_qprog(qasm_str: str, machine: QuantumMachine) -> list:
    """
    Transform QASM string into QProg.
    
    Args:
        qasm_str: QASM string.
    
        machine: initialized quantum machine.
    
    Returns:
        A list containing QProg, qubit_list, and cbit_list.
    
    """
    ...

def convert_qasm_to_qprog(file_path: str, machine: QuantumMachine) -> list:
    """
    Read a QASM file and transform it into QProg.
    
    Args:
        file_path: QASM file path.
    
        machine: initialized quantum machine.
    
    Returns:
        A list containing QProg, qubit_list, and cbit_list.
    
    """
    ...

@overload
def convert_qprog_to_binary(qprog: QProg, machine: QuantumMachine) -> List[int]:
    """
    Convert a quantum program into binary data.
    
    Args:
        qprog: quantum program.
    
        machine: quantum machine.
    
    Returns:
        string: binary data representation of the quantum program.
    
    
    """
    ...

@overload
def convert_qprog_to_binary(qprog: QProg, machine: QuantumMachine, fname: str) -> None:
    """
    Store the quantum program in a binary file.
    
    Args:
        qprog: quantum program.
    
        machine: quantum machine.
    
        fname: name of the binary data file.
    
    Returns:
        none: This function does not return a value.
    
    """
    ...

def convert_qprog_to_originir(*args, **kwargs) -> Any:
    """
    Convert QProg to OriginIR string.
    
    Args:
        qprog: quantum program (QProg&).
    
        machine: quantum machine (QuantumMachine*).
    
    Returns:
        originir: OriginIR string. For more information, see the OriginIR introduction:
    
      https://pyqpanda-toturial.readthedocs.io/zh/latest
    
    """
    ...

def convert_qprog_to_qasm(qprog: QProg, machine: QuantumMachine) -> str:
    """
    Convert a quantum program to a QASM instruction string.
    
    Args:
        qprog: The quantum program to be converted.
    
        machine: The quantum machine used for execution.
    
    Returns:
        str: A QASM string representing the quantum program.
    
    """
    ...

def convert_qprog_to_quil(qprog: QProg, machine: QuantumMachine) -> str:
    """
    Convert QProg to Quil instruction.
    
    Args:
        qprog: quantum program (QProg).
    
        machine: quantum machine (QuantumMachine*).
    
    Returns:
        Quil instruction string.
    
    """
    ...

def cos(arg0: var) -> var:
    """
    """
    ...

@overload
def count_gate(quantum_prog: QProg) -> int:
    """
    Count quantum gate number in the quantum program.
    
    Args:
        quantum_prog: quantum program.
    
    Returns:
        result: gate count.
    
    
    """
    ...

@overload
def count_gate(quantum_circuit: QCircuit) -> int:
    """
    Count quantum gate number in the quantum circuit.
    
    Args:
        quantum_circuit: quantum circuit.
    
    Returns:
        result: gate count.
    
    """
    ...

@overload
def count_prog_info(node: QProg, selected_types: List[GateType] = []) -> ProgCount:
    """
    Count quantum program information.
    
    Args:
        node: quantum program (QProg).
    
        selected_types: vector of selected GateType (default is empty).
    
    Returns:
        ProgCount struct.
    
    
    """
    ...

@overload
def count_prog_info(node: QCircuit, selected_types: List[GateType] = []) -> ProgCount:
    """
    Count quantum program information.
    
    Args:
        node: quantum circuit (QCircuit).
    
        selected_types: vector of selected GateType (default is empty).
    
    Returns:
        ProgCount struct.
    
    """
    ...

@overload
def count_qgate_num(prog: QProg, gate_type: int = -1) -> int:
    """
    Count quantum gate number in the quantum program.
    
    Args:
        prog: quantum program (QProg&).
    
        gate_type: type of gate to count (const GateType).
    
    Returns:
        result: number of quantum gates of the specified GateType.
    
    
    """
    ...

@overload
def count_qgate_num(circuit: QCircuit, gate_type: int = -1) -> int:
    """
    Count quantum gate number in the quantum circuit.
    
    Args:
        circuit: quantum circuit (QCircuit&).
    
        gate_type: type of gate to count (const GateType).
    
    Returns:
        result: number of quantum gates of the specified GateType.
    
    """
    ...

def create_empty_circuit() -> QCircuit:
    """
    Create an empty QCircuit container.
    
    Args:
        none
    
    Returns:
        result: An empty QCircuit.
    
    """
    ...

def create_empty_qprog() -> QProg:
    """
    Create an empty QProg container.
    
    Args:
        none.
    
    Returns:
        an empty QProg.
    
    """
    ...

@overload
def create_if_prog(classical_condition: ClassicalCondition, true_node: QProg) -> QIfProg:
    """
    Create a classical quantum IfProg.
    
    Args:
        classical_condition: A quantum cbit representing the condition.
    
        true_node: A quantum IfProg node that defines the operation to execute if the condition is true.
    
    Returns:
        result: A classical quantum IfProg that executes based on the specified condition.
    
    
    """
    ...

@overload
def create_if_prog(classical_condition: ClassicalCondition, true_node: QProg, false_node: QProg) -> QIfProg:
    """
    Create a classical quantum IfProg.
    
    Args:
        classical_condition: A quantum cbit representing the condition.
    
        true_node: A quantum IfProg node that defines the operation to execute if the condition is true.
    
        false_node: A quantum IfProg node that defines the operation to execute if the condition is false.
    
    Returns:
        result: A classical quantum IfProg that executes based on the specified condition.
    
    """
    ...

def create_while_prog(classical_condition: ClassicalCondition, true_node: QProg) -> QWhileProg:
    """
    Create a WhileProg.
    
    Args:
        classical_condition: A quantum cbit representing the condition.
    
        true_node: A quantum QWhile node that defines the operation to execute while the condition is true.
    
    Returns:
        result: A WhileProg that executes the specified operations based on the condition.
    
    """
    ...

def crossEntropy(arg0: var, arg1: var) -> var:
    """
    """
    ...

@overload
def decompose_multiple_control_qgate(qprog: QProg, machine: QuantumMachine, config_file: str = 'QPandaConfig.json') -> QProg:
    """
    Decompose a multiple control quantum gate.
    
    Args:
        qprog: the quantum program containing the gate to be decomposed.
    
        machine: the quantum machine used for decomposition.
    
        config_file: path to the configuration file (default is CONFIG_PATH).
    
    Returns:
        the updated quantum program after the decomposition.
    
    
    """
    ...

@overload
def decompose_multiple_control_qgate(qprog: QProg, machine: QuantumMachine, convert_single_gates: List[str], convert_double_gates: List[str], b_transform_to_base_qgate: bool = True) -> QProg:
    """
    Decompose multiple control QGate.
    
    Args:
        qprog: Quantum program.
    
        machine: Quantum machine.
    
        convert_single_gates: Sets of quantum single gates.
    
        convert_double_gates: Sets of quantum double gates.
    
        b_transform_to_base_qgate: Transform to base QGate sets.
    
    Returns:
        A new program after decomposition.
    
    """
    ...

@overload
def deep_copy(node: QProg) -> QProg:
    """
    Create a deep copy of the given quantum program node.
    
    Args:
        node: The quantum program node to copy.
    
    Returns:
        A deep copy of the quantum program node.
    
    
    """
    ...

@overload
def deep_copy(node: QCircuit) -> QCircuit:
    """
    Create a deep copy of the given quantum program node.
    
    Args:
        node: The quantum program node to copy.
    
    Returns:
        A deep copy of the quantum program node.
    
    
    """
    ...

@overload
def deep_copy(node: QGate) -> QGate:
    """
    Create a deep copy of the given quantum program node.
    
    Args:
        node: The quantum program node to copy.
    
    Returns:
        A deep copy of the quantum program node.
    
    
    """
    ...

@overload
def deep_copy(node: QMeasure) -> QMeasure:
    """
    Create a deep copy of the given quantum program node.
    
    Args:
        node: The quantum program node to copy.
    
    Returns:
        A deep copy of the quantum program node.
    
    
    """
    ...

@overload
def deep_copy(node: ClassicalProg) -> ClassicalProg:
    """
    Create a deep copy of the given quantum program node.
    
    Args:
        node: The quantum program node to copy.
    
    Returns:
        A deep copy of the quantum program node.
    
    
    """
    ...

@overload
def deep_copy(node: QIfProg) -> QIfProg:
    """
    Create a deep copy of the given quantum program node.
    
    Args:
        node: The quantum program node to copy.
    
    Returns:
        A deep copy of the quantum program node.
    
    
    """
    ...

@overload
def deep_copy(node: QWhileProg) -> QWhileProg:
    """
    Create a deep copy of the given quantum program node.
    
    Args:
        node: The quantum program node to copy.
    
    Returns:
        A deep copy of the quantum program node.
    
    """
    ...

def del_weak_edge(topo_data: List[List[int]]) -> None:
    """
    Delete weakly connected edges from the quantum program topology.
    
    Args:
        topo_data: The topology data of the quantum program.
    
    Returns:
        None.
    
    """
    ...

def del_weak_edge2(topo_data: List[List[int]], max_connect_degree: int, sub_graph_set: List[int]) -> list:
    """
    Delete weakly connected edges from the quantum program topology.
    
    Args:
        topo_data: The topology data of the quantum program.
    
        max_connect_degree: The maximum allowable connection degree.
    
        sub_graph_set: A list of subgraph identifiers.
    
    Returns:
        A list containing the updated topology data, intermediary points, and candidate edges.
    
    """
    ...

def del_weak_edge3(topo_data: List[List[int]], sub_graph_set: List[int], max_connect_degree: int, lamda1: float, lamda2: float, lamda3: float) -> list:
    """
    Delete weakly connected edges based on specified parameters.
    
    Args:
        topo_data: The topology data of the quantum program.
    
        sub_graph_set: A list of subgraph identifiers.
    
        max_connect_degree: The maximum allowable connection degree.
    
        lamda1: Weight parameter for edge evaluation.
    
        lamda2: Weight parameter for edge evaluation.
    
        lamda3: Weight parameter for edge evaluation.
    
    Returns:
        A list containing the updated topology data and intermediary points.
    
    """
    ...

def destroy_quantum_machine(machine: QuantumMachine) -> None:
    """
    Destroy a quantum machine.
    
    Args:
        machine: type should be one of CPUQVM, CPUSingleThreadQVM, GPUQVM, NoiseQVM.
    
    Returns:
        None.
    
    """
    ...

def directly_run(qprog: QProg, noise_model: Noise = NoiseModel()) -> Dict[str,bool]:
    """
    Directly run a quantum program
    After init()
    
    Args:
        qprog: The quantum program to be executed.
    
        noise_model: The noise model to be used, default is no noise. The noise model only works on CPUQVM currently.
    
    Returns:
        Dict[str, bool]: Result of the quantum program execution in one shot.
                        The first element is the final qubit register state,
                        and the second is its measurement probability.
    
    """
    ...

@overload
def div(arg0: ClassicalCondition, arg1: ClassicalCondition) -> ClassicalCondition:
    """
    Divide one ClassicalCondition by another.
    
    Args:
        a: The numerator ClassicalCondition.
    
        b: The denominator ClassicalCondition.
    
    Returns:
        ClassicalCondition: The result of the division.
    
    
    """
    ...

@overload
def div(arg0: ClassicalCondition, arg1: int) -> ClassicalCondition:
    """
    Divide a ClassicalCondition by a bit size.
    
    Args:
        a: The ClassicalCondition (numerator).
    
        b: The bit size (denominator).
    
    Returns:
        ClassicalCondition: The result of the division.
    
    
    """
    ...

@overload
def div(arg0: int, arg1: ClassicalCondition) -> ClassicalCondition:
    """
    Divide a bit size by a ClassicalCondition.
    
    Args:
        a: The bit size (numerator).
    
        b: The ClassicalCondition (denominator).
    
    Returns:
        ClassicalCondition: The result of the division.
    
    """
    ...

def dot(arg0: var, arg1: var) -> var:
    """
    """
    ...

def draw_qprog_latex(prog: QProg, auto_wrap_len: int = 100, output_file: str = 'QCircuit.tex', with_logo: bool = False, itr_start: NodeIter = NodeIter(), itr_end: NodeIter = NodeIter()) -> str:
    """
    Convert a quantum prog/circuit to LaTeX representation,
    
    and save the output in a file named QCircuit.tex in the current path.
    
    Args:
        QProg: Quantum prog.
    
        auto_wrap_len: Default is 100.
    
        output_file: Result output file name.
    
        with_logo: Include logo in the output.
    
        itr_start: Node iterator start.
    
        itr_end: Node iterator end.
    
    Returns:
        A tuple containing program info.
    
    """
    ...

def draw_qprog_latex_with_clock(prog: QProg, config_data: str = 'QPandaConfig.json', auto_wrap_len: bool = 100, output_file: int = 'QCircuit.tex', with_logo: str = False, itr_start: NodeIter = NodeIter(), itr_end: NodeIter = NodeIter()) -> str:
    """
    Convert a quantum prog/circuit to LaTeX source code with time sequence,
    and save the source code to a file in the current path named QCircuit.tex.
    
    Args:
        prog: Quantum prog.
    
        config_data: Default config file is QPandaConfig.json.
    
        auto_wrap_len: Default is 100.
    
        output_file: Result output file name.
    
        with_logo: Whether to include a logo in the output.
    
        itr_start: Node iterator start.
    
        itr_end: Node iterator end.
    
    Returns:
        A tuple containing program info.
    
    """
    ...

def draw_qprog_text(qprog: QProg, auto_wrap_len: int = 100, output_file: str = 'QCircuitTextPic.txt', itr_start: NodeIter = NodeIter(), itr_end: NodeIter = NodeIter()) -> str:
    """
    Convert a quantum prog/circuit to text-pic (UTF-8 code),
    
    and save the text-pic in a file named QCircuitTextPic.txt in the current path.
    
    Args:
        QProg: Quantum prog.
    
        auto_wrap_len: Default is 100.
    
        output_file: Result output file name.
    
        itr_start: Node iterator start.
    
        itr_end: Node iterator end.
    
    Returns:
        A tuple containing program info.
    
    """
    ...

def draw_qprog_text_with_clock(prog: QProg, config_data: str = 'QPandaConfig.json', auto_wrap_len: int = 100, output_file: str = 'QCircuitTextPic.txt', itr_start: NodeIter = NodeIter(), itr_end: NodeIter = NodeIter()) -> str:
    """
    Convert a quantum prog/circuit to text-pic (UTF-8 code) with time sequence,
    
    and save the text-pic in a file named QCircuitTextPic.txt in the current path.
    
    Args:
        prog: Quantum prog.
    
        config_data: Configuration data.
    
        auto_wrap_len: Default is 100.
    
        output_file: Result output file name.
    
        itr_start: Node iterator start.
    
        itr_end: Node iterator end.
    
    Returns:
        A tuple containing program info.
    
    """
    ...

def dropout(arg0: var, arg1: var) -> var:
    """
    """
    ...

@overload
def equal(arg0: ClassicalCondition, arg1: ClassicalCondition) -> ClassicalCondition:
    """
    Check if two ClassicalConditions are equal.
    
    Args:
        a: The first ClassicalCondition.
    
        b: The second ClassicalCondition.
    
    Returns:
        bool: True if both ClassicalConditions are equal, otherwise False.
    
    
    """
    ...

@overload
def equal(arg0: ClassicalCondition, arg1: int) -> ClassicalCondition:
    """
    Check if a ClassicalCondition is equal to a bit size.
    
    Args:
        a: The ClassicalCondition to compare.
    
        b: The bit size to compare against.
    
    Returns:
        bool: True if the ClassicalCondition is equal to the bit size, otherwise False.
    
    
    """
    ...

@overload
def equal(arg0: int, arg1: ClassicalCondition) -> ClassicalCondition:
    """
    Check if a bit size is equal to a ClassicalCondition.
    
    Args:
        a: The bit size to compare.
    
        b: The ClassicalCondition to compare against.
    
    Returns:
        bool: True if the bit size is equal to the ClassicalCondition, otherwise False.
    
    """
    ...

def estimate_topology(topo_data: List[List[int]]) -> float:
    """
    Evaluate topology performance.
    
    Args:
        topo_data: Quantum program topology data.
    
    Returns:
        Result data.
    
    """
    ...

@overload
def eval(arg0: var, arg1: bool) -> numpy.ndarray[numpy.float64[m,n]]:
    """
    """
    ...

@overload
def eval(arg0: var) -> numpy.ndarray[numpy.float64[m,n]]:
    """
    """
    ...

def exp(arg0: var) -> var:
    """
    """
    ...

def expMat(arg0: complex, arg1: numpy.ndarray[numpy.complex128[m,n]], arg2: float) -> numpy.ndarray[numpy.complex128[m,n]]:
    """
    Calculate the matrix power of e.
    
    This function returns the power of matrix e.
    
    Args:
         None
    
    Returns:
         The computed matrix.
    
    """
    ...

@overload
def expand_linear_equations(matrix: List[complex], list: List[float]) -> list:
    """
    Extending linear equations to N dimension, N = 2 ^ n
    
    Args:
        matrix: the source matrix, which will be extend to N*N, N = 2 ^ n
    
        list: the source vector b, which will be extend to 2 ^ n
    
    """
    ...

@overload
def expand_linear_equations(matrix: List[complex], list: List[float]) -> list:
    """
    Extending linear equations to N dimension, N = 2 ^ n
    
    Args:
        matrix: the source matrix, which will be extend to N*N, N = 2 ^ n
    
        list: the source vector b, which will be extend to 2 ^ n
    """
    ...

def fill_qprog_by_I(qprog: QProg) -> QProg:
    """
    Fill the input quantum program with I gates and return a new quantum program.
    
    Args:
        qprog: the input quantum program.
    
    Returns:
        a new quantum program filled with I gates.
    
    """
    ...

def finalize() -> None:
    """
    Finalize the environment and destroy global unique quantum machine.
    
    Args:
        none
    
    Returns:
        none
    
    """
    ...

def fit_to_gbk(utf8_str: str) -> str:
    """
    Special character conversion.
    
    Args:
        utf8_str: string using utf-8 encoding.
    
    Returns:
        result: converted string.
    
    """
    ...

@overload
def flatten(qprog: QProg) -> None:
    """
    Flatten a quantum program in place.
    
    Args:
        qprog: The quantum program to be flattened.
    
    Returns:
        None: The function modifies the quantum program directly.
    
    
    """
    ...

@overload
def flatten(qcircuit: QCircuit) -> None:
    """
    Flatten a quantum circuit in place.
    
    Args:
        qcircuit: The quantum circuit to be flattened.
    
    Returns:
        None: The function modifies the circuit directly.
    
    """
    ...

def getAllocateCMem() -> int:
    """
    Deprecated, use get_allocate_cmem_num instead.
    
    Args:
        none
    
    Returns:
        allocate qubit num.
    
    """
    ...

def getAllocateQubitNum() -> int:
    """
    Deprecated, use get_allocate_qubit_num instead.
    
    Args:
        none
    
    Returns:
        allocate cbit num.
    
    """
    ...

def get_adjacent_qgate_type(qprog: QProg, node_iter: NodeIter) -> List[NodeInfo]:
    """
    Get the adjacent quantum gates' (the front one and the back one) type info from QProg.
    
    Args:
        qprog: Target quantum program.
    
        node_iter: Gate node iterator in qprog.
    
    Returns:
        The front and back node info of node_iter in qprog.
    
    """
    ...

def get_all_used_qubits(qprog: QProg) -> List[Qubit]:
    """
    Get all the quantum bits used in the input program.
    
    Args:
        qprog: A quantum program.
    
    Returns:
        result: A list of all used qubits.
    
    """
    ...

def get_all_used_qubits_to_int(qprog: QProg) -> List[int]:
    """
    Get the addresses of all used quantum bits in the input program.
    
    Args:
        qprog: A quantum program.
    
    Returns:
        result: A list of addresses of all used qubits.
    
    """
    ...

def get_allocate_cbits() -> List[ClassicalCondition]:
    """
    Get allocated cbits of QuantumMachine
    
    Args:
        None
    
    Returns:
        A list of allocated cbits.
    
    """
    ...

def get_allocate_cmem_num() -> int:
    """
    Get allocate cmem num.
    
    Args:
        none.
    
    Returns:
        cbit_num: allocate cbit num.
    
    """
    ...

def get_allocate_qubit_num() -> int:
    """
    Get allocate qubit num.
    
    Args:
        none.
    
    Returns:
        qubit_num: allocate qubit num.
    
    """
    ...

def get_allocate_qubits() -> List[Qubit]:
    """
    Get allocated qubits of QuantumMachine
    
    Args:
        None
    
    Returns:
        A list of allocated qubits.
    
    """
    ...

def get_bin_data(qprog: QProg) -> List[int]:
    """
    Get quantum program binary data.
    
    Args:
        qprog: quantum program (QProg).
    
    Returns:
        binary data as a list.
    
    """
    ...

def get_bin_str(qprog: QProg, machine: QuantumMachine) -> str:
    """
    Transform a quantum program into a string representation.
    
    Args:
        qprog: quantum program.
    
        machine: quantum machine.
    
    Returns:
        string: base64-encoded string of the binary representation.
    
    """
    ...

def get_circuit_optimal_topology(qprog: QProg, machine: QuantumMachine, max_connect_degree: int, config_file: str = 'QPandaConfig.json') -> List[List[int]]:
    """
    Retrieve the optimal topology of the input quantum circuit.
    
    Args:
        qprog: The quantum program for which to determine the topology.
    
        machine: The quantum machine used for execution.
    
        max_connect_degree: The maximum allowable connection degree.
    
        config_file: Path to the configuration file (default is CONFIG_PATH).
    
    Returns:
        The topology program data.
    
    """
    ...

def get_clock_cycle(qpog: QProg) -> int:
    """
    Get quantum program clock cycle.
    
    Args:
        qprog: quantum program (QProg).
    
    Returns:
        clock_cycle.
    
    """
    ...

def get_complex_points(topo_data: List[List[int]], max_connect_degree: int) -> List[int]:
    """
    Retrieve complex points from the given topology data.
    
    Args:
        topo_data: The topology data of the quantum program.
    
        max_connect_degree: The maximum allowable connection degree.
    
    Returns:
        A list of complex points extracted from the topology data.
    
    """
    ...

def get_double_gate_block_topology(qprog: QProg) -> List[List[int]]:
    """
    Retrieve the double gate block topology from the input quantum program.
    
    Args:
        qprog: The quantum program for which to extract the double gate block topology.
    
    Returns:
        The topology program data.
    
    """
    ...

def get_matrix(*args, **kwargs) -> Any:
    """
    Get the target matrix between the input two NodeIters.
    
    Args:
        qprog: Quantum program.
    
        positive_seq: Qubit order of output matrix; true for positive sequence (q0q1q2),
      false for inverted order (q2q1q0), default is false.
    
        nodeitr_start: The start NodeIter.
    
        nodeitr_end: The end NodeIter.
    
    Returns:
        The target matrix including all the QGate's matrices (multiplied).
    
    """
    ...

def get_prob_dict(qubit_list: QVec, select_max: int = -1) -> Dict[str,float]:
    """
    Get pmeasure result as dict
    
    Args:
        qubit_list: pmeasure qubits list.
    
        select_max: max returned element num in returned tuple, should be in [-1, 1<<len(qubit_list)],
    
        default is -1, meaning no limit.
    
    Returns:
        Measure result of quantum machine.
    
    """
    ...

def get_prob_list(qubit_list: QVec, select_max: int = -1) -> List[float]:
    """
    Get pmeasure result as list
    
    Args:
        qubit_list: pmeasure qubits list.
    
        select_max: max returned element num in returned tuple, should be in [-1, 1<<len(qubit_list)],
    
        default is -1, meaning no limit.
    
    Returns:
        Measure result of quantum machine.
    
    """
    ...

@overload
def get_qgate_num(quantum_prog: QProg) -> int:
    """
    Count quantum gate number in the quantum program.
    
    Args:
        quantum_prog: quantum program.
    
    Returns:
        result: gate count.
    
    
    """
    ...

@overload
def get_qgate_num(quantum_circuit: QCircuit) -> int:
    """
    Count quantum gate number in the quantum circuit.
    
    Args:
        quantum_circuit: quantum circuit.
    
    Returns:
        result: gate count.
    
    
    """
    ...

@overload
def get_qgate_num(qprog: QProg) -> int:
    """
    Count the number of quantum gates in a quantum program.
    
    Args:
        qprog: The quantum program to analyze.
    
    Returns:
        int: The number of quantum gates in the quantum program.
    
    """
    ...

def get_qprog_clock_cycle(qprog: QProg, machine: QuantumMachine, optimize: bool = False) -> int:
    """
    Get Quantum Program Clock Cycle.
    
    Args:
        qprog: quantum program (QProg).
    
        machine: quantum machine (QuantumMachine*).
    
        optimize: whether to optimize qprog (default is false).
    
    Returns:
        QProg time consumed, no unit, not in seconds.
    
    """
    ...

@overload
def get_qstate() -> List[complex]:
    """
    """
    ...

@overload
def get_qstate() -> Any:
    """
    """
    ...

def get_sub_graph(topo_data: List[List[int]]) -> List[int]:
    """
    Retrieve a subgraph from the provided topology data.
    
    Args:
        topo_data: The topology data of the quantum program.
    
    Returns:
        sub graph: The extracted subgraph from the provided topology.
    
    """
    ...

def get_tuple_list(qubit_list: QVec, select_max: int = -1) -> List[Tuple[int,float]]:
    """
    Get pmeasure result as tuple list
    
    Args:
        qubit_list: pmeasure qubits list.
    
        select_max: max returned element num in returned tuple, should be in [-1, 1<<len(qubit_list)],
    
        default is -1, meaning no limit.
    
    Returns:
        Measure result of quantum machine.
    
    """
    ...

def get_unitary(*args, **kwargs) -> Any:
    """
    Get the target unitary matrix between the input two NodeIters.
    
    Args:
        qprog: Quantum program.
    
        positive_seq: Qubit order of output matrix; true for positive sequence (q0q1q2),
      false for inverted order (q2q1q0), default is false.
    
        nodeitr_start: The start NodeIter.
    
        nodeitr_end: The end NodeIter.
    
    Returns:
        The target unitary matrix including all the QGate's matrices (multiplied).
    
    """
    ...

def get_unsupport_qgate_num(qprog: QProg, support_gates: List[List[str]]) -> int:
    """
    Count the number of unsupported gates in a quantum program.
    
    Args:
        qprog: The quantum program to analyze.
    
        support_gates: A list of supported gates.
    
    Returns:
        int: The number of unsupported gates in the quantum program.
    
    """
    ...

def getstat(*args, **kwargs) -> Any:
    """
    Get the status of the Quantum machine
    
    Args:
        None
    
    Returns:
        The status of the Quantum machine, see QMachineStatus.
    
    """
    ...

@overload
def iSWAP(first_qubit: Qubit, second_qubit: Qubit) -> QGate:
    """
    Returns:
        a iSWAP gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def iSWAP(first_qubit_list: QVec, second_qubit_list: QVec) -> QCircuit:
    """
    Returns:
        a iSWAP gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def iSWAP(first_qubit_addr: int, second_qubit_addr: int) -> QGate:
    """
    """
    ...

@overload
def iSWAP(first_qubit_addr_list: List[int], second_qubit_addr_list: List[int]) -> QCircuit:
    """
    Returns:
        a iSWAP gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def iSWAP(first_qubit: Qubit, second_qubit: Qubit, theta_angle: float) -> QGate:
    """
    Returns:
        a iSWAP gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def iSWAP(first_qubit_list: QVec, second_qubit_list: QVec, theta_angle: float) -> QCircuit:
    """
    Returns:
        a iSWAP gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def iSWAP(first_qubit_addr: int, second_qubit_addr: int, theta_angle: float) -> QGate:
    """
    Returns:
        a iSWAP gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    
    """
    ...

@overload
def iSWAP(first_qubit_addr_list: List[int], second_qubit_addr_list: List[int], theta_angle: float) -> QCircuit:
    """
    Returns:
        a iSWAP gate node
    Raises:
        run_fail: An error occurred in construct gate node
    
    """
    ...

def init(machine_type: QMachineType = QMachineType.CPU) -> bool:
    """
    Init the global unique quantum machine at background.
    
    Args:
        machine_type: quantum machine type, see pyQPanda.QMachineType
    
    Returns:
        bool: true if initialization success
    
    """
    ...

def init_quantum_machine(machine_type: QMachineType = QMachineType.CPU) -> QuantumMachine:
    """
    Create and initialize a new quantum machine, and let it be a globally unique quantum machine.
    
    Args:
        machine_type: quantum machine type, see pyQPanda.QMachineType.
    
    Returns:
        object: the quantum machine, type depends on machine_type:
    
            QMachineType.CPU               --> pyQPanda.CPUQVM
    
            QMachineType.CPU_SINGLE_THREAD --> pyQPanda.CPUSingleThreadQVM
    
            QMachineType.GPU               --> pyQPanda.GPUQVM (if pyQPanda is built with GPU)
    
            QMachineType.NOISE             --> pyQPanda.NoiseQVM
    
            return None if initialization fails.
    
    """
    ...

def inverse(arg0: var) -> var:
    """
    """
    ...

def isCarry(arg0: QVec, arg1: QVec, arg2: Qubit, arg3: Qubit) -> QCircuit:
    """
    Construct a circuit to determine if there is a carry
    """
    ...

def is_match_topology(gate: QGate, topo: List[List[float]]) -> bool:
    """
    Judge if the QGate matches the target topologic structure of the quantum circuit.
    
    Args:
        gate (QGate): The quantum gate to evaluate.
    
        topo: The target topologic structure of the quantum circuit.
    
    Returns:
        bool: True if it matches, otherwise false.
    
    """
    ...

def is_supported_qgate_type(nodeitr: NodeIter) -> bool:
    """
    Judge if the target node is a QGate type.
    
    Args:
        nodeitr: Node iterator in the quantum program.
    
    Returns:
        bool: True if the target node is a QGate type, otherwise false.
    
    """
    ...

def is_swappable(prog: QProg, nodeitr_1: NodeIter, nodeitr_2: NodeIter) -> bool:
    """
    Judge whether the specified two NodeIters in the quantum program can be exchanged.
    
    Args:
        prog: Target quantum program.
    
        nodeitr_1: Node iterator 1 in the quantum program.
    
        nodeitr_2: Node iterator 2 in the quantum program.
    
    Returns:
        bool: True if the two NodeIters can be exchanged, otherwise false.
    
    """
    ...

def iterative_amplitude_estimation(arg0: QCircuit, arg1: QVec, arg2: float, arg3: float) -> float:
    """
    estimate the probability corresponding to the ground state |1> of the last bit
    Args:
        QCircuit: quantum circuit
        qvec: qubit list
        double: epsilon
        double: confidence
    
    Returns:
        result iterative amplitude
    Raises:
        run_fail: An error occurred in iterative_amplitude_estimation
    
    """
    ...

def ldd_decompose(qprog: QProg) -> QProg:
    """
    Decompose a multiple control quantum gate using LDD.
    
    Args:
        qprog: the quantum program to be decomposed.
    
    Returns:
        the updated quantum program after decomposition.
    
    """
    ...

def log(arg0: var) -> var:
    """
    """
    ...

@overload
def matrix_decompose(qubits: QVec, matrix: numpy.ndarray[numpy.complex128[m,n]], mode: DecompositionMode = DecompositionMode.QSD, b_positive_seq: bool = True) -> QCircuit:
    """
    Matrix decomposition
    
    Args:
        qubits: the used qubits
    
        matrix: The target matrix
    
        mode: DecompositionMode decomposition mode, default is QSD
    
        b_positive_seq: true for positive sequence(q0q1q2), false for inverted order(q2q1q0), default is true
    
    Returns:
        QCircuit The quantum circuit for target matrix
    
    """
    ...

@overload
def matrix_decompose(qubits: QVec, matrix: List[complex], mode: DecompositionMode = DecompositionMode.QSD, b_positive_seq: bool = True) -> QCircuit:
    """
    Matrix decomposition
    
    Args:
        qubits: the used qubits
    
        matrix: The target matrix
    
        mode: DecompositionMode decomposition mode, default is QSD
    
        b_positive_seq: true for positive sequence(q0q1q2), false for inverted order(q2q1q0), default is true
    
    Returns:
        QCircuit The quantum circuit for target matrix
    """
    ...

@overload
def matrix_decompose_paulis(arg0: QuantumMachine, arg1: numpy.ndarray[numpy.float64[m,n]]) -> List[Tuple[float,QCircuit]]:
    """
    decompose matrix into paulis combination
    
    Args:
        quantum_machine: quantum machine
    
        matrix: 2^N *2^N double matrix 
    
    Returns:
        result : linearcom contains pauli circuit
    
    """
    ...

@overload
def matrix_decompose_paulis(arg0: QVec, arg1: numpy.ndarray[numpy.float64[m,n]]) -> List[Tuple[float,QCircuit]]:
    """
    decompose matrix into paulis combination
    
    Args:
        quantum_machine: quantum machine
        matrix: 2^N *2^N double matrix 
    
    Returns:
        result : linearcom contains pauli circuit
    """
    ...

@overload
def measure_all(qubit_list: QVec, cbit_list: List[ClassicalCondition]) -> QProg:
    """
    Create a list of measure nodes.
    
    Args:
        qubit_list: the qubits to be measured.
    
        cbit_list: classical bits that store the quantum measurement results.
    
    Returns:
        a list of measure nodes.
    
    
    """
    ...

@overload
def measure_all(qubit_addr_list: List[int], cbit_addr_list: List[int]) -> QProg:
    """
    Create a list of measure nodes.
    
    Args:
        qubit_addr_list: list of addresses of the qubits to be measured.
    
        cbit_addr_list: list of addresses of the classical bits that store the quantum measurement results.
    
    Returns:
        a list of measure nodes.
    
    """
    ...

@overload
def mul(arg0: ClassicalCondition, arg1: ClassicalCondition) -> ClassicalCondition:
    """
    Multiply two ClassicalConditions.
    
    Args:
        a: The first ClassicalCondition.
    
        b: The second ClassicalCondition to multiply with.
    
    Returns:
        ClassicalCondition: The result of the multiplication.
    
    
    """
    ...

@overload
def mul(arg0: ClassicalCondition, arg1: int) -> ClassicalCondition:
    """
    Multiply a ClassicalCondition by a bit size.
    
    Args:
        a: The ClassicalCondition to be multiplied.
    
        b: The bit size to multiply with the ClassicalCondition.
    
    Returns:
        ClassicalCondition: The resulting ClassicalCondition after multiplication.
    
    
    """
    ...

@overload
def mul(arg0: int, arg1: ClassicalCondition) -> ClassicalCondition:
    """
    Multiply a bit size by a ClassicalCondition.
    
    Args:
        a: The bit size to be multiplied.
    
        b: The ClassicalCondition to multiply with the bit size.
    
    Returns:
        ClassicalCondition: The resulting ClassicalCondition after multiplication.
    
    """
    ...

def originir_to_qprog(file_path: str, machine: QuantumMachine) -> QProg:
    """
    Read an OriginIR file and transform it into QProg.
    
    Args:
        file_path: OriginIR file path.
    
        machine: initialized quantum machine.
    
    Returns:
        Transformed QProg.
    
    """
    ...

def pauli_combination_replace(arg0: List[Tuple[float,QCircuit]], arg1: QuantumMachine, arg2: str, arg3: str) -> List[Tuple[float,QCircuit]]:
    """
    """
    ...

def planarity_testing(topo_data: List[List[int]]) -> bool:
    """
    Perform planarity testing.
    
    Args:
        topo_data: Quantum program topology data.
    
    Returns:
        Result data.
    
    """
    ...

def pmeasure(qubit_list: QVec, select_max: int) -> List[Tuple[int,float]]:
    """
    Get the probability distribution over qubits.
    
    Args:
        qubit_list: qubit list to measure.
    
        select_max: max returned element num in returned tuple, should be in [-1, 1<<len(qubit_list)];
    
        default is -1, means no limit.
    
    Returns:
        Measure result of quantum machine in tuple form.
    
    """
    ...

def pmeasure_no_index(qubit_list: QVec) -> List[float]:
    """
    Get the probability distribution over qubits.
    
    Args:
        qubit_list: qubit list to measure.
    
    Returns:
        Measure result of quantum machine in list form.
    
    """
    ...

def poly(arg0: var, arg1: var) -> var:
    """
    """
    ...

def print_matrix(matrix: List[complex], precision: int = 8) -> str:
    """
    Print matrix elements.
    
    Args:
        matrix (QStat): The matrix to print.
    
        precision (int, optional): Double value to string cutoff precision (default is 8).
    
    Returns:
        A string representation of the matrix.
    
    """
    ...

def prob_run_dict(qprog: QProg, qubit_list: QVec, select_max: int = -1) -> Dict[str,float]:
    """
    Run quantum program and get pmeasure result as dict
    
    Args:
        qprog: quantum program.
    
        qubit_list: pmeasure qubits list.
    
        select_max: max returned element num in returned tuple, should be in [-1, 1<<len(qubit_list)],
    
        default is -1, meaning no limit.
    
    Returns:
        Measure result of quantum machine.
    
    """
    ...

def prob_run_list(qprog: QProg, qubit_list: QVec, select_max: int = -1) -> List[float]:
    """
    Run quantum program and get pmeasure result as list
    
    Args:
        qprog: quantum program.
    
        qubit_list: pmeasure qubits list.
    
        select_max: max returned element num in returned tuple, should be in [-1, 1<<len(qubit_list)],
    
        default is -1, meaning no limit.
    
    Returns:
        Measure result of quantum machine.
    
    """
    ...

def prob_run_tuple_list(qptog: QProg, qubit_list: QVec, select_max: int = -1) -> List[Tuple[int,float]]:
    """
    Run quantum program and get pmeasure result as tuple list
    
    Args:
        qprog: quantum program.
    
        qubit_list: pmeasure qubits list.
    
        select_max: max returned element num in returned tuple, should be in [-1, 1<<len(qubit_list)],
    
        default is -1, meaning no limit.
    
    Returns:
        Measure result of quantum machine.
    
    """
    ...

def prog_layer(*args, **kwargs) -> Any:
    """
    Process the given quantum program layer.
    
    Args:
        prog: The quantum program to be processed.
    
    Returns:
        Processed quantum program layer.
    
    """
    ...

def prog_to_dag(prog: QProg) -> QProgDAG:
    """
    Convert a quantum program into a directed acyclic graph (DAG).
    
    Args:
         prog: The quantum program to be converted.
    
    Returns:
         QProgDAG: A reference to the resulting DAG.
    
    """
    ...

@overload
def qAlloc() -> Qubit:
    """
    Create a qubit
    After init()
    
    Args:
        None: No parameters are required for this function.
    
    Returns:
        Qubit: A new qubit.
    
        None: If the quantum machine has created the maximum number of qubits, which is 29.
    
    
    """
    ...

@overload
def qAlloc(qubit_addr: int) -> Qubit:
    """
    Allocate a qubit
    After init()
    
    Args:
        qubit_addr: The physical address of the qubit, should be in [0, 29).
    
    Returns:
        Qubit: A new qubit.
    
        None: If qubit_addr is invalid or if the maximum number of allowed qubits has been reached.
    
    """
    ...

def qAlloc_many(qubit_num: int) -> List[Qubit]:
    """
    Allocate several qubits
    After init()
    
    Args:
        qubit_num: The number of qubits to be created.
    
    Returns:
        list[pyQPanda.Qubit]: list of qubit.
    
    """
    ...

def qFree(qubit: Qubit) -> None:
    """
    Free a qubit
    
    Args:
        qubit: a qubit
    
    Returns:
        None
    
    """
    ...

@overload
def qFree_all() -> None:
    """
    Free all qubits
    
    Args:
        None
    
    Returns:
        None
    
    
    """
    ...

@overload
def qFree_all(qubit_list: QVec) -> None:
    """
    Free a list of qubits
    
    Args:
        qubit_list: A list of qubits to be freed.
    
    Returns:
        None
    
    """
    ...

@overload
def qop(VariationalQuantumCircuit: VariationalQuantumCircuit, Hamiltonian, QuantumMachine: QuantumMachine, qubitList: List[Qubit]) -> var:
    """
    """
    ...

@overload
def qop(VariationalQuantumCircuit: VariationalQuantumCircuit, Hamiltonian, QuantumMachine: QuantumMachine, qubitList: Dict[int,Qubit]) -> var:
    """
    """
    ...

def qop_pmeasure(arg0: VariationalQuantumCircuit, arg1: List[int], arg2: QuantumMachine, arg3: List[Qubit]) -> var:
    """
    """
    ...

def quantum_chip_adapter(qprog: QProg, machine: QuantumMachine, mapping: bool = True, config_file: str = 'QPandaConfig.json') -> list:
    """
    Perform adaptive conversion for the quantum chip.
    
    Args:
        qprog: the quantum program.
    
        machine: the quantum machine to be used.
    
        mapping: whether to perform the mapping operation (default is true).
    
        config_file: configuration file path (default is CONFIG_PATH).
    
    Returns:
        a list containing the quantum program and the list of qubits after mapping; if mapping is false, the qubit list may be misoperated.
    
    """
    ...

def quantum_walk_alg(*args, **kwargs) -> Any:
    """
    Build quantum-walk algorithm quantum circuit
    """
    ...

def quantum_walk_search(list: List[int], Classical_condition: ClassicalCondition, QuantumMachine: QuantumMachine, data: int = 2) -> list:
    """
    Use Quantum-walk Algorithm to search target data, return QProg and search_result
    
    Args:
        list: data list
        Classical_condition: quantum Classical condition
        QuantumMachine: quantum machine
        repeat: search repeat times
    
    Returns:
        result : Quantum-walk search result
    Raises:
        run_fail: An error occurred in Quantum-walk
    
    """
    ...

def quick_measure(qubit_list: QVec, shots: int) -> Dict[str,int]:
    """
    Quick measure.
    
    Args:
        qubit_list: qubit list to measure.
    
        shots: the repeat number of measure operations.
    
    Returns:
        result: result of quantum program execution.
    
    """
    ...

def random_qcircuit(qvec: QVec, depth: int = 100, gate_type: List[str] = []) -> QCircuit:
    """
    Generate a random quantum circuit.
    
    Args:
        qvec: Output circuits for the random circuit.
    
        depth: Circuit depth (default is 100).
    
        gate_type: Types of gates to use (default is an empty vector).
    
    Returns:
        A random quantum circuit.
    
    """
    ...

def random_qprog(qubit_row: int, qubit_col: int, depth: int, qvm: QuantumMachine, qvec: QVec) -> QProg:
    """
    Generate a random quantum program.
    
    Args:
        qubit_row: Circuit qubit row value.
    
        qubit_col: Circuit qubit column value.
    
        depth: Circuit depth.
    
        qvm: Quantum machine.
    
        qvec: Output circuits for the random quantum program.
    
    Returns:
        A random quantum program.
    
    """
    ...

def recover_edges(topo_data: List[List[int]], max_connect_degree: int, candidate_edges: List[Tuple[int,List[int]]]) -> List[List[int]]:
    """
    Recover edges using the specified candidate edges.
    
    Args:
        topo_data: The topology data of the quantum program.
    
        max_connect_degree: The maximum allowed connection degree.
    
        candidate_edges: A list of edges to consider for recovery.
    
    Returns:
        The updated topology data after recovery.
    
    """
    ...

def remap(prog: QProg, target_qlist: QVec, target_clist: List[ClassicalCondition] = []) -> QProg:
    """
    Map the source quantum program to the target qubits.
    
    Args:
        prog: Source quantum program.
    
        target_qlist: Target qubits.
    
        target_clist: Target classical bits (default is an empty vector).
    
    Returns:
        The target quantum program.
    
    """
    ...

def replace_complex_points(src_topo_data: List[List[int]], max_connect_degree: int, sub_topo_vec: List[Tuple[int,List[List[int]]]]) -> None:
    """
    Replace complex points in the source topology with subgraphs.
    
    Args:
        src_topo_data: The source topology data of the quantum program.
    
        max_connect_degree: The maximum allowable connection degree.
    
        sub_topo_vec: A list of sub-topologies to replace the complex points.
    
    Returns:
        None: This function modifies the source topology in place.
    
    """
    ...

def run_with_configuration(*args, **kwargs) -> Any:
    """
    
    1. run_with_configuration(program: pyQPanda.QProg, cbit_list: List[pyQPanda.ClassicalCondition], shots: int, noise_model: pyQPanda.Noise = NoiseModel()) -> Dict[str, int]
    
    Run quantum program with configuration
    
    Args:
        program: quantum program.
    
        cbit_list: classical cbits list.
    
        shots: number of times to repeat the quantum program.
    
        noise_model: noise model; defaults to no noise. Noise model only works on CPUQVM now.
    
    Returns:
        Result of quantum program execution in shots.
      First is the final qubit register state, second is its hit count.
    
    
    2. run_with_configuration(program: pyQPanda.QProg, shots: int, noise_model: pyQPanda.Noise = NoiseModel()) -> Dict[str, int]
    
    Run quantum program with configuration.
    
    Args:
        program: quantum program.
    
        shots: repeat run quantum program times.
    
        noise_model: noise model, default is no noise. Noise model only works on CPUQVM now.
    
    Returns:
        tuple: result of quantum program execution in shots.
    
        First is the final qubit register state, second is its hit shot.
    
    """
    ...

@overload
def sabre_mapping(prog: QProg, quantum_machine: QuantumMachine, init_map: List[int], max_look_ahead: int = 20, max_iterations: int = 10, config_data: str = 'QPandaConfig.json') -> QProg:
    """
    sabre mapping
    
    Args:
        prog: the target prog
    
        quantum_machine: quantum machine
    
        init_map: init map
    
        max_look_ahead: sabre_mapping max_look_ahead
    
        max_iterations: sabre_mapping max_iterations
    
        config_data: config data, @See JsonConfigParam::load_config()
    
    Returns:
        mapped quantum program
    
    """
    ...

@overload
def sabre_mapping(prog: QProg, quantum_machine: QuantumMachine, init_map: List[int], max_look_ahead: int, max_iterations: int, arch_matrix: numpy.ndarray[numpy.float64[m,n]]) -> QProg:
    """
    sabre mapping
    
    Args:
        prog: the target prog
    
        quantum_machine: quantum machine
    
        init_map: init map
    
        max_look_ahead: sabre_mapping max_look_ahead, default is 20 
    
        max_iterations: sabre_mapping max_iterations, default is 10 
    
        arch_matrix: arch matrix
    
    Returns:
        mapped quantum program
    
    """
    ...

@overload
def sabre_mapping(prog: QProg, quantum_machine: QuantumMachine, max_look_ahead: int = 20, max_iterations: int = 10, config_data: str = 'QPandaConfig.json') -> QProg:
    """
    sabre mapping
    
    Args:
        prog: the target prog
    
        quantum_machine: quantum machine
    
        max_look_ahead: sabre_mapping max_look_ahead
    
        max_iterations: sabre_mapping max_iterations
    
        config_data: config data, @See JsonConfigParam::load_config()
    
    Returns:
        mapped quantum program
    
    """
    ...

@overload
def sabre_mapping(prog: QProg, quantum_machine: QuantumMachine, max_look_ahead: int, max_iterations: int, arch_matrix: numpy.ndarray[numpy.float64[m,n]]) -> QProg:
    """
    sabre mapping
    
    Args:
        prog: the target prog
    
        quantum_machine: quantum machine
    
        max_look_ahead: sabre_mapping max_look_ahead, default is 20 
    
        max_iterations: sabre_mapping max_iterations, default is 10 
    
        arch_matrix: arch matrix
    
    Returns:
        mapped quantum program
    """
    ...

def sigmoid(arg0: var) -> var:
    """
    """
    ...

def sin(arg0: var) -> var:
    """
    """
    ...

def softmax(arg0: var) -> var:
    """
    """
    ...

def split_complex_points(complex_points: List[int], max_connect_degree: int, topo_data: List[List[int]], split_method: ComplexVertexSplitMethod = ComplexVertexSplitMethod.LINEAR) -> List[Tuple[int,List[List[int]]]]:
    """
    Split complex points into multiple discrete points.
    
    Args:
        complex_points: A list of complex points to be split.
    
        max_connect_degree: The maximum allowable connection degree.
    
        topo_data: The topology data of the quantum program.
    
        split_method: Method for splitting, as defined in ComplexVertexSplitMethod. Defaults to ComplexVertexSplitMethod.LINEAR.
    
    Returns:
        None: The function modifies the input data in place.
    
    """
    ...

def stack(arg0: int, *args) -> var:
    """
    """
    ...

@overload
def state_fidelity(state1: List[complex], state2: List[complex]) -> float:
    """
    Compare two quantum states and calculate their fidelity.
    
    Args:
        state1: first quantum state represented as a list.
    
        state2: second quantum state represented as a list.
    
    Returns:
        The fidelity between the two states, a value in the range [0, 1].
    
    
    """
    ...

@overload
def state_fidelity(matrix1: List[List[complex]], matrix2: List[List[complex]]) -> float:
    """
    Compare two quantum state matrices and calculate their fidelity.
    
       Args:
           matrix1: first quantum state matrix.
    
           matrix2: second quantum state matrix.
    
       Returns:
           The fidelity between the two matrices, a value in the range [0, 1].
    
    
    """
    ...

@overload
def state_fidelity(state1: List[complex], state2: List[List[complex]]) -> float:
    """
    Compare a quantum state with a state matrix and calculate their fidelity.
    
    Args:
        state: a single quantum state represented as a list.
    
        matrix: a quantum state matrix.
    
    Returns:
        The fidelity between the state and the matrix, a value in the range [0, 1].
    
    
    """
    ...

@overload
def state_fidelity(state1: List[List[complex]], state2: List[complex]) -> float:
    """
    Compare a quantum state matrix with a quantum state and calculate their fidelity.
    
    Args:
        matrix: a quantum state matrix.
    
        state: a single quantum state represented as a list.
    
    Returns:
        The fidelity between the matrix and the state, a value in the range [0, 1].
    
    """
    ...

@overload
def sub(arg0: ClassicalCondition, arg1: ClassicalCondition) -> ClassicalCondition:
    """
    Subtract one ClassicalCondition from another.
    
    Args:
        a: The ClassicalCondition to subtract from.
    
        b: The ClassicalCondition to subtract.
    
    Returns:
        ClassicalCondition: The result of the subtraction.
    
    
    """
    ...

@overload
def sub(arg0: ClassicalCondition, arg1: int) -> ClassicalCondition:
    """
    Subtract a bit size from a ClassicalCondition.
    
    Args:
        a: The ClassicalCondition from which the bit size will be subtracted.
    
        b: The bit size to subtract from the ClassicalCondition.
    
    Returns:
        ClassicalCondition: The resulting ClassicalCondition after subtraction.
    
    
    """
    ...

@overload
def sub(arg0: int, arg1: ClassicalCondition) -> ClassicalCondition:
    """
    Subtract a ClassicalCondition from a bit size.
    
    Args:
        a: The bit size to subtract from.
    
        b: The ClassicalCondition to be subtracted.
    
    Returns:
        ClassicalCondition: The resulting ClassicalCondition after subtraction.
    
    """
    ...

def sum(arg0: var) -> var:
    """
    """
    ...

def tan(arg0: var) -> var:
    """
    """
    ...

def to_Quil(qprog: QProg, machine: QuantumMachine) -> str:
    """
    Transform QProg to Quil instruction.
    
    Args:
        qprog: quantum program (QProg).
    
        machine: quantum machine (QuantumMachine*).
    
    Returns:
        Quil instruction string.
    
    """
    ...

@overload
def to_originir(qprog: QProg, machine: QuantumMachine) -> str:
    """
    Transform QProg to OriginIR string.
    
    Args:
         qprog: T, the quantum program or circuit to transform.
    
         machine: QuantumMachine*, the quantum machine being used.
    
    Returns:
         OriginIR string, the transformed representation of the quantum program.
    
    
    """
    ...

@overload
def to_originir(qprog: QCircuit, machine: QuantumMachine) -> str:
    """
    Transform QProg to OriginIR string.
    
    Args:
         qprog: T, the quantum program or circuit to transform.
    
         machine: QuantumMachine*, the quantum machine being used.
    
    Returns:
         OriginIR string, the transformed representation of the quantum program.
    
    
    """
    ...

@overload
def to_originir(qprog: QGate, machine: QuantumMachine) -> str:
    """
    Transform QProg to OriginIR string.
    
    Args:
         qprog: T, the quantum program or circuit to transform.
    
         machine: QuantumMachine*, the quantum machine being used.
    
    Returns:
         OriginIR string, the transformed representation of the quantum program.
    
    
    """
    ...

@overload
def to_originir(qprog: QIfProg, machine: QuantumMachine) -> str:
    """
    Transform QProg to OriginIR string.
    
    Args:
         qprog: T, the quantum program or circuit to transform.
    
         machine: QuantumMachine*, the quantum machine being used.
    
    Returns:
         OriginIR string, the transformed representation of the quantum program.
    
    
    """
    ...

@overload
def to_originir(qprog: QWhileProg, machine: QuantumMachine) -> str:
    """
    Transform QProg to OriginIR string.
    
    Args:
         qprog: T, the quantum program or circuit to transform.
    
         machine: QuantumMachine*, the quantum machine being used.
    
    Returns:
         OriginIR string, the transformed representation of the quantum program.
    
    
    """
    ...

@overload
def to_originir(qprog: QMeasure, machine: QuantumMachine) -> str:
    """
    Transform QProg to OriginIR string.
    
    Args:
         qprog: T, the quantum program or circuit to transform.
    
         machine: QuantumMachine*, the quantum machine being used.
    
    Returns:
         OriginIR string, the transformed representation of the quantum program.
    
    """
    ...

def topology_match(qprog: QProg, qubit_list: QVec, machine: QuantumMachine, confing_file: str = 'QPandaConfig.json') -> list:
    """
    Judge whether a quantum program matches the topology of the physical qubits.
    
    Args:
        qprog: The quantum program to be evaluated.
    
        qubit_list: The list of qubits in the quantum program.
    
        machine: The quantum machine used for execution.
    
        confing_file: The configuration file path for matching (default: QPandaConfig.json).
    
    Returns:
        list: Contains the resulting quantum program and the qubit list.
    
    """
    ...

def transform_binary_data_to_qprog(machine: QuantumMachine, data: List[int]) -> QProg:
    """
    Parse binary data to transform it into a quantum program.
    
    Args:
        machine: quantum machine.
    
        data: list containing binary data from transform_qprog_to_binary().
    
    Returns:
        QProg: the resulting quantum program.
    
    """
    ...

def transform_originir_to_qprog(fname: str, machine: QuantumMachine) -> QProg:
    """
    Transform OriginIR instruction from a file into a QProg.
    
    Args:
        fname: file containing the OriginIR instructions.
    
        machine: the quantum machine.
    
    Returns:
        QProg: the resulting quantum program.
    
    """
    ...

@overload
def transform_qprog_to_binary(qprog: QProg, machine: QuantumMachine) -> List[int]:
    """
    Transform quantum program to binary data.
    
    Args:
        qprog: quantum program (QProg).
    
        machine: quantum machine.
    
    Returns:
        binary data as a list.
    
    
    """
    ...

@overload
def transform_qprog_to_binary(qprog: QProg, machine: QuantumMachine, fname: str) -> None:
    """
    Save quantum program to file as binary data.
    
    Args:
        qprog: quantum program (QProg).
    
        machine: quantum machine.
    
        fname: name of the file to save to.
    
    """
    ...

def transform_qprog_to_originir(qprog: QProg, machine: QuantumMachine) -> str:
    """
    Transform a quantum program into an OriginIR instruction string.
    
    Args:
        qprog: the quantum program (QProg).
    
        machine: the quantum machine.
    
    Returns:
        string: the resulting OriginIR instruction string.
    
    """
    ...

def transform_qprog_to_quil(qprog: QProg, machine: QuantumMachine) -> str:
    """
    Transform QProg to Quil instruction.
    
    Args:
        qprog: quantum program (QProg).
    
        machine: quantum machine (QuantumMachine*).
    
    Returns:
        Quil instruction string.
    
    """
    ...

@overload
def transform_to_base_qgate(qprog: QProg, machine: QuantumMachine, config_file: str = 'QPandaConfig.json') -> QProg:
    """
    Convert quantum gates to basic quantum gates.
    
    Args:
        qprog: the quantum program to be transformed.
    
        machine: the quantum machine used for the transformation.
    
        config_file: path to the configuration file (default is CONFIG_PATH).
    
    Returns:
        the updated quantum program after transformation.
    
    
    """
    ...

@overload
def transform_to_base_qgate(qprog: QProg, machine: QuantumMachine, convert_single_gates: List[str], convert_double_gates: List[str]) -> QProg:
    """
    Convert quantum gates to basic gates.
    
    Args:
        qprog: the quantum program to transform.
    
        machine: the quantum machine for the transformation.
    
        convert_single_gates: a set of quantum single gates to convert.
    
        convert_double_gates: a set of quantum double gates to convert.
    
    Returns:
        the updated quantum program after the conversion.
    
    """
    ...

def transfrom_pauli_operator_to_matrix(arg0) -> List[complex]:
    """
    transfrom pauli operator to matrix
    
    Args:
        matrix: 2^N *2^N double matrix 
    
    Returns:
        result : hamiltonian
    """
    ...

def transpose(arg0: var) -> var:
    """
    """
    ...

def validate_double_qgate_type(gate_str_list: List[str]) -> list:
    """
    Get valid QGates and valid double bit QGate type.
    
    Args:
        double_gates: A list of double gate strings.
    
    Returns:
        result: A list containing the validated gate type and valid double gates.
    
    """
    ...

def validate_single_qgate_type(gate_str_list: List[str]) -> list:
    """
    Get valid QGates and valid single bit QGate type.
    
    Args:
        single_gates: A list of single gate strings.
    
    Returns:
        result: A list containing the validated gate type and valid single gates.
    
    """
    ...

def vector_dot(x: List[float], y: List[float]) -> float:
    """
    Compute the inner product of two vectors.
    
    Args:
        x: A list representing the first vector.
    
        y: A list representing the second vector.
    
    Returns:
        dot result: The dot product of vectors x and y.
    
    """
    ...

def virtual_z_transform(prog: QProg, quantum_machine: QuantumMachine, b_del_rz_gate: bool = False, config_data: str = 'QPandaConfig.json') -> QProg:
    """
    virtual z transform
    
    Args:
        prog: the target prog
    
        quantum_machine: quantum machine
    
        b_del_rz_gate: whether delete the rz gate 
    
        config_data: config data, @See JsonConfigParam::load_config()
    
    Returns:
        mapped quantum program
    """
    ...

