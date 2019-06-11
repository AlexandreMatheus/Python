def desculpaspalavra(a, ab, val, c): 
    if c == 0 or a == 0 : 
        return 0

    if (ab[c-1] > a): 
        return desculpaspalavra(a, ab, val, c-1) 

    else: 
        return max(val[c-1] + desculpaspalavra(a-ab[c-1], ab, val, c-1), 
                   desculpaspalavra(a, ab, val, c-1)) 

t= 0
while True:
  c ,f = [int(x) for x in input().split()]
  if c == 0 and f == 0:
    break
  lenlista = []
  desculpas = []
  
  t+=1
  for i in range(f):
    temp = [int(x) for x in input().split()]
    lenlista.append(temp[0])
    desculpas.append(temp[1])

  print("Teste "+str(t)+":")
  print("Solução Gulosa: "+str(desculpaspalavra(c,lenlista,desculpas,f)))
  print()
