from typing import NoReturn, Tuple, List

def missing () -> NoReturn:
  # TODO
  return

def unknown () -> NoReturn:
  # TODO
  return

def help (argv: List[str]) -> NoReturn:
  # TODO
  return

# ⟪x, y⟫ = 2^x * (2y + 1)
def coding1 (argv: List[str]) -> int:
  # TODO: Assume there are two arguments
  x: int = int (argv[0])
  y: int = int (argv[1])
  return 2 ** x * (2 * y + 1)

# <x, y> = 2^x * (2y + 1) - 1
def coding2 (argv: List[str]) -> int:
  # TODO: Assume there are two arguments
  return coding1 (argv) - 1

def __decoding (num: int) -> Tuple[int, int]:
  y: int = -1
  remain: int = 0
  while (remain == 0):
    remain = num % 2
    num = int (num / 2)
    y += 1
  return (y, num)

def decoding1 (argv: List[str]) -> Tuple[int, int]:
  # TODO: Assume there are one arguments
  return __decoding (int (argv[0]))

def decoding2 (argv: List[str]) -> Tuple[int, int]:
  # TODO: Assume there are one arguments
  return __decoding (int (argv[0]) + 1)