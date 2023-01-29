text = "Marlin e dory sairam para procurar o Nemo"
convertStringInArray = text.split()
posicion = convertStringInArray.index('Nemo') + 1
if posicion >= 0:
  print("I found Nemo at %d!" %posicion)
else:
  print("I can't find Nemo :(" )
