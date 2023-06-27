def filter(request):
  # get all character from beginning to position 'name='
  clean_rq = request[:request.index("name=") + 5]
  # get all character from position 'name=' to end
  remain_rq = request[request.index("name=") +5:] 
  # check in remaining request string has special characters
  for char in remain_rq:     
    if char.isalnum():
      clean_rq += char
  return clean_rq
def filter2(request):
  special_char = ['/','<','>','.',')','(']
  strs = request[:request.index("name=") +5]
  str_clean = ''.join(char for char in request[request.index('name=')+5:] if char not in special_char)
  strs += str_clean
  return strs

 