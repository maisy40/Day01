class Solution2:
  def isValid(self, s:str) -> bool:
    dic = {
      '(' : ')',
      '{' : '}',
      '[' : ']'
    }
    stack = []
    
    for c in s:
      if c in dic:
        stack.append(c)

      elif not stack or dic[stack.pop()] != c:
        return False

    if stack:
      return False

    return True