import sys
from enum import Enum
from strHelp import isOneOf
from instrHandler import *

class instrType (Enum):
  MISSING   = 0
  UNKNOWN   = 1
  HELP      = 9
  CODING1   = 10
  CODING2   = 11
  DECODING1 = 12
  DECODING2 = 13

def getInstrType (argc: int, argv: list[str]) -> instrType:
  if (argc < 2):
    return instrType.MISSING
  instr: str = argv[1]
  if   (isOneOf (instr, ["-h", "--help"])):
    return instrType.HELP
  elif (isOneOf (instr, ["-c1", "--coding1"])):
    return instrType.CODING1
  elif (isOneOf (instr, ["-c2", "--coding2"])):
    return instrType.CODING2
  elif (isOneOf (instr, ["-d1", "--decoding1"])):
    return instrType.DECODING1
  elif (isOneOf (instr, ["-d2", "--decoding2"])):
    return instrType.DECODING2
  else:
    return instrType.UNKNOWN

def main (argc: int, argv: list[str]) -> int:
  instr: instrType = getInstrType (argc, argv)
  args: list[str] = argv[2:]
  if   (instr == instrType.MISSING):
    missing ()
  elif (instr == instrType.UNKNOWN):
    unknown ()
  elif (instr == instrType.HELP):
    help (args)
  elif (instr == instrType.CODING1):
    print (coding1 (args))
  elif (instr == instrType.CODING2):
    print (coding2 (args))
  elif (instr == instrType.DECODING1):
    print (decoding1 (args))
  elif (instr == instrType.DECODING2):
    print (decoding2 (args))
  return 0

if __name__ == "__main__":
  sys.exit (main (len (sys.argv), sys.argv))