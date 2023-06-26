from typing import Any, Dict, List, Tuple

from typing import Set
from typing import overload
import numpy

class FermionOperator:
    """
    """
    @overload
    def __init__(self) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: float) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: complex) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: str, arg1: complex) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: Dict[str,complex]) -> None:
        """
        """
        ...

    def data(self) -> List[Tuple[Tuple[List[Tuple[int,bool]],str],complex]]:
        """
        """
        ...

    def error_threshold(self) -> float:
        """
        """
        ...

    def isEmpty(self) -> bool:
        """
        """
        ...

    def is_empty(self) -> bool:
        """
        """
        ...

    def normal_ordered(self) -> FermionOperator:
        """
        """
        ...

    def setErrorThreshold(self, arg0: float) -> None:
        """
        """
        ...

    def set_error_threshold(self, arg0: float) -> None:
        """
        """
        ...

    def toString(self) -> str:
        """
        """
        ...

    def to_string(self) -> str:
        """
        """
        ...

    @overload
    def __add__(self, arg0: FermionOperator) -> FermionOperator:
        """
        """
        ...

    @overload
    def __add__(self, arg0: complex) -> FermionOperator:
        """
        """
        ...

    def __iadd__(self, arg0: FermionOperator) -> FermionOperator:
        """
        """
        ...

    def __imul__(self, arg0: FermionOperator) -> FermionOperator:
        """
        """
        ...

    def __isub__(self, arg0: FermionOperator) -> FermionOperator:
        """
        """
        ...

    @overload
    def __mul__(self, arg0: FermionOperator) -> FermionOperator:
        """
        """
        ...

    @overload
    def __mul__(self, arg0: complex) -> FermionOperator:
        """
        """
        ...

    def __radd__(self, arg0: complex) -> FermionOperator:
        """
        """
        ...

    def __rmul__(self, arg0: complex) -> FermionOperator:
        """
        """
        ...

    def __rsub__(self, arg0: complex) -> FermionOperator:
        """
        """
        ...

    @overload
    def __sub__(self, arg0: FermionOperator) -> FermionOperator:
        """
        """
        ...

    @overload
    def __sub__(self, arg0: complex) -> FermionOperator:
        """
        """
        ...


class PauliOperator:
    """
    """
    @overload
    def __init__(self) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: complex) -> None:
        """
        """
        ...

    @overload
    def __init__(self, matrix: numpy.ndarray[numpy.float64[m,n]], is_reduce_duplicates: bool = False) -> None:
        """
        """
        ...

    @overload
    def __init__(self, key: str, value: complex, is_reduce_duplicates: bool = False) -> None:
        """
        """
        ...

    @overload
    def __init__(self, pauli_map: Dict[str,complex], is_reduce_duplicates: bool = False) -> None:
        """
        """
        ...

    def dagger(self) -> PauliOperator:
        """
        """
        ...

    def data(self) -> List[Tuple[Tuple[Dict[int,str],str],complex]]:
        """
        """
        ...

    def error_threshold(self) -> float:
        """
        """
        ...

    def getMaxIndex(self) -> int:
        """
        """
        ...

    def get_max_index(self) -> int:
        """
        """
        ...

    def isAllPauliZorI(self) -> bool:
        """
        """
        ...

    def isEmpty(self) -> bool:
        """
        """
        ...

    def is_all_pauli_z_or_i(self) -> bool:
        """
        """
        ...

    def is_empty(self) -> bool:
        """
        """
        ...

    def reduce_duplicates(self) -> None:
        """
        """
        ...

    def remapQubitIndex(self, arg0: Dict[int,int]) -> PauliOperator:
        """
        """
        ...

    def remap_qubit_index(self, arg0: Dict[int,int]) -> PauliOperator:
        """
        """
        ...

    def setErrorThreshold(self, arg0: float) -> None:
        """
        """
        ...

    def set_error_threshold(self, arg0: float) -> None:
        """
        """
        ...

    def toHamiltonian(self, arg0: bool) -> List[Tuple[Dict[int,str],float]]:
        """
        """
        ...

    def toString(self) -> str:
        """
        """
        ...

    def to_hamiltonian(self, arg0: bool) -> List[Tuple[Dict[int,str],float]]:
        """
        """
        ...

    def to_matrix(self) -> numpy.ndarray[numpy.complex128[m,n]]:
        """
        """
        ...

    def to_string(self) -> str:
        """
        """
        ...

    @overload
    def __add__(self, arg0: PauliOperator) -> PauliOperator:
        """
        """
        ...

    @overload
    def __add__(self, arg0: complex) -> PauliOperator:
        """
        """
        ...

    def __iadd__(self, arg0: PauliOperator) -> PauliOperator:
        """
        """
        ...

    def __imul__(self, arg0: PauliOperator) -> PauliOperator:
        """
        """
        ...

    def __isub__(self, arg0: PauliOperator) -> PauliOperator:
        """
        """
        ...

    @overload
    def __mul__(self, arg0: PauliOperator) -> PauliOperator:
        """
        """
        ...

    @overload
    def __mul__(self, arg0: complex) -> PauliOperator:
        """
        """
        ...

    def __radd__(self, arg0: complex) -> PauliOperator:
        """
        """
        ...

    def __rmul__(self, arg0: complex) -> PauliOperator:
        """
        """
        ...

    def __rsub__(self, arg0: complex) -> PauliOperator:
        """
        """
        ...

    @overload
    def __sub__(self, arg0: PauliOperator) -> PauliOperator:
        """
        """
        ...

    @overload
    def __sub__(self, arg0: complex) -> PauliOperator:
        """
        """
        ...


class VarFermionOperator:
    """
    """
    @overload
    def __init__(self) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: float) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: complex_var) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: str, arg1: complex_var) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: Dict[str,complex_var]) -> None:
        """
        """
        ...

    def data(self) -> List[Tuple[Tuple[List[Tuple[int,bool]],str],complex_var]]:
        """
        """
        ...

    def error_threshold(self) -> float:
        """
        """
        ...

    def isEmpty(self) -> bool:
        """
        """
        ...

    def is_empty(self) -> bool:
        """
        """
        ...

    def normal_ordered(self) -> VarFermionOperator:
        """
        """
        ...

    def setErrorThreshold(self, arg0: float) -> None:
        """
        """
        ...

    def set_error_threshold(self, arg0: float) -> None:
        """
        """
        ...

    def toString(self) -> str:
        """
        """
        ...

    def to_string(self) -> str:
        """
        """
        ...

    @overload
    def __add__(self, arg0: VarFermionOperator) -> VarFermionOperator:
        """
        """
        ...

    @overload
    def __add__(self, arg0: complex_var) -> VarFermionOperator:
        """
        """
        ...

    def __iadd__(self, arg0: VarFermionOperator) -> VarFermionOperator:
        """
        """
        ...

    def __imul__(self, arg0: VarFermionOperator) -> VarFermionOperator:
        """
        """
        ...

    def __isub__(self, arg0: VarFermionOperator) -> VarFermionOperator:
        """
        """
        ...

    @overload
    def __mul__(self, arg0: VarFermionOperator) -> VarFermionOperator:
        """
        """
        ...

    @overload
    def __mul__(self, arg0: complex_var) -> VarFermionOperator:
        """
        """
        ...

    def __radd__(self, arg0: complex_var) -> VarFermionOperator:
        """
        """
        ...

    def __rmul__(self, arg0: complex_var) -> VarFermionOperator:
        """
        """
        ...

    def __rsub__(self, arg0: complex_var) -> VarFermionOperator:
        """
        """
        ...

    @overload
    def __sub__(self, arg0: VarFermionOperator) -> VarFermionOperator:
        """
        """
        ...

    @overload
    def __sub__(self, arg0: complex_var) -> VarFermionOperator:
        """
        """
        ...


class VarPauliOperator:
    """
    """
    @overload
    def __init__(self) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: float) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: complex_var) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: str, arg1: complex_var) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0: Dict[str,complex_var]) -> None:
        """
        """
        ...

    def dagger(self) -> VarPauliOperator:
        """
        """
        ...

    def data(self) -> List[Tuple[Tuple[Dict[int,str],str],complex_var]]:
        """
        """
        ...

    @overload
    def error_threshold(self) -> float:
        """
        """
        ...

    @overload
    def error_threshold(self) -> float:
        """
        """
        ...

    def getMaxIndex(self) -> int:
        """
        """
        ...

    def get_maxIndex(self) -> int:
        """
        """
        ...

    def isAllPauliZorI(self) -> bool:
        """
        """
        ...

    def isEmpty(self) -> bool:
        """
        """
        ...

    def is_all_pauli_z_or_i(self) -> bool:
        """
        """
        ...

    def is_empty(self) -> bool:
        """
        """
        ...

    def remapQubitIndex(self, arg0: Dict[int,int]) -> VarPauliOperator:
        """
        """
        ...

    def remap_qubit_index(self, arg0: Dict[int,int]) -> VarPauliOperator:
        """
        """
        ...

    def setErrorThreshold(self, arg0: float) -> None:
        """
        """
        ...

    def set_error_threshold(self, arg0: float) -> None:
        """
        """
        ...

    def toHamiltonian(self, arg0: bool) -> List[Tuple[Dict[int,str],float]]:
        """
        """
        ...

    def toString(self) -> str:
        """
        """
        ...

    def to_hamiltonian(self, arg0: bool) -> List[Tuple[Dict[int,str],float]]:
        """
        """
        ...

    def to_string(self) -> str:
        """
        """
        ...

    @overload
    def __add__(self, arg0: VarPauliOperator) -> VarPauliOperator:
        """
        """
        ...

    @overload
    def __add__(self, arg0: complex_var) -> VarPauliOperator:
        """
        """
        ...

    def __iadd__(self, arg0: VarPauliOperator) -> VarPauliOperator:
        """
        """
        ...

    def __imul__(self, arg0: VarPauliOperator) -> VarPauliOperator:
        """
        """
        ...

    def __isub__(self, arg0: VarPauliOperator) -> VarPauliOperator:
        """
        """
        ...

    @overload
    def __mul__(self, arg0: VarPauliOperator) -> VarPauliOperator:
        """
        """
        ...

    @overload
    def __mul__(self, arg0: complex_var) -> VarPauliOperator:
        """
        """
        ...

    def __radd__(self, arg0: complex_var) -> VarPauliOperator:
        """
        """
        ...

    def __rmul__(self, arg0: complex_var) -> VarPauliOperator:
        """
        """
        ...

    def __rsub__(self, arg0: complex_var) -> VarPauliOperator:
        """
        """
        ...

    @overload
    def __sub__(self, arg0: VarPauliOperator) -> VarPauliOperator:
        """
        """
        ...

    @overload
    def __sub__(self, arg0: complex_var) -> VarPauliOperator:
        """
        """
        ...


class complex_var:
    """
    """
    @overload
    def __init__(self) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0) -> None:
        """
        """
        ...

    @overload
    def __init__(self, arg0, arg1) -> None:
        """
        """
        ...

    def imag(self, *args, **kwargs) -> Any:
        """
        """
        ...

    def real(self, *args, **kwargs) -> Any:
        """
        """
        ...

    def __add__(self, arg0: complex_var) -> complex_var:
        """
        """
        ...

    def __mul__(self, arg0: complex_var) -> complex_var:
        """
        """
        ...

    def __sub__(self, arg0: complex_var) -> complex_var:
        """
        """
        ...

    def __truediv__(self, arg0: complex_var) -> complex_var:
        """
        """
        ...


def i(arg0: int) -> PauliOperator:
    """
    construct a pauli i operator
    
    Args:
        int: pauli operate index
    
    Returns:
        pauli operator i  
    Raises:
        run_fail: An error occurred in construct a pauli i operator
    
    """
    ...

def matrix_decompose_hamiltonian(arg0: numpy.ndarray[numpy.float64[m,n]]) -> PauliOperator:
    """
    decompose matrix into hamiltonian
    
    Args:
        quantum_machine: quantum machine
        matrix: 2^N *2^N double matrix 
    
    Returns:
        result : hamiltonian
    """
    ...

def trans_Pauli_operator_to_vec(arg0: PauliOperator) -> List[float]:
    """
    Transfrom Pauli operator to vector
    """
    ...

def trans_vec_to_Pauli_operator(arg0: List[float]) -> PauliOperator:
    """
    Transfrom vector to pauli operator
    """
    ...

def x(index: int) -> PauliOperator:
    """
    construct a pauli x operator
    
    Args:
        int: pauli operate index
    
    Returns:
        pauli operator x  
    Raises:
        run_fail: An error occurred in construct a pauli x operator
    
    """
    ...

def y(arg0: int) -> PauliOperator:
    """
    construct a pauli y operator
    
    Args:
        int: pauli operate index
    
    Returns:
        pauli operator y  
    Raises:
        run_fail: An error occurred in construct a pauli y operator
    
    """
    ...

def z(arg0: int) -> PauliOperator:
    """
    construct a pauli z operator
    
    Args:
        int: pauli operate index
    
    Returns:
        pauli operator z  
    Raises:
        run_fail: An error occurred in construct a pauli z operator
    
    """
    ...

