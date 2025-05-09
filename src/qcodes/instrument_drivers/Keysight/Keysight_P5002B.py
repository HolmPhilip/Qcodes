from typing import TYPE_CHECKING

from . import N52xx

if TYPE_CHECKING:
    from typing_extensions import Unpack

    from qcodes.instrument import VisaInstrumentKWArgs


class KeysightP5002B(N52xx.KeysightPNAxBase):
    def __init__(
        self, name: str, address: str, **kwargs: "Unpack[VisaInstrumentKWArgs]"
    ):
        super().__init__(
            name,
            address,
            min_freq=9e3,
            max_freq=9e9,
            min_power=-100,
            max_power=20,
            nports=2,
            **kwargs,
        )
