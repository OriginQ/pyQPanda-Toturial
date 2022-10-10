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
BARRIER_GATE: GateType
CNOT_GATE: LATEX_GATE_TYPE
CPHASE_GATE: GateType
CPU: BackendType
CPU_SINGLE_THREAD: BackendType
CP_GATE: GateType
CU_GATE: GateType
CZ_GATE: GateType
DOUBLE_BIT_GATE: DoubleGateTransferType
DOUBLE_CONTINUOUS: SingleGateTransferType
DOUBLE_DISCRETE: SingleGateTransferType
DOUBLE_GATE_INVALID: DoubleGateTransferType
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
LINEAR: ComplexVertexSplitMethod
METHOD_UNDEFINED: ComplexVertexSplitMethod
MPS: BackendType
NELDER_MEAD: OptimizerType
NOISE: BackendType
ORACLE_GATE: GateType
P00_GATE: GateType
P0_GATE: GateType
P11_GATE: GateType
P1_GATE: GateType
PAULI_X_GATE: GateType
PAULI_Y_GATE: GateType
PAULI_Z_GATE: GateType
POWELL: OptimizerType
P_GATE: GateType
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
WUYUAN_1: ChipID
WUYUAN_2: ChipID
WUYUAN_3: ChipID
X_HALF_PI: GateType
Y_HALF_PI: GateType
Z_HALF_PI: GateType
computing: task_status
failed: task_status
finished: task_status
origin_wuyuan_d3: real_chip_type
origin_wuyuan_d4: real_chip_type
origin_wuyuan_d5: real_chip_type
queuing: task_status
waiting: task_status

class AbstractOptimizer:
    """
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
    """
    def __init__(self, arg0: var, arg1: float, arg2: float, arg3: float) -> None:
        """
        """
        ...

    def get_loss(self) -> float:
        """
        """
        ...

    def get_variables(self) -> Set[var]:
        """
        """
        ...

    def minimize(self, arg0: float, arg1: float, arg2: float) -> Optimizer:
        """
        """
        ...

    def run(self, arg0: Set[var], arg1: int) -> bool:
        """
        """
        ...


class AdamOptimizer:
    """
    """
    def __init__(self, arg0: var, arg1: float, arg2: float, arg3: float, arg4: float) -> None:
        """
        """
        ...

    def get_loss(self) -> float:
        """
        """
        ...

    def get_variables(self) -> Set[var]:
        """
        """
        ...

    def minimize(self, arg0: float, arg1: float, arg2: float, arg3: float) -> Optimizer:
        """
        """
        ...

    def run(self, arg0: Set[var], arg1: int) -> bool:
        """
        """
        ...


class Ansatz:
    """
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
    Members:
    
      AGT_X
    
      AGT_H
    
      AGT_RX
    
      AGT_RY
    
      AGT_RZ
    """
    AGT_H: ClassVar[AnsatzGateType] = ...
    AGT_RX: ClassVar[AnsatzGateType] = ...
    AGT_RY: ClassVar[AnsatzGateType] = ...
    AGT_RZ: ClassVar[AnsatzGateType] = ...
    AGT_X: ClassVar[AnsatzGateType] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, arg0: int) -> None:
        """
        """
        ...

    def __eq__(self, other) -> Any:
        """
        """
        ...

    def __ge__(self, other) -> Any:
        """
        """
        ...

    def __getstate__(self) -> Any:
        """
        """
        ...

    def __gt__(self, other) -> Any:
        """
        """
        ...

    def __hash__(self) -> Any:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __le__(self, other) -> Any:
        """
        """
        ...

    def __lt__(self, other) -> Any:
        """
        """
        ...

    def __ne__(self, other) -> Any:
        """
        """
        ...

    def __setstate__(self, state) -> Any:
        """
        """
        ...

    @property
    def name(self) -> str: ...

class BackendType:
    """
    Members:
    
      CPU
    
      GPU
    
      CPU_SINGLE_THREAD
    
      NOISE
    
      MPS
    """
    CPU: ClassVar[BackendType] = ...
    CPU_SINGLE_THREAD: ClassVar[BackendType] = ...
    GPU: ClassVar[BackendType] = ...
    MPS: ClassVar[BackendType] = ...
    NOISE: ClassVar[BackendType] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, arg0: int) -> None:
        """
        """
        ...

    def __eq__(self, other) -> Any:
        """
        """
        ...

    def __getstate__(self) -> Any:
        """
        """
        ...

    def __hash__(self) -> Any:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other) -> Any:
        """
        """
        ...

    def __setstate__(self, state) -> Any:
        """
        """
        ...

    @property
    def name(self) -> str: ...

class CBit:
    """
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
    Members:
    
      Simulation
    
      WUYUAN_1
    
      WUYUAN_2
    
      WUYUAN_3
    """
    Simulation: ClassVar[ChipID] = ...
    WUYUAN_1: ClassVar[ChipID] = ...
    WUYUAN_2: ClassVar[ChipID] = ...
    WUYUAN_3: ClassVar[ChipID] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, arg0: int) -> None:
        """
        """
        ...

    def __eq__(self, other) -> Any:
        """
        """
        ...

    def __getstate__(self) -> Any:
        """
        """
        ...

    def __hash__(self) -> Any:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other) -> Any:
        """
        """
        ...

    def __setstate__(self, state) -> Any:
        """
        """
        ...

    @property
    def name(self) -> str: ...

class ClassicalCondition:
    """
    Classical condition class  Proxy class of cexpr class
    """
    def __init__(self, *args, **kwargs) -> None:
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
    """
    def __init__(self, arg0: ClassicalCondition) -> None:
        """
        """
        ...


class ComplexVertexSplitMethod:
    """
    Members:
    
      METHOD_UNDEFINED
    
      LINEAR
    
      RING
    """
    LINEAR: ClassVar[ComplexVertexSplitMethod] = ...
    METHOD_UNDEFINED: ClassVar[ComplexVertexSplitMethod] = ...
    RING: ClassVar[ComplexVertexSplitMethod] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, arg0: int) -> None:
        """
        """
        ...

    def __eq__(self, other) -> Any:
        """
        """
        ...

    def __getstate__(self) -> Any:
        """
        """
        ...

    def __hash__(self) -> Any:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other) -> Any:
        """
        """
        ...

    def __setstate__(self, state) -> Any:
        """
        """
        ...

    @property
    def name(self) -> str: ...

class DAGNodeType:
    """
    Members:
    
      NUKNOW_SEQ_NODE_TYPE
    
      MAX_GATE_TYPE
    
      MEASURE
    
      QUBIT
    
      RESET
    """
    MAX_GATE_TYPE: ClassVar[DAGNodeType] = ...
    MEASURE: ClassVar[DAGNodeType] = ...
    NUKNOW_SEQ_NODE_TYPE: ClassVar[DAGNodeType] = ...
    QUBIT: ClassVar[DAGNodeType] = ...
    RESET: ClassVar[DAGNodeType] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, arg0: int) -> None:
        """
        """
        ...

    def __eq__(self, other) -> Any:
        """
        """
        ...

    def __getstate__(self) -> Any:
        """
        """
        ...

    def __hash__(self) -> Any:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other) -> Any:
        """
        """
        ...

    def __setstate__(self, state) -> Any:
        """
        """
        ...

    @property
    def name(self) -> str: ...

class DecompositionMode:
    """
    Members:
    
      QR
    
      HOUSEHOLDER_QR
    
      QSDecomposition
    """
    HOUSEHOLDER_QR: ClassVar[DecompositionMode] = ...
    QR: ClassVar[DecompositionMode] = ...
    QSDecomposition: ClassVar[DecompositionMode] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, arg0: int) -> None:
        """
        """
        ...

    def __eq__(self, other) -> Any:
        """
        """
        ...

    def __getstate__(self) -> Any:
        """
        """
        ...

    def __hash__(self) -> Any:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other) -> Any:
        """
        """
        ...

    def __setstate__(self, state) -> Any:
        """
        """
        ...

    @property
    def name(self) -> str: ...

class DoubleGateTransferType:
    """
    Members:
    
      DOUBLE_GATE_INVALID
    
      DOUBLE_BIT_GATE
    """
    DOUBLE_BIT_GATE: ClassVar[DoubleGateTransferType] = ...
    DOUBLE_GATE_INVALID: ClassVar[DoubleGateTransferType] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, arg0: int) -> None:
        """
        """
        ...

    def __eq__(self, other) -> Any:
        """
        """
        ...

    def __getstate__(self) -> Any:
        """
        """
        ...

    def __hash__(self) -> Any:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other) -> Any:
        """
        """
        ...

    def __setstate__(self, state) -> Any:
        """
        """
        ...

    @property
    def name(self) -> str: ...

class Encode:
    """
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
        """
        ...

    def angle_encode(self, qubit: QVec, data: List[float], gate_type: GateType = GateType.RY_GATE) -> None:
        """
        """
        ...

    def approx_mps(self, qubit: QVec, data: List[float], iterator_chi_list: List[int] = [], tol: float = 3e-05, iterator_step: int = 5, chi: int = 2) -> None:
        """
        """
        ...

    def basic_encode(self, qubit: QVec, data: str) -> None:
        """
        """
        ...

    def bid_amplitude_encode(self, qubit: QVec, data: List[float], split: int = 0) -> None:
        """
        """
        ...

    def dc_amplitude_encode(self, qubit: QVec, data: List[float]) -> None:
        """
        """
        ...

    def dense_angle_encode(self, qubit: QVec, data: List[float]) -> None:
        """
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

    def get_normalization_constant(self) -> float:
        """
        """
        ...

    def get_out_qubits(self) -> QVec:
        """
        """
        ...

    def iqp_encode(self, qubit: QVec, data: List[float], control_list: List[Tuple[int,int]] = [], bool_inverse: bool = False, repeats: int = 1) -> None:
        """
        """
        ...

    def schmidt_encode(self, qubit: QVec, data: List[float], cutoff: float) -> None:
        """
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


class Fusion:
    """
    """
    def __init__(self) -> None:
        """
        """
        ...

    @overload
    def aggregate_operations(self, circuit: QCircuit, qvm) -> None:
        """
        """
        ...

    @overload
    def aggregate_operations(self, circuit: QProg, qvm) -> None:
        """
        """
        ...


class GateType:
    """
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
    def __init__(self, arg0: int) -> None:
        """
        """
        ...

    def __eq__(self, other) -> Any:
        """
        """
        ...

    def __getstate__(self) -> Any:
        """
        """
        ...

    def __hash__(self) -> Any:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other) -> Any:
        """
        """
        ...

    def __setstate__(self, state) -> Any:
        """
        """
        ...

    @property
    def name(self) -> str: ...

class HHLAlg:
    """
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

    def get_ancillary_qubit(self) -> Qubit:
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
    Members:
    
      GENERAL_GATE
    
      CNOT_GATE
    
      SWAP_GATE
    """
    CNOT_GATE: ClassVar[LATEX_GATE_TYPE] = ...
    GENERAL_GATE: ClassVar[LATEX_GATE_TYPE] = ...
    SWAP_GATE: ClassVar[LATEX_GATE_TYPE] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, arg0: int) -> None:
        """
        """
        ...

    def __eq__(self, other) -> Any:
        """
        """
        ...

    def __getstate__(self) -> Any:
        """
        """
        ...

    def __hash__(self) -> Any:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other) -> Any:
        """
        """
        ...

    def __setstate__(self, state) -> Any:
        """
        """
        ...

    @property
    def name(self) -> str: ...

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

    def insert_barrier(self, rows: Set[int], from_col: int) -> int:
        """
        
        Args:
            rows: rows need be barriered, may not continus
        """
        ...

    def insert_gate(self, target_rows: Set[int], ctrl_rows: Set[int], from_col: int, gate_type: LATEX_GATE_TYPE, gate_name: str = '', dagger: bool = False, param: str = '') -> int:
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

    def pmeasure_bin_index(self, program: QProg, string: str) -> complex:
        """
        """
        ...

    def pmeasure_bin_subset(self, program: QProg, string_list: List[str]) -> List[complex]:
        """
        """
        ...

    def pmeasure_dec_index(self, program: QProg, string: str) -> complex:
        """
        """
        ...

    def pmeasure_dec_subset(self, program: QProg, string_list: List[str]) -> List[complex]:
        """
        """
        ...

    def pmeasure_no_index(self, qubit_list: QVec) -> List[float]:
        """
        Get the probability distribution over qubits
        """
        ...

    def prob_run_dict(self, program: QProg, qubit_list: QVec, select_max: int = -1) -> Dict[str,float]:
        """
        """
        ...

    def prob_run_list(self, program: QProg, qubit_list: QVec, select_max: int = -1) -> List[float]:
        """
        """
        ...

    def prob_run_tuple_list(self, program: QProg, qubit_list: QVec, select_max: int = -1) -> List[Tuple[int,float]]:
        """
        """
        ...

    def quick_measure(self, qubit_list: QVec, shots: int) -> Dict[str,int]:
        """
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
    """
    def __init__(self, arg0: var, arg1: float, arg2: float) -> None:
        """
        """
        ...

    def get_loss(self) -> float:
        """
        """
        ...

    def get_variables(self) -> Set[var]:
        """
        """
        ...

    def minimize(self, arg0: float, arg1: float) -> Optimizer:
        """
        """
        ...

    def run(self, arg0: Set[var], arg1: int) -> bool:
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
    """
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


class NodeSortProblemGenerator:
    """
    """
    def __init__(self) -> None:
        """
        """
        ...

    def exec(self) -> None:
        """
        """
        ...

    def get_Hamiltonian(self, *args, **kwargs) -> Any:
        """
        """
        ...

    def get_ansatz(self) -> List[AnsatzGate]:
        """
        """
        ...

    def set_problem_graph(self, arg0: List[List[float]]) -> None:
        """
        """
        ...


class NodeType:
    """
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
    def __init__(self, arg0: int) -> None:
        """
        """
        ...

    def __eq__(self, other) -> Any:
        """
        """
        ...

    def __getstate__(self) -> Any:
        """
        """
        ...

    def __hash__(self) -> Any:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other) -> Any:
        """
        """
        ...

    def __setstate__(self, state) -> Any:
        """
        """
        ...

    @property
    def name(self) -> str: ...

class Noise:
    """
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
    BITFLIP_KRAUS_OPERATOR: ClassVar[NoiseModel] = ...
    BIT_PHASE_FLIP_OPRATOR: ClassVar[NoiseModel] = ...
    DAMPING_KRAUS_OPERATOR: ClassVar[NoiseModel] = ...
    DECOHERENCE_KRAUS_OPERATOR: ClassVar[NoiseModel] = ...
    DEPHASING_KRAUS_OPERATOR: ClassVar[NoiseModel] = ...
    DEPOLARIZING_KRAUS_OPERATOR: ClassVar[NoiseModel] = ...
    PAULI_KRAUS_MAP: ClassVar[NoiseModel] = ...
    PHASE_DAMPING_OPRATOR: ClassVar[NoiseModel] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, arg0: int) -> None:
        """
        """
        ...

    def __eq__(self, other) -> Any:
        """
        """
        ...

    def __getstate__(self) -> Any:
        """
        """
        ...

    def __hash__(self) -> Any:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other) -> Any:
        """
        """
        ...

    def __setstate__(self, state) -> Any:
        """
        """
        ...

    @property
    def name(self) -> str: ...

class NoiseQVM(QuantumMachine):
    """
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
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        """
        ...

    def get_loss(self) -> float:
        """
        """
        ...

    def get_variables(self) -> Set[var]:
        """
        """
        ...

    def run(self, arg0: Set[var], arg1: int) -> bool:
        """
        """
        ...


class OptimizerFactory:
    """
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
    Members:
    """
    __entries: ClassVar[dict] = ...
    def __init__(self, arg0: int) -> None:
        """
        """
        ...

    def __eq__(self, other) -> Any:
        """
        """
        ...

    def __getstate__(self) -> Any:
        """
        """
        ...

    def __hash__(self) -> Any:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other) -> Any:
        """
        """
        ...

    def __setstate__(self, state) -> Any:
        """
        """
        ...

    @property
    def name(self) -> str: ...

class OptimizerType:
    """
    Members:
    
      NELDER_MEAD
    
      POWELL
    
      GRADIENT
    """
    GRADIENT: ClassVar[OptimizerType] = ...
    NELDER_MEAD: ClassVar[OptimizerType] = ...
    POWELL: ClassVar[OptimizerType] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, arg0: int) -> None:
        """
        """
        ...

    def __eq__(self, other) -> Any:
        """
        """
        ...

    def __ge__(self, other) -> Any:
        """
        """
        ...

    def __getstate__(self) -> Any:
        """
        """
        ...

    def __gt__(self, other) -> Any:
        """
        """
        ...

    def __hash__(self) -> Any:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __le__(self, other) -> Any:
        """
        """
        ...

    def __lt__(self, other) -> Any:
        """
        """
        ...

    def __ne__(self, other) -> Any:
        """
        """
        ...

    def __setstate__(self, state) -> Any:
        """
        """
        ...

    @property
    def name(self) -> str: ...

class OriginCMem:
    """
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
    """
    def __init__(self) -> None:
        """
        """
        ...

    def get_prob_dict(self, arg0: QVec) -> Dict[str,float]:
        """
        """
        ...

    def init_qvm(self, type: BackendType = BackendType.CPU) -> None:
        """
        init quantum virtual machine
        """
        ...

    def pmeasure_bin_index(self, bin_index: str) -> complex:
        """
        PMeasure_bin_index
        """
        ...

    def pmeasure_dec_index(self, dec_index: str) -> complex:
        """
        PMeasure_dec_index
        """
        ...

    def pmeasure_subset(self, index_list: List[str]) -> Dict[str,complex]:
        """
        pmeasure_subset
        """
        ...

    def prob_run_dict(self, arg0: QProg, arg1: QVec) -> Dict[str,float]:
        """
        """
        ...

    @overload
    def run(self, qprog: QProg, noise_model: Noise = NoiseModel()) -> None:
        """
        load the quantum program
        
        """
        ...

    @overload
    def run(self, qprog: QCircuit, noise_model: Noise = NoiseModel()) -> None:
        """
        load the quantum program
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


class QCircuit:
    """
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
    Members:
    
      Merge_H_X
    
      Merge_U3
    
      Merge_RX
    
      Merge_RY
    
      Merge_RZ
    """
    Merge_H_X: ClassVar[QCircuitOPtimizerMode] = ...
    Merge_RX: ClassVar[QCircuitOPtimizerMode] = ...
    Merge_RY: ClassVar[QCircuitOPtimizerMode] = ...
    Merge_RZ: ClassVar[QCircuitOPtimizerMode] = ...
    Merge_U3: ClassVar[QCircuitOPtimizerMode] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, arg0: int) -> None:
        """
        """
        ...

    def __eq__(self, other) -> Any:
        """
        """
        ...

    def __getstate__(self) -> Any:
        """
        """
        ...

    def __hash__(self) -> Any:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other) -> Any:
        """
        """
        ...

    def __or__(self, arg0: QCircuitOPtimizerMode) -> int:
        """
        bitwise or
        """
        ...

    def __setstate__(self, state) -> Any:
        """
        """
        ...

    @property
    def name(self) -> str: ...

class QCloud(QuantumMachine):
    """
    """
    def __init__(self) -> None:
        """
        """
        ...

    def full_amplitude_measure(self, prog: QProg, shot: int, task_name: str = 'Qurator Experiment') -> Dict[str,float]:
        """
        """
        ...

    def full_amplitude_measure_batch(self, prog_array: List[QProg], shot: int, task_name: str = 'QPanda Experiment') -> List[Dict[str,float]]:
        """
        """
        ...

    def full_amplitude_measure_batch_commit(self, prog_array: List[QProg], shot: int, status: task_status, task_name: str = 'QPanda Experiment') -> Dict[int,str]:
        """
        """
        ...

    def full_amplitude_measure_batch_query(self, taskid_map: Dict[int,str]) -> Dict[int,Dict[str,float]]:
        """
        """
        ...

    def full_amplitude_pmeasure(self, prog: QProg, qvec: List[int], task_name: str = 'Qurator Experiment') -> Dict[str,float]:
        """
        """
        ...

    def full_amplitude_pmeasure_batch(self, prog_array: List[QProg], qvec: List[int], task_name: str = 'QPanda Experiment') -> List[Dict[str,float]]:
        """
        """
        ...

    def full_amplitude_pmeasure_batch_commit(self, prog_array: List[QProg], qvec: List[int], status: task_status, task_name: str = 'QPanda Experiment') -> Dict[int,str]:
        """
        """
        ...

    def full_amplitude_pmeasure_batch_query(self, taskid_map: Dict[int,str]) -> Dict[int,Dict[str,float]]:
        """
        """
        ...

    def get_expectation(self, prog: QProg, hamiltonian: List[Tuple[Dict[int,str],float]], qvec: QVec, status: task_status, task_name: str = 'Qurator Experiment') -> float:
        """
        """
        ...

    def get_expectation_commit(self, prog: QProg, hamiltonian: List[Tuple[Dict[int,str],float]], qvec: QVec, status: task_status, task_name: str = 'QPanda Experiment') -> float:
        """
        """
        ...

    def get_expectation_exec(self, taskid: str, status: task_status) -> float:
        """
        """
        ...

    def get_expectation_query(self, taskid: str, status: task_status) -> float:
        """
        """
        ...

    def get_state_fidelity(self, prog: QProg, shot: int, chip_id: real_chip_type = real_chip_type.origin_wuyuan_d5, is_amend: bool = True, is_mapping: bool = True, is_optimization: bool = True, task_name: str = 'Qurator Experiment') -> float:
        """
        """
        ...

    def get_state_tomography_density(self, prog: QProg, shot: int, chip_id: real_chip_type = real_chip_type.origin_wuyuan_d5, is_amend: bool = True, is_mapping: bool = True, is_optimization: bool = True, task_name: str = 'Qurator Experiment') -> List[List[complex]]:
        """
        """
        ...

    def init_qvm(self, token: str, is_logged: bool = False) -> None:
        """
        init quantum virtual machine
        """
        ...

    def noise_measure(self, prog: QProg, shot: int, task_name: str = 'Qurator Experiment') -> Dict[str,float]:
        """
        """
        ...

    def noise_measure_batch(self, prog_array: List[QProg], shot: int, task_name: str = 'QPanda Experiment') -> List[Dict[str,float]]:
        """
        """
        ...

    def partial_amplitude_pmeasure(self, prog: QProg, amp_vec: List[str], task_name: str = 'Qurator Experiment') -> Dict[str,complex]:
        """
        """
        ...

    def partial_amplitude_pmeasure_batch(self, prog_array: List[QProg], amp_vec: List[str], task_name: str = 'QPanda Experiment') -> List[Dict[str,complex]]:
        """
        """
        ...

    def real_chip_measure(self, prog: QProg, shot: int, chip_id: real_chip_type = real_chip_type.origin_wuyuan_d5, is_amend: bool = True, is_mapping: bool = True, is_optimization: bool = True, task_name: str = 'Qurator Experiment') -> Dict[str,float]:
        """
        """
        ...

    def real_chip_measure_batch(self, prog_array: List[QProg], shot: int, chip_id: real_chip_type = real_chip_type.origin_wuyuan_d3, is_amend: bool = True, is_mapping: bool = True, is_optimization: bool = True, task_name: str = 'QPanda Experiment') -> List[Dict[str,float]]:
        """
        """
        ...

    def real_chip_measure_batch_commit(self, prog_array: List[QProg], shot: int, status: task_status, chip_id: real_chip_type = real_chip_type.origin_wuyuan_d3, is_amend: bool = True, is_mapping: bool = True, is_optimization: bool = True, task_name: str = 'QPanda Experiment') -> Dict[int,str]:
        """
        """
        ...

    def real_chip_measure_batch_query(self, taskid_map: Dict[int,str]) -> Dict[int,Dict[str,float]]:
        """
        """
        ...

    def set_batch_compute_url(self, arg0: str) -> None:
        """
        """
        ...

    def set_batch_inquire_url(self, arg0: str) -> None:
        """
        """
        ...

    def set_compute_url(self, arg0: str) -> None:
        """
        """
        ...

    def set_inquire_url(self, arg0: str) -> None:
        """
        """
        ...

    def set_noise_model(self, arg0: NoiseModel, arg1: List[float], arg2: List[float]) -> None:
        """
        """
        ...

    def set_qcloud_api(self, arg0: str) -> None:
        """
        """
        ...

    def single_amplitude_pmeasure(self, prog: QProg, amplitude: str, task_name: str = 'Qurator Experiment') -> complex:
        """
        """
        ...

    def single_amplitude_pmeasure_batch(self, prog: List[QProg], amplitude: str, task_name: str = 'QPanda Experiment') -> List[complex]:
        """
        """
        ...


class QError:
    """
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
    def __init__(self, arg0: int) -> None:
        """
        """
        ...

    def __eq__(self, other) -> Any:
        """
        """
        ...

    def __getstate__(self) -> Any:
        """
        """
        ...

    def __hash__(self) -> Any:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other) -> Any:
        """
        """
        ...

    def __setstate__(self, state) -> Any:
        """
        """
        ...

    @property
    def name(self) -> str: ...

class QGate:
    """
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

    def set_pauli_matrix(self, arg0: QuantumMachine, arg1: numpy.ndarray[float64[m,n]]) -> None:
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
    Members:
    
      CPU
    
      GPU
    
      CPU_SINGLE_THREAD
    
      NOISE
    """
    CPU: ClassVar[QMachineType] = ...
    CPU_SINGLE_THREAD: ClassVar[QMachineType] = ...
    GPU: ClassVar[QMachineType] = ...
    NOISE: ClassVar[QMachineType] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, arg0: int) -> None:
        """
        """
        ...

    def __eq__(self, other) -> Any:
        """
        """
        ...

    def __getstate__(self) -> Any:
        """
        """
        ...

    def __hash__(self) -> Any:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other) -> Any:
        """
        """
        ...

    def __setstate__(self, state) -> Any:
        """
        """
        ...

    @property
    def name(self) -> str: ...

class QMeasure:
    """
    """
    def __init__(self, arg0: NodeIter) -> None:
        """
        """
        ...


class QOperator:
    """
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
        """
        ...

    @overload
    def __init__(self, arg0: QCircuit) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: QIfProg) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: QWhileProg) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: QGate) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: QMeasure) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: QReset) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: ClassicalCondition) -> None:
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
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        """
        ...

    def allocate_qubit_through_phy_address(self, address: int) -> Qubit:
        """
        """
        ...

    def allocate_qubit_through_vir_address(self, address: int) -> Qubit:
        """
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

    def directly_run(self, qprog: QProg, noise_model: Noise = NoiseModel()) -> Dict[str,bool]:
        """
        """
        ...

    def finalize(self) -> None:
        """
        finalize
        """
        ...

    def getAllocateCMem(self) -> int:
        """
        getAllocateCMem
        """
        ...

    def getAllocateQubitNum(self) -> int:
        """
        getAllocateQubitNum
        """
        ...

    def getStatus(self, *args, **kwargs) -> Any:
        """
        get the status(ptr) of the quantum machine
        """
        ...

    def get_allocate_cbits(self) -> List[ClassicalCondition]:
        """
        get allocate cbits of QuantumMachine
        """
        ...

    def get_allocate_cmem_num(self) -> int:
        """
        getAllocateCMem
        """
        ...

    def get_allocate_qubit_num(self) -> int:
        """
        getAllocateQubitNum
        """
        ...

    def get_allocate_qubits(self) -> QVec:
        """
        get allocate qubits of QuantumMachine
        """
        ...

    def get_async_result(self) -> Dict[str,bool]:
        """
        """
        ...

    @overload
    def get_expectation(self, qprog: QProg, hamiltonian: List[Tuple[Dict[int,str],float]], qubit_list: QVec) -> float:
        """
        """
        ...

    @overload
    def get_expectation(self, qprog: QProg, hamiltonian: List[Tuple[Dict[int,str],float]], qubit_list: QVec, shots: int) -> float:
        """
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
        getState
        """
        ...

    def get_status(self, *args, **kwargs) -> Any:
        """
        get the status(ptr) of the quantum machine
        """
        ...

    def initQVM(self) -> None:
        """
        init quantum virtual machine
        """
        ...

    def init_qvm(self) -> None:
        """
        init quantum virtual machine
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

    @overload
    def run_with_configuration(self, qprog: QProg, cbit_list: List[ClassicalCondition], data: dict, noise_model: Noise = NoiseModel()) -> Dict[str,int]:
        """
        """
        ...

    @overload
    def run_with_configuration(self, qprog: QProg, cbit_list: List[ClassicalCondition], shot: int, noise_model: Noise = NoiseModel()) -> Dict[str,int]:
        """
        """
        ...

    @overload
    def run_with_configuration(self, qprog: QProg, shot: int, noise_model: Noise = NoiseModel()) -> Dict[str,int]:
        """
        """
        ...

    @overload
    def run_with_configuration(self, qprog: QProg, cbit_list: List[int], shot: int, noise_model: Noise = NoiseModel()) -> Dict[str,int]:
        """
        """
        ...

    def set_configure(self, max_qubit: int, max_cbit: int) -> None:
        """
        set QVM max qubit and max cbit
        """
        ...


class QuantumStateTomography:
    """
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
    """
    def __init__(self, arg0: var, arg1: float, arg2: float, arg3: float) -> None:
        """
        """
        ...

    def get_loss(self) -> float:
        """
        """
        ...

    def get_variables(self) -> Set[var]:
        """
        """
        ...

    def minimize(self, arg0: float, arg1: float, arg2: float) -> Optimizer:
        """
        """
        ...

    def run(self, arg0: Set[var], arg1: int) -> bool:
        """
        """
        ...


class SingleAmpQVM(QuantumMachine):
    """
    """
    def __init__(self) -> None:
        """
        """
        ...

    @overload
    def get_prob_dict(self, arg0: QVec) -> Dict[str,float]:
        """
        """
        ...

    @overload
    def get_prob_dict(self, arg0: List[int]) -> Dict[str,float]:
        """
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

    def pmeasure_bin_index(self, arg0: str) -> float:
        """
        PMeasure by binary index
        """
        ...

    def pmeasure_dec_index(self, arg0: str) -> float:
        """
        PMeasure by decimal  index
        """
        ...

    @overload
    def prob_run_dict(self, arg0: QProg, arg1: QVec) -> Dict[str,float]:
        """
        """
        ...

    @overload
    def prob_run_dict(self, arg0: QProg, arg1: List[int]) -> Dict[str,float]:
        """
        """
        ...

    @overload
    def run(self, prog: QProg, qv: QVec, max_rank: int = 30, alloted_time: int = 5) -> None:
        """
        run the quantum program
        
        """
        ...

    @overload
    def run(self, arg0: QProg, arg1: QVec, arg2: int, arg3: List[List[Tuple[int,bool]]]) -> None:
        """
        run the quantum program
        """
        ...


class SingleGateTransferType:
    """
    Members:
    
      SINGLE_GATE_INVALID
    
      ARBITRARY_ROTATION
    
      DOUBLE_CONTINUOUS
    
      SINGLE_CONTINUOUS_DISCRETE
    
      DOUBLE_DISCRETE
    """
    ARBITRARY_ROTATION: ClassVar[SingleGateTransferType] = ...
    DOUBLE_CONTINUOUS: ClassVar[SingleGateTransferType] = ...
    DOUBLE_DISCRETE: ClassVar[SingleGateTransferType] = ...
    SINGLE_CONTINUOUS_DISCRETE: ClassVar[SingleGateTransferType] = ...
    SINGLE_GATE_INVALID: ClassVar[SingleGateTransferType] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, arg0: int) -> None:
        """
        """
        ...

    def __eq__(self, other) -> Any:
        """
        """
        ...

    def __getstate__(self) -> Any:
        """
        """
        ...

    def __hash__(self) -> Any:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other) -> Any:
        """
        """
        ...

    def __setstate__(self, state) -> Any:
        """
        """
        ...

    @property
    def name(self) -> str: ...

class UpdateMode:
    """
    Members:
    
      GD_VALUE
    
      GD_DIRECTION
    """
    GD_DIRECTION: ClassVar[UpdateMode] = ...
    GD_VALUE: ClassVar[UpdateMode] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, arg0: int) -> None:
        """
        """
        ...

    def __eq__(self, other) -> Any:
        """
        """
        ...

    def __ge__(self, other) -> Any:
        """
        """
        ...

    def __getstate__(self) -> Any:
        """
        """
        ...

    def __gt__(self, other) -> Any:
        """
        """
        ...

    def __hash__(self) -> Any:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __le__(self, other) -> Any:
        """
        """
        ...

    def __lt__(self, other) -> Any:
        """
        """
        ...

    def __ne__(self, other) -> Any:
        """
        """
        ...

    def __setstate__(self, state) -> Any:
        """
        """
        ...

    @property
    def name(self) -> str: ...

class VanillaGradientDescentOptimizer:
    """
    """
    def __init__(self, arg0: var, arg1: float, arg2: float, arg3: OptimizerMode) -> None:
        """
        """
        ...

    def get_loss(self) -> float:
        """
        """
        ...

    def get_variables(self) -> Set[var]:
        """
        """
        ...

    def minimize(self, arg0: float, arg1: float) -> Optimizer:
        """
        """
        ...

    def run(self, arg0: Set[var], arg1: int) -> bool:
        """
        """
        ...


class VariationalQuantumCircuit:
    """
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


class expression:
    """
    """
    def __init__(self, arg0: var) -> None:
        """
        """
        ...

    @overload
    def backprop(self, arg0: Dict[var,numpy.ndarray[float64[m,n]]]) -> None:
        """
        """
        ...

    @overload
    def backprop(self, arg0: Dict[var,numpy.ndarray[float64[m,n]]], arg1: Set[var]) -> None:
        """
        """
        ...

    def find_leaves(self) -> List[var]:
        """
        """
        ...

    def find_non_consts(self, arg0: List[var]) -> Set[var]:
        """
        """
        ...

    def get_root(self) -> var:
        """
        """
        ...

    @overload
    def propagate(self) -> numpy.ndarray[float64[m,n]]:
        """
        """
        ...

    @overload
    def propagate(self, arg0: List[var]) -> numpy.ndarray[float64[m,n]]:
        """
        """
        ...


class hadamard_circuit(QCircuit):
    """
    """
    def __init__(self, arg0: QVec) -> None:
        """
        """
        ...


class real_chip_type:
    """
    Members:
    
      origin_wuyuan_d3
    
      origin_wuyuan_d4
    
      origin_wuyuan_d5
    """
    __entries: ClassVar[dict] = ...
    origin_wuyuan_d3: ClassVar[real_chip_type] = ...
    origin_wuyuan_d4: ClassVar[real_chip_type] = ...
    origin_wuyuan_d5: ClassVar[real_chip_type] = ...
    def __init__(self, arg0: int) -> None:
        """
        """
        ...

    def __eq__(self, other) -> Any:
        """
        """
        ...

    def __getstate__(self) -> Any:
        """
        """
        ...

    def __hash__(self) -> Any:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other) -> Any:
        """
        """
        ...

    def __setstate__(self, state) -> Any:
        """
        """
        ...

    @property
    def name(self) -> str: ...

class task_status:
    """
    Members:
    
      waiting
    
      computing
    
      finished
    
      failed
    
      queuing
    """
    __entries: ClassVar[dict] = ...
    computing: ClassVar[task_status] = ...
    failed: ClassVar[task_status] = ...
    finished: ClassVar[task_status] = ...
    queuing: ClassVar[task_status] = ...
    waiting: ClassVar[task_status] = ...
    def __init__(self, arg0: int) -> None:
        """
        """
        ...

    def __eq__(self, other) -> Any:
        """
        """
        ...

    def __getstate__(self) -> Any:
        """
        """
        ...

    def __hash__(self) -> Any:
        """
        """
        ...

    def __int__(self) -> int:
        """
        """
        ...

    def __ne__(self, other) -> Any:
        """
        """
        ...

    def __setstate__(self, state) -> Any:
        """
        """
        ...

    @property
    def name(self) -> str: ...

class var:
    """
    """
    @overload
    def __init__(self, arg0: float) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: numpy.ndarray[float64[m,n],flags.writeable]) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: float, arg1: bool) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: numpy.ndarray[float64[m,n],flags.writeable], arg1: bool) -> None:
        """
        """
        ...

    def clone(self) -> var:
        """
        """
        ...

    def get_value(self) -> numpy.ndarray[float64[m,n]]:
        """
        """
        ...

    @overload
    def set_value(self, arg0: numpy.ndarray[float64[m,n]]) -> None:
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

    def __eq__(self, arg0: var) -> bool:
        """
        """
        ...

    def __getitem__(self, arg0: int) -> var:
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
    Create an BARRIER gate
    
    """
    ...

@overload
def BARRIER(qubit_list: int) -> QGate:
    """
    Create an BARRIER gate
    
    """
    ...

@overload
def BARRIER(qubit_list: QVec) -> QGate:
    """
    Create an BARRIER gate
    
    """
    ...

@overload
def BARRIER(qubit_addr_list: List[int]) -> QGate:
    """
    Create an BARRIER gate
    """
    ...

@overload
def CNOT(control_qubit: Qubit, target_qubit: Qubit) -> QGate:
    """
    Create a CNOT gate
    
    """
    ...

@overload
def CNOT(control_qubit_list: QVec, target_qubit_list: QVec) -> QCircuit:
    """
    Create a CNOT gate
    
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
    Create a CNOT gate
    """
    ...

@overload
def CP(control_qubit: Qubit, target_qubit: Qubit, theta_angle: float) -> QGate:
    """
    Create a CP gate
    
    """
    ...

@overload
def CP(control_qubit_list: QVec, target_qubit_list: QVec, theta_angle: float) -> QCircuit:
    """
    Create a CP gate
    
    """
    ...

@overload
def CP(control_qubit_addr: int, target_qubit_addr: int, theta_angle: float) -> QGate:
    """
    Create a CP gate
    
    """
    ...

@overload
def CP(control_qubit_addr_list: List[int], target_qubit_addr_list: List[int], theta_angle: float) -> QCircuit:
    """
    Create a CP gate
    """
    ...

@overload
def CR(control_qubit: Qubit, target_qubit: Qubit, theta_angle: float) -> QGate:
    """
    Create a CR gate
    
    """
    ...

@overload
def CR(control_qubit_list: QVec, target_qubit_list: QVec, theta_angle: float) -> QCircuit:
    """
    Create a CR gate
    
    """
    ...

@overload
def CR(control_qubit_addr: int, target_qubit_addr: int, theta_angle: float) -> QGate:
    """
    Create a CR gate
    
    """
    ...

@overload
def CR(control_qubit_addr_list: List[int], target_qubit_addr_list: List[int], theta_angle: float) -> QCircuit:
    """
    Create a CR gate
    """
    ...

@overload
def CU(alpha_angle: float, beta_angle: float, gamma_angle: float, delta_angle: float, control_qubit: Qubit, target_qubit: Qubit) -> QGate:
    """
    Create a CU gate
    
    """
    ...

@overload
def CU(alpha_angle: float, beta_angle: float, gamma_angle: float, delta_angle: float, control_qubit_list: QVec, target_qubi_list: QVec) -> QCircuit:
    """
    Create a CU gate
    
    """
    ...

@overload
def CU(matrix: List[complex], control_qubit: Qubit, target_qubit: Qubit) -> QGate:
    """
    Create a CU gate
    
    """
    ...

@overload
def CU(matrix: List[complex], control_qubit_list: QVec, target_qubit_list: QVec) -> QCircuit:
    """
    Create a CU gate
    
    """
    ...

@overload
def CU(control_qubit: Qubit, target_qubit: Qubit, alpha_angle: float, beta_angle: float, gamma_angle: float, delta_angle: float) -> QGate:
    """
    Create a CU gate
    
    """
    ...

@overload
def CU(control_qubit_list: QVec, target_qubit_list: QVec, alpha_angle: float, beta_angle: float, gamma_angle: float, delta_angle: float) -> QCircuit:
    """
    Create a CU gate
    
    """
    ...

@overload
def CU(control_qubit_addr: int, target_qubit_addr: int, alpha_angle: float, beta_angle: float, gamma_angle: float, delta_angle: float) -> QGate:
    """
    Create a CU gate
    
    """
    ...

@overload
def CU(control_qubit_addr_list: List[int], target_qubit_addr_list: List[int], alpha_angle: float, beta_angle: float, gamma_angle: float, delta_angle: float) -> QCircuit:
    """
    Create a CU gate
    
    """
    ...

@overload
def CU(control_qubit: Qubit, target_qubit: Qubit, matrix: List[complex]) -> QGate:
    """
    Create a CU gate
    
    """
    ...

@overload
def CU(control_qubit_list: QVec, target_qubit_list: QVec, matrix: List[complex]) -> QCircuit:
    """
    Create a CU gate
    
    """
    ...

@overload
def CU(control_qubit_addr: int, target_qubit_addr: int, matrix: List[complex]) -> QGate:
    """
    Create a CU gate
    
    """
    ...

@overload
def CU(control_qubit_addr_list: List[int], target_qubit_addr_list: List[int], matrix: List[complex]) -> QCircuit:
    """
    Create a CU gate
    """
    ...

@overload
def CZ(control_qubit: Qubit, target_qubit: Qubit) -> QGate:
    """
    Create a CZ gate
    
    """
    ...

@overload
def CZ(control_qubit_list: QVec, target_qubit_list: QVec) -> QCircuit:
    """
    Create a CZ gate
    
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
    Create a CZ gate
    """
    ...

def CreateEmptyCircuit() -> QCircuit:
    """
    Create an empty QCircuit Container
    """
    ...

def CreateEmptyQProg() -> QProg:
    """
    Create an empty QProg Container
    
    Returns:
        a empty QProg
    """
    ...

@overload
def CreateIfProg(classical_condition: ClassicalCondition, true_node: QProg) -> QIfProg:
    """
    Create a classical quantum IfProg
    
    """
    ...

@overload
def CreateIfProg(classical_condition: ClassicalCondition, true_node: QProg, false_node: QProg) -> QIfProg:
    """
    Create a IfProg
    """
    ...

def CreateWhileProg(classical_condition: ClassicalCondition, true_node: QProg) -> QWhileProg:
    """
    Create a WhileProg
    """
    ...

def Grover(*args, **kwargs) -> Any:
    """
    Build Grover quantum circuit
    """
    ...

@overload
def Grover_search(list: List[int], Classical_condition: ClassicalCondition, QuantumMachine: QuantumMachine, data: int = 2) -> list:
    """
    use Grover algorithm to search target data, return QProg and search_result
    
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
    
    """
    ...

@overload
def H(qubit_list: QVec) -> QCircuit:
    """
    Create a H gate
    
    """
    ...

@overload
def H(qubit_addr: int) -> QGate:
    """
    Create a H gate
    
    """
    ...

@overload
def H(qubit_addr_list: List[int]) -> QCircuit:
    """
    Create a H gate
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
    
    """
    ...

@overload
def I(qubit_list: QVec) -> QCircuit:
    """
    Create a I gate
    
    """
    ...

@overload
def I(qubit_addr: int) -> QGate:
    """
    Create a I gate
    
    """
    ...

@overload
def I(qubit_addr_list: List[int]) -> QCircuit:
    """
    Create a I gate
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
def Measure(qubit: Qubit, cbit: ClassicalCondition) -> QMeasure:
    """
    Create a Measure operation
    
    """
    ...

@overload
def Measure(qubit: Qubit, cbit: CBit) -> QMeasure:
    """
    Create a Measure operation
    
    """
    ...

@overload
def Measure(qubit_addr: int, cbit_addr: int) -> QMeasure:
    """
    Create a Measure operation
    """
    ...

def OBMT_mapping(prog: QProg, quantum_machine: QuantumMachine, b_optimization: bool = False, max_partial: int = 4294967295, max_children: int = 4294967295, config_data: str = 'QPandaConfig.json') -> QProg:
    """
    OPT_BMT mapping
    
    Args:
        prog: the target prog
        quantum_machine: quantum machine
        b_optimization:
        max_partial: Limits the max number of partial solutions per step, There is no limit by default
        max_children: Limits the max number of candidate - solutions per double gate, There is no limit by default
        config_data: config data, @See JsonConfigParam::load_config()
    
    Returns:
        mapped quantum program
    """
    ...

@overload
def P(qubit: Qubit, angle: float) -> QGate:
    """
    Create a P gate
    
    """
    ...

@overload
def P(qubit_list: QVec, angle: float) -> QCircuit:
    """
    Create a P gate
    
    """
    ...

@overload
def P(qubit_addr: int, angle: float) -> QGate:
    """
    Create a P gate
    
    """
    ...

@overload
def P(qubit_addr_list: List[int], angle: float) -> QCircuit:
    """
    Create a P gate
    """
    ...

def PMeasure(arg0: QVec, arg1: int) -> List[Tuple[int,float]]:
    """
    Deprecated, use pmeasure instead
    """
    ...

def PMeasure_no_index(arg0: QVec) -> List[float]:
    """
    Deprecated, use pmeasure_no_index instead
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
    Quantum adder ignore carry
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
    Quantum division with accuracy
    """
    ...

def QDivider(a: QVec, b: QVec, c: QVec, k: QVec, t: ClassicalCondition) -> QProg:
    """
    Quantum division, only supports positive division, and the highest position of a and b and c is sign bit
    """
    ...

def QDividerWithAccuracy(a: QVec, b: QVec, c: QVec, k: QVec, f: QVec, s: List[ClassicalCondition]) -> QProg:
    """
    Quantum division with accuracy, only supports positive division, and the highest position of a and b and c is sign bit
    """
    ...

@overload
def QDouble(first_qubit: Qubit, second_qubit: Qubit, matrix: List[complex]) -> QGate:
    """
    Create a QDouble gate
    
    """
    ...

@overload
def QDouble(first_qubit_list: QVec, second_qubit_list: QVec, matrix: List[complex]) -> QCircuit:
    """
    Create a QDouble gate
    
    """
    ...

@overload
def QDouble(first_qubit_addr: int, second_qubit_addr: int, matrix: List[complex]) -> QGate:
    """
    Create a QDouble gate
    
    """
    ...

@overload
def QDouble(first_qubit_addr_list: List[int], second_qubit_addr_list: List[int], matrix: List[complex]) -> QCircuit:
    """
    Create a QDouble gate
    """
    ...

def QFT(qubits: QVec) -> QCircuit:
    """
    Build QFT quantum circuit
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

def QOracle(qubit_list: QVec, matrix: numpy.ndarray[complex128[m,n]]) -> QGate:
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
    Build QPE quantum circuit
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
    Create a RX gate
    
    """
    ...

@overload
def RX(qubit_list: QVec, angle: float) -> QCircuit:
    """
    Create a RX gate
    
    """
    ...

@overload
def RX(qubit_addr: int, angle: float) -> QGate:
    """
    Create a RX gate
    
    """
    ...

@overload
def RX(qubit_addr_list: List[int], angle: float) -> QCircuit:
    """
    Create a RX gate
    """
    ...

@overload
def RXX(control_qubit: Qubit, target_qubit: Qubit, alpha_angle: float) -> QGate:
    """
    Create a RXX gate
    
    """
    ...

@overload
def RXX(control_qubit_list: QVec, target_qubit_list: QVec, alpha_angle: float) -> QCircuit:
    """
    Create a RXX circuit
    
    """
    ...

@overload
def RXX(control_qubit_addr: int, target_qubit_addr: int, matrix: float) -> QGate:
    """
    Create a RXX gate
    
    """
    ...

@overload
def RXX(control_qubit_addr_list: List[int], target_qubit_addr_list: List[int], matrix: float) -> QCircuit:
    """
    Create a RXX circuit
    """
    ...

@overload
def RY(qubit: Qubit, angle: float) -> QGate:
    """
    Create a RY gate
    
    """
    ...

@overload
def RY(qubit_list: QVec, angle: float) -> QCircuit:
    """
    Create a RY gate
    
    """
    ...

@overload
def RY(qubit_addr: int, angle: float) -> QGate:
    """
    Create a RY gate
    
    """
    ...

@overload
def RY(qubit_addr_list: List[int], angle: float) -> QCircuit:
    """
    Create a RY gate
    """
    ...

@overload
def RYY(control_qubit: Qubit, target_qubit: Qubit, alpha_angle: float) -> QGate:
    """
    Create a RYY gate
    
    """
    ...

@overload
def RYY(control_qubit_list: QVec, target_qubit_list: QVec, alpha_angle: float) -> QCircuit:
    """
    Create a RYY circuit
    
    """
    ...

@overload
def RYY(control_qubit_addr: int, target_qubit_addr: int, matrix: float) -> QGate:
    """
    Create a RYY gate
    
    """
    ...

@overload
def RYY(control_qubit_addr_list: List[int], target_qubit_addr_list: List[int], matrix: float) -> QCircuit:
    """
    Create a RYY circuit
    """
    ...

@overload
def RZ(qubit: Qubit, angle: float) -> QGate:
    """
    Create a RZ gate
    
    """
    ...

@overload
def RZ(qubit_list: QVec, angle: float) -> QCircuit:
    """
    Create a RZ gate
    
    """
    ...

@overload
def RZ(qubit_addr: int, angle: float) -> QGate:
    """
    Create a RZ gate
    
    """
    ...

@overload
def RZ(qubit_addr_list: List[int], angle: float) -> QCircuit:
    """
    Create a RZ gate
    """
    ...

@overload
def RZX(control_qubit: Qubit, target_qubit: Qubit, alpha_angle: float) -> QGate:
    """
    Create a RZX gate
    
    """
    ...

@overload
def RZX(control_qubit_list: QVec, target_qubit_list: QVec, alpha_angle: float) -> QCircuit:
    """
    Create a RZX circuit
    
    """
    ...

@overload
def RZX(control_qubit_addr: int, target_qubit_addr: int, matrix: float) -> QGate:
    """
    Create a RZX gate
    
    """
    ...

@overload
def RZX(control_qubit_addr_list: List[int], target_qubit_addr_list: List[int], matrix: float) -> QCircuit:
    """
    Create a RZX circuit
    """
    ...

@overload
def RZZ(control_qubit: Qubit, target_qubit: Qubit, alpha_angle: float) -> QGate:
    """
    Create a RZZ gate
    
    """
    ...

@overload
def RZZ(control_qubit_list: QVec, target_qubit_list: QVec, alpha_angle: float) -> QCircuit:
    """
    Create a RZZ circuit
    
    """
    ...

@overload
def RZZ(control_qubit_addr: int, target_qubit_addr: int, matrix: float) -> QGate:
    """
    Create a RZZ gate
    
    """
    ...

@overload
def RZZ(control_qubit_addr_list: List[int], target_qubit_addr_list: List[int], matrix: float) -> QCircuit:
    """
    Create a RZZ circuit
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
    
    """
    ...

@overload
def S(qubit_list: QVec) -> QCircuit:
    """
    Create a S gate
    
    """
    ...

@overload
def S(qubit_addr: int) -> QGate:
    """
    Create a S gate
    
    """
    ...

@overload
def S(qubit_addr_list: List[int]) -> QCircuit:
    """
    Create a S gate
    """
    ...

@overload
def SWAP(first_qubit: Qubit, second_qubit: Qubit) -> QGate:
    """
    Create a SWAP gate
    
    """
    ...

@overload
def SWAP(first_qubit_list: QVec, second_qubit_list: QVec) -> QCircuit:
    """
    Create a SWAP gate
    
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
    Create a SWAP gate
    """
    ...

def Shor_factorization(arg0: int) -> Tuple[bool,Tuple[int,int]]:
    """
    Shor Algorithm function
    """
    ...

@overload
def SqiSWAP(first_qubit: Qubit, second_qubit: Qubit) -> QGate:
    """
    Create a SqiSWAP gate
    
    """
    ...

@overload
def SqiSWAP(first_qubit_list: QVec, second_qubit_list: QVec) -> QCircuit:
    """
    Create a SqiSWAP gate
    
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
    Create a SqiSWAP gate
    """
    ...

@overload
def T(qubit: Qubit) -> QGate:
    """
    Create a T gate
    
    """
    ...

@overload
def T(qubit_list: QVec) -> QCircuit:
    """
    Create a T gate
    
    """
    ...

@overload
def T(qubit_addr: int) -> QGate:
    """
    Create a T gate
    
    """
    ...

@overload
def T(qubit_addr_list: List[int]) -> QCircuit:
    """
    Create a T gate
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
    Create a U1 gate
    
    """
    ...

@overload
def U1(qubit_list: QVec, angle: float) -> QCircuit:
    """
    Create a U1 gate
    
    """
    ...

@overload
def U1(qubit_addr: int, angle: float) -> QGate:
    """
    Create a U1 gate
    
    """
    ...

@overload
def U1(qubit_addr_list: List[int], angle: float) -> QCircuit:
    """
    Create a U1 gate
    """
    ...

@overload
def U2(qubit: Qubit, phi_angle: float, lambda_angle: float) -> QGate:
    """
    Create a U2 gate
    
    """
    ...

@overload
def U2(qubit_list: QVec, phi_angle: float, lambda_angle: float) -> QCircuit:
    """
    Create a U2 gate
    
    """
    ...

@overload
def U2(qubit_addr: int, phi_angle: float, lambda_angle: float) -> QGate:
    """
    Create a U2 gate
    
    """
    ...

@overload
def U2(qubit_addr_list: List[int], phi_angle: float, lambda_angle: float) -> QCircuit:
    """
    Create a U2 gate
    """
    ...

@overload
def U3(qubit: Qubit, theta_angle: float, phi_angle: float, lambda_angle: float) -> QGate:
    """
    Create a U3 gate
    
    """
    ...

@overload
def U3(qubit_list: QVec, theta_angle: float, phi_angle: float, lambda_angle: float) -> QCircuit:
    """
    Create a U3 gate
    
    """
    ...

@overload
def U3(qubit_addr: int, theta_angle: float, phi_angle: float, lambda_angle: float) -> QGate:
    """
    Create a U3 gate
    
    """
    ...

@overload
def U3(qubit_addr_list: List[int], theta_angle: float, phi_angle: float, lambda_angle: float) -> QCircuit:
    """
    Create a U3 gate
    """
    ...

@overload
def U4(matrix: List[complex], qubit: Qubit) -> QGate:
    """
    Create a U4 gate
    
    """
    ...

@overload
def U4(alpha_angle: float, beta_angle: float, gamma_angle: float, delta_angle: float, qubit: Qubit) -> QGate:
    """
    Create a U4 gate
    
    """
    ...

@overload
def U4(qubit: Qubit, matrix: List[complex]) -> QGate:
    """
    Create a U4 gate
    
    """
    ...

@overload
def U4(qubit_list: QVec, matrix: List[complex]) -> QCircuit:
    """
    Create a U4 gate
    
    """
    ...

@overload
def U4(qubit_addr: int, matrix: List[complex]) -> QGate:
    """
    Create a U4 gate
    
    """
    ...

@overload
def U4(qubit_addr_list: List[int], matrix: List[complex]) -> QCircuit:
    """
    Create a U4 gate
    
    """
    ...

@overload
def U4(qubit: Qubit, alpha_anlge: float, beta_anlge: float, gamma_anlge: float, delta_anlge: float) -> QGate:
    """
    Create a U4 gate
    
    """
    ...

@overload
def U4(qubit_list: QVec, alpha_angle: float, beta_angle: float, gamma_angle: float, delta_angle: float) -> QCircuit:
    """
    Create a U4 gate
    
    """
    ...

@overload
def U4(qubit_addr: int, alpha_anlge: float, beta_anlge: float, gamma_anlge: float, delta_anlge: float) -> QGate:
    """
    Create a U4 gate
    
    """
    ...

@overload
def U4(qubit_addr_list: List[int], alpha_anlge: float, beta_anlge: float, gamma_anlge: float, delta_anlge: float) -> QCircuit:
    """
    Create a U4 gate
    """
    ...

def UMA(arg0: Qubit, arg1: Qubit, arg2: Qubit) -> QCircuit:
    """
    Quantum adder UMA module
    """
    ...

def VQG_CNOT_batch(*args, **kwargs) -> Any:
    """
    """
    ...

def VQG_CU_batch(*args, **kwargs) -> Any:
    """
    """
    ...

def VQG_CZ_batch(*args, **kwargs) -> Any:
    """
    """
    ...

def VQG_H_batch(*args, **kwargs) -> Any:
    """
    """
    ...

def VQG_I_batch(*args, **kwargs) -> Any:
    """
    """
    ...

def VQG_SWAP_batch(*args, **kwargs) -> Any:
    """
    """
    ...

def VQG_S_batch(*args, **kwargs) -> Any:
    """
    """
    ...

def VQG_SqiSWAP_batch(*args, **kwargs) -> Any:
    """
    """
    ...

def VQG_T_batch(*args, **kwargs) -> Any:
    """
    """
    ...

def VQG_U1_batch(*args, **kwargs) -> Any:
    """
    """
    ...

def VQG_U2_batch(*args, **kwargs) -> Any:
    """
    """
    ...

def VQG_U3_batch(*args, **kwargs) -> Any:
    """
    """
    ...

def VQG_U4_batch(*args, **kwargs) -> Any:
    """
    """
    ...

def VQG_X1_batch(*args, **kwargs) -> Any:
    """
    """
    ...

def VQG_X_batch(*args, **kwargs) -> Any:
    """
    """
    ...

def VQG_Y1_batch(*args, **kwargs) -> Any:
    """
    """
    ...

def VQG_Y_batch(*args, **kwargs) -> Any:
    """
    """
    ...

def VQG_Z1_batch(*args, **kwargs) -> Any:
    """
    """
    ...

def VQG_Z_batch(*args, **kwargs) -> Any:
    """
    """
    ...

def VQG_iSWAP_batch(*args, **kwargs) -> Any:
    """
    """
    ...

@overload
def X(qubit: Qubit) -> QGate:
    """
    Create a X gate
    
    """
    ...

@overload
def X(qubit_list: QVec) -> QCircuit:
    """
    Create a X gate
    
    """
    ...

@overload
def X(qubit_addr: int) -> QGate:
    """
    Create a X gate
    
    """
    ...

@overload
def X(qubit_addr_list: List[int]) -> QCircuit:
    """
    Create a X gate
    """
    ...

@overload
def X1(qubit: Qubit) -> QGate:
    """
    Create a X1 gate
    
    """
    ...

@overload
def X1(qubit_list: QVec) -> QCircuit:
    """
    Create a X1 gate
    
    """
    ...

@overload
def X1(qubit_addr: int) -> QGate:
    """
    Create a X1 gate
    
    """
    ...

@overload
def X1(qubit_addr_list: List[int]) -> QCircuit:
    """
    Create a X1 gate
    """
    ...

@overload
def Y(qubit: Qubit) -> QGate:
    """
    Create a Y gate
    
    """
    ...

@overload
def Y(qubit_list: QVec) -> QCircuit:
    """
    Create a Y gate
    
    """
    ...

@overload
def Y(qubit_addr: int) -> QGate:
    """
    Create a Y gate
    
    """
    ...

@overload
def Y(qubit_addr_list: List[int]) -> QCircuit:
    """
    Create a Y gate
    """
    ...

@overload
def Y1(qubit: Qubit) -> QGate:
    """
    Create a Y1 gate
    
    """
    ...

@overload
def Y1(qubit_list: QVec) -> QCircuit:
    """
    Create a Y1 gate
    
    """
    ...

@overload
def Y1(qubit_addr: int) -> QGate:
    """
    Create a Y1 gate
    
    """
    ...

@overload
def Y1(qubit_addr_list: List[int]) -> QCircuit:
    """
    Create a Y1 gate
    """
    ...

@overload
def Z(qubit: Qubit) -> QGate:
    """
    Create a Z gate
    
    """
    ...

@overload
def Z(qubit_list: QVec) -> QCircuit:
    """
    Create a Z gate
    
    """
    ...

@overload
def Z(qubit_addr: int) -> QGate:
    """
    Create a Z gate
    
    """
    ...

@overload
def Z(qubit_addr_list: List[int]) -> QCircuit:
    """
    Create a Z gate
    """
    ...

@overload
def Z1(qubit: Qubit) -> QGate:
    """
    Create a Z1 gate
    
    """
    ...

@overload
def Z1(qubit_list: QVec) -> QCircuit:
    """
    Create a Z1 gate
    
    """
    ...

@overload
def Z1(qubit_addr: int) -> QGate:
    """
    Create a Z1 gate
    
    """
    ...

@overload
def Z1(qubit_addr_list: List[int]) -> QCircuit:
    """
    Create a Z1 gate
    """
    ...

@overload
def _back(arg0: expression, arg1: Dict[var,numpy.ndarray[float64[m,n]]], arg2: Set[var]) -> None:
    """
    """
    ...

@overload
def _back(arg0: expression, arg1: Dict[var,numpy.ndarray[float64[m,n]]]) -> None:
    """
    """
    ...

@overload
def _back(arg0: var, arg1: Dict[var,numpy.ndarray[float64[m,n]]]) -> None:
    """
    """
    ...

@overload
def _back(arg0: var, arg1: Dict[var,numpy.ndarray[float64[m,n]]], arg2: Set[var]) -> None:
    """
    """
    ...

def accumulateProbability(probability_list: List[float]) -> List[float]:
    """
    Accumulate the probability from a prob list
    
    Args:
        probability_list: measured result in probability list form
    
    Returns:
        accumulated result
    """
    ...

def accumulate_probabilities(probability_list: List[float]) -> List[float]:
    """
    Accumulate the probability from a prob list
    
    Args:
        probability_list: measured result in probability list form
    
    Returns:
        accumulated result
    """
    ...

def accumulate_probability(probability_list: List[float]) -> List[float]:
    """
    Accumulate the probability from a prob list
    
    Args:
        probability_list: measured result in probability list form
    
    Returns:
        accumulated result
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
    """
    ...

@overload
def amplitude_encode(qubit: QVec, data: List[float], b_need_check_normalization: bool = True) -> QCircuit:
    """
    Encode the input double data to the amplitude of qubits
    
    """
    ...

@overload
def amplitude_encode(qubit: QVec, data: List[complex]) -> QCircuit:
    """
    Encode the input complex data to the amplitude of qubits
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

@overload
def average_gate_fidelity(state1: numpy.ndarray[complex128[m,n]], state2: List[complex]) -> float:
    """
    Get average_gate_fidelity
    
    """
    ...

@overload
def average_gate_fidelity(state1: numpy.ndarray[complex128[m,n]], state2: numpy.ndarray[complex128[m,n]]) -> float:
    """
    Get average_gate_fidelity
    """
    ...

def bin_to_prog(bin_data: List[int], qubit_list: QVec, cbit_list: List[ClassicalCondition], qprog: QProg) -> bool:
    """
    Parse binary data transfor to quantum program
    """
    ...

def bind_data(arg0: int, arg1: QVec) -> QCircuit:
    """
    Quantum bind data
    """
    ...

def bind_nonnegative_data(arg0: int, arg1: QVec) -> QCircuit:
    """
    Quantum bind nonnegative integer
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
    Free a cbit
    """
    ...

@overload
def cFree_all() -> None:
    """
    Free all cbits
    
    """
    ...

@overload
def cFree_all(cbit_list: List[ClassicalCondition]) -> None:
    """
    Free a list of cbits
    """
    ...

@overload
def calculate_quantum_volume(noise_qvm: NoiseQVM, qubit_list: List[List[int]], ntrials: int, shots: int = 1000) -> int:
    """
    calculate quantum volume
    
    """
    ...

@overload
def calculate_quantum_volume(cloud_qvm: QCloud, qubit_list: List[List[int]], ntrials: int, shots: int = 1000) -> int:
    """
    calculate quantum volume
    """
    ...

def cast_qprog_qcircuit(qprog: QProg) -> QCircuit:
    """
    Cast QProg to QCircuit
    """
    ...

def cast_qprog_qgate(qprog: QProg) -> QGate:
    """
    Cast QProg to QGate
    """
    ...

def cast_qprog_qmeasure(qprog: QProg) -> QMeasure:
    """
    Cast QProg to QMeasure
    """
    ...

def circuit_layer(qprog: QProg, ChipID: ChipID, qvm: QuantumMachine) -> list:
    """
    Quantum circuit layering
    """
    ...

def circuit_optimizer(qprog: QProg, optimizer_cir_vec: List[Tuple[QCircuit,QCircuit]] = [], mode_list: List[QCircuitOPtimizerMode] = []) -> QProg:
    """
    Optimize QCircuit
    """
    ...

def circuit_optimizer_by_config(qprog: QProg, config_file: str = 'QPandaConfig.json', mode_list: List[QCircuitOPtimizerMode] = []) -> QProg:
    """
    QCircuit optimizer
    """
    ...

def constModAdd(arg0: QVec, arg1: int, arg2: int, arg3: QVec, arg4: QVec) -> QCircuit:
    """
    Quantum modular adder
    """
    ...

def constModExp(arg0: QVec, arg1: QVec, arg2: int, arg3: int, arg4: QVec, arg5: QVec, arg6: QVec) -> QCircuit:
    """
    Quantum modular exponents
    """
    ...

def constModMul(arg0: QVec, arg1: int, arg2: int, arg3: QVec, arg4: QVec, arg5: QVec) -> QCircuit:
    """
    Quantum modular multiplier
    """
    ...

def convert_binary_data_to_qprog(machine: QuantumMachine, data: List[int]) -> QProg:
    """
    Parse  binary data to quantum program
    """
    ...

def convert_originir_str_to_qprog(originir_str: str, machine: QuantumMachine) -> list:
    """
    Trans OriginIR to QProg
    
    Args:
        originir_str: OriginIR string
        machine: initialized quantum machine
    
    Returns:
        list cotains QProg, qubit_list, cbit_list
    """
    ...

def convert_originir_to_qprog(file_path: str, machine: QuantumMachine) -> list:
    """
    Read OriginIR file and trans to QProg
    
    Args:
        file_path: OriginIR file path
        machine: initialized quantum machine
    
    Returns:
        list cotains QProg, qubit_list, cbit_list
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
        list cotains QProg, qubit_list, cbit_list
    """
    ...

@overload
def convert_qprog_to_binary(qprog: QProg, machine: QuantumMachine) -> List[int]:
    """
    Trans quantum program to binary data
    
    """
    ...

@overload
def convert_qprog_to_binary(qprog: QProg, machine: QuantumMachine, fname: str) -> None:
    """
    Store quantum program in binary file 
    """
    ...

def convert_qprog_to_originir(qprog: QProg, machine: QuantumMachine) -> str:
    """
    Convert QProg to OriginIR
    """
    ...

def convert_qprog_to_qasm(qprog: QProg, machine: QuantumMachine) -> str:
    """
    Convert QProg to QASM instruction string
    """
    ...

def convert_qprog_to_quil(qprog: QProg, machine: QuantumMachine) -> str:
    """
    Convert QProg to Quil
    """
    ...

@overload
def count_gate(quantum_prog: QProg) -> int:
    """
    Count quantum gate num under quantum program, quantum circuit
    
    """
    ...

@overload
def count_gate(quantum_circuit: QCircuit) -> int:
    """
    Count quantum gate num under quantum program, quantum circuit
    """
    ...

@overload
def count_qgate_num(quantum_prog: QProg, gtype: GateType = GateType.GATE_UNDEFINED) -> int:
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
def count_qgate_num(quantum_circuit: QCircuit, gtype: GateType = GateType.GATE_UNDEFINED) -> int:
    """
    Count quantum gate num under quantum circuit
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
    """
    ...

def create_empty_qprog() -> QProg:
    """
    Create an empty QProg Container
    """
    ...

@overload
def create_if_prog(classical_condition: ClassicalCondition, true_node: QProg) -> QIfProg:
    """
    Create a IfProg
    
    """
    ...

@overload
def create_if_prog(classical_condition: ClassicalCondition, true_node: QProg, false_node: QProg) -> QIfProg:
    """
    Create a IfProg
    """
    ...

def create_while_prog(classical_condition: ClassicalCondition, true_node: QProg) -> QWhileProg:
    """
    Create a WhileProg
    """
    ...

def crossEntropy(arg0: var, arg1: var) -> var:
    """
    """
    ...

def decompose_multiple_control_qgate(qprog: QProg, machine: QuantumMachine, config_file: str = 'QPandaConfig.json') -> QProg:
    """
    Decompose multiple control QGate
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
    """
    ...

def del_weak_edge2(topo_data: List[List[int]], max_connect_degree: int, sub_graph_set: List[int]) -> list:
    """
    Delete weakly connected edges
    """
    ...

def del_weak_edge3(topo_data: List[List[int]], sub_graph_set: List[int], max_connect_degree: int, lamda1: float, lamda2: float, lamda3: float) -> list:
    """
    Delete weakly connected edges
    """
    ...

def destroy_quantum_machine(machine: QuantumMachine) -> None:
    """
    Destroy a quantum machine
    
    Args:
        machine: type should be one of CPUQVM, CPUSingleThreadQVM, GPUQVM, NoiseQVM
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
def double_gate_xeb(cloud_qvm: QCloud, qubit0: Qubit, qubit1: Qubit, clifford_range: List[int], num_circuits: int, shots: int, gate_type: GateType = GateType.CZ_GATE) -> Dict[int,float]:
    """
    double gate xeb with WU YUAN chip
    
    """
    ...

@overload
def double_gate_xeb(noise_qvm: NoiseQVM, qubit0: Qubit, qubit1: Qubit, clifford_range: List[int], num_circuits: int, shots: int, gate_type: GateType = GateType.CZ_GATE) -> Dict[int,float]:
    """
    double gate xeb with WU YUAN chip
    """
    ...

@overload
def double_qubit_rb(qvm: NoiseQVM, qubit0: Qubit, qubit1: Qubit, clifford_range: List[int], num_circuits: int, shots: int, interleaved_gates: List[QGate] = []) -> Dict[int,float]:
    """
    double qubit rb with noise quantum virtual machine
    
    """
    ...

@overload
def double_qubit_rb(qvm: QCloud, qubit0: Qubit, qubit1: Qubit, clifford_range: List[int], num_circuits: int, shots: int, interleaved_gates: List[QGate] = []) -> Dict[int,float]:
    """
    double qubit rb with WU YUAN chip
    """
    ...

def draw_qprog_latex(prog: QProg, auto_wrap_len: int = 100, output_file: str = 'QCircuit.tex', with_logo: bool = False, itr_start: NodeIter = NodeIter(), itr_end: NodeIter = NodeIter()) -> str:
    """
    Convert a quantum prog/circuit to latex source code, and save the source code to file in current path with name QCircuit.tex
    """
    ...

def draw_qprog_latex_with_clock(prog: QProg, config_data: str = 'QPandaConfig.json', auto_wrap_len: bool = 100, output_file: int = 'QCircuit.tex', with_logo: str = False, itr_start: NodeIter = NodeIter(), itr_end: NodeIter = NodeIter()) -> str:
    """
    Convert a quantum prog/circuit to latex source code with time sequence, and save the source code to file in current path with name QCircuit.tex
    """
    ...

def draw_qprog_text(qprog: QProg, auto_wrap_len: int = 100, output_file: str = 'QCircuitTextPic.txt', itr_start: NodeIter = NodeIter(), itr_end: NodeIter = NodeIter()) -> str:
    """
    Convert a quantum prog/circuit to text-pic(UTF-8 code),
    and will save the text-pic in file named QCircuitTextPic.txt in the same time in current path
    """
    ...

def draw_qprog_text_with_clock(prog: QProg, config_data: str = 'QPandaConfig.json', auto_wrap_len: int = 100, output_file: str = 'QCircuitTextPic.txt', itr_start: NodeIter = NodeIter(), itr_end: NodeIter = NodeIter()) -> str:
    """
    Convert a quantum prog/circuit to text-pic(UTF-8 code) with time sequence,
    and will save the text-pic in file named QCircuitTextPic.txt in the same time in current path
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
    """
    ...

@overload
def eval(arg0: var, arg1: bool) -> numpy.ndarray[float64[m,n]]:
    """
    """
    ...

@overload
def eval(arg0: var) -> numpy.ndarray[float64[m,n]]:
    """
    """
    ...

def exp(arg0: var) -> var:
    """
    """
    ...

def expMat(arg0: complex, arg1: numpy.ndarray[complex128[m,n]], arg2: float) -> numpy.ndarray[complex128[m,n]]:
    """
    calculate the matrix power of e
    """
    ...

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
    """
    ...

def finalize() -> None:
    """
    Finalize the environment and destory global unique quantum machine.
    Use this before exit.
    """
    ...

def fit_to_gbk(utf8_str: str) -> str:
    """
    Special character conversion
    """
    ...

@overload
def flatten(qprog: QProg) -> None:
    """
    Flatten quantum program
    
    """
    ...

@overload
def flatten(qcircuit: QCircuit) -> None:
    """
    Flatten quantum circuit
    """
    ...

def getAllocateCMem() -> int:
    """
    Deprecated, use get_allocate_qubit_num instead
    """
    ...

def getAllocateQubitNum() -> int:
    """
    Deprecated, use get_allocate_cmem_num instead
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
    """
    ...

def get_all_used_qubits_to_int(qprog: QProg) -> List[int]:
    """
    Get all the used quantum bits addr in the input prog
    """
    ...

def get_allocate_cbits() -> List[ClassicalCondition]:
    """
    Get allocate cbits of QuantumMachine
    Returns:
        cbits list
    """
    ...

def get_allocate_cmem_num() -> int:
    """
    get allocate cmemnum
    """
    ...

def get_allocate_qubit_num() -> int:
    """
    get allocate qubit num
    """
    ...

def get_allocate_qubits() -> QVec:
    """
    Get allocated qubits of QuantumMachine
    
    Returns:
        qubits list
    """
    ...

def get_bin_data(qprog: QProg) -> List[int]:
    """
    Get quantum program binary data
    """
    ...

def get_bin_str(qprog: QProg, machine: QuantumMachine) -> str:
    """
    Transfor quantum program to string
    """
    ...

def get_circuit_optimal_topology(qprog: QProg, machine: QuantumMachine, max_connect_degree: int, config_file: str = 'QPandaConfig.json') -> List[List[int]]:
    """
    Get the optimal topology of the input circuit
    """
    ...

def get_clock_cycle(qpog: QProg) -> int:
    """
    Get quantum program clock cycle
    """
    ...

def get_complex_points(topo_data: List[List[int]], max_connect_degree: int) -> List[int]:
    """
    Get complex points
    """
    ...

def get_double_gate_block_topology(qprog: QProg) -> List[List[int]]:
    """
    get double gate block topology
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
    """
    ...

@overload
def get_qgate_num(quantum_prog: QProg) -> int:
    """
    Count quantum gate num under quantum program, quantum circuit
    
    """
    ...

@overload
def get_qgate_num(quantum_circuit: QCircuit) -> int:
    """
    Count quantum gate num under quantum program, quantum circuit
    
    """
    ...

@overload
def get_qgate_num(qprog: QProg) -> int:
    """
    Count quantum gate num under quantum program
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

def get_qstate() -> List[complex]:
    """
    Get quantum machine state vector
    """
    ...

def get_sub_graph(topo_data: List[List[int]]) -> List[int]:
    """
    Get sub graph
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
    """
    ...

def get_unsupport_qgate_num(qprog: QProg, support_gates: List[List[str]]) -> int:
    """
    Count quantum program unsupported gate numner
    """
    ...

def getstat(*args, **kwargs) -> Any:
    """
    Get the status of the Quantum machine
    
    """
    ...

@overload
def iSWAP(first_qubit: Qubit, second_qubit: Qubit) -> QGate:
    """
    Create a iSWAP gate
    
    """
    ...

@overload
def iSWAP(first_qubit_list: QVec, second_qubit_list: QVec) -> QCircuit:
    """
    Create a iSWAP gate
    
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
    Create a iSWAP gate
    
    """
    ...

@overload
def iSWAP(first_qubit: Qubit, second_qubit: Qubit, theta_angle: float) -> QGate:
    """
    Create a iSWAP gate
    
    """
    ...

@overload
def iSWAP(first_qubit_list: QVec, second_qubit_list: QVec, theta_angle: float) -> QCircuit:
    """
    Create a iSWAP gate
    
    """
    ...

@overload
def iSWAP(first_qubit_addr: int, second_qubit_addr: int, theta_angle: float) -> QGate:
    """
    Create a iSWAP gate
    
    """
    ...

@overload
def iSWAP(first_qubit_addr_list: List[int], second_qubit_addr_list: List[int], theta_angle: float) -> QCircuit:
    """
    Create a iSWAP gate
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
    """
    ...

def is_swappable(prog: QProg, nodeitr_1: NodeIter, nodeitr_2: NodeIter) -> bool:
    """
    Judge the specialed two NodeIters in qprog whether can be exchanged
    """
    ...

def iterative_amplitude_estimation(arg0: QCircuit, arg1: QVec, arg2: float, arg3: float) -> float:
    """
    estimate the probability corresponding to the ground state |1> of the last bit
    """
    ...

def ldd_decompose(qprog: QProg) -> QProg:
    """
    Decompose multiple control QGate
    """
    ...

def log(arg0: var) -> var:
    """
    """
    ...

@overload
def matrix_decompose(qubits: QVec, matrix: numpy.ndarray[complex128[m,n]], mode: DecompositionMode = DecompositionMode.QSD, b_positive_seq: bool = True) -> QCircuit:
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

def matrix_decompose_paulis(arg0: QuantumMachine, arg1: numpy.ndarray[float64[m,n]]) -> List[Tuple[float,QCircuit]]:
    """
    """
    ...

@overload
def measure_all(qubit_list: QVec, cbit_list: List[ClassicalCondition]) -> QProg:
    """
    Create a Measure operation
    
    """
    ...

@overload
def measure_all(qubit_addr_list: List[int], cbit_addr_list: List[int]) -> QProg:
    """
    Create a Measure operation
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
        Transformed QProg
    """
    ...

def planarity_testing(topo_data: List[List[int]]) -> bool:
    """
    planarity testing
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
    """
    ...

@overload
def qFree_all() -> None:
    """
    Free all qbits
    
    """
    ...

@overload
def qFree_all(qubit_list: QVec) -> None:
    """
    Free a list of qubits
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
    use quantum-walk algorithm to search target data, return QProg and search_result
    """
    ...

def quick_measure(qubit_list: QVec, shots: int) -> Dict[str,int]:
    """
    Quick measure
    
    Args:
        qubit_list: qubit list to measure
        shots: the repeat num  of measure operate
    
    Returns:
        result of quantum program
    """
    ...

def random_qcircuit(qvec: QVec, depth: int = 100, gate_type: List[str] = []) -> QCircuit:
    """
    Generate random quantum circuit
    """
    ...

def random_qprog(qubit_row: int, qubit_col: int, depth: int, qvm: QuantumMachine, qvec: QVec) -> QProg:
    """
    Generate random quantum program
    """
    ...

def recover_edges(topo_data: List[List[int]], max_connect_degree: int, candidate_edges: List[Tuple[int,List[int]]]) -> List[List[int]]:
    """
    Recover edges from the candidate edges
    """
    ...

def replace_complex_points(src_topo_data: List[List[int]], max_connect_degree: int, sub_topo_vec: List[Tuple[int,List[List[int]]]]) -> None:
    """
    Replacing complex points with subgraphs
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
        first is the final qubit register state, second is it's hit shot
    
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
        first is the final qubit register state, second is it's hit shot
    """
    ...

def sigmoid(arg0: var) -> var:
    """
    """
    ...

@overload
def single_qubit_rb(qvm: NoiseQVM, qubit: Qubit, clifford_range: List[int], num_circuits: int, shots: int, interleaved_gates: List[QGate] = []) -> Dict[int,float]:
    """
    Single qubit rb with noise quantum virtual machine
    
    """
    ...

@overload
def single_qubit_rb(qvm: QCloud, qubit: Qubit, clifford_range: List[int], num_circuits: int, shots: int, interleaved_gates: List[QGate] = []) -> Dict[int,float]:
    """
    Single qubit rb with WU YUAN chip
    """
    ...

def softmax(arg0: var) -> var:
    """
    """
    ...

def split_complex_points(complex_points: List[int], max_connect_degree: int, topo_data: List[List[int]], split_method: ComplexVertexSplitMethod = ComplexVertexSplitMethod.LINEAR) -> List[Tuple[int,List[List[int]]]]:
    """
    Splitting complex points into multiple points
    """
    ...

def stack(arg0: int, *args) -> var:
    """
    """
    ...

@overload
def state_fidelity(state1: List[complex], state2: List[complex]) -> float:
    """
    Get state fidelity
    
    """
    ...

@overload
def state_fidelity(matrix1: List[List[complex]], matrix2: List[List[complex]]) -> float:
    """
    Get matrix fidelity
    
    """
    ...

@overload
def state_fidelity(state1: List[complex], state2: List[List[complex]]) -> float:
    """
    Get state fidelity
    
    """
    ...

@overload
def state_fidelity(state1: List[List[complex]], state2: List[complex]) -> float:
    """
    Get state fidelity
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

def transform_to_base_qgate(qprog: QProg, machine: QuantumMachine, config_file: str = 'QPandaConfig.json') -> QProg:
    """
    Basic quantum - gate conversion
    """
    ...

def transpose(arg0: var) -> var:
    """
    """
    ...

def validate_double_qgate_type(gate_str_list: List[str]) -> list:
    """
    Get valid QGates and valid double QGate type
    """
    ...

def validate_single_qgate_type(gate_str_list: List[str]) -> list:
    """
    Get valid QGates and valid single bit QGate type
    """
    ...

def vector_dot(x: List[float], y: List[float]) -> float:
    """
    Inner product of vector x and y
    """
    ...

def virtual_z_transform(prog: QProg, quantum_machine: QuantumMachine, b_del_rz_gate: bool = False, config_data: str = 'QPandaConfig.json') -> None:
    """
    """
    ...

