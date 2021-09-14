from enum import Enum
from datetime import datetime

import numpy as np

# import MetaTrader5 as mt5
# from MetaTrader5 import SymbolInfo as MtSymbolInfo


class Timeframe(Enum):
    M1 = 1
    M2 = 2
    M3 = 3
    M4 = 4
    M5 = 5
    M6 = 6
    M10 = 10
    M12 = 12
    M15 = 15
    M20 = 20
    M30 = 30
    H1 = 1  | 0x4000
    H2 = 2  | 0x4000
    H4 = 4  | 0x4000
    H3 = 3  | 0x4000
    H6 = 6  | 0x4000
    H8 = 8  | 0x4000
    H12 = 12 | 0x4000
    D1 = 24 | 0x4000
    W1 = 1  | 0x8000
    MN1 = 1  | 0xC000



# def initialize() -> bool:
#     return mt5.initialize()


# def shutdown() -> None:
#     mt5.shutdown()


# def copy_rates_range(symbol: str, timeframe: Timeframe, date_from: datetime, date_to: datetime) -> np.ndarray:
#     return mt5.copy_rates_range(symbol, timeframe.value, date_from, date_to)


# def symbol_info(symbol: str) -> MtSymbolInfo:
#     return mt5.symbol_info(symbol)
