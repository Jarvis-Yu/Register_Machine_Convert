from __future__ import annotations
import sys
from enum import Enum, auto
from instrHandler import *
from typing import List

class instrType (Enum):
  MISSING   = (auto (), [])
  UNKNOWN   = (auto (), [])
  HELP      = (auto (), ["-h", "--help"])
  CODING1   = (auto (), ["-c1", "--coding1"])
  CODING2   = (auto (), ["-c2", "--coding2"])
  DECODING1 = (auto (), ["-d1", "--decoding1"])
  DECODING2 = (auto (), ["-d2", "--decoding2"])

  def isThis (self, token: str) -> bool:
    return token in self.value[1]

  @staticmethod
  def getType (token: str) -> instrType:
    for instr in list (instrType):
      if instr.isThis (token):
        return instr
    return instrType.UNKNOWN

  @staticmethod
  def getTypeFromArgs(argv: List[str]) -> Tuple[instrType, List[str]]:
    if (not argv):
      return (instrType.MISSING, argv[1:])
    instr: str = argv[0]
    return (instrType.getType (instr), argv[1:])

  @staticmethod
  def runInstr(instr: instrType, args: List[str]) -> int:
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

def main (argc: int, argv: List[str]) -> int:
  instr: instrType; args: List[str]
  instr, args = instrType.getTypeFromArgs (argv[1:])
  return instr.runInstr (instr, args)
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