from typing import Any, Callable, ClassVar, Dict, List, Tuple

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
        """
        ...

    def getResult(self, *args, **kwargs) -> Any:
        """
        """
        ...

    def registerFunc(self, arg0: Callable[[List[float],List[float],int,int],Tuple[str,float]], arg1: List[float]) -> None:
        """
        """
        ...

    def setAdaptive(self, arg0: bool) -> None:
        """
        """
        ...

    def setCacheFile(self, arg0: str) -> None:
        """
        """
        ...

    def setDisp(self, arg0: bool) -> None:
        """
        """
        ...

    def setFatol(self, arg0: float) -> None:
        """
        """
        ...

    def setMaxFCalls(self, arg0: int) -> None:
        """
        """
        ...

    def setMaxIter(self, arg0: int) -> None:
        """
        """
        ...

    def setRestoreFromCacheFile(self, arg0: bool) -> None:
        """
        """
        ...

    def setXatol(self, arg0: float) -> None:
        """
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
    __doc__: ClassVar[str] = ...  # read-only
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
    __doc__: ClassVar[str] = ...  # read-only
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
        """
        ...

    def get_prob_list(self, qubit_list: QVec, select_max: int = -1) -> List[float]:
        """
        """
        ...

    def get_prob_tuple_list(self, qubit_list: QVec, select_max: int = -1) -> List[Tuple[int,float]]:
        """
        """
        ...

    @overload
    def init_qvm(self, arg0: bool) -> None:
        """
        """
        ...

    @overload
    def init_qvm(self) -> None:
        """
        """
        ...

    def pmeasure(self, qubit_list: QVec, select_max: int = -1) -> List[Tuple[int,float]]:
        """
        Get the probability distribution over qubits
        """
        ...

    def pmeasure_no_index(self, qubit_list: QVec) -> List[float]:
        """
        Get the probability distribution over qubits
        """
        ...

    @overload
    def prob_run_dict(self, program: QProg, qubit_list: QVec, select_max: int = -1) -> Dict[str,float]:
        """
        """
        ...

    @overload
    def prob_run_dict(self, program: QProg, qubit_addr_list: List[int], select_max: int = -1) -> Dict[str,float]:
        """
        """
        ...

    @overload
    def prob_run_list(self, program: QProg, qubit_list: QVec, select_max: int = -1) -> List[float]:
        """
        """
        ...

    @overload
    def prob_run_list(self, program: QProg, qubit_addr_list: List[int], select_max: int = -1) -> List[float]:
        """
        """
        ...

    @overload
    def prob_run_tuple_list(self, program: QProg, qubit_list: QVec, select_max: int = -1) -> List[Tuple[int,float]]:
        """
        """
        ...

    @overload
    def prob_run_tuple_list(self, program: QProg, qubit_addr_list: List[int], select_max: int = -1) -> List[Tuple[int,float]]:
        """
        """
        ...

    def quick_measure(self, qubit_list: QVec, shots: int) -> Dict[str,int]:
        """
        """
        ...

    def set_max_threads(self, size: int) -> None:
        """
        set CPUQVM max thread size
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
        """
        ...

    def get_prob_list(self, qubit_list: QVec, select_max: int = -1) -> List[float]:
        """
        """
        ...

    def get_prob_tuple_list(self, qubit_list: QVec, select_max: int = -1) -> List[Tuple[int,float]]:
        """
        """
        ...

    def pmeasure(self, qubit_list: QVec, select_max: int = -1) -> List[Tuple[int,float]]:
        """
        Get the probability distribution over qubits
        """
        ...

    def pmeasure_no_index(self, qubit_list: QVec) -> List[float]:
        """
        Get the probability distribution over qubits
        """
        ...

    @overload
    def prob_run_dict(self, program: QProg, qubit_list: QVec, select_max: int = -1) -> Dict[str,float]:
        """
        """
        ...

    @overload
    def prob_run_dict(self, program: QProg, qubit_addr_list: List[int], select_max: int = -1) -> Dict[str,float]:
        """
        """
        ...

    @overload
    def prob_run_list(self, program: QProg, qubit_list: QVec, select_max: int = -1) -> List[float]:
        """
        """
        ...

    @overload
    def prob_run_list(self, program: QProg, qubit_addr_list: List[int], select_max: int = -1) -> List[float]:
        """
        """
        ...

    @overload
    def prob_run_tuple_list(self, program: QProg, qubit_list: QVec, select_max: int = -1) -> List[Tuple[int,float]]:
        """
        """
        ...

    @overload
    def prob_run_tuple_list(self, program: QProg, qubit_addr_list: List[int], select_max: int = -1) -> List[Tuple[int,float]]:
        """
        """
        ...

    def quick_measure(self, qubit_list: QVec, shots: int) -> Dict[str,int]:
        """
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
    __doc__: ClassVar[str] = ...  # read-only
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
        """
        ...

    @overload
    def c_and(self, arg0: ClassicalCondition) -> ClassicalCondition:
        """
        """
        ...

    def c_not(self) -> ClassicalCondition:
        """
        """
        ...

    @overload
    def c_or(self, arg0: int) -> ClassicalCondition:
        """
        """
        ...

    @overload
    def c_or(self, arg0: ClassicalCondition) -> ClassicalCondition:
        """
        """
        ...

    def get_val(self) -> int:
        """
        get value
        """
        ...

    def set_val(self, arg0: int) -> None:
        """
        set value
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
    __doc__: ClassVar[str] = ...  # read-only
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
    __doc__: ClassVar[str] = ...  # read-only
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
    __doc__: ClassVar[str] = ...  # read-only
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
        Run quantum program and get full density matrix
        
        Args:
            prog: quantum program 
        
        Returns:
            full density matrix 
        Raises:
            run_fail: An error occurred in get_density_matrix
        
        """
        ...

    @overload
    def get_expectation(self, prog: QProg, hamiltonian: List[Tuple[Dict[int,str],float]], qubits: QVec) -> float:
        """
        Run quantum program and hamiltonian expection for current qubits
        
        Args:
            prog: quantum program 
            hamiltonian: QHamiltonian 
            qubits: select qubits 
        
        Returns:
            hamiltonian expection for current qubits
        Raises:
            run_fail: An error occurred in get_expectation
        
        
        """
        ...

    @overload
    def get_expectation(self, prog: QProg, hamiltonian: List[Tuple[Dict[int,str],float]], qubits: List[int]) -> float:
        """
        Run quantum program and hamiltonian expection for current qubits
        
        Args:
            prog: quantum program 
            hamiltonian: QHamiltonian 
            qubits: select qubits 
        
        Returns:
            hamiltonian expection for current qubits
        Raises:
            run_fail: An error occurred in get_expectation
        
        """
        ...

    @overload
    def get_probabilities(self, prog: QProg) -> List[float]:
        """
        Run quantum program and get all indices probabilities
        
        Args:
            prog: quantum program 
        
        Returns:
            probabilities result of quantum program 
        Raises:
            run_fail: An error occurred in get_probabilities
        
        
        """
        ...

    @overload
    def get_probabilities(self, prog: QProg, qubits: QVec) -> List[float]:
        """
        Run quantum program and get all indices probabilities for current qubits
        
        Args:
            prog: quantum program 
            qubits: select qubits 
        
        Returns:
            probabilities result of quantum program 
        Raises:
            run_fail: An error occurred in get_probabilities
        
        
        """
        ...

    @overload
    def get_probabilities(self, prog: QProg, qubits: List[int]) -> List[float]:
        """
        Run quantum program and get all indices probabilities for current qubits
        
        Args:
            prog: quantum program 
            qubits: select qubits 
        
        Returns:
            probabilities result of quantum program 
        Raises:
            run_fail: An error occurred in get_probabilities
        
        
        """
        ...

    @overload
    def get_probabilities(self, prog: QProg, indices: List[str]) -> List[float]:
        """
        Run quantum program and get all indices probabilities for current binary indices
        
        Args:
            prog: quantum program 
            indices: select binary indices 
        
        Returns:
            probabilities result of quantum program 
        Raises:
            run_fail: An error occurred in get_probabilities
        
        """
        ...

    @overload
    def get_probability(self, prog: QProg, index: int) -> float:
        """
        Run quantum program and get index probability
        
        Args:
            prog: quantum program 
            index: measure index in [0,2^N - 1] 
        
        Returns:
            probability result of quantum program 
        Raises:
            run_fail: An error occurred in get_probability
        
        
        """
        ...

    @overload
    def get_probability(self, prog: QProg, index: str) -> float:
        """
        Run quantum program and get index probability
        
        Args:
            prog: quantum program 
            index: measure index in [0,2^N - 1] 
        
        Returns:
            probability result of quantum program 
        Raises:
            run_fail: An error occurred in get_probability
        
        """
        ...

    @overload
    def get_reduced_density_matrix(self, prog: QProg, qubits: QVec) -> numpy.ndarray[numpy.complex128[m,n]]:
        """
        Run quantum program and get density matrix for current qubits
        
        Args:
            prog: quantum program 
            qubits: quantum program select qubits
        
        Returns:
            density matrix 
        Raises:
            run_fail: An error occurred in get_reduced_density_matrix
        
        
        """
        ...

    @overload
    def get_reduced_density_matrix(self, prog: QProg, qubits: List[int]) -> numpy.ndarray[numpy.complex128[m,n]]:
        """
        Run quantum program and get density matrix for current qubits
        
        Args:
            prog: quantum program 
            qubits: quantum program select qubits
        
        Returns:
            density matrix 
        Raises:
            run_fail: An error occurred in get_reduced_density_matrix
        
        """
        ...

    def init_qvm(self, is_double_precision: bool = True) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: numpy.ndarray[numpy.complex128[m,n]]) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: numpy.ndarray[numpy.complex128[m,n]], arg1: List[GateType]) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: List[numpy.ndarray[numpy.complex128[m,n]]]) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: List[numpy.ndarray[numpy.complex128[m,n]]], arg1: List[GateType]) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: List[GateType], arg2: float) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float, arg3: QVec) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: List[GateType], arg2: float, arg3: QVec) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float, arg3: List[QVec]) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float, arg3: float, arg4: float) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: List[GateType], arg2: float, arg3: float, arg4: float) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float, arg3: float, arg4: float, arg5: QVec) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: List[GateType], arg2: float, arg3: float, arg4: float, arg5: QVec) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float, arg3: float, arg4: float, arg5: List[QVec]) -> None:
        """
        """
        ...


class DoubleGateTransferType:
    """
    Quantum double gate transfer type
    
    Members:
    
      DOUBLE_GATE_INVALID
    
      DOUBLE_BIT_GATE
    """
    __doc__: ClassVar[str] = ...  # read-only
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
        """
        ...

    @overload
    def amplitude_encode(self, qubit: QVec, data: List[complex]) -> None:
        """
        """
        ...

    @overload
    def amplitude_encode_recursive(self, qubit: QVec, data: List[float]) -> None:
        """
        """
        ...

    @overload
    def amplitude_encode_recursive(self, qubit: QVec, data: List[complex]) -> None:
        """
        Encode by amplitude recursive
        
        Args:
            QVec: qubits 
            QStat: amplitude 
        
        Returns:
            circuit
        Raises:
            run_fail: An error occurred in get amplitude_encode_recursive
        
        """
        ...

    def angle_encode(self, qubit: QVec, data: List[float], gate_type: GateType = GateType.RY_GATE) -> None:
        """
        Encode by angle
        
        Args:
            QVec: qubits 
            prob_vec: data 
        
        Returns:
            circuit
        Raises:
            run_fail: An error occurred in get angle_encode
        
        """
        ...

    @overload
    def approx_mps(self, qubit: QVec, data: List[float], layers: int = 3, sweeps: int = 100, double2float: bool = False) -> None:
        """
        """
        ...

    @overload
    def approx_mps(self, qubit: QVec, data: List[complex], layers: int = 3, sweeps: int = 100) -> None:
        """
        approx mps encode
        
        Args:
            Qubit: qubits 
            data: std::vector<qcomplex_t> 
            int: layer 
            int: step 
        
        Returns:
            circuit
        Raises:
            run_fail: An error occurred in approx_mps
        
        """
        ...

    def basic_encode(self, qubit: QVec, data: str) -> None:
        """
        basic_encode
        
        Args:
            QVec: qubits 
            string: data 
        
        Returns:
            circuit
        Raises:
            run_fail: An error occurred in basic_encode
        
        """
        ...

    def bid_amplitude_encode(self, qubit: QVec, data: List[float], split: int = 0) -> None:
        """
        Encode by bid
        
        Args:
            QVec: qubits 
            QStat: amplitude 
            split: int 
        
        Returns:
            circuit
        Raises:
            run_fail: An error occurred in bid_amplitude_encode
        
        """
        ...

    def dc_amplitude_encode(self, qubit: QVec, data: List[float]) -> None:
        """
        Encode by dc amplitude
        
        Args:
            QVec: qubits 
            QStat: amplitude 
        
        Returns:
            circuit
        Raises:
            run_fail: An error occurred in dc_amplitude_encode
        
        """
        ...

    def dense_angle_encode(self, qubit: QVec, data: List[float]) -> None:
        """
        Encode by dense angle
        
        Args:
            QVec: qubits 
            prob_vec: data 
        
        Returns:
            circuit
        Raises:
            run_fail: An error occurred in dense_angle_encode
        
        """
        ...

    @overload
    def ds_quantum_state_preparation(self, qubit: QVec, data: Dict[str,float]) -> None:
        """
        """
        ...

    @overload
    def ds_quantum_state_preparation(self, qubit: QVec, data: Dict[str,complex]) -> None:
        """
        """
        ...

    @overload
    def ds_quantum_state_preparation(self, qubit: QVec, data: List[float]) -> None:
        """
        """
        ...

    @overload
    def ds_quantum_state_preparation(self, qubit: QVec, data: List[complex]) -> None:
        """
        """
        ...

    @overload
    def efficient_sparse(self, qubit: QVec, data: Dict[str,float]) -> None:
        """
        """
        ...

    @overload
    def efficient_sparse(self, qubit: QVec, data: Dict[str,complex]) -> None:
        """
        """
        ...

    @overload
    def efficient_sparse(self, qubit: QVec, data: List[float]) -> None:
        """
        """
        ...

    @overload
    def efficient_sparse(self, qubit: QVec, data: List[complex]) -> None:
        """
        """
        ...

    def get_circuit(self) -> QCircuit:
        """
        """
        ...

    @overload
    def get_fidelity(self, data: List[float]) -> float:
        """
        """
        ...

    @overload
    def get_fidelity(self, data: List[complex]) -> float:
        """
        """
        ...

    @overload
    def get_fidelity(self, data: List[float]) -> float:
        """
        """
        ...

    def get_out_qubits(self) -> QVec:
        """
        """
        ...

    def iqp_encode(self, qubit: QVec, data: List[float], control_list: List[Tuple[int,int]] = [], bool_inverse: bool = False, repeats: int = 1) -> None:
        """
        Encode by iqp
        
        Args:
            QVec: qubits 
            prob_vec: data 
            list: control_list 
            bool: bool_inverse 
            int: repeats 
        
        Returns:
            circuit
        Raises:
            run_fail: An error occurred in iqp_encode
        
        """
        ...

    def schmidt_encode(self, qubit: QVec, data: List[float], cutoff: float) -> None:
        """
        Encode by schmidt
        
        Args:
            QVec: qubits 
            QStat: amplitude 
            double: cut_off 
        
        Returns:
            circuit
        Raises:
            run_fail: An error occurred in schmidt_encode
        
        """
        ...

    @overload
    def sparse_isometry(self, qubit: QVec, data: Dict[str,float]) -> None:
        """
        """
        ...

    @overload
    def sparse_isometry(self, qubit: QVec, data: Dict[str,complex]) -> None:
        """
        """
        ...

    @overload
    def sparse_isometry(self, qubit: QVec, data: List[float]) -> None:
        """
        """
        ...

    @overload
    def sparse_isometry(self, qubit: QVec, data: List[complex]) -> None:
        """
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
    __doc__: ClassVar[str] = ...  # read-only
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
        """
        ...

    @overload
    def aggregate_operations(self, qprog: QProg) -> None:
        """
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
    __doc__: ClassVar[str] = ...  # read-only
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
    __doc__: ClassVar[str] = ...  # read-only
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
        
        Args:
            rows: rows need be barriered, may not continus
        """
        ...

    def insert_gate(self, target_rows: List[int], ctrl_rows: List[int], from_col: int, gate_type: LATEX_GATE_TYPE, gate_name: str = '', dagger: bool = False, param: str = '') -> int:
        """
        Insert a gate into circute
        
        Args:
            target_rows: gate targets row of latex matrix
            ctrl_rows    from_col: gate wanted col pos, but there may be not enough zone to put gate
            gate_type: enum type of LATEX_GATE_TYPE
            gate_name
            dagger: dagger flag
            param: gate param str
        
        Returns:
            int: real col num. if there is no enough zone to put gate at 'from_col', we will find suitable col to put gate after 'from_col'
        """
        ...

    def insert_measure(self, q_row: int, c_row: int, from_col: int) -> int:
        """
        """
        ...

    def insert_reset(self, q_row: int, from_col: int) -> int:
        """
        """
        ...

    def insert_timeseq(self, t_col: int, time_seq: int) -> None:
        """
        Beware we do not check col num, may cause overwrite. user must take care col num self
        """
        ...

    def set_label(self, qubit_label: Dict[int,str], cbit_label: Dict[int,str] = {}, time_seq_label: str = '', head: bool = True) -> None:
        """
        Set Label at left most head col or right most tail col
        label can be reseted at any time
        
        Args:
            qubit_label: label for qwire left most head label, at row, in latex syntax. not given row will keep empty
                         eg. {0: 'q_{1}', 2:'q_{2}'}
            cbit_label: classic label string, support latex str
            time_seq_label: if given, set time squence lable
            head: if true, label append head; false, append at tail
        """
        ...

    def set_logo(self, logo: str = '') -> None:
        """
        Add a logo string
        """
        ...

    def str(self, with_time: bool = False) -> str:
        """
        return final latex source code, can be called at any time
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
        """
        ...

    @overload
    def add_single_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float, arg3: float, arg4: float) -> None:
        """
        """
        ...

    def get_prob_dict(self, qubit_list: QVec, select_max: int = -1) -> Dict[str,float]:
        """
        Get pmeasure result as dict
        
        Args:
            qubit_list: pmeasure qubits list
            select_max: max returned element num in returnd tuple, should in [-1, 1<<len(qubit_list)]
                        default is -1, means no limit
        Returns:
            measure result of quantum machine
        Raises:
            run_fail: An error occurred in get_prob_dict
        
        """
        ...

    def get_prob_list(self, qubit_list: QVec, select_max: int = -1) -> List[float]:
        """
        Get pmeasure result as list
        
        Args:
            qubit_list: pmeasure qubits list
            select_max: max returned element num in returnd tuple, should in [-1, 1<<len(qubit_list)]
                        default is -1, means no limit
        Returns:
            measure result of quantum machine
        Raises:
            run_fail: An error occurred in get_prob_list
        
        """
        ...

    def get_prob_tuple_list(self, qubit_list: QVec, select_max: int = -1) -> List[Tuple[int,float]]:
        """
        Get pmeasure result as list
        
        Args:
            qubit_list: pmeasure qubits list
            select_max: max returned element num in returnd tuple, should in [-1, 1<<len(qubit_list)]
                        default is -1, means no limit
        Returns:
            measure result of quantum machine
        Raises:
            run_fail: An error occurred in get_prob_tuple_list
        
        """
        ...

    def pmeasure(self, qubit_list: QVec, select_max: int = -1) -> List[Tuple[int,float]]:
        """
        Get the probability distribution over qubits
        
        Args:
            qubit_list: qubit list to measure
            select_max: max returned element num in returnd tuple, should in [-1, 1<<len(qubit_list)]
                        default is -1, means no limit
        
        Returns:
            measure result of quantum machine in tuple form
        """
        ...

    def pmeasure_bin_index(self, program: QProg, string: str) -> complex:
        """
        pmeasure bin index quantum state amplitude
        
        Args:
            string : bin string
        
        Returns:
            complex : bin amplitude
        Raises:
            run_fail: An error occurred in pmeasure_bin_index
        
        """
        ...

    def pmeasure_bin_subset(self, program: QProg, string_list: List[str]) -> List[complex]:
        """
        pmeasure quantum state amplitude subset
        
        Args:
            list : bin state string list
        
        Returns:
            list : bin amplitude result list
        Raises:
            run_fail: An error occurred in pmeasure_bin_subset
        
        """
        ...

    def pmeasure_dec_index(self, program: QProg, string: str) -> complex:
        """
        pmeasure dec index quantum state amplitude
        
        Args:
            string : dec string
        
        Returns:
            complex : dec amplitude
        Raises:
            run_fail: An error occurred in pmeasure_dec_index
        
        """
        ...

    def pmeasure_dec_subset(self, program: QProg, string_list: List[str]) -> List[complex]:
        """
        pmeasure quantum state amplitude subset
        
        Args:
            list : dec state string list
        
        Returns:
            list : dec amplitude result list
        Raises:
            run_fail: An error occurred in pmeasure_dec_subset
        
        """
        ...

    def pmeasure_no_index(self, qubit_list: QVec) -> List[float]:
        """
        Get the probability distribution over qubits
        
        Args:
            qubit_list: qubit list to measure
        
        Returns:
            measure result of quantum machine in list form
        """
        ...

    def prob_run_dict(self, program: QProg, qubit_list: QVec, select_max: int = -1) -> Dict[str,float]:
        """
        Run quantum program and get pmeasure result as dict
        
        Args:
            qprog: quantum program
            qubit_list: pmeasure qubits list
            select_max: max returned element num in returnd tuple, should in [-1, 1<<len(qubit_list)]
                        default is -1, means no limit
        Returns:
            measure result of quantum machine
        Raises:
            run_fail: An error occurred in measure quantum program
        
        """
        ...

    def prob_run_list(self, program: QProg, qubit_list: QVec, select_max: int = -1) -> List[float]:
        """
        Run quantum program and get pmeasure result as list
        
        Args:
            qprog: quantum program
            qubit_list: pmeasure qubits list
            select_max: max returned element num in returnd tuple, should in [-1, 1<<len(qubit_list)]
                        default is -1, means no limit
        Returns:
            measure result of quantum machine
        Raises:
            run_fail: An error occurred in measure quantum program
        
        """
        ...

    def prob_run_tuple_list(self, program: QProg, qubit_list: QVec, select_max: int = -1) -> List[Tuple[int,float]]:
        """
        Run quantum program and get pmeasure result as tuple list
        
        Args:
            qprog: quantum program
            qubit_list: pmeasure qubits list
            select_max: max returned element num in returnd tuple, should in [-1, 1<<len(qubit_list)]
                      default is -1, means no limit
        Returns:
          measure result of quantum machine
        Raises:
            run_fail: An error occurred in prob_run_tuple_list
        
        """
        ...

    def quick_measure(self, qubit_list: QVec, shots: int) -> Dict[str,int]:
        """
        Quick measure
        
        Args:
            qubit_list: qubit list to measure
            shots: the repeat num  of measure operate
        
        Returns:
            result of quantum program
        Raises:
            run_fail: An error occurred in measure quantum program
        
        """
        ...

    @overload
    def set_measure_error(self, arg0: NoiseModel, arg1: float) -> None:
        """
        """
        ...

    @overload
    def set_measure_error(self, arg0: NoiseModel, arg1: float, arg2: float, arg3: float) -> None:
        """
        """
        ...

    @overload
    def set_mixed_unitary_error(self, arg0: GateType, arg1: List[List[complex]], arg2: List[QVec]) -> None:
        """
        """
        ...

    @overload
    def set_mixed_unitary_error(self, arg0: GateType, arg1: List[List[complex]], arg2: List[float], arg3: List[QVec]) -> None:
        """
        """
        ...

    @overload
    def set_mixed_unitary_error(self, arg0: GateType, arg1: List[List[complex]]) -> None:
        """
        """
        ...

    @overload
    def set_mixed_unitary_error(self, arg0: GateType, arg1: List[List[complex]], arg2: List[float]) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float, arg3: List[QVec]) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float, arg3: float, arg4: float) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float, arg3: float, arg4: float, arg5: List[QVec]) -> None:
        """
        """
        ...

    def set_readout_error(self, readout_params: List[List[float]], qubits: QVec) -> None:
        """
        """
        ...

    def set_reset_error(self, reset_0_param: float, reset_1_param: float) -> None:
        """
        """
        ...

    def set_rotation_error(self, param: float) -> None:
        """
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
        """
        ...

    def reset(self) -> None:
        """
        """
        ...


class NodeIter:
    """
    quantum node iter
    """
    __hash__: ClassVar[None] = ...
    def __init__(self) -> None:
        """
        """
        ...

    def get_next(self) -> NodeIter:
        """
        """
        ...

    def get_node_type(self) -> NodeType:
        """
        """
        ...

    def get_pre(self) -> NodeIter:
        """
        """
        ...

    def __eq__(self, arg0: NodeIter) -> bool:
        """
        """
        ...

    def __ne__(self, arg0: NodeIter) -> bool:
        """
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
    __doc__: ClassVar[str] = ...  # read-only
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
        """
        ...

    @overload
    def add_mixed_unitary_error(self, gate_types: GateType, unitary_matrices: List[List[complex]], probs: List[float]) -> None:
        """
        """
        ...

    @overload
    def add_mixed_unitary_error(self, gate_types: GateType, unitary_matrices: List[List[complex]], probs: List[float], qubits: QVec) -> None:
        """
        """
        ...

    @overload
    def add_mixed_unitary_error(self, gate_types: GateType, unitary_matrices: List[List[complex]], probs: List[float], qubits: List[QVec]) -> None:
        """
        """
        ...

    @overload
    def add_noise_model(self, noise_model: NoiseModel, gate_type: GateType, prob: float) -> None:
        """
        """
        ...

    @overload
    def add_noise_model(self, noise_model: NoiseModel, gate_types: List[GateType], prob: float) -> None:
        """
        """
        ...

    @overload
    def add_noise_model(self, noise_model: NoiseModel, gate_type: GateType, prob: float, qubits: QVec) -> None:
        """
        """
        ...

    @overload
    def add_noise_model(self, noise_model: NoiseModel, gate_types: List[GateType], prob: float, qubits: QVec) -> None:
        """
        """
        ...

    @overload
    def add_noise_model(self, noise_model: NoiseModel, gate_type: GateType, prob: float, qubits: List[QVec]) -> None:
        """
        """
        ...

    @overload
    def add_noise_model(self, noise_model: NoiseModel, gate_type: GateType, t1: float, t2: float, t_gate: float) -> None:
        """
        """
        ...

    @overload
    def add_noise_model(self, noise_model: NoiseModel, gate_types: List[GateType], t1: float, t2: float, t_gate: float) -> None:
        """
        """
        ...

    @overload
    def add_noise_model(self, noise_model: NoiseModel, gate_type: GateType, t1: float, t2: float, t_gate: float, qubits: QVec) -> None:
        """
        """
        ...

    @overload
    def add_noise_model(self, noise_model: NoiseModel, gate_types: List[GateType], t1: float, t2: float, t_gate: float, qubits: QVec) -> None:
        """
        """
        ...

    @overload
    def add_noise_model(self, noise_model: NoiseModel, gate_type: GateType, t1: float, t2: float, t_gate: float, qubits: List[QVec]) -> None:
        """
        """
        ...

    @overload
    def set_measure_error(self, noise_model: NoiseModel, prob: float, qubits: QVec = ...) -> None:
        """
        """
        ...

    @overload
    def set_measure_error(self, noise_model: NoiseModel, t1: float, t2: float, t_gate: float, qubits: QVec = ...) -> None:
        """
        """
        ...

    def set_readout_error(self, prob_list: List[List[float]], qubits: QVec = ...) -> None:
        """
        """
        ...

    def set_reset_error(self, p0: float, p1: float, qubits: QVec) -> None:
        """
        """
        ...

    def set_rotation_error(self, error: float) -> None:
        """
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
    __doc__: ClassVar[str] = ...  # read-only
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
        set NoiseQVM max thread size
        """
        ...

    @overload
    def set_measure_error(self, model: NoiseModel, prob: float, qubits: QVec = ...) -> None:
        """
        """
        ...

    @overload
    def set_measure_error(self, model: NoiseModel, T1: float, T2: float, t_gate: float, qubits: QVec = ...) -> None:
        """
        """
        ...

    @overload
    def set_mixed_unitary_error(self, arg0: GateType, arg1: List[List[complex]], arg2: List[float]) -> None:
        """
        """
        ...

    @overload
    def set_mixed_unitary_error(self, arg0: GateType, arg1: List[List[complex]], arg2: List[float], arg3: QVec) -> None:
        """
        """
        ...

    @overload
    def set_mixed_unitary_error(self, arg0: GateType, arg1: List[List[complex]], arg2: List[float], arg3: List[QVec]) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: List[GateType], arg2: float) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float, arg3: QVec) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: List[GateType], arg2: float, arg3: QVec) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float, arg3: List[QVec]) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float, arg3: float, arg4: float) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: List[GateType], arg2: float, arg3: float, arg4: float) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float, arg3: float, arg4: float, arg5: QVec) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: List[GateType], arg2: float, arg3: float, arg4: float, arg5: QVec) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float, arg3: float, arg4: float, arg5: List[QVec]) -> None:
        """
        """
        ...

    def set_readout_error(self, probs_list: List[List[float]], qubits: QVec = ...) -> None:
        """
        """
        ...

    def set_reset_error(self, p0: float, p1: float, qubits: QVec = ...) -> None:
        """
        """
        ...

    def set_rotation_error(self, arg0: float) -> None:
        """
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
        Please input OptimizerType 
        
        """
        ...

    @overload
    def makeOptimizer(self) -> AbstractOptimizer:
        """
        Please input the Optimizer's name(string)
        """
        ...


class OptimizerMode:
    """
    variational quantum OptimizerMode
    
    Members:
    """
    __doc__: ClassVar[str] = ...  # read-only
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
    __doc__: ClassVar[str] = ...  # read-only
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
        """
        ...

    @overload
    def Allocate_CBit(self) -> CBit:
        """
        """
        ...

    @overload
    def Allocate_CBit(self, cbit_num: int) -> CBit:
        """
        """
        ...

    def Free_CBit(self, cbit: CBit) -> None:
        """
        """
        ...

    @overload
    def cAlloc(self) -> CBit:
        """
        """
        ...

    @overload
    def cAlloc(self, cbit_num: int) -> CBit:
        """
        """
        ...

    def cAlloc_many(self, count: int) -> List[ClassicalCondition]:
        """
        """
        ...

    def cFree(self, classical_cond: ClassicalCondition) -> None:
        """
        """
        ...

    @overload
    def cFree_all(self, classical_cond_list: List[ClassicalCondition]) -> None:
        """
        """
        ...

    @overload
    def cFree_all(self) -> None:
        """
        """
        ...

    def clearAll(self) -> None:
        """
        """
        ...

    def getIdleMem(self) -> int:
        """
        """
        ...

    def getMaxMem(self) -> int:
        """
        """
        ...

    def get_allocate_cbits(self) -> List[ClassicalCondition]:
        """
        Get allocate cbits
        """
        ...

    def get_capacity(self) -> int:
        """
        """
        ...

    def get_cbit_by_addr(self, cbit_addr: int) -> CBit:
        """
        """
        ...

    def set_capacity(self, arg0: int) -> None:
        """
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
        Construct a new Origin Collection by read a json file
        
        """
        ...

    @overload
    def __init__(self, arg0: OriginCollection) -> None:
        """
        """
        ...

    def getFilePath(self) -> str:
        """
        Get file path
        """
        ...

    def getJsonString(self) -> str:
        """
        Get Json String
        """
        ...

    def getKeyVector(self) -> List[str]:
        """
        Get key vector
        """
        ...

    def getValue(self, key_name: str) -> List[str]:
        """
        Get value by Key name
        """
        ...

    @overload
    def getValueByKey(self, key_value: str) -> str:
        """
        Get Value by key value
        
        """
        ...

    @overload
    def getValueByKey(self, key_value: int) -> str:
        """
        Get Value by key value
        """
        ...

    def insertValue(self, key: str, *args) -> None:
        """
        """
        ...

    def open(self, file_name: str) -> bool:
        """
        Read the json file of the specified path
        """
        ...

    def setNames(self, *args) -> None:
        """
        """
        ...

    def write(self) -> bool:
        """
        write json file
        """
        ...


class OriginQubitPool:
    """
    quantum qubit pool
    """
    def __init__(self) -> None:
        """
        """
        ...

    def allocateQubitThroughPhyAddress(self, qubit_addr: int) -> Qubit:
        """
        """
        ...

    def allocateQubitThroughVirAddress(self, qubit_num: int) -> Qubit:
        """
        """
        ...

    def clearAll(self) -> None:
        """
        """
        ...

    def getIdleQubit(self) -> int:
        """
        """
        ...

    def getMaxQubit(self) -> int:
        """
        """
        ...

    def getPhysicalQubitAddr(self, qubit: Qubit) -> int:
        """
        """
        ...

    def getVirtualQubitAddress(self, qubit: Qubit) -> int:
        """
        """
        ...

    def get_allocate_qubits(self) -> QVec:
        """
        get allocate qubits
        """
        ...

    def get_capacity(self) -> int:
        """
        """
        ...

    def get_max_usedqubit_addr(self) -> int:
        """
        """
        ...

    def get_qubit_by_addr(self, qubit_addr: int) -> Qubit:
        """
        """
        ...

    def qAlloc(self) -> Qubit:
        """
        """
        ...

    def qAlloc_many(self, qubit_num: int) -> List[Qubit]:
        """
        Allocate a list of qubits
        """
        ...

    def qFree(self, arg0: Qubit) -> None:
        """
        """
        ...

    @overload
    def qFree_all(self, arg0: QVec) -> None:
        """
        """
        ...

    @overload
    def qFree_all(self) -> None:
        """
        """
        ...

    def set_capacity(self, arg0: int) -> None:
        """
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
        Get pmeasure result as dict
        
        Args:
            qubit_list: pmeasure qubits list
        
        Returns:
            measure result of quantum machine
        Raises:
            run_fail: An error occurred in get_prob_dict
        
        """
        ...

    def init_qvm(self, backend_type: int = 0) -> None:
        """
        """
        ...

    def pmeasure_bin_index(self, bin_index: str) -> complex:
        """
        pmeasure bin index quantum state amplitude
        
        Args:
            string : bin string
        
        Returns:
            complex : bin amplitude
        Raises:
            run_fail: An error occurred in pmeasure_bin_index
        
        """
        ...

    def pmeasure_dec_index(self, dec_index: str) -> complex:
        """
        pmeasure dec index quantum state amplitude
        
        Args:
            string : dec string
        
        Returns:
            complex : dec amplitude
        Raises:
            run_fail: An error occurred in pmeasure_dec_index
        
        """
        ...

    def pmeasure_subset(self, index_list: List[str]) -> Dict[str,complex]:
        """
        pmeasure quantum state amplitude subset
        
        Args:
            list : dec state string list
        
        Returns:
            list : dec amplitude result list
        Raises:
            run_fail: An error occurred in pmeasure_dec_index
        
        """
        ...

    def prob_run_dict(self, arg0: QProg, arg1: QVec) -> Dict[str,float]:
        """
        Run quantum program and get pmeasure result as dict
        
        Args:
            qprog: quantum program
            qubit_list: pmeasure qubits list
        
        Returns:
            measure result of quantum machine
        Raises:
            run_fail: An error occurred in measure quantum program
        
        """
        ...

    @overload
    def run(self, qprog: QProg, noise_model: Noise = NoiseModel()) -> None:
        """
        run the quantum program
        
        Args:
            QProg: quantum prog 
            size_t : NoiseModel
        
        Returns:
            none
        Raises:
            run_fail: An error occurred in run
        
        
        """
        ...

    @overload
    def run(self, qprog: QCircuit, noise_model: Noise = NoiseModel()) -> None:
        """
        run the quantum program
        
        Args:
            QProg: quantum prog 
            size_t : NoiseModel
        
        Returns:
            none
        Raises:
            run_fail: An error occurred in run
        
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
        """
        ...

    def begin(self) -> NodeIter:
        """
        """
        ...

    def control(self, control_qubits: QVec) -> QCircuit:
        """
        """
        ...

    def dagger(self) -> QCircuit:
        """
        """
        ...

    def end(self) -> NodeIter:
        """
        """
        ...

    def head(self) -> NodeIter:
        """
        """
        ...

    @overload
    def insert(self, arg0: QCircuit) -> QCircuit:
        """
        """
        ...

    @overload
    def insert(self, arg0: QGate) -> QCircuit:
        """
        """
        ...

    def is_empty(self) -> bool:
        """
        """
        ...

    def last(self) -> NodeIter:
        """
        """
        ...

    def set_control(self, control_qubits: QVec) -> None:
        """
        """
        ...

    def set_dagger(self, arg0: bool) -> None:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: QCircuit) -> QCircuit:
        """
        """
        ...

    @overload
    def __lshift__(self, arg0: QGate) -> QCircuit:
        """
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
    __doc__: ClassVar[str] = ...  # read-only
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

class QCloudService(QuantumMachine):
    """
    origin quantum cloud machine
    """
    batch_compute_url: str
    batch_inquire_url: str
    big_data_batch_compute_url: str
    compute_url: str
    configuration_header_data: str
    estimate_url: str
    inquire_url: str
    measure_qubits_num: List[int]
    pqc_batch_compute_url: str
    pqc_batch_inquire_url: str
    pqc_compute_url: str
    pqc_init_url: str
    pqc_inquire_url: str
    pqc_keys_url: str
    use_compress_data: bool
    user_token: str
    def __init__(self) -> None:
        """
        """
        ...

    def batch_cyclic_query(self, arg0: str) -> Tuple[bool,List[str]]:
        """
        """
        ...

    def build_error_mitigation(self, shots: int, chip_id: int, expectations: List[str], noise_strength: List[float], qemMethod: em_method) -> str:
        """
        """
        ...

    def build_full_amplitude_measure(self, shots: int) -> str:
        """
        """
        ...

    def build_full_amplitude_pmeasure(self, qubit_vec: List[int]) -> str:
        """
        """
        ...

    def build_get_expectation(self, hamiltonian: List[Tuple[Dict[int,str],float]], qubits: List[int]) -> str:
        """
        """
        ...

    def build_get_state_fidelity(self, shot: int, chip_id: int = 2, is_amend: bool = True, is_mapping: bool = True, is_optimization: bool = True) -> str:
        """
        """
        ...

    def build_get_state_tomography_density(self, shot: int, chip_id: int = 2, is_amend: bool = True, is_mapping: bool = True, is_optimization: bool = True) -> str:
        """
        """
        ...

    @overload
    def build_init_object(self, arg0: QProg, arg1: str, arg2: int) -> None:
        """
        """
        ...

    @overload
    def build_init_object(self, arg0: str, arg1: str, arg2: int) -> None:
        """
        """
        ...

    def build_noise_measure(self, shots: int) -> str:
        """
        """
        ...

    def build_partial_amplitude_pmeasure(self, amplitudes: List[str]) -> str:
        """
        """
        ...

    def build_read_out_mitigation(self, shots: int, chip_id: int, expectations: List[str], noise_strength: List[float], qem_method: em_method) -> str:
        """
        """
        ...

    def build_real_chip_measure(self, shots: int, chip_id: int = 2, is_amend: bool = True, is_mapping: bool = True, is_optimization: bool = True) -> str:
        """
        """
        ...

    @overload
    def build_real_chip_measure_batch(self, prog_list: List[str], shots: int, chip_id: int = 2, is_amend: bool = True, is_mapping: bool = True, is_optimization: bool = True, enable_compress_check: bool = False, batch_id: str = '', task_from: int = 4) -> str:
        """
        """
        ...

    @overload
    def build_real_chip_measure_batch(self, prog_list: List[QProg], shots: int, chip_id: int = 2, is_amend: bool = True, is_mapping: bool = True, is_optimization: bool = True, enable_compress_check: bool = False, batch_id: str = '', task_from: int = 4) -> str:
        """
        """
        ...

    def build_single_amplitude_pmeasure(self, amplitude: str) -> str:
        """
        """
        ...

    def cyclic_query(self, arg0: str) -> Tuple[bool,str]:
        """
        """
        ...

    def init(self, user_token: str, is_logged: bool = False) -> None:
        """
        """
        ...

    def parse_get_task_id(self, arg0: str) -> str:
        """
        """
        ...

    def query_comolex_result(self, arg0: str) -> complex:
        """
        """
        ...

    def query_prob_dict_result(self, arg0: str) -> Dict[str,float]:
        """
        """
        ...

    def query_prob_dict_result_batch(self, arg0: List[str]) -> List[Dict[str,float]]:
        """
        """
        ...

    def query_prob_result(self, arg0: str) -> float:
        """
        """
        ...

    def query_prob_vec_result(self, arg0: str) -> List[float]:
        """
        """
        ...

    def query_qst_result(self, arg0: str) -> List[List[complex]]:
        """
        """
        ...

    def query_state_dict_result(self, arg0: str) -> Dict[str,complex]:
        """
        """
        ...

    def set_noise_model(self, arg0: NoiseModel, arg1: List[float], arg2: List[float]) -> None:
        """
        """
        ...

    def set_qcloud_url(self, cloud_url: str) -> None:
        """
        """
        ...


class QCloudTaskConfig:
    """
    """
    chip_id: real_chip_type
    cloud_token: str
    open_amend: bool
    open_mapping: bool
    open_optimization: bool
    shots: int
    def __init__(self) -> None:
        """
        """
        ...


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
    __doc__: ClassVar[str] = ...  # read-only
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
        """
        ...

    def control(self, control_qubits: QVec) -> QGate:
        """
        Get a control quantumgate  base on current quantum gate node
        """
        ...

    def dagger(self) -> QGate:
        """
        """
        ...

    def gate_matrix(self) -> List[complex]:
        """
        """
        ...

    def gate_type(self) -> int:
        """
        """
        ...

    def get_control_qubit_num(self) -> int:
        """
        """
        ...

    def get_control_qubits(self, control_qubits: QVec) -> int:
        """
        Get control vector fron current quantum gate node
        
        Args:
            qvec: control qubits output
        
        Returns:
            int: size of control qubits
        """
        ...

    def get_qubits(self, qubits: QVec) -> int:
        """
        Get qubit vector inside this quantum gate
        
        Args:
            qvec: qubits output
        
        Returns:
            int: size of qubits
        """
        ...

    def get_target_qubit_num(self) -> int:
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
        """
        ...

    @overload
    def __init__(self, classical_cond: ClassicalCondition, true_branch_qprog: QProg) -> None:
        """
        """
        ...

    @overload
    def __init__(self, classical_cond: ClassicalCondition, true_branch_qprog: QProg, false_branch_qprog: QProg) -> None:
        """
        """
        ...

    def get_classical_condition(self) -> ClassicalCondition:
        """
        """
        ...

    def get_false_branch(self) -> QProg:
        """
        """
        ...

    def get_true_branch(self) -> QProg:
        """
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
    __doc__: ClassVar[str] = ...  # read-only
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
        """
        ...


class QOperator:
    """
    quantum operator class
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
    def __init__(self, arg0: QCircuit) -> None:
        """
        """
        ...

    def get_matrix(self) -> List[complex]:
        """
        """
        ...

    def to_instruction(self, arg0: str) -> str:
        """
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
        """
        ...


class QPilotMachine:
    """
    pliot machine
    """
    def __init__(self) -> None:
        """
        """
        ...

    def build_noise_params(self, nose_model_type: int, single_params: List[float], double_params: List[float]) -> PilotNoiseParams:
        """
        """
        ...

    def execute_callback_full_amplitude_expectation(self, prog_str: str, hamiltonian: List[Tuple[Dict[int,str],float]], qubit_vec: List[int], cb_func: Callable[[ErrorCode,float],None], chip_id: int = 33554433) -> ErrorCode:
        """
        """
        ...

    def execute_callback_full_amplitude_measure_task(self, prog_str: str, cb_func: Callable[[ErrorCode,Dict[str,float]],None], chip_id: int = 33554433, shots: int = 1000) -> ErrorCode:
        """
        """
        ...

    def execute_callback_full_amplitude_pmeasure_task(self, prog_str: str, qubit_vec: List[int], cb_func: Callable[[ErrorCode,Dict[str,float]],None], chip_id: int = 33554433) -> ErrorCode:
        """
        """
        ...

    def execute_callback_measure_task(self, prog_str: str, cb_func: Callable[[ErrorCode,Dict[str,float]],None], chip_id: int = 33554432, b_mapping: bool = True, b_optimization: bool = True, shots: int = 1000, specified_block: List[int] = []) -> ErrorCode:
        """
        """
        ...

    def execute_callback_noise_measure_task(self, prog_str: str, noise_params: PilotNoiseParams, cb_func: Callable[[ErrorCode,Dict[str,float]],None], chip_id: int = 33554433, shots: int = 1000) -> ErrorCode:
        """
        """
        ...

    def execute_callback_partial_amplitude_task(self, prog_str: str, target_amplitude_vec: List[str], cb_func: Callable[[ErrorCode,Dict[str,complex]],None], chip_id: int = 33554433) -> ErrorCode:
        """
        """
        ...

    def execute_callback_single_amplitude_task(self, prog_str: str, target_amplitude: str, cb_func: Callable[[ErrorCode,complex],None], chip_id: int = 33554433) -> ErrorCode:
        """
        """
        ...

    def execute_full_amplitude_expectation(self, prog_str: str, hamiltonian: List[Tuple[Dict[int,str],float]], qubit_vec: List[int], chip_id: int = 33554433) -> float:
        """
        """
        ...

    def execute_full_amplitude_measure_task(self, prog_str: str, chip_id: int = 33554433, shots: int = 1000) -> Dict[str,float]:
        """
        """
        ...

    def execute_full_amplitude_pmeasure_task(self, prog_str: str, qubit_vec: List[int], chip_id: int = 33554433) -> Dict[str,float]:
        """
        """
        ...

    def execute_measure_task(self, prog_str: str, chip_id: int = 33554432, b_mapping: bool = True, b_optimization: bool = True, shots: int = 1000, specified_block: List[int] = []) -> List[Dict[str,float]]:
        """
        """
        ...

    def execute_noise_measure_task(self, prog_str: str, noise_params: PilotNoiseParams, chip_id: int = 33554433, shots: int = 1000) -> Dict[str,float]:
        """
        """
        ...

    def execute_partial_amplitude_task(self, prog_str: str, target_amplitude_vec: List[str], chip_id: int = 33554433) -> Dict[str,complex]:
        """
        """
        ...

    def execute_single_amplitude_task(self, prog_str: str, target_amplitude: str, chip_id: int = 33554433) -> complex:
        """
        """
        ...

    def init(self, pilot_url: str, log_cout: bool = False) -> bool:
        """
        """
        ...

    def init_withconfig(self, config_path: str = 'pilotmachine.conf') -> bool:
        """
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

    def async_em_compute(self, parameter_json: str) -> str:
        """
        """
        ...

    def async_real_chip_expectation(self, prog: QProg, hamiltonian: str, qubits: List[int] = [], shot: int = 1000, chip_id: int = 33554432, is_amend: bool = True, is_mapping: bool = True, is_optimization: bool = True, specified_block: List[int] = [], describe: str = '') -> str:
        """
        """
        ...

    @overload
    def async_real_chip_measure(self, prog: QProg, shot: int = 1000, chip_id: int = 33554432, is_amend: bool = True, is_mapping: bool = True, is_optimization: bool = True, specified_block: List[int] = [], is_prob_counts: bool = True, describe: str = '') -> str:
        """
        """
        ...

    @overload
    def async_real_chip_measure(self, ir: str, shot: int = 1000, chip_id: int = 33554432, is_amend: bool = True, is_mapping: bool = True, is_optimization: bool = True, specified_block: List[int] = [], is_prob_counts: bool = True, describe: str = '') -> str:
        """
        """
        ...

    @overload
    def async_real_chip_measure(self, prog: List[QProg], shot: int = 1000, chip_id: int = 33554432, is_amend: bool = True, is_mapping: bool = True, is_optimization: bool = True, specified_block: List[int] = [], is_prob_counts: bool = True, describe: str = '') -> str:
        """
        """
        ...

    @overload
    def async_real_chip_measure(self, ir: List[str], shot: int = 1000, chip_id: int = 33554432, is_amend: bool = True, is_mapping: bool = True, is_optimization: bool = True, specified_block: List[int] = [], is_prob_counts: bool = True, describe: str = '') -> str:
        """
        """
        ...

    @overload
    def async_real_chip_measure(self, prog: List[QProg], config_str: str) -> str:
        """
        """
        ...

    @overload
    def async_real_chip_measure_vec(self, prog: List[QProg], shot: int = 1000, chip_id: int = 33554432, is_amend: bool = True, is_mapping: bool = True, is_optimization: bool = True, specified_block: List[int] = [], is_prob_counts: bool = True, describe: str = '') -> str:
        """
        """
        ...

    @overload
    def async_real_chip_measure_vec(self, ir: List[str], shot: int = 1000, chip_id: int = 33554432, is_amend: bool = True, is_mapping: bool = True, is_optimization: bool = True, specified_block: List[int] = [], is_prob_counts: bool = True, describe: str = '') -> str:
        """
        """
        ...

    def async_real_chip_qst(self, prog: QProg, shot: int = 1000, chip_id: int = 33554432, is_amend: bool = True, is_mapping: bool = True, is_optimization: bool = True, specified_block: List[int] = [], describe: str = '') -> str:
        """
        """
        ...

    def async_real_chip_qst_density(self, prog: QProg, shot: int = 1000, chip_id: int = 33554432, is_amend: bool = True, is_mapping: bool = True, is_optimization: bool = True, specified_block: List[int] = [], describe: str = '') -> str:
        """
        """
        ...

    def async_real_chip_qst_fidelity(self, prog: QProg, shot: int = 1000, chip_id: int = 33554432, is_amend: bool = True, is_mapping: bool = True, is_optimization: bool = True, specified_block: List[int] = [], describe: str = '') -> str:
        """
        """
        ...

    def build_init_msg(self, api_key: str) -> str:
        """
        """
        ...

    def build_query_msg(self, task_id: str) -> str:
        """
        """
        ...

    def build_task_msg(self, prog: List[QProg], shot: int, chip_id: int, is_amend: bool, is_mapping: bool, is_optimization: bool, specified_block: List[int], task_describe: str) -> str:
        """
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

    def em_compute(self, parameter_json: str) -> List[float]:
        """
        """
        ...

    def finalize(self) -> None:
        """
        finalize
        """
        ...

    def get_expectation_result(self, task_id: str) -> list:
        """
        """
        ...

    @overload
    def get_measure_result(self, task_id: str) -> list:
        """
        """
        ...

    @overload
    def get_measure_result(self, task_id: str) -> list:
        """
        """
        ...

    def get_qst_density_result(self, task_id: str) -> list:
        """
        """
        ...

    def get_qst_fidelity_result(self, task_id: str) -> list:
        """
        """
        ...

    def get_qst_result(self, task_id: str) -> list:
        """
        """
        ...

    def get_token(self, rep_json: str) -> ErrorCode:
        """
        """
        ...

    @overload
    def init(self) -> None:
        """
        """
        ...

    @overload
    def init(self, url: str, log_cout: bool = False, api_key: str = None) -> None:
        """
        """
        ...

    @overload
    def init(self, url: str, log_cout: bool = False, username: str = None, password: str = None) -> None:
        """
        """
        ...

    def init_config(self, url: str, log_cout: bool) -> None:
        """
        """
        ...

    def noise_learning(self, parameter_json: str = True) -> str:
        """
        """
        ...

    def output_version(self) -> str:
        """
        """
        ...

    def pMeasureBinindex(self, prog: QProg, index: str, backendID: int = 33554433) -> float:
        """
        """
        ...

    def pMeasureDecindex(self, prog: QProg, index: str, backendID: int = 33554433) -> float:
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

    def parser_sync_result(self, json_str: str) -> list:
        """
        """
        ...

    def pmeasure_subset(self, prog: QProg, amplitude: List[str], backendID: int = 33554433) -> Dict[str,complex]:
        """
        """
        ...

    def probRunDict(self, prog: QProg, qubit_vec: List[int], backendID: int = 33554433) -> Dict[str,float]:
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

    def query_compile_prog(self, task_id: str, without_compensate: bool = True) -> list:
        """
        Query Task compile prog by task_id
        Args:
            without_compensate: whether return the prog without angle compensate
        
        Returns:
            bool: whether find compile prog success
        Raises:
            none
        
        """
        ...

    @overload
    def query_task_state(self, task_id: str) -> list:
        """
        Query Task State by task_id
        Args:
            task_id: Taeget task id, got by async_real_chip_measure
        
        Returns:
            string: task state: 2: Running; 3: Finished; 4: Failed
            string: task result string
        Raises:
            none
        
        
        """
        ...

    @overload
    def query_task_state(self, task_id: str, is_save: bool, file_path: str = '') -> list:
        """
        """
        ...

    def query_task_state_vec(self, task_id: str) -> list:
        """
        Query Task State by task_id
        Args:
            task_id: Taeget task id, got by async_real_chip_measure
        
        Returns:
            string: task state: 2: Running; 3: Finished; 4: Failed
            array: task result array
        Raises:
            none
        
        """
        ...

    def real_chip_expectation(self, prog: QProg, hamiltonian: str, qubits: List[int] = [], shot: int = 1000, chip_id: int = 33554432, is_amend: bool = True, is_mapping: bool = True, is_optimization: bool = True, specified_block: List[int] = [], describe: str = '') -> float:
        """
        """
        ...

    @overload
    def real_chip_measure(self, prog: QProg, shot: int = 1000, chip_id: int = 33554432, is_amend: bool = True, is_mapping: bool = True, is_optimization: bool = True, specified_block: List[int] = [], describe: str = '') -> Dict[str,float]:
        """
        """
        ...

    @overload
    def real_chip_measure(self, ir: str, shot: int = 1000, chip_id: int = 33554432, is_amend: bool = True, is_mapping: bool = True, is_optimization: bool = True, specified_block: List[int] = [], describe: str = '') -> Dict[str,float]:
        """
        """
        ...

    @overload
    def real_chip_measure(self, prog: List[QProg], shot: int = 1000, chip_id: int = 33554432, is_amend: bool = True, is_mapping: bool = True, is_optimization: bool = True, specified_block: List[int] = [], describe: str = '') -> List[Dict[str,float]]:
        """
        """
        ...

    @overload
    def real_chip_measure(self, ir: List[str], shot: int = 1000, chip_id: int = 33554432, is_amend: bool = True, is_mapping: bool = True, is_optimization: bool = True, specified_block: List[int] = [], describe: str = '') -> List[Dict[str,float]]:
        """
        """
        ...

    @overload
    def real_chip_measure(self, prog: List[QProg], config_str: str) -> str:
        """
        """
        ...

    @overload
    def real_chip_measure_prob_count(self, ir: str, shot: int = 1000, chip_id: int = 33554432, is_mapping: bool = True, is_optimization: bool = True, specified_block: List[int] = [], describe: str = '') -> Dict[str,int]:
        """
        """
        ...

    @overload
    def real_chip_measure_prob_count(self, prog: QProg, shot: int = 1000, chip_id: int = 33554432, is_mapping: bool = True, is_optimization: bool = True, specified_block: List[int] = [], describe: str = '') -> Dict[str,int]:
        """
        """
        ...

    @overload
    def real_chip_measure_prob_count(self, ir: List[str], shot: int = 1000, chip_id: int = 33554432, is_mapping: bool = True, is_optimization: bool = True, specified_block: List[int] = [], describe: str = '') -> List[Dict[str,int]]:
        """
        """
        ...

    @overload
    def real_chip_measure_prob_count(self, prog: List[QProg], shot: int = 1000, chip_id: int = 33554432, is_mapping: bool = True, is_optimization: bool = True, specified_block: List[int] = [], describe: str = '') -> List[Dict[str,int]]:
        """
        """
        ...

    @overload
    def real_chip_measure_vec(self, prog: List[QProg], shot: int = 1000, chip_id: int = 33554432, is_amend: bool = True, is_mapping: bool = True, is_optimization: bool = True, specified_block: List[int] = [], describe: str = '') -> List[Dict[str,float]]:
        """
        """
        ...

    @overload
    def real_chip_measure_vec(self, ir: List[str], shot: int = 1000, chip_id: int = 33554432, is_amend: bool = True, is_mapping: bool = True, is_optimization: bool = True, specified_block: List[int] = [], describe: str = '') -> List[Dict[str,float]]:
        """
        """
        ...

    def runWithConfiguration(self, prog: QProg, shots: int = 1000, backend_id: int = 33554433, noise_model: Noise = ...) -> Dict[str,int]:
        """
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
        construct a prog node
        Args:
            none
        
        Returns:
            a prog node
        
        """
        ...

    @overload
    def __init__(self, arg0: QCircuit) -> None:
        """
        construct a prog node from QCircuit node
        
        Args:
            QCircuit
        
        Returns:
            a prog node
        
        """
        ...

    @overload
    def __init__(self, arg0: QIfProg) -> None:
        """
        construct a prog node from QIfProg node
        
        Args:
            QIfProg
        
        Returns:
            a prog node
        
        """
        ...

    @overload
    def __init__(self, arg0: QWhileProg) -> None:
        """
        construct a prog node from QWhileProg node
        
        Args:
            QWhileProg
        
        Returns:
            a prog node
        
        """
        ...

    @overload
    def __init__(self, arg0: QGate) -> None:
        """
        construct a prog node from QGate node
        
        Args:
            QGate
        
        Returns:
            a prog node
        
        """
        ...

    @overload
    def __init__(self, arg0: QMeasure) -> None:
        """
        construct a prog node from QMeasure node
        
        Args:
            QMeasure
        
        Returns:
            a prog node
        
        """
        ...

    @overload
    def __init__(self, arg0: QReset) -> None:
        """
        construct a prog node from QReset node
        
        Args:
            QReset
        
        Returns:
            a prog node
        
        """
        ...

    @overload
    def __init__(self, arg0: ClassicalCondition) -> None:
        """
        construct a prog node from ClassicalCondition node
        
        Args:
            ClassicalCondition
        
        Returns:
            a prog node
        
        """
        ...

    @overload
    def __init__(self, arg0: NodeIter) -> None:
        """
        construct a prog node from ClassicalCondition node
        
        Args:
            ClassicalCondition
        
        Returns:
            a prog node
        """
        ...

    def begin(self) -> NodeIter:
        """
        """
        ...

    def end(self) -> NodeIter:
        """
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
        get a list cbits of prog
        """
        ...

    def get_used_qubits(self, qubit_vector: QVec) -> QVec:
        """
        get a list qubits of prog
        """
        ...

    def head(self) -> NodeIter:
        """
        """
        ...

    @overload
    def insert(self, arg0: QProg) -> QProg:
        """
        """
        ...

    @overload
    def insert(self, arg0: QGate) -> QProg:
        """
        """
        ...

    @overload
    def insert(self, arg0: QCircuit) -> QProg:
        """
        """
        ...

    @overload
    def insert(self, arg0: QIfProg) -> QProg:
        """
        """
        ...

    @overload
    def insert(self, arg0: QWhileProg) -> QProg:
        """
        """
        ...

    @overload
    def insert(self, arg0: QMeasure) -> QProg:
        """
        """
        ...

    @overload
    def insert(self, arg0: QReset) -> QProg:
        """
        """
        ...

    @overload
    def insert(self, arg0: ClassicalCondition) -> QProg:
        """
        """
        ...

    def is_empty(self) -> bool:
        """
        """
        ...

    def is_measure_last_pos(self) -> bool:
        """
        """
        ...

    def last(self) -> NodeIter:
        """
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
        """
        ...

    def get_target_vertex(self, vertice_num: int) -> QProgDAGVertex:
        """
        """
        ...

    def get_vertex_set(self) -> List[QProgDAGVertex]:
        """
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
        """
        ...

    def get_control_vec(self) -> QVec:
        """
        """
        ...

    def get_iter(self) -> NodeIter:
        """
        """
        ...

    def get_qubits_vec(self) -> QVec:
        """
        """
        ...

    def is_dagger(self) -> bool:
        """
        """
        ...


class QReset:
    """
    quantum reset node
    """
    def __init__(self, arg0: NodeIter) -> None:
        """
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
        """
        ...

    @overload
    def __init__(self, qubit_list: List[Qubit]) -> None:
        """
        """
        ...

    @overload
    def __init__(self, qvec: QVec) -> None:
        """
        """
        ...

    @overload
    def __init__(self, qubit: Qubit) -> None:
        """
        """
        ...

    def append(self, qubit: Qubit) -> None:
        """
        """
        ...

    def pop(self) -> None:
        """
        """
        ...

    def to_list(self) -> List[Qubit]:
        """
        """
        ...

    @overload
    def __getitem__(self, qubit_addr: int) -> Qubit:
        """
        """
        ...

    @overload
    def __getitem__(self, classical_cond) -> Qubit:
        """
        """
        ...

    def __len__(self) -> int:
        """
        """
        ...


class QWhileProg:
    """
    quantum while node
    """
    @overload
    def __init__(self, arg0: NodeIter) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: ClassicalCondition, arg1: QProg) -> None:
        """
        """
        ...

    def get_classical_condition(self) -> ClassicalCondition:
        """
        """
        ...

    def get_true_branch(self) -> QProg:
        """
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
        allocate qubits through phy address
        
        Args:
            address: qubit phy address
        
        Returns:
            Qubit
        
        Raises:
            run_fail: An error occurred in allocated qubits of QuantumMachine
        
        """
        ...

    def allocate_qubit_through_vir_address(self, address: int) -> Qubit:
        """
        allocate qubits through vir address
        
        Args:
            address: qubit vir address
        
        Returns:
            Qubit
        
        Raises:
            run_fail: An error occurred in allocated qubits of QuantumMachine
        
        """
        ...

    def async_run(self, qprog: QProg, noise_model: Noise = NoiseModel()) -> None:
        """
        Run quantum prog asynchronously at background
        Use get_processed_qgate_num() to get check the asynchronous process progress
        Use is_async_finished() check whether asynchronous process finished
        Use get_async_result() block current code and get asynchronous process result unitll it finished
        """
        ...

    @overload
    def cAlloc(self) -> ClassicalCondition:
        """
        Allocate a CBit
        After init()
        
        Args:
            cbit_addr: cbit address, should in [0,29)
        Returns:
            classic result cbit
        
        """
        ...

    @overload
    def cAlloc(self, cbit: int) -> ClassicalCondition:
        """
        Allocate a CBit
        After init()
        
        Args:
            cbit_addr: cbit address, should in [0,29)
        Returns:
            classic result cbit
        """
        ...

    def cAlloc_many(self, cbit_num: int) -> List[ClassicalCondition]:
        """
        Allocate several CBits
        After init()
        
        Args:
            cbit_num: numbers of cbit want to be created
        
        Returns:
            list of cbit
        """
        ...

    def cFree(self, arg0: ClassicalCondition) -> None:
        """
        Free a CBit
        
        Args:
            CBit: a CBit
        
        Returns:
            none
        
        """
        ...

    @overload
    def cFree_all(self, cbit_list: List[ClassicalCondition]) -> None:
        """
        Free all cbits
        
        Args:
            none
        
        Returns:
            none
        
        
        """
        ...

    @overload
    def cFree_all(self) -> None:
        """
        Free all cbits
        
        Args:
            none
        
        Returns:
            none
        
        """
        ...

    def directly_run(self, qprog: QProg, noise_model: Noise = NoiseModel()) -> Dict[str,bool]:
        """
        Directly run quantum prog
        After init()
        
        Args:
            qprog: quantum program
            noise_model: noise model, default is no noise. noise model only work on CPUQVM now
        
        Returns:
            Dict[str, bool]: result of quantum program execution one shot.
                             first is the final qubit register state, second is it's measure probability
        """
        ...

    def finalize(self) -> None:
        """
        finalize quantum machine
        
        Args:
            none
        
        Returns:
            none
        Raises:
            run_fail: An error occurred in finalize
        
        """
        ...

    def getAllocateCMem(self) -> int:
        """
        Get allocated cbits of QuantumMachine
        
        Args:
            none
        
        Returns:
            cbit list
        
        Raises:
            run_fail: An error occurred in allocated cbits of QuantumMachine
        
        """
        ...

    def getAllocateQubitNum(self) -> int:
        """
        Get allocated qubits of QuantumMachine
        
        Args:
            none
        
        Returns:
            qubit list
        
        Raises:
            run_fail: An error occurred in allocated qubits of QuantumMachine
        
        """
        ...

    def getStatus(self, *args, **kwargs) -> Any:
        """
        Get the status of the Quantum machine
        
        Args:
            none
        
        Returns:
            the status of the Quantum machine, see QMachineStatus
        
        Raises:
            init_fail: An error occurred
        
        """
        ...

    def get_allocate_cbits(self) -> List[ClassicalCondition]:
        """
        Get allocated cbits of QuantumMachine
        
        Args:
            none
        
        Returns:
            cbit list
        
        Raises:
            run_fail: An error occurred in allocated cbits of QuantumMachine
        
        """
        ...

    def get_allocate_cmem_num(self) -> int:
        """
        Get allocated cbits of QuantumMachine
        
        Args:
            none
        
        Returns:
            cbit list
        
        Raises:
            run_fail: An error occurred in allocated cbits of QuantumMachine
        
        """
        ...

    def get_allocate_qubit_num(self) -> int:
        """
        Get allocated qubits of QuantumMachine
        
        Args:
            none
        
        Returns:
            qubit list
        
        Raises:
            run_fail: An error occurred in allocated qubits of QuantumMachine
        
        """
        ...

    def get_allocate_qubits(self) -> QVec:
        """
        Get allocated qubits of QuantumMachine
        
        Args:
            none
        
        Returns:
            qubit list
        
        Raises:
            run_fail: An error occurred in allocated qubits of QuantumMachine
        
        """
        ...

    def get_async_result(self) -> Dict[str,bool]:
        """
        """
        ...

    @overload
    def get_expectation(self, qprog: QProg, hamiltonian: List[Tuple[Dict[int,str],float]], qubit_list: QVec) -> float:
        """
        get expectation of current hamiltonian
        
        Args:
            qprog : quantum prog 
            hamiltonian: selected hamiltonian 
            qubit_list : measure qubit list 
        
        Returns:
            double : expectation of current hamiltonian
        
        Raises:
            run_fail: An error occurred in get_expectation
        
        
        """
        ...

    @overload
    def get_expectation(self, qprog: QProg, hamiltonian: List[Tuple[Dict[int,str],float]], qubit_list: QVec, shots: int) -> float:
        """
        get expectation of current hamiltonian
        
        Args:
            qprog : quantum prog 
            hamiltonian: selected hamiltonian 
            qubit_list : measure qubit list 
            shots : measure shots 
        
        Returns:
            double : expectation of current hamiltonian
        
        Raises:
            run_fail: An error occurred in get_expectation
        
        """
        ...

    def get_gate_time_map(self) -> Dict[GateType,int]:
        """
        """
        ...

    def get_processed_qgate_num(self) -> int:
        """
        """
        ...

    def get_qstate(self) -> List[complex]:
        """
        Get the status of the Quantum machine
        
        Args:
            none
        
        Returns:
            the status of the Quantum machine, see QMachineStatus
        
        Raises:
            init_fail: An error occurred
        
        """
        ...

    def get_status(self, *args, **kwargs) -> Any:
        """
        Get the status of the Quantum machine
        
        Args:
            none
        
        Returns:
            the status of the Quantum machine, see QMachineStatus
        
        Raises:
            init_fail: An error occurred
        
        """
        ...

    def initQVM(self) -> None:
        """
        Init the global unique quantum machine at background.
        
        Args:
            machine_type: quantum machine type, see pyQPanda.QMachineType
        
        Returns:
            bool: ture if initialization success
        """
        ...

    def init_qvm(self) -> None:
        """
        Init the global unique quantum machine at background.
        
        Args:
            machine_type: quantum machine type, see pyQPanda.QMachineType
        
        Returns:
            bool: ture if initialization success
        """
        ...

    def init_sparse_state(self, *args, **kwargs) -> Any:
        """
        """
        ...

    def init_state(self, state: List[complex] = QStat(), qlist: QVec = QVec()) -> None:
        """
        """
        ...

    def is_async_finished(self) -> bool:
        """
        """
        ...

    def qAlloc(self) -> Qubit:
        """
        Allocate a qubits
        After init()
        
        Args:
            qubit_addr: qubit physic address, should in [0,29)
        
        Returns:
            pyQPanda.Qubit: None, if qubit_addr error, or reached max number of allowed qubit
        """
        ...

    def qAlloc_many(self, qubit_num: int) -> List[Qubit]:
        """
        Allocate several qubits
        After init()
        
        Args:
            qubit_num: numbers of qubit want to be created
        
        Returns:
            list[pyQPanda.Qubit]: list of qubit
        """
        ...

    def qFree(self, qubit: Qubit) -> None:
        """
        Free a CBit
        
        Args:
            CBit: a CBit
        
        Returns:
            none
        
        """
        ...

    @overload
    def qFree_all(self, qubit_list: QVec) -> None:
        """
        Free all cbits
        
        Args:
            none
        
        Returns:
            none
        
        
        """
        ...

    @overload
    def qFree_all(self, arg0: QVec) -> None:
        """
        Free all qubits
        
        Args:
            none
        
        Returns:
            none
        
        """
        ...

    @overload
    def run_with_configuration(self, qprog: QProg, cbit_list: List[ClassicalCondition], data: dict, noise_model: Noise = NoiseModel()) -> Dict[str,int]:
        """
        Run quantum program with configuration
        
        Args:
            program: quantum program
            cbit_list: classic cbits list
            shots: repeate run quantum program times
            noise_model: noise model, default is no noise. noise model only work on CPUQVM now
        
        Returns:
            result of quantum program execution in shots.
            first is the final qubit register state, second is it's hit shotRaises:
            run_fail: An error occurred in measure quantum program
        
        
        """
        ...

    @overload
    def run_with_configuration(self, qprog: QProg, cbit_list: List[ClassicalCondition], shot: int, noise_model: Noise = NoiseModel()) -> Dict[str,int]:
        """
        Run quantum program with configuration
        
        Args:
            program: quantum program
            cbit_list: classic cbits list
            shots: repeate run quantum program times
            noise_model: noise model, default is no noise. noise model only work on CPUQVM now
        
        Returns:
            result of quantum program execution in shots.
            first is the final qubit register state, second is it's hit shotRaises:
            run_fail: An error occurred in measure quantum program
        
        
        """
        ...

    @overload
    def run_with_configuration(self, qprog: QProg, shot: int, noise_model: Noise = NoiseModel()) -> Dict[str,int]:
        """
        Run quantum program with configuration
        
        Args:
            program: quantum program
            shots: repeate run quantum program times
            noise_model: noise model, default is no noise. noise model only work on CPUQVM now
        
        Returns:
            result of quantum program execution in shots.
            first is the final qubit register state, second is it's hit shotRaises:
            run_fail: An error occurred in measure quantum program
        
        
        """
        ...

    @overload
    def run_with_configuration(self, qprog: QProg, cbit_list: List[int], shot: int, noise_model: Noise = NoiseModel()) -> Dict[str,int]:
        """
        Run quantum program with configuration
        
        Args:
            program: quantum program
            cbit_list: classic cbits list
            shots: repeate run quantum program times
            noise_model: noise model, default is no noise. noise model only work on CPUQVM now
        
        Returns:
            result of quantum program execution in shots.
            first is the final qubit register state, second is it's hit shotRaises:
            run_fail: An error occurred in measure quantum program
        
        """
        ...

    def set_configure(self, max_qubit: int, max_cbit: int) -> None:
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
        caculate tomography density
        """
        ...

    @overload
    def combine_qprogs(self, circuit: QProg, qlist: QVec) -> List[QProg]:
        """
        Return a list of quantum state tomography quantum programs.
        
        """
        ...

    @overload
    def combine_qprogs(self, circuit: QCircuit, qlist: QVec) -> List[QProg]:
        """
        Return a list of quantum state tomography quantum programs.
        
        """
        ...

    @overload
    def combine_qprogs(self, circuit: QProg, qlist: List[int]) -> List[QProg]:
        """
        Return a list of quantum state tomography quantum programs.
        
        """
        ...

    @overload
    def combine_qprogs(self, circuit: QCircuit, qlist: List[int]) -> List[QProg]:
        """
        Return a list of quantum state tomography quantum programs.
        """
        ...

    def exec(self, qm, shots: int) -> List[List[complex]]:
        """
        run state tomography QProgs
        """
        ...

    def set_qprog_results(self, qlist: int, results: List[Dict[str,float]]) -> None:
        """
        set combine_qprogs result
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
        """
        ...

    def get_phy_addr(self) -> int:
        """
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
        Get pmeasure result as dict
        
        Args:
            qubit_list: pmeasure qubits list
        
        Returns:
            measure result of quantum machine
        Raises:
            run_fail: An error occurred in get_prob_dict
        
        
        """
        ...

    @overload
    def get_prob_dict(self, arg0: List[int]) -> Dict[str,float]:
        """
        Get pmeasure result as dict
        
        Args:
            qubit_list: pmeasure qubits list
        
        Returns:
            measure result of quantum machineRaises:
            run_fail: An error occurred in get_prob_dict
        
        """
        ...

    def get_quick_map_vertice(self, arg0: List[Tuple[int,int]]) -> None:
        """
        get quick map vertice
        """
        ...

    def get_sequence(self, arg0: List[int], arg1: List[List[Tuple[int,bool]]]) -> int:
        """
        get prog sequence
        """
        ...

    def pmeasure_bin_amplitude(self, arg0: str) -> complex:
        """
        pmeasure bin index quantum state amplitude
        
        Args:
            string : bin string
        
        Returns:
            complex : bin amplitude
        Raises:
            run_fail: An error occurred in pmeasure_bin_index
        
        """
        ...

    def pmeasure_bin_index(self, arg0: str) -> float:
        """
        pmeasure bin index quantum state amplitude
        
        Args:
            string : bin string
        
        Returns:
            double : bin amplitude prob
        Raises:
            run_fail: An error occurred in pmeasure_bin_index
        
        """
        ...

    def pmeasure_dec_amplitude(self, arg0: str) -> complex:
        """
        pmeasure dec index quantum state amplitude
        
        Args:
            string : dec string
        
        Returns:
            complex : dec amplitude amplitude
        Raises:
            run_fail: An error occurred in pmeasure_dec_index
        
        """
        ...

    def pmeasure_dec_index(self, arg0: str) -> float:
        """
        pmeasure dec index quantum state amplitude
        
        Args:
            string : dec string
        
        Returns:
            double : dec amplitude prob
        Raises:
            run_fail: An error occurred in pmeasure_dec_index
        
        """
        ...

    @overload
    def prob_run_dict(self, arg0: QProg, arg1: QVec) -> Dict[str,float]:
        """
        Run quantum program and get pmeasure result as dict
        
        Args:
            qprog: quantum program
            qubit_list: pmeasure qubits list
        
        Returns:
            measure result of quantum machine
        Raises:
            run_fail: An error occurred in measure quantum program
        
        
        """
        ...

    @overload
    def prob_run_dict(self, arg0: QProg, arg1: List[int]) -> Dict[str,float]:
        """
        Run quantum program and get pmeasure result as dict
        
        Args:
            qprog: quantum program
            qubit_list: pmeasure qubits list
        
        Returns:
            measure result of quantum machine
        Raises:
            run_fail: An error occurred in measure quantum program
        
        """
        ...

    @overload
    def run(self, prog: QProg, qv: QVec, max_rank: int = 30, alloted_time: int = 5) -> None:
        """
        run the quantum program
        
        Args:
            QProg: quantum prog 
            QVec: qubits list
            size_t: max_rank
            size_t: alloted_time
        
        Returns:
            none
        Raises:
            run_fail: An error occurred in run
        
        
        """
        ...

    @overload
    def run(self, arg0: QProg, arg1: QVec, arg2: int, arg3: List[List[Tuple[int,bool]]]) -> None:
        """
        run the quantum program
        
        Args:
            QProg: quantum prog 
            QVec: qubits list
            size_t: max_rank
            list: sequences
        
        Returns:
            none
        Raises:
            run_fail: An error occurred in run
        
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
    __doc__: ClassVar[str] = ...  # read-only
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
        Run quantum program and get pmeasure result as dict
        
        Args:
            qprog: quantum program
        
        Returns:
             Dict[str, bool]: result of quantum program execution one shot.
        Raises:
            run_fail: An error occurred in measure quantum program
        
        """
        ...

    def directly_run(self, arg0: QProg) -> Dict[str,bool]:
        """
        Run quantum program and get pmeasure result as dict
        
        Args:
            qprog: quantum program
        
        Returns:
            measure result of quantum machine
        Raises:
            run_fail: An error occurred in measure quantum program
        
        """
        ...

    def init_qvm(self) -> None:
        """
        init quantum virtual machine
        """
        ...

    def prob_run_dict(self, arg0: QProg) -> Dict[str,float]:
        """
        Run quantum program and get pmeasure result as dict
        
        Args:
            qprog: quantum program
        
        Returns:
            measure result of quantum machine
        Raises:
            run_fail: An error occurred in measure quantum program
        
        """
        ...

    def run_with_configuration(self, arg0: QProg, arg1: List[ClassicalCondition], arg2: int) -> Dict[str,int]:
        """
        Run quantum program and get pmeasure result as dict
        
        Args:
            qprog: quantum program
        
        Args:
            cbits: quantum cbits
        
        Args:
            shots: samble shots
        
        Returns:
            measure result of quantum machine
        Raises:
            run_fail: An error occurred in measure quantum program
        
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
        Run quantum program and get probabilities
        
        Args:
            prog: quantum program 
            qubits: pmeasure qubits
        
        Returns:
            probabilities result of quantum program 
        Raises:
            run_fail: An error occurred in prob_run_dict
        
        """
        ...

    def run_with_configuration(self, qprog: QProg, shot: int) -> Dict[str,int]:
        """
        Run quantum program and get shots result 
        
        Args:
            prog: quantum program 
            int: measure shots
        
        Returns:
            shots result of quantum program 
        Raises:
            run_fail: An error occurred in run_with_configuration
        
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: List[GateType], arg2: float) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float, arg3: QVec) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: List[GateType], arg2: float, arg3: QVec) -> None:
        """
        """
        ...

    @overload
    def set_noise_model(self, arg0: NoiseModel, arg1: GateType, arg2: float, arg3: List[QVec]) -> None:
        """
        """
        ...


class UpdateMode:
    """
    quantum imaginary time evolution update mode
    
    Members:
    
      GD_VALUE
    
      GD_DIRECTION
    """
    __doc__: ClassVar[str] = ...  # read-only
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
    __doc__: ClassVar[str] = ...  # read-only
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
    __doc__: ClassVar[str] = ...  # read-only
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
    Create a BARRIER gate
    
    Args:
        qubit : measure qubit
    
    Returns:
        a BARRIER node
    
    """
    ...

@overload
def BARRIER(qubit_list: int) -> QGate:
    """
    Create a BARRIER gate
    
    Args:
        qubit : measure qubit
    
    Returns:
        a BARRIER node
    
    """
    ...

@overload
def BARRIER(qubit_list: QVec) -> QGate:
    """
    Create a BARRIER gate
    
    Args:
        qubit_list : measure qubits list
    
    Returns:
        a BARRIER node
    
    """
    ...

@overload
def BARRIER(qubit_addr_list: List[int]) -> QGate:
    """
    Create a BARRIER gate
    
    Args:
        qubit_list : measure qubits list
    
    Returns:
        a BARRIER node
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
    Create a CU gate
    
    Args:
        double : u4 gate alpha angle
        double : u4 gate beta angle
        double : u4 gate gamma angle
        double : u4 gate delta angle
        qubit : control qubit 
        qubit : target qubit
    
    Returns:
        a CU node
    
    """
    ...

@overload
def CU(alpha_angle: float, beta_angle: float, gamma_angle: float, delta_angle: float, control_qubit_list: QVec, target_qubi_list: QVec) -> QCircuit:
    """
    Create a CU gate
    
    Args:
        double : u4 gate alpha angle
        double : u4 gate beta angle
        double : u4 gate gamma angle
        double : u4 gate delta angle
        control_qubit_list : control qubit list 
        target_qubi_list : target qubit list
    
    Returns:
        a CU node
    
    """
    ...

@overload
def CU(matrix: List[complex], control_qubit: Qubit, target_qubit: Qubit) -> QGate:
    """
    Create a CU gate
    
    Args:
        matrix : CU gate matrix
        qubit : control qubit 
        qubit : target qubit
    
    Returns:
        a CU node
    
    """
    ...

@overload
def CU(matrix: List[complex], control_qubit_list: QVec, target_qubit_list: QVec) -> QCircuit:
    """
    Create a CU gate
    
    Args:
        matrix : CU gate matrix
        control_qubit_list : control qubit list 
        target_qubi_list : target qubit list
    
    Returns:
        a CU node
    
    """
    ...

@overload
def CU(control_qubit: Qubit, target_qubit: Qubit, alpha_angle: float, beta_angle: float, gamma_angle: float, delta_angle: float) -> QGate:
    """
    Create a CU gate
    
    Args:
        double : u4 gate alpha angle
        double : u4 gate beta angle
        double : u4 gate gamma angle
        double : u4 gate delta angle
        qubit : control qubit 
        qubit : target qubit
    
    Returns:
        a CU node
    
    """
    ...

@overload
def CU(control_qubit_list: QVec, target_qubit_list: QVec, alpha_angle: float, beta_angle: float, gamma_angle: float, delta_angle: float) -> QCircuit:
    """
    Create a CU gate
    
    Args:
        double : u4 gate alpha angle
        double : u4 gate beta angle
        double : u4 gate gamma angle
        double : u4 gate delta angle
        control_qubit_list : control qubit list 
        target_qubi_list : target qubit list
    
    Returns:
        a CU node
    
    """
    ...

@overload
def CU(control_qubit_addr: int, target_qubit_addr: int, alpha_angle: float, beta_angle: float, gamma_angle: float, delta_angle: float) -> QGate:
    """
    Create a CU gate
    
    Args:
        double : u4 gate alpha angle
        double : u4 gate beta angle
        double : u4 gate gamma angle
        double : u4 gate delta angle
        qubit addr: control qubit addr
        qubit addr: target qubit addr
    
    Returns:
        a CU node
    
    """
    ...

@overload
def CU(control_qubit_addr_list: List[int], target_qubit_addr_list: List[int], alpha_angle: float, beta_angle: float, gamma_angle: float, delta_angle: float) -> QCircuit:
    """
    Create a CU gate
    
    Args:
        double : u4 gate alpha angle
        double : u4 gate beta angle
        double : u4 gate gamma angle
        double : u4 gate delta angle
        qubit addr list: control qubit addr list
        qubit addr list: target qubit addr list
    
    Returns:
        a CU node
    
    """
    ...

@overload
def CU(control_qubit: Qubit, target_qubit: Qubit, matrix: List[complex]) -> QGate:
    """
    Create a CU gate
    
    Args:
        matrix : CU gate matrix
        qubit : control qubit 
        qubit : target qubit
    
    Returns:
        a CU node
    
    """
    ...

@overload
def CU(control_qubit_list: QVec, target_qubit_list: QVec, matrix: List[complex]) -> QCircuit:
    """
    Create a CU gate
    
    Args:
        matrix : CU gate matrix
        qubit list: control qubit list
        qubit list: target qubit list
    
    Returns:
        a CU node
    
    """
    ...

@overload
def CU(control_qubit_addr: int, target_qubit_addr: int, matrix: List[complex]) -> QGate:
    """
    Create a CU gate
    
    Args:
        matrix : CU gate matrix
        qubit addr: control qubit addr
        qubit addr: target qubit addr
    
    Returns:
        a CU node
    
    """
    ...

@overload
def CU(control_qubit_addr_list: List[int], target_qubit_addr_list: List[int], matrix: List[complex]) -> QCircuit:
    """
    Create a CU gate
    
    Args:
        matrix : CU gate matrix
        qubit addr list: control qubit addr list
        qubit addr list: target qubit addr list
    
    Returns:
        a CU node
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
    Create an empty QCircuit Container
    
    Args:
        none
    
    Returns:
        a empty QCircuit
    """
    ...

def CreateEmptyQProg() -> QProg:
    """
    Create an empty QProg Container
    
    Args:
        none
    
    Returns:
        a empty QProg
    """
    ...

@overload
def CreateIfProg(classical_condition: ClassicalCondition, true_node: QProg) -> QIfProg:
    """
    Create a classical quantum IfProg
    
    Args:
        classical_condition: quatum cbit
        true_node: quantum IfProg qnode
    
    Returns:
        a classical quantum IfProg
    
    """
    ...

@overload
def CreateIfProg(classical_condition: ClassicalCondition, true_node: QProg, false_node: QProg) -> QIfProg:
    """
    Create a classical quantum IfProg
    
    Args:
        classical_condition: quatum cbit
        true_node: quantum IfProg true qnode
        false_node: quantum IfProg false qnode
    
    Returns:
        a classical quantum IfProg
    """
    ...

def CreateWhileProg(classical_condition: ClassicalCondition, true_node: QProg) -> QWhileProg:
    """
    Create a WhileProg
    Args:
        classical_condition: quatum cbit
        true_node: quantum QWhile qnode
    
    Returns:
        a WhileProg
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
    Create an measure node
    
    Args:
        qubit : measure qubit
        cbit : cbit stores quantum measure result
    
    Returns:
        a quantum measure node
    
    """
    ...

@overload
def Measure(qubit: Qubit, cbit: CBit) -> QMeasure:
    """
    Create an measure node
    
    Args:
        qubit : measure qubit
        cbit : cbit stores quantum measure result
    
    Returns:
        a quantum measure node
    
    """
    ...

@overload
def Measure(qubit_addr: int, cbit_addr: int) -> QMeasure:
    """
    Create an measure node
    
    Args:
        qubit : measure qubit
        cbit : cbit stores quantum measure result
    
    Returns:
        a quantum measure node
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
    Deprecated, use pmeasure instead
    
    Args:
       QVec : pmeasure qubits list
       select_num : result select num
    Returns:
        result: pmeasure qubits result
    Raises:
        run_fail: An error occurred in pmeasure
    
    """
    ...

def PMeasure_no_index(arg0: QVec) -> List[float]:
    """
    Deprecated, use pmeasure_no_index instead
    
    Args:
       QVec : pmeasure qubits list
    Returns:
        result: pmeasure qubits result
    Raises:
        run_fail: An error occurred in pmeasure_no_index
    
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
    Generate QOracle Gate
    
    Args:    qubit_list: gate in qubit list
        matrix: gate operator matrix
    
    Return:
        Oracle gate
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
    Create a Reset node
    
    """
    ...

@overload
def Reset(qubit_addr: int) -> QReset:
    """
    Create a Reset node
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
    Create a Toffoli gate
    
    """
    ...

@overload
def Toffoli(control_qubit_addr_first: int, control_qubit_addr_second: int, target_qubit_addr: int) -> QGate:
    """
    Create a Toffoli gate
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
    Create a U4 gate
    
    Args:
        matrix : U4 gate matrix
        qubit : U4 gate target qubit
    
    Returns:
        a U4 node
    
    """
    ...

@overload
def U4(alpha_angle: float, beta_angle: float, gamma_angle: float, delta_angle: float, qubit: Qubit) -> QGate:
    """
    Create a U4 gate
    
    Args:
        double : u4 gate alpha angle
        double : u4 gate beta angle
        double : u4 gate gamma angle
        double : u4 gate delta angle
        qubit : U4 gate target qubit
    
    Returns:
        a U4 node
    
    """
    ...

@overload
def U4(qubit: Qubit, matrix: List[complex]) -> QGate:
    """
    Create a U4 gate
    
    Args:
        matrix : U4 gate matrix
        qubit : U4 gate target qubit
    
    Returns:
        a U4 node
    
    """
    ...

@overload
def U4(qubit_list: QVec, matrix: List[complex]) -> QCircuit:
    """
    Create a U4 gate
    
    Args:
        matrix : U4 gate matrix
        qubit_list : U4 gate target qubit_list
    
    Returns:
        a U4 node
    
    """
    ...

@overload
def U4(qubit_addr: int, matrix: List[complex]) -> QGate:
    """
    Create a U4 gate
    
    Args:
        matrix : U4 gate matrix
        qubit : U4 gate target qubit
    
    Returns:
        a U4 node
    
    """
    ...

@overload
def U4(qubit_addr_list: List[int], matrix: List[complex]) -> QCircuit:
    """
    Create a U4 gate
    
    Args:
        matrix : U4 gate matrix
        qubit_list : U4 gate target qubit_list
    
    Returns:
        a U4 node
    
    """
    ...

@overload
def U4(qubit: Qubit, alpha_anlge: float, beta_anlge: float, gamma_anlge: float, delta_anlge: float) -> QGate:
    """
    Create a U4 gate
    
    Args:
        double : u4 gate alpha angle
        double : u4 gate beta angle
        double : u4 gate gamma angle
        double : u4 gate delta angle
        qubit : U4 gate target qubit
    
    Returns:
        a U4 node
    
    """
    ...

@overload
def U4(qubit_list: QVec, alpha_angle: float, beta_angle: float, gamma_angle: float, delta_angle: float) -> QCircuit:
    """
    Create a U4 gate
    
    Args:
        double : u4 gate alpha angle
        double : u4 gate beta angle
        double : u4 gate gamma angle
        double : u4 gate delta angle
        qubit_list : U4 gate target qubit_list
    
    Returns:
        a U4 node
    
    """
    ...

@overload
def U4(qubit_addr: int, alpha_anlge: float, beta_anlge: float, gamma_anlge: float, delta_anlge: float) -> QGate:
    """
    Create a U4 gate
    
    Args:
        double : u4 gate alpha angle
        double : u4 gate beta angle
        double : u4 gate gamma angle
        double : u4 gate delta angle
        qubit : U4 gate target qubit
    
    Returns:
        a U4 node
    
    """
    ...

@overload
def U4(qubit_addr_list: List[int], alpha_anlge: float, beta_anlge: float, gamma_anlge: float, delta_anlge: float) -> QCircuit:
    """
    Create a U4 gate
    
    Args:
        double : u4 gate alpha angle
        double : u4 gate beta angle
        double : u4 gate gamma angle
        double : u4 gate delta angle
        qubit_addr_list : U4 gate target qubit_addr_list
    
    Returns:
        a U4 node
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
    Accumulate the probability from a prob list
    
    Args:
        probability_list: measured result in probability list form
    
    Returns:
        accumulated resultRaises:
        run_fail: An error occurred in accumulateProbability
    
    """
    ...

def accumulate_probabilities(probability_list: List[float]) -> List[float]:
    """
    Accumulate the probability from a prob list
    
    Args:
        probability_list: measured result in probability list form
    
    Returns:
        accumulated resultRaises:
        run_fail: An error occurred in accumulate_probabilities
    
    """
    ...

def accumulate_probability(probability_list: List[float]) -> List[float]:
    """
    Accumulate the probability from a prob list
    
    Args:
        probability_list: measured result in probability list form
    
    Returns:
        accumulated resultRaises:
        run_fail: An error occurred in accumulate_probability
    
    """
    ...

def acos(arg0: var) -> var:
    """
    """
    ...

@overload
def add(arg0: ClassicalCondition, arg1: ClassicalCondition) -> ClassicalCondition:
    """
    """
    ...

@overload
def add(arg0: ClassicalCondition, arg1: int) -> ClassicalCondition:
    """
    """
    ...

@overload
def add(arg0: int, arg1: ClassicalCondition) -> ClassicalCondition:
    """
    """
    ...

def all_cut_of_graph(adjacent_matrix: List[List[float]], all_cut_list: List[float], target_value_list: List[int]) -> float:
    """
    Generate graph of maxcut problem
    
    Args:
        adjacent_matrix: adjacent_matrix for quantum prog 
        all_cut_list: all cut graph list in quantum prog 
        target_value_list: target cut value list 
    
    Returns:
        max value
    Raises:
        run_fail: An error occurred in all_cut_of_graph
    
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
    Apply QGate to qubits
    
    Args:
        qubit_list: qubit list
        func_obj: QGate(Qubit) like function object accept Qubit as argument
    
    Returns:
        QCircuit contain QGate operation on all qubit
    
    """
    ...

@overload
def apply_QGate(qubit_addr_list: List[int], func_obj: Callable[[int],QGate]) -> QCircuit:
    """
    Apply QGate to qubits
    
    Args:
        qubit_addr_list: qubit address list
        func_obj: QGate(int) like function object accept Qubit address as argument
    
    Returns:
        QCircuit contain QGate operation on all qubit
    """
    ...

def asin(arg0: var) -> var:
    """
    """
    ...

@overload
def assign(arg0: ClassicalCondition, arg1: ClassicalCondition) -> ClassicalCondition:
    """
    """
    ...

@overload
def assign(arg0: ClassicalCondition, arg1: int) -> ClassicalCondition:
    """
    """
    ...

def atan(arg0: var) -> var:
    """
    """
    ...

@overload
def average_gate_fidelity(state1: numpy.ndarray[numpy.complex128[m,n]], state2: List[complex]) -> float:
    """
    compare two quantum states , Get the state fidelity
    
    Args:
        state1: quantum state matrix 1
        state2: quantum state list 2
    
    Returns:
        state fidelity bewteen [0,1]
    
    """
    ...

@overload
def average_gate_fidelity(state1: numpy.ndarray[numpy.complex128[m,n]], state2: numpy.ndarray[numpy.complex128[m,n]]) -> float:
    """
    compare two quantum states , Get the state fidelity
    
    Args:
        state1: quantum state matrix 1
        state2: quantum state list 2
    
    Returns:
        state fidelity bewteen [0,1]
    """
    ...

def bin_to_prog(bin_data: List[int], qubit_list: QVec, cbit_list: List[ClassicalCondition], qprog: QProg) -> bool:
    """
    Parse binary data transfor to quantum program
    Args:
        bin_data: binary data stores quantum prog information
        qubit_list: quantum qubits list 
        cbit_list: quantum cbits list
        qprog: quantum prog
    
    Returns:
        prog
    
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
        cbit_addr: cbit address, should in [0,29)
    Returns:
        classic result cbit
    """
    ...

def cAlloc_many(cbit_num: int) -> List[ClassicalCondition]:
    """
    Allocate several CBits
    After init()
    
    Args:
        cbit_num: numbers of cbit want to be created
    
    Returns:
        list of cbit
    """
    ...

def cFree(cbit: ClassicalCondition) -> None:
    """
    Free a CBit
    
    Args:
        CBit: a CBit
    
    Returns:
        none
    
    """
    ...

@overload
def cFree_all() -> None:
    """
    Free all cbits
    
    Args:
        none
    
    Returns:
        none
    
    
    """
    ...

@overload
def cFree_all(cbit_list: List[ClassicalCondition]) -> None:
    """
    Free all cbits
    
    Args:
        a list of cbits
    
    Returns:
        none
    
    """
    ...

@overload
def calculate_quantum_volume(noise_qvm: NoiseQVM, qubit_list: List[List[int]], ntrials: int, shots: int = 1000) -> int:
    """
    calculate quantum volume
    
    Args:
        noise_qvm: noise quantum machine
        qubit_list: qubit list 
        ntrials: ntrials
        shots: measure shots
    
    Returns:
        result data dict
    Raises:
        run_fail: An error occurred in calculate_quantum_volume
    
    
    """
    ...

@overload
def calculate_quantum_volume(cloud_qvm, qubit_list: List[List[int]], ntrials: int, shots: int = 1000) -> int:
    """
    calculate quantum volume
    
    Args:
        noise_qvm: noise quantum machine
        qubit_list: qubit list 
        ntrials: ntrials
        shots: measure shots
    
    Returns:
        result data dict
    Raises:
        run_fail: An error occurred in calculate_quantum_volume
    
    
    """
    ...

@overload
def calculate_quantum_volume(config: QCloudTaskConfig, qubit_list: List[List[int]], ntrials: int) -> int:
    """
    calculate quantum volume
    
    Args:
        config: QCloudTaskConfig
        qubit_list: qubit list 
        ntrials: ntrials
    
    Returns:
        result data dict
    Raises:
        run_fail: An error occurred in calculate_quantum_volume
    
    """
    ...

def cast_qprog_qcircuit(qprog: QProg) -> QCircuit:
    """
    Cast QProg to QCircuit
    
    Args:
        qprog: quantum prog 
    
    Returns:
        none
    Raises:
        run_fail: An error occurred in cast_qprog_qcircuit
    
    """
    ...

def cast_qprog_qgate(qprog: QProg) -> QGate:
    """
    Cast QProg to QGate
    
    Args:
        qprog: quantum prog 
    
    Returns:
        none
    Raises:
        run_fail: An error occurred in cast_qprog_qgate
    
    """
    ...

def cast_qprog_qmeasure(qprog: QProg) -> QMeasure:
    """
    Cast QProg to QMeasure
    
    Args:
        qprog: quantum prog 
    
    Returns:
        none
    Raises:
        run_fail: An error occurred in cast_qprog_qmeasure
    
    """
    ...

def circuit_layer(qprog: QProg) -> list:
    """
    Quantum circuit layering
    
    Args:
        QProg: quantum prog 
    
    Returns:
        result data tuple contains layer info
    Raises:
        run_fail: An error occurred in get circuit_layer
    
    """
    ...

def circuit_optimizer(qprog: QProg, optimizer_cir_vec: List[Tuple[QCircuit,QCircuit]] = [], mode_list: List[QCircuitOPtimizerMode] = []) -> QProg:
    """
    Optimize QCircuit
    
    Args:
        qprog: quantum program
        optimizer_cir_vec: quantum circuit list 
        mode_list: optimize mode list
    
    Returns:
        a new prog after optimize
    """
    ...

def circuit_optimizer_by_config(qprog: QProg, config_file: str = 'QPandaConfig.json', mode_list: List[QCircuitOPtimizerMode] = []) -> QProg:
    """
    QCircuit optimizer
    
    Args:
        qprog: quantum program
        config_file: optimize config 
        mode_list: optimize mode list
    
    Returns:
        a new prog after optimize
    """
    ...

def comm_protocol_decode(encode_data: bytes, machine: QuantumMachine) -> Tuple[List[QProg],CommProtocolConfig]:
    """
    decode binary data to comm protocol prog list
    
    Args:
        encode_data: quantum prog_list encode data
    
    Returns:
        result prog list
    Raises:
        run_fail: An error occurred in comm_protocol_decode
    
    """
    ...

@overload
def comm_protocol_encode(prog: QProg, config: CommProtocolConfig = ...) -> bytes:
    """
    encode comm protocol data to binary data
    
    Args:
        prog: quantum prog
        config: comm_protocol config
    
    Returns:
        result data list
    Raises:
        run_fail: An error occurred in comm_protocol_encode
    
    
    """
    ...

@overload
def comm_protocol_encode(prog_list: List[QProg], config: CommProtocolConfig = ...) -> bytes:
    """
    encode comm protocol data to binary data
    
    Args:
        prog_list: quantum prog_list
        config: comm_protocol config
    
    Returns:
        result data list
    Raises:
        run_fail: An error occurred in comm_protocol_encode
    
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
    Parse  binary data to quantum program
    
    Args:
        machine: quantum machine
        data: quantum prog data
    
    Returns:
        quantum prog
    Raises:
        run_fail: An error occurred in convert_binary_data_to_qprog
    
    """
    ...

def convert_originir_str_to_qprog(originir_str: str, machine: QuantumMachine) -> list:
    """
    Trans OriginIR to QProg
    
    Args:
        originir_str: OriginIR string
        machine: initialized quantum machine
    
    Returns:
        list cotains QProg, qubit_list, cbit_listRaises:
        run_fail: An error occurred in convert_originir_str_to_qprog
    
    """
    ...

def convert_originir_to_qprog(file_path: str, machine: QuantumMachine) -> list:
    """
    Read OriginIR file and trans to QProg
    
    Args:
        file_path: OriginIR file path
        machine: initialized quantum machine
    
    Returns:
        list cotains QProg, qubit_list, cbit_listRaises:
        run_fail: An error occurred in convert_originir_to_qprog
    
    """
    ...

def convert_qasm_string_to_qprog(qasm_str: str, machine: QuantumMachine) -> list:
    """
    Trans QASM to QProg
    
    Args:
        qasm_str: QASM string
        machine: initialized quantum machine
    
    Returns:
        list cotains QProg, qubit_list, cbit_list
    """
    ...

def convert_qasm_to_qprog(file_path: str, machine: QuantumMachine) -> list:
    """
    Read QASM file and trans to QProg
    
    Args:
        file_path: QASM file path
        machine: initialized quantum machine
    
    Returns:
        list cotains QProg, qubit_list, cbit_listRaises:
        run_fail: An error occurred in convert_qasm_to_qprog
    
    """
    ...

@overload
def convert_qprog_to_binary(qprog: QProg, machine: QuantumMachine) -> List[int]:
    """
    Trans quantum program to binary data
    Args:
        machine: quantum machine
        qprog: quantum prog
    
    Returns:
        string for binary data
    
    
    """
    ...

@overload
def convert_qprog_to_binary(qprog: QProg, machine: QuantumMachine, fname: str) -> None:
    """
    Store quantum program in binary file 
    Args:
        machine: quantum machine
        qprog: quantum prog
        fname: binary data file name
    
    Returns:
        none
    
    """
    ...

def convert_qprog_to_originir(qprog: QProg, machine: QuantumMachine) -> str:
    """
    Args:
        qprog: quantum prog
        machine: quantum machine
    
    Returns:
        originir : originir string , see originir indroduction :https://pyqpanda-toturial.readthedocs.io/zh/latest/QProgToOriginIR.html
    
    """
    ...

def convert_qprog_to_qasm(qprog: QProg, machine: QuantumMachine) -> str:
    """
    Convert QProg to QASM instruction string
    
    Args:
        machine: quantum machine
        qprog: quantum prog 
    
    Returns:
        qsm string stores prog
    Raises:
        run_fail: An error occurred in convert_qprog_to_qasm
    
    """
    ...

def convert_qprog_to_quil(qprog: QProg, machine: QuantumMachine) -> str:
    """
    convert QProg to Quil instruction
    
    Args:
        qprog: QProg
        machine: quantum machine
    
    Returns:
        Quil instruction string
    """
    ...

def cos(arg0: var) -> var:
    """
    """
    ...

@overload
def count_gate(quantum_prog: QProg) -> int:
    """
    Count quantum gate num under quantum program, quantum circuit
    
    Args:
       prog : quantum_prog
    Returns:
        result: gate count
    Raises:
        run_fail: An error occurred in get_qgate_num
    
    
    """
    ...

@overload
def count_gate(quantum_circuit: QCircuit) -> int:
    """
    Count quantum gate num under quantum program, quantum circuit
    Args:
       circuit : quantum_circuit
    Returns:
        result: gate count
    Raises:
        run_fail: An error occurred in get_qgate_num
    
    """
    ...

@overload
def count_prog_info(node: QProg, selected_types: List[GateType] = []) -> ProgCount:
    """
    count quantum program info
    Args:
        qprog: QProg
        optimize: whether to enable the optimization circuit switch.
    
    Returns:
        ProgCount struct
    
    """
    ...

@overload
def count_prog_info(node: QCircuit, selected_types: List[GateType] = []) -> ProgCount:
    """
    count quantum program info
    Args:
        qprog: QProg
        optimize: whether to enable the optimization circuit switch.
    
    Returns:
        ProgCount struct
    """
    ...

@overload
def count_qgate_num(prog: QProg, gate_type: int = -1) -> int:
    """
    Count quantum gate num under quantum program
    
    Args:
        quantum_prog: QProg&
        gtype: const GateType
    
    Returns:
        this GateType quantum gate num
    
    """
    ...

@overload
def count_qgate_num(circuit: QCircuit, gate_type: int = -1) -> int:
    """
    Count quantum gate num under quantum program
    
    Args:
        quantum_circuit: QCircuit&
        gtype: const GateType
    
    Returns:
        this GateType quantum gate num
    """
    ...

def create_empty_circuit() -> QCircuit:
    """
    Create an empty QCircuit Container
    
    Args:
        none
    
    Returns:
        a empty QCircuit
    """
    ...

def create_empty_qprog() -> QProg:
    """
    Create an empty QProg Container
    
    Args:
        none
    
    Returns:
        a empty QProg
    """
    ...

@overload
def create_if_prog(classical_condition: ClassicalCondition, true_node: QProg) -> QIfProg:
    """
    Create a classical quantum IfProg
    
    Args:
        classical_condition: quatum cbit
        true_node: quantum IfProg qnode
    
    Returns:
        a classical quantum IfProg
    
    """
    ...

@overload
def create_if_prog(classical_condition: ClassicalCondition, true_node: QProg, false_node: QProg) -> QIfProg:
    """
    Create a classical quantum IfProg
    
    Args:
        classical_condition: quatum cbit
        true_node: quantum IfProg true qnode
        false_node: quantum IfProg false qnode
    
    Returns:
        a classical quantum IfProg
    """
    ...

def create_while_prog(classical_condition: ClassicalCondition, true_node: QProg) -> QWhileProg:
    """
    Create a WhileProg
    
    Args:
        classical_condition: quatum cbit
        true_node: quantum QWhile qnode
    
    Returns:
        a WhileProg
    """
    ...

def crossEntropy(arg0: var, arg1: var) -> var:
    """
    """
    ...

@overload
def decompose_multiple_control_qgate(qprog: QProg, machine: QuantumMachine, config_file: str = 'QPandaConfig.json') -> QProg:
    """
    Decompose multiple control QGate
    
    Args:
        qprog: quantum program
        machine: quantum machine
        config_file: config file
    
    Returns:
        a new prog after decomposition
    
    """
    ...

@overload
def decompose_multiple_control_qgate(qprog: QProg, machine: QuantumMachine, convert_single_gates: List[str], convert_double_gates: List[str], b_transform_to_base_qgate: bool = True) -> QProg:
    """
    Decompose multiple control QGate
    
    Args:
        qprog: quantum program
        machine: quantum machine
        convert_single_gates: quantum single gates sets
        convert_double_gates: quantum double gates sets
        transform_to_base_qgate:  transform to base qgate sets
    
    Returns:
        a new prog after decomposition
    """
    ...

@overload
def deep_copy(node: QProg) -> QProg:
    """
    """
    ...

@overload
def deep_copy(node: QCircuit) -> QCircuit:
    """
    """
    ...

@overload
def deep_copy(node: QGate) -> QGate:
    """
    """
    ...

@overload
def deep_copy(node: QMeasure) -> QMeasure:
    """
    """
    ...

@overload
def deep_copy(node: ClassicalProg) -> ClassicalProg:
    """
    """
    ...

@overload
def deep_copy(node: QIfProg) -> QIfProg:
    """
    """
    ...

@overload
def deep_copy(node: QWhileProg) -> QWhileProg:
    """
    """
    ...

def del_weak_edge(topo_data: List[List[int]]) -> None:
    """
    Delete weakly connected edges
    
    Args:
        topo_data: quantum program topo_data
    
    Returns:
        none
    Raises:
        run_fail: An error occurred in del_weak_edge
    
    """
    ...

def del_weak_edge2(topo_data: List[List[int]], max_connect_degree: int, sub_graph_set: List[int]) -> list:
    """
    Delete weakly connected edges
    
    Args:
        topo_data: quantum program topo_data
        max_connect_degree: max value of connect degree
        sub_graph_set: sub graph set list
    
    Returns:
        result data 
    Raises:
        run_fail: An error occurred in del_weak_edge2
    
    """
    ...

def del_weak_edge3(topo_data: List[List[int]], sub_graph_set: List[int], max_connect_degree: int, lamda1: float, lamda2: float, lamda3: float) -> list:
    """
    Delete weakly connected edges
    
    Args:
        topo_data: quantum program topo_data
        max_connect_degree: max value of connect degree
        sub_graph_set: sub graph set list
        lamda1: lamda1
        lamda2: lamda2
        lamda3: lamda3
    
    Returns:
        result data 
    Raises:
        run_fail: An error occurred in del_weak_edge3
    
    """
    ...

def destroy_quantum_machine(machine: QuantumMachine) -> None:
    """
    Destroy a quantum machine
    
    Args:
        machine: type should be one of CPUQVM, CPUSingleThreadQVM, GPUQVM, NoiseQVM
    Returns:
        noneRaises:
        run_fail: An error occurred in destroy_quantum_machine
    
    """
    ...

def directly_run(qprog: QProg, noise_model: Noise = NoiseModel()) -> Dict[str,bool]:
    """
    Directly run quantum prog
    After init()
    
    Args:
        qprog: quantum program
        noise_model: noise model, default is no noise. noise model only work on CPUQVM now
    
    Returns:
        Dict[str, bool]: result of quantum program execution one shot.
                         first is the final qubit register state, second is it's measure probability
    """
    ...

@overload
def div(arg0: ClassicalCondition, arg1: ClassicalCondition) -> ClassicalCondition:
    """
    """
    ...

@overload
def div(arg0: ClassicalCondition, arg1: int) -> ClassicalCondition:
    """
    """
    ...

@overload
def div(arg0: int, arg1: ClassicalCondition) -> ClassicalCondition:
    """
    """
    ...

def dot(arg0: var, arg1: var) -> var:
    """
    """
    ...

@overload
def double_gate_xeb(config: QCloudTaskConfig, qubit0: int, qubit1: int, clifford_range: List[int], num_circuits: int, gate_type: GateType = GateType.CZ_GATE) -> Dict[int,float]:
    """
    double gate xeb
    
    Args:
        qvm: quantum machine
        qubit0: double qubit 0
        qubit1: double qubit 1
        clifford_range: clifford range list
        num_circuits: the num of circuits
        interleaved_gates: interleaved gates list
    
    Returns:
        result data dict
    Raises:
        run_fail: An error occurred in double_gate_xeb
    
    
    """
    ...

@overload
def double_gate_xeb(qvm: QuantumMachine, qubit0: Qubit, qubit1: Qubit, clifford_range: List[int], num_circuits: int, shots: int, chip_id: int = 2, gate_type: GateType = GateType.CZ_GATE) -> Dict[int,float]:
    """
    double gate xeb
    
    Args:
        qvm: quantum machine
        qubit0: double qubit 0
        qubit1: double qubit 1
        clifford_range: clifford range list
        num_circuits: the num of circuits
        shots: measure shots
        chip type: RealChipType
        interleaved_gates: interleaved gates list
    
    Returns:
        result data dict
    Raises:
        run_fail: An error occurred in double_gate_xeb
    
    """
    ...

@overload
def double_qubit_rb(qvm: QuantumMachine, qubit0: Qubit, qubit1: Qubit, clifford_range: List[int], num_circuits: int, shots: int, chip_id: int = 2, interleaved_gates: List[QGate] = []) -> Dict[int,float]:
    """
    double qubit rb with WU YUAN chip
    Args:
        qvm: quantum machine
        qubit0: double qubit 0
        qubit1: double qubit 1
        clifford_range: clifford range list
        num_circuits: the num of circuits
        shots: measure shots
        chip type: RealChipType
        interleaved_gates: interleaved gates list
    
    Returns:
        result data dict
    Raises:
        run_fail: An error occurred in double_qubit_rb
    
    
    """
    ...

@overload
def double_qubit_rb(config: QCloudTaskConfig, qubit0: int, qubit1: int, clifford_range: List[int], num_circuits: int, interleaved_gates: List[QGate] = []) -> Dict[int,float]:
    """
    double qubit rb with origin chip
    Args:
        config: QCloudTaskConfig
        qubit0: double qubit 0
        qubit1: double qubit 1
        clifford_range: clifford range list
        num_circuits: the num of circuits
        interleaved_gates: interleaved gates list
    
    Returns:
        result data dict
    Raises:
        run_fail: An error occurred in double_qubit_rb
    
    """
    ...

def draw_qprog_latex(prog: QProg, auto_wrap_len: int = 100, output_file: str = 'QCircuit.tex', with_logo: bool = False, itr_start: NodeIter = NodeIter(), itr_end: NodeIter = NodeIter()) -> str:
    """
    Convert a quantum prog/circuit to latex source code, and save the source code to file in current path with name QCircuit.tex
    Args:
        QProg: quantum prog 
        auto_wrap_len: defaut is 100 
        output_file: result output file name 
        itr_start: nodeiter start 
        itr_end: nodeiter end 
    
    Returns:
        result data tuple contains prog info
    Raises:
        run_fail: An error occurred in get draw_qprog_text
    
    """
    ...

def draw_qprog_latex_with_clock(prog: QProg, config_data: str = 'QPandaConfig.json', auto_wrap_len: bool = 100, output_file: int = 'QCircuit.tex', with_logo: str = False, itr_start: NodeIter = NodeIter(), itr_end: NodeIter = NodeIter()) -> str:
    """
    Convert a quantum prog/circuit to latex source code with time sequence, and save the source code to file in current path with name QCircuit.tex
    Args:
        QProg: quantum prog 
        config_data: default config file is QPandaConfig.json 
        auto_wrap_len: defaut is 100 
        output_file: result output file name 
        itr_start: nodeiter start 
        itr_end: nodeiter end 
    
    Returns:
        result data tuple contains prog info
    Raises:
        run_fail: An error occurred in get draw_qprog_text
    
    """
    ...

def draw_qprog_text(qprog: QProg, auto_wrap_len: int = 100, output_file: str = 'QCircuitTextPic.txt', itr_start: NodeIter = NodeIter(), itr_end: NodeIter = NodeIter()) -> str:
    """
    Convert a quantum prog/circuit to text-pic(UTF-8 code),
    and will save the text-pic in file named QCircuitTextPic.txt in the same time in current path
    Args:
        QProg: quantum prog 
        auto_wrap_len: defaut is 100 
        output_file: result output file name 
        itr_start: nodeiter start 
        itr_end: nodeiter end 
    
    Returns:
        result data tuple contains prog info
    Raises:
        run_fail: An error occurred in get draw_qprog_text
    
    """
    ...

def draw_qprog_text_with_clock(prog: QProg, config_data: str = 'QPandaConfig.json', auto_wrap_len: int = 100, output_file: str = 'QCircuitTextPic.txt', itr_start: NodeIter = NodeIter(), itr_end: NodeIter = NodeIter()) -> str:
    """
    Convert a quantum prog/circuit to text-pic(UTF-8 code) with time sequence,
    and will save the text-pic in file named QCircuitTextPic.txt in the same time in current path
    Args:
        QProg: quantum prog 
        auto_wrap_len: defaut is 100 
        output_file: result output file name 
        itr_start: nodeiter start 
        itr_end: nodeiter end 
    
    Returns:
        result data tuple contains prog info
    Raises:
        run_fail: An error occurred in get draw_qprog_text
    
    """
    ...

def dropout(arg0: var, arg1: var) -> var:
    """
    """
    ...

@overload
def equal(arg0: ClassicalCondition, arg1: ClassicalCondition) -> ClassicalCondition:
    """
    """
    ...

@overload
def equal(arg0: ClassicalCondition, arg1: int) -> ClassicalCondition:
    """
    """
    ...

@overload
def equal(arg0: int, arg1: ClassicalCondition) -> ClassicalCondition:
    """
    """
    ...

def estimate_topology(topo_data: List[List[int]]) -> float:
    """
    Evaluate topology performance
    
    Args:
        topo_data: quantum program topo data
    
    Returns:
        result data 
    Raises:
        run_fail: An error occurred in estimate_topology
    
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
    calculate the matrix power of e
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
    Fill the input QProg by I gate, return a new quantum program
    
    Args:
        prog: quantum prog 
    
    Returns:
        a new quantum program
    Raises:
        run_fail: An error occurred in get fill_qprog_by_I
    
    """
    ...

def finalize() -> None:
    """
    Finalize the environment and destory global unique quantum machine.
    
    Args:
        none
    
    Returns:
        none
    """
    ...

def fit_to_gbk(utf8_str: str) -> str:
    """
    Special character conversion
    
    Args:
        utf8_str: string using utf-8 encode 
    
    Returns:
        result string
    Raises:
        run_fail: An error occurred in get fit_to_gbk
    
    """
    ...

@overload
def flatten(qprog: QProg) -> None:
    """
    Flatten quantum program
    
    Args:
        qprog: quantum prog
    
    Returns:
        none
    
    
    """
    ...

@overload
def flatten(qcircuit: QCircuit) -> None:
    """
    Flatten quantum circuit
    
    Args:
        qprog: quantum circuit
    
    Returns:
        none
    
    """
    ...

def getAllocateCMem() -> int:
    """
    Deprecated, use get_allocate_cmem_num instead
    Args:
       none
    Returns:
        allocate qubit num
    Raises:
        run_fail: An error occurred in get_allocate_cmem_num
    
    """
    ...

def getAllocateQubitNum() -> int:
    """
    Deprecated, use get_allocate_qubit_num instead
    Args:
       none
    Returns:
        allocate cbit num
    Raises:
        run_fail: An error occurred in get_allocate_qubit_num
    
    """
    ...

def get_adjacent_qgate_type(qprog: QProg, node_iter: NodeIter) -> List[NodeInfo]:
    """
    Get the adjacent quantum gates's(the front one and the back one) typeinfo from QProg
    
    Args:
        qprog: target quantum program
        node_iter:  gate node iter in qprog
    
    Returns:
        the front one and back node info of node_iter in qprog
    """
    ...

def get_all_used_qubits(qprog: QProg) -> QVec:
    """
    Get all the used quantum bits in the input prog
    Args:
        qprog: quantum program
    
    Returns:
        all used qubits
    """
    ...

def get_all_used_qubits_to_int(qprog: QProg) -> List[int]:
    """
    Get all the used quantum bits addr in the input prog
    Args:
        qprog: quantum program
    
    Returns:
        all used qubits
    """
    ...

def get_allocate_cbits() -> List[ClassicalCondition]:
    """
    Get allocated cbits of QuantumMachine
    
    Args:
        none
    
    Returns:
        cbit list
    
    Raises:
        run_fail: An error occurred in allocated cbits of QuantumMachine
    
    """
    ...

def get_allocate_cmem_num() -> int:
    """
    get allocate cmem num
    Args:
       none
    Returns:
        qubit_num : allocate cbit num
    Raises:
        run_fail: An error occurred in get_allocate_cmem_num
    
    """
    ...

def get_allocate_qubit_num() -> int:
    """
    get allocate qubit num
    
    Args:
       none
    Returns:
        qubit_num : allocate qubit num
    Raises:
        run_fail: An error occurred in get_allocate_qubit_num
    
    """
    ...

def get_allocate_qubits() -> QVec:
    """
    Get allocated qubits of QuantumMachine
    
    Args:
        none
    
    Returns:
        qubit list
    
    Raises:
        run_fail: An error occurred in allocated qubits of QuantumMachine
    
    """
    ...

def get_bin_data(qprog: QProg) -> List[int]:
    """
    Get quantum program binary data
    
    Args:
        qprog: QProg
        machine: quantum machine
    
    Returns:
        binary data in list
    """
    ...

def get_bin_str(qprog: QProg, machine: QuantumMachine) -> str:
    """
    Transfor quantum program to string
    Args:
        machine: quantum machine
        qprog: quantum prog
    
    Returns:
        string for bin_str
    
    """
    ...

def get_circuit_optimal_topology(qprog: QProg, machine: QuantumMachine, max_connect_degree: int, config_file: str = 'QPandaConfig.json') -> List[List[int]]:
    """
    Get the optimal topology of the input circuit
    
    Args:
        qprog: quantum program
        machine: quantum machine
        max_connect_degree: max value of connect degree
        config_file: config file
    
    Returns:
        Topology prog DataRaises:
        run_fail: An error occurred in get_circuit_optimal_topology
    
    """
    ...

def get_clock_cycle(qpog: QProg) -> int:
    """
    Get quantum program clock cycle
    Args:
        qprog: QProg
    
    Returns:
        clock_cycle
    """
    ...

def get_complex_points(topo_data: List[List[int]], max_connect_degree: int) -> List[int]:
    """
    Get complex points
    
    Args:
        topo_data: quantum program topo_data
        max_connect_degree: max value of connect degree
    
    Returns:
        complex points list 
    Raises:
        run_fail: An error occurred in get_complex_points
    
    """
    ...

def get_double_gate_block_topology(qprog: QProg) -> List[List[int]]:
    """
    get double gate block topology
    
    Args:
        qprog: quantum program
    
    Returns:
        Topology prog DataRaises:
        run_fail: An error occurred in get_double_gate_block_topology
    
    """
    ...

def get_matrix(qprog: QProg, positive_seq: bool = False, nodeitr_start: NodeIter = NodeIter(), nodeitr_end: NodeIter = NodeIter()) -> List[complex]:
    """
    Get the target matrix between the input two Nodeiters
    
    Args:
        qprog: quantum program
        positive_seq: Qubit order of output matrix
                      true for positive sequence(q0q1q2), false for inverted order(q2q1q0), default is false
        nodeiter_start: the start NodeIter
        nodeiter_end: the end NodeIter
    
    Returns:
        target matrix include all the QGate's matrix (multiply)
    """
    ...

def get_prob_dict(qubit_list: QVec, select_max: int = -1) -> Dict[str,float]:
    """
    Get pmeasure result as dict
    
    Args:
        qubit_list: pmeasure qubits list
        select_max: max returned element num in returnd tuple, should in [-1, 1<<len(qubit_list)]
                    default is -1, means no limit
    Returns:
        measure result of quantum machine
    Raises:
        run_fail: An error occurred in get_prob_dict
    
    """
    ...

def get_prob_list(qubit_list: QVec, select_max: int = -1) -> List[float]:
    """
    Get pmeasure result as list
    
    Args:
        qubit_list: pmeasure qubits list
        select_max: max returned element num in returnd tuple, should in [-1, 1<<len(qubit_list)]
                    default is -1, means no limit
    Returns:
        measure result of quantum machine
    Raises:
        run_fail: An error occurred in get_prob_list
    
    """
    ...

@overload
def get_qgate_num(quantum_prog: QProg) -> int:
    """
    Count quantum gate num under quantum program, quantum circuit
    Args:
       prog : quantum_prog
    Returns:
        result: gate count
    Raises:
        run_fail: An error occurred in get_qgate_num
    
    
    """
    ...

@overload
def get_qgate_num(quantum_circuit: QCircuit) -> int:
    """
    Count quantum gate num under quantum program, quantum circuit
    
    Args:
       circuit : quantum_circuit
    Returns:
        result: gate count
    Raises:
        run_fail: An error occurred in get_qgate_num
    
    
    """
    ...

@overload
def get_qgate_num(qprog: QProg) -> int:
    """
    Count quantum gate num under quantum program
    
    Args:
        qprog: quantum prog
    
    Returns:
        quantum gate num under quantum program
    
    """
    ...

def get_qprog_clock_cycle(qprog: QProg, machine: QuantumMachine, optimize: bool = False) -> int:
    """
    Get Quantum Program Clock Cycle
    
    Args:
        qprog: quantum program
        machine: quantum machine
        optimize: optimize qprog
    
    Returns:
        QProg time comsume, no unit, not in seconds
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
    Get sub graph
    
    Args:
        topo_data: quantum program topo data
    
    Returns:
        sub graph 
    Raises:
        run_fail: An error occurred in sub graph
    
    """
    ...

def get_tuple_list(qubit_list: QVec, select_max: int = -1) -> List[Tuple[int,float]]:
    """
    Get pmeasure result as tuple list
    
    Args:
        qubit_list: pmeasure qubits list
        select_max: max returned element num in returnd tuple, should in [-1, 1<<len(qubit_list)]
                    default is -1, means no limit
    Returns:
        measure result of quantum machine
    Raises:
        run_fail: An error occurred in get_tuple_list
    
    """
    ...

def get_unitary(qprog: QProg, positive_seq: bool = False, nodeitr_start: NodeIter = NodeIter(), nodeitr_end: NodeIter = NodeIter()) -> List[complex]:
    """
    Get the target matrix between the input two Nodeiters
    
    Args:
        qprog: quantum program
        positive_seq: Qubit order of output matrix
                      true for positive sequence(q0q1q2), false for inverted order(q2q1q0), default is false
        nodeiter_start: the start NodeIter
        nodeiter_end: the end NodeIter
    
    Returns:
        target matrix include all the QGate's matrix (multiply)
    """
    ...

def get_unsupport_qgate_num(qprog: QProg, support_gates: List[List[str]]) -> int:
    """
    Count quantum program unsupported gate numner
    
    Args:
        qprog: quantum prog
        support_gates: support_gates
    
    Returns:
        unsupported gate numner
    
    """
    ...

def getstat(*args, **kwargs) -> Any:
    """
    Get the status of the Quantum machine
    
    Args:
        none
    
    Returns:
        the status of the Quantum machine, see QMachineStatus
    
    Raises:
        init_fail: An error occurred
    
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
        bool: ture if initialization success
    """
    ...

def init_quantum_machine(machine_type: QMachineType = QMachineType.CPU) -> QuantumMachine:
    """
    Create and initialize a new quantum machine, and let it be global unique quantum machine
    
    Args:
        machine_type: quantum machine type, see pyQPanda.QMachineType
    
    Returns:
        the quantum machine, type is depend on machine_type
        QMachineType.CPU               --> pyQPanda.CPUQVM
        QMachineType.CPU_SINGLE_THREAD --> pyQPanda.CPUSingleThreadQVM
        QMachineType.GPU               --> pyQPanda.GPUQVM (if pyQPanda is build with GPU)
        QMachineType.NOISE             --> pyQPanda.NoiseQVM
        return None if initial machine faild
    Raises:
        init_fail: An error occurred in init_quantum_machine
    
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
    Judge the QGate if match the target topologic structure of quantum circuit
    
    Args:
        gate: QGate
        topo: the target topologic structure of quantum circuit
    
    Returns:
        true if match, else false
    """
    ...

def is_supported_qgate_type(nodeitr: NodeIter) -> bool:
    """
    Judge if the target node is a QGate type
    
    Args:
        node_iter:  node iter  in qprog
    
    Returns:
        true ir false if the target node is a QGate type
    """
    ...

def is_swappable(prog: QProg, nodeitr_1: NodeIter, nodeitr_2: NodeIter) -> bool:
    """
    Judge the specialed two NodeIters in qprog whether can be exchanged
    
    Args:
        qprog: target quantum program
        node_iter1:  node iter 1 in qprog
        node_iter2:  node iter 2 in qprog
    
    Returns:
        true ir false for two NodeIters in qprog whether can be exchanged
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
    Decompose multiple control QGate
    
    Args:
        qprog: quantum program
    
    Returns:
        a new prog after decomposition
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
    Create a list of measure node
    
    Args:
        qubit_list : measure qubits
        cbit_list : cbits stores quantum measure result
    
    Returns:
        a list of measure node
    
    """
    ...

@overload
def measure_all(qubit_addr_list: List[int], cbit_addr_list: List[int]) -> QProg:
    """
    Create a list of measure node
    
    Args:
        qubit_list : measure qubits list
        cbit_list : cbits stores quantum measure result
    
    Returns:
        a list of measure node
    """
    ...

@overload
def mul(arg0: ClassicalCondition, arg1: ClassicalCondition) -> ClassicalCondition:
    """
    """
    ...

@overload
def mul(arg0: ClassicalCondition, arg1: int) -> ClassicalCondition:
    """
    """
    ...

@overload
def mul(arg0: int, arg1: ClassicalCondition) -> ClassicalCondition:
    """
    """
    ...

def originir_to_qprog(file_path: str, machine: QuantumMachine) -> QProg:
    """
    Read OriginIR file and trans to QProg
    
    Args:
        file_path: OriginIR file path
        machine: initialized quantum machine
    
    Returns:
        Transformed QProgRaises:
        run_fail: An error occurred in originir_to_qprog
    
    """
    ...

def pauli_combination_replace(arg0: List[Tuple[float,QCircuit]], arg1: QuantumMachine, arg2: str, arg3: str) -> List[Tuple[float,QCircuit]]:
    """
    """
    ...

def planarity_testing(topo_data: List[List[int]]) -> bool:
    """
    planarity testing
    
    Args:
        topo_data: quantum program topo data
    
    Returns:
        result data 
    Raises:
        run_fail: An error occurred in planarity_testing
    
    """
    ...

def pmeasure(qubit_list: QVec, select_max: int) -> List[Tuple[int,float]]:
    """
    Get the probability distribution over qubits
    
    Args:
        qubit_list: qubit list to measure    select_max: max returned element num in returnd tuple, should in [-1, 1<<len(qubit_list)]
                    default is -1, means no limit
    
    Returns:
        measure result of quantum machine in tuple form
    """
    ...

def pmeasure_no_index(qubit_list: QVec) -> List[float]:
    """
    Get the probability distribution over qubits
    
    Args:
        qubit_list: qubit list to measure
    Returns:
        measure result of quantum machine in list form
    """
    ...

def poly(arg0: var, arg1: var) -> var:
    """
    """
    ...

def print_matrix(matrix: List[complex], precision: int = 8) -> str:
    """
    Print matrix element
    
    Args:
        matrix: matrix
        precision: double value to string cutoff precision
    
    Returns:
        string of matrix
    """
    ...

def prob_run_dict(qprog: QProg, qubit_list: QVec, select_max: int = -1) -> Dict[str,float]:
    """
    Run quantum program and get pmeasure result as dict
    
    Args:
        qprog: quantum program
        qubit_list: pmeasure qubits list
        select_max: max returned element num in returnd tuple, should in [-1, 1<<len(qubit_list)]
                    default is -1, means no limit
    Returns:
        measure result of quantum machine
    Raises:
        run_fail: An error occurred in measure quantum program
    
    """
    ...

def prob_run_list(qprog: QProg, qubit_list: QVec, select_max: int = -1) -> List[float]:
    """
    Run quantum program and get pmeasure result as list
    
    Args:
        qprog: quantum program
        qubit_list: pmeasure qubits list
        select_max: max returned element num in returnd tuple, should in [-1, 1<<len(qubit_list)]
                    default is -1, means no limit
    Returns:
        measure result of quantum machine
    Raises:
        run_fail: An error occurred in measure quantum program
    
    """
    ...

def prob_run_tuple_list(qptog: QProg, qubit_list: QVec, select_max: int = -1) -> List[Tuple[int,float]]:
    """
    Run quantum program and get pmeasure result as tuple list
    
    Args:
        qprog: quantum program
        qubit_list: pmeasure qubits list
        select_max: max returned element num in returnd tuple, should in [-1, 1<<len(qubit_list)]
                  default is -1, means no limit
    Returns:
      measure result of quantum machine
    Raises:
        run_fail: An error occurred in prob_run_tuple_list
    
    """
    ...

def prog_layer(*args, **kwargs) -> Any:
    """
    """
    ...

def prog_to_dag(prog: QProg) -> QProgDAG:
    """
    """
    ...

@overload
def qAlloc() -> Qubit:
    """
    Create a qubit
    After init()
    
    Returns:
        a new qubit.    None, if quantum machine had created max number of qubit, which is 29
    
    """
    ...

@overload
def qAlloc(qubit_addr: int) -> Qubit:
    """
    Allocate a qubits
    After init()
    
    Args:
        qubit_addr: qubit physic address, should in [0,29)
    
    Returns:
        pyQPanda.Qubit: None, if qubit_addr error, or reached max number of allowed qubit
    """
    ...

def qAlloc_many(qubit_num: int) -> List[Qubit]:
    """
    Allocate several qubits
    After init()
    
    Args:
        qubit_num: numbers of qubit want to be created
    
    Returns:
        list[pyQPanda.Qubit]: list of qubit
    """
    ...

def qFree(qubit: Qubit) -> None:
    """
    Free a qubit
    
    Args:
        Qubit: a qubit
    
    Returns:
        none
    
    """
    ...

@overload
def qFree_all() -> None:
    """
    Free all qubits
    
    Args:
        none
    
    Returns:
        none
    
    
    """
    ...

@overload
def qFree_all(qubit_list: QVec) -> None:
    """
    Free a list of qubits
    
    Args:
        a list of qubits
    
    Returns:
        none
    
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
    Quantum chip adaptive conversion
    
    Args:
        qprog: quantum program
        machine: quantum machine
        mapping: whether or not perform the mapping operation
        config_file: config file
    
    Returns:
        list contains qprog and qubit_list after mapping, if mapping is false, the qubit_list may be misoperated
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
    Quick measure
    
    Args:
        qubit_list: qubit list to measure
        shots: the repeat num  of measure operate
    
    Returns:
        result of quantum programRaises:
        run_fail: An error occurred in measure quantum program
    
    """
    ...

def random_qcircuit(qvec: QVec, depth: int = 100, gate_type: List[str] = []) -> QCircuit:
    """
    Generate random quantum circuit
    
    Args:
        qubit_row: circuit qubit row value
        qubit_col: circuit qubit col value
        depth: circuit depth
        qvm: quantum machine
        qvec: out put circuits for random circuit
    
    Returns:
        random quantum program
    Raises:
        run_fail: An error occurred in generate random circuit
    
    """
    ...

def random_qprog(qubit_row: int, qubit_col: int, depth: int, qvm: QuantumMachine, qvec: QVec) -> QProg:
    """
    Generate random quantum program
    
    Args:
        qubit_row: circuit qubit row value
        qubit_col: circuit qubit col value
        depth: circuit depth
        qvm: quantum machine
        qvec: out put circuits for random qprog
    
    Returns:
        random quantum program
    Raises:
        run_fail: An error occurred in generate random qprog
    
    """
    ...

def recover_edges(topo_data: List[List[int]], max_connect_degree: int, candidate_edges: List[Tuple[int,List[int]]]) -> List[List[int]]:
    """
    Recover edges from the candidate edges
    
    Args:
        topo_data: quantum program topo_data
        max_connect_degree: max value of connect degree
        candidate_edges: candidate edges
    
    Returns:
        topo data 
    Raises:
        run_fail: An error occurred in recover_edges
    
    """
    ...

def remap(prog: QProg, target_qlist: QVec, target_clist: List[ClassicalCondition] = []) -> QProg:
    """
    Source qunatum program is mapped to the target qubits
    
    Args:
        prog: source quantum progprom 
        target_qlist: target qubits
        target_clist: target cbits
    
    Returns:
        target quantum program
    
    """
    ...

def replace_complex_points(src_topo_data: List[List[int]], max_connect_degree: int, sub_topo_vec: List[Tuple[int,List[List[int]]]]) -> None:
    """
    Replacing complex points with subgraphs
    
    Args:
        src_topo_data: quantum program source topo data
        max_connect_degree: max value of connect degree
        sub_topo_vec: sub topo list
    
    Returns:
        none 
    Raises:
        run_fail: An error occurred in replace_complex_points
    
    """
    ...

@overload
def run_with_configuration(program: QProg, cbit_list: List[ClassicalCondition], shots: int, noise_model: Noise = NoiseModel()) -> Dict[str,int]:
    """
    Run quantum program with configuration
    
    Args:
        program: quantum program
        cbit_list: classic cbits list
        shots: repeate run quantum program times
        noise_model: noise model, default is no noise. noise model only work on CPUQVM now
    
    Returns:
        result of quantum program execution in shots.
        first is the final qubit register state, second is it's hit shotRaises:
        run_fail: An error occurred in measure quantum program
    
    
    """
    ...

@overload
def run_with_configuration(program: QProg, shots: int, noise_model: Noise = NoiseModel()) -> Dict[str,int]:
    """
    Run quantum program with configuration
    
    Args:
        program: quantum program
        cbit_list: classic cbits list
        shots: repeate run quantum program times
        noise_model: noise model, default is no noise. noise model only work on CPUQVM now
    
    Returns:
        result of quantum program execution in shots.
        first is the final qubit register state, second is it's hit shotRaises:
        run_fail: An error occurred in measure quantum program
    
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

@overload
def single_qubit_rb(qvm: QuantumMachine, qubit: Qubit, clifford_range: List[int], num_circuits: int, shots: int, chip_id: int = 2, interleaved_gates: List[QGate] = []) -> Dict[int,float]:
    """
    Single qubit rb with WU YUAN chip
    
    Args:
        qvm: quantum machine
        qubit: single qubit
        clifford_range: clifford range list
        num_circuits: the num of circuits
        shots: measure shots
        chip type: RealChipType
        interleaved_gates: interleaved gates list
    
    Returns:
        result data dict
    Raises:
        run_fail: An error occurred in single_qubit_rb
    
    
    """
    ...

@overload
def single_qubit_rb(config: QCloudTaskConfig, qubit: int, clifford_range: List[int], num_circuits: int, interleaved_gates: List[QGate] = []) -> Dict[int,float]:
    """
    Single qubit rb with origin chip
    
    Args:
        config: quantum QCloudTaskConfig
        qubit: single qubit
        clifford_range: clifford range list
        num_circuits: the num of circuits
        interleaved_gates: interleaved gates list
    
    Returns:
        result data dict
    Raises:
        run_fail: An error occurred in single_qubit_rb
    
    """
    ...

def softmax(arg0: var) -> var:
    """
    """
    ...

def split_complex_points(complex_points: List[int], max_connect_degree: int, topo_data: List[List[int]], split_method: ComplexVertexSplitMethod = ComplexVertexSplitMethod.LINEAR) -> List[Tuple[int,List[List[int]]]]:
    """
    Splitting complex points into multiple points
    
    Args:
        topo_data: quantum program topo_data
        max_connect_degree: max value of connect degree
        complex_points: complex points list
        split_method: see ComplexVertexSplitMethod, default is ComplexVertexSplitMethod.LINEAR
    
    Returns:
        none 
    Raises:
        run_fail: An error occurred in split_complex_points
    
    """
    ...

def stack(arg0: int, *args) -> var:
    """
    """
    ...

@overload
def state_fidelity(state1: List[complex], state2: List[complex]) -> float:
    """
    compare two quantum states , Get the state fidelity
    
    Args:
        state1: quantum state list 1
        state2: quantum state list 2
    
    Returns:
        state fidelity bewteen [0,1]
    
    """
    ...

@overload
def state_fidelity(matrix1: List[List[complex]], matrix2: List[List[complex]]) -> float:
    """
    compare two quantum states matrix, Get the state fidelity
    
    Args:
        state1: quantum state matrix 1
        state2: quantum state matrix 2
    
    Returns:
        state fidelity bewteen [0,1]
    
    """
    ...

@overload
def state_fidelity(state1: List[complex], state2: List[List[complex]]) -> float:
    """
    compare two quantum states , Get the state fidelity
    
    Args:
        state1: quantum state list 1
        state2: quantum state matrix 2
    
    Returns:
        state fidelity bewteen [0,1]
    
    """
    ...

@overload
def state_fidelity(state1: List[List[complex]], state2: List[complex]) -> float:
    """
    compare two quantum states , Get the state fidelity
    
    Args:
        state1: quantum state matrix 1
        state2: quantum state list 2
    
    Returns:
        state fidelity bewteen [0,1]
    """
    ...

@overload
def sub(arg0: ClassicalCondition, arg1: ClassicalCondition) -> ClassicalCondition:
    """
    """
    ...

@overload
def sub(arg0: ClassicalCondition, arg1: int) -> ClassicalCondition:
    """
    """
    ...

@overload
def sub(arg0: int, arg1: ClassicalCondition) -> ClassicalCondition:
    """
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
    Transform QProg to Quil instruction
    
    Args:
        qprog: QProg
        machine: quantum machine
    
    Returns:
        Quil instruction string
    """
    ...

@overload
def to_originir(qprog: QProg, machine: QuantumMachine) -> str:
    """
    Transform QProg to OriginIR string
    
    Args:
        qprog: QProg or QCircute
        machine: quantum machine
    
    Returns:
        QriginIR string
    
    """
    ...

@overload
def to_originir(qprog: QCircuit, machine: QuantumMachine) -> str:
    """
    Transform QProg to OriginIR string
    
    Args:
        qprog: QProg or QCircute
        machine: quantum machine
    
    Returns:
        QriginIR string
    
    """
    ...

@overload
def to_originir(qprog: QGate, machine: QuantumMachine) -> str:
    """
    Transform QProg to OriginIR string
    
    Args:
        qprog: QProg or QCircute
        machine: quantum machine
    
    Returns:
        QriginIR string
    
    """
    ...

@overload
def to_originir(qprog: QIfProg, machine: QuantumMachine) -> str:
    """
    Transform QProg to OriginIR string
    
    Args:
        qprog: QProg or QCircute
        machine: quantum machine
    
    Returns:
        QriginIR string
    
    """
    ...

@overload
def to_originir(qprog: QWhileProg, machine: QuantumMachine) -> str:
    """
    Transform QProg to OriginIR string
    
    Args:
        qprog: QProg or QCircute
        machine: quantum machine
    
    Returns:
        QriginIR string
    
    """
    ...

@overload
def to_originir(qprog: QMeasure, machine: QuantumMachine) -> str:
    """
    Transform QProg to OriginIR string
    
    Args:
        qprog: QProg or QCircute
        machine: quantum machine
    
    Returns:
        QriginIR string
    """
    ...

def topology_match(qprog: QProg, qubit_list: QVec, machine: QuantumMachine, confing_file: str = 'QPandaConfig.json') -> list:
    """
    Judge QProg/QCircuit matches the topology of the physical qubits
    
    Args:
        qprog: quantum prog 
        qubit_list: qubits list in quantum prog 
        machine: quantum machine 
        confing_file: match configfilepath, default is QPandaConfig.json 
    
    Returns:
        result data
    Raises:
        run_fail: An error occurred in topology_match
    
    """
    ...

def transform_binary_data_to_qprog(machine: QuantumMachine, data: List[int]) -> QProg:
    """
    Parse binary data trans to quantum program
    
    Args:
        machine: quantum machine
        data: list contains binary data from transform_qprog_to_binary()
    
    Returns:
        QProg
    """
    ...

def transform_originir_to_qprog(fname: str, machine: QuantumMachine) -> QProg:
    """
    Transform OriginIR to QProg
    
    Args:
        fname: file sotred OriginIR instruction    machine: quantum machine
    
    Returns:
        QProg
    """
    ...

@overload
def transform_qprog_to_binary(qprog: QProg, machine: QuantumMachine) -> List[int]:
    """
    Get quantum program binary data
    
    Args:
        qprog: QProg
        machine: quantum machine
    
    Returns:
        binary data in list
    
    """
    ...

@overload
def transform_qprog_to_binary(qprog: QProg, machine: QuantumMachine, fname: str) -> None:
    """
    Save quantum program to file as binary data
    
    Args:
        qprog: QProg
        machine: quantum machine
        fname: save to file name
    
    """
    ...

def transform_qprog_to_originir(qprog: QProg, machine: QuantumMachine) -> str:
    """
    Quantum program transform to OriginIR string
    
    Args:
        qprog: QProg
        machine: quantum machine
    
    Returns:
        OriginIR instruction string
    """
    ...

def transform_qprog_to_quil(qprog: QProg, machine: QuantumMachine) -> str:
    """
    Transform QProg to Quil instruction
    
    Args:
        qprog: QProg
        machine: quantum machine
    
    Returns:
        Quil instruction string
    """
    ...

@overload
def transform_to_base_qgate(qprog: QProg, machine: QuantumMachine, config_file: str = 'QPandaConfig.json') -> QProg:
    """
    Basic quantum - gate conversion
    
    Args:
        qprog: quantum program
        machine: quantum machine
        config_file: config file
    
    Returns:
        a new prog after transform_to_base_qgate
    
    """
    ...

@overload
def transform_to_base_qgate(qprog: QProg, machine: QuantumMachine, convert_single_gates: List[str], convert_double_gates: List[str]) -> QProg:
    """
    Basic quantum - gate conversion
    
    Args:
        qprog: quantum program
        machine: quantum machine
        convert_single_gates: quantum single gates sets
        convert_double_gates: quantum double gates sets
    
    Returns:
        a new prog after transform_to_base_qgate
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
    Get valid QGates and valid double bit QGate type
    
    Args:
        double_gates: double gates list
    
    Returns:
        result list
    
    """
    ...

def validate_single_qgate_type(gate_str_list: List[str]) -> list:
    """
    Get valid QGates and valid single bit QGate type
    
    Args:
        single_gates: single gates list
    
    Returns:
        result list
    
    """
    ...

def vector_dot(x: List[float], y: List[float]) -> float:
    """
    Inner product of vector x and y
    
    Args:
        x: list x 
        y: list y  
    
    Returns:
        dot result 
    Raises:
        run_fail: An error occurred in vector_dot
    
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

