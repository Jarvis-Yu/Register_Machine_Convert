from __future__ import annotations
from typing import List
from coding import *

def encodeStatement (statement: str) -> int:
  tokens: List[str] = statement.split()
  if (not tokens):
    return -1
  i: int; j: int; k: int
  if (tokens[0][:2] == "R+"):
    i = int (tokens[0][2:])
    j = int (tokens[2][1:])
    return encode1 (2*i, j)
  elif (tokens[0][:2] == "R-"):
    i = int (tokens[0][2:])
    j = int (tokens[2][1:])
    k = int (tokens[3][1:])
    return encode1 (2*i+1, encode2 (j, k))
  elif (tokens[0] == "HALT"):
    return 0
  else:
    return -1

def decodeStatement (num: int) -> str:
  if (num == 0):
    return "HALT"
  i: int; j: int; k: int
  i, j = decode1 (num)
  if (i % 2 == 0):  # R+
    i //= 2
    return "R+%d -> L%d"%(i, j)
  else:
    i //= 2
    j, k = decode2 (j)
    return "R-%d -> L%d L%d"%(i, j, k)