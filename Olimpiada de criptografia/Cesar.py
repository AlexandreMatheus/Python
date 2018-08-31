'''Script para criptografia estilo -Cesar- andando um numero de casas para frente ou para tras... '''

l1=["A" , "B" , "C" , "D" , "E" , "F" , "G" , "H" , "I" , "J" , "K" , "L" , "M" , "N" , "O" , "P" , "Q" , "R" , "S" , "T" , "U" , "V" , "W" , "X" , "Y" , "Z"] #lista do alfabeto em maiusculo
lado=input("para qual lado andar? (d ou e)") #pega qual lado andar
andar=int(input("quantas casas?"))#pega quantas casas andar
palavra=input("qual palavra/frase ?").upper() # pega a palavra e ja coloca tudo pra maiusculo
newpalavra='' #cria uma variavel nova para a palavra que vai ser transformada
while andar>26: #enquanto a entrada das casas for maior que 26 diminui 26 para dar index da lista
    andar-=26
while andar<0:#enquanto a entrada das casas for menor que 26 aumenta 26 para dar index da lista
    andar+=26

#se lado for -D- entra aqui ...###################
if lado == "d": 
  for letra in palavra: # anda na palavra letra por letra
    if letra==" ": # verifica se é espaço para não dar erro no codigo atual e ja adiciona um espaço na nova palavra
      newpalavra+=" "
    else:
      indexletra=l1.index(letra) # se não for espaço pega o indice da letra
      newpalavra+=l1[indexletra+andar] # adiciona na nova palavra a letra transformada
  print(newpalavra)
################################################


#se lado for -E- entra aqui ...###################
else:
  for letra in palavra: # anda na palavra letra por letra
    if letra==" ":# verifica se é espaço para não dar erro no codigo atual e ja adiciona um espaço na nova palavra
      newpalavra+=" "
    else:
      indexletra=l1.index(letra)# se não for espaço pega o indice da letra
      newpalavra+=l1[indexletra-andar]# adiciona na nova palavra a letra transformada
  print(newpalavra)
################################################
