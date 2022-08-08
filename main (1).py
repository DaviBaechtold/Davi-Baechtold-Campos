import operator, time

ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
while True:
  try:
    st = []
    for tk in input("Coloque seu calculo (sem utilizar parenteses): ").split():
      start_time = time.time()
      if tk in ops:
        y,x = st.pop(),st.pop()
        z = ops[tk](x,y)
      else:
        z = float(tk)
      st.append(z)
    assert len(st)<=1
    if len(st)==1: 
      print(st.pop())
      print('%s segundos'%(time.time() - start_time))
  except EOFError:  break
  except:  print('Erro ao executar o codigo ou erro de formatação')