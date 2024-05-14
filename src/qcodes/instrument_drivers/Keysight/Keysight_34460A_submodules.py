from typing import TYPE_CHECKING

from .private.Keysight_344xxA_submodules import _Keysight_344xxA

if TYPE_CHECKING:
    from typing_extensions import Unpack

    from qcodes.instrument import VisaInstrumentKWArgs


class Keysight34460A(_Keysight_344xxA):
    """
    This is the qcodes driver for the Keysight 34460A Multimeter
    """

    def __init__(
        self,
        name: str,
        address: str,
        silent: bool = False,
        **kwargs: "Unpack[VisaInstrumentKWArgs]",
    ):
        super().__init__(name, address, silent, **kwargs)


class Keysight_34460A(Keysight34460A):
    """
    Alias for backwards compatibility.
    """
