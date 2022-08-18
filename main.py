class Solution:
  def isValid(self, s:str)->bool:
    stack = []
    
    for c in s:
      if len(stack) == 0: # 최초의 stack이 비어있더라도 loop진행중 stack이 비워지면 다시 채워 넣기. 
        stack.append(c)
      elif stack[-1] == "{" and c == "}":
        stack.pop()
      elif stack[-1] == "(" and c == ")":
        stack.pop()
      elif stack[-1] == "[" and c == "]":
        stack.pop()
      else:
        stack.append(c)

    # stack이 일치하는 경우 pop시켜서 비워주기 때문에 len이 0일 경우  True반환
    if len(stack) == 0:
      return True
    else:
      return False
        