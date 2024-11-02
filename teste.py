
def inverse_str (str): 
  str_reverse = ""
  for char in str:
    str_reverse = char + str_reverse  
  return str_reverse

str = "ABCDE"
print(inverse_str(str))