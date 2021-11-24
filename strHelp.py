def isOneOf (compared: str, ss: list[str]) -> bool:
  for s in ss:
    if compared == s:
      return True
  return False