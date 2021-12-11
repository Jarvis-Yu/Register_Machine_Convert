from typing import NoReturn, Tuple, List
from main import argsCheckMissing
from coding import *

def missing () -> NoReturn:
  print ("[!] Argument Missing")

def unknown () -> NoReturn:
  print ("[!] Unknown Instruction")

def help (argv: List[str]) -> NoReturn:
  return

# ⟪x, y⟫ = 2^x * (2y + 1)
def coding1Arg (argv: List[str]) -> int:
  if (not argsCheckMissing (argv, 2)):
    return -1
  x: int = int (argv[0])
  y: int = int (argv[1])
  return encode1 (x, y)

# <x, y> = 2^x * (2y + 1) - 1
def coding2Arg (argv: List[str]) -> int:
  if (not argsCheckMissing (argv, 2)):
    return -1
  x: int = int (argv[0])
  y: int = int (argv[1])
  return encode2 (x, y)

def decoding1Arg (argv: List[str]) -> Tuple[int, int]:
  if (not argsCheckMissing (argv, 2)):
    return -1
  return decode1 (int (argv[0]))

def decoding2Arg (argv: List[str]) -> Tuple[int, int]:
  if (not argsCheckMissing (argv, 2)):
    return -1
  return decode2 (int (argv[0]))
