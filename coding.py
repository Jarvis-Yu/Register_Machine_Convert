from __future__ import annotations
from typing import List, Tuple

# <<x, y >>
def encode1 (a: int, b: int) -> int:
  return 2 ** a * (2 * b + 1)

# <x, y>
def encode2 (a: int, b: int) -> int:
  return encode1 (a, b) - 1

def decode1 (num: int) -> Tuple[int, int]:
  tmp: int = -1
  remain: int = 0
  while (remain == 0):
    remain = num % 2
    num = num // 2
    tmp += 1
  return (tmp, num)

def decode2 (num: int) -> Tuple[int, int]:
  return decode1 (num + 1)

def encodeList1 (nums: List[int]) -> int:
  return __encodeListWith (nums, encode1)

def encodeList2 (nums: List[int]) -> int:
  return __encodeListWith (nums, encode2)

def __encodeListWith (nums: List[int], encode: function) -> int:
  ret: int = 0
  for i in reversed (nums):
    ret = encode (i, ret)
  return ret

def decodeList1 (num: int) -> List[int]:
  return __decodeListWith (num, decode1)

def decodeList2 (num: int) -> List[int]:
  return __decodeListWith (num, decode2)

def __decodeListWith (num: int, decode: function) -> List[int]:
  ret: List[int] = []
  if (num == 0):
    return ret
  while (True):
    x: int; y: int
    x, num = decode (num)
    ret.append (x)
    if (num == 0):
      break
  return ret