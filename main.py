import math

# Funcion para imprimir la cantidad de monedas de cada denominacion que fueron utilizadas
def printUsedCoins(coins, denL): 
  coinsT = {coin:0 for coin in denL}
  start = len(coins) - 1

  # Establecemos la cantidad de veces que fue utilizada cada moneda
  while start != 0:
    j = coins[start]
    coinsT[denL[j]] += 1
    start -= int(denL[j])
    
  # Ciclamos la impresion de nuestro arreglo de denominaciones
  for coin in denL:
    print(f"Coin {coin} used {coinsT[coin]} times")

    
# Funcion para calcular la menor cantidad de monedas posible para dar el cambio
def minNumofCoins(T, denL):
  # Ayudantes (su proposito es ayudarnos con el calculo de monedas)
  n = (T+1) * [0]
  coins = (T+1) * [0]

  # Igualamos los valores del arreglo n a infinito y las del arreglo coins a -1
  for i in range(1, T+1):
    n[i] = math.inf
    coins[i] = -1

  # Utilizamos nuestros ayudantes para verificar que una denominacion se puede utilizar
  # Repetimos el proceso hasta conseguir el monto total de cambio
  for i in range(0, len(denL)):
    for j in range(1, T+1):
      if j >= int(denL[i]):
        # Usamos la denominacion mas grande hasta que ya no sea posible
        if n[j-(int(denL[i]))] + 1 < n[j]:
          n[j] = 1 + n[j-int(denL[i])]
          coins[j] = i
                  
  # Imprimimos cuantas monedas ocupamos de cada denominacion
  printUsedCoins(coins, denL)
  # Regresa la cantidad total de monedas utilizadas
  return n[T]

# Caso de Prueba
T = int(input("Enter the amount of change: "))
denL = list(input("Enter the list of available denominations: (Make sure to space your different denominations)\n").split())
print(f"Total numbers of coins: {minNumofCoins(T, denL)}")
