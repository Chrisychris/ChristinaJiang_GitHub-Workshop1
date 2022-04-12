price = float(input("Enter the price of the item(s): "))  #a)
change = 5 - price
print("Change: ", change)

toonies = change // 2  #num of toonies
print("toonies: ", toonies)
tooniesChange = change % 2  

loonies = (tooniesChange) // 1  #num of loonies
print("loonies: ", loonies)
looniesChange = (tooniesChange) % 1 

dimes = (looniesChange) // 0.1  #num of dimes
print("dimes: ", dimes)
dimesChange = (looniesChange) % 0.1

nickels = (dimesChange) // 0.05  #num of nickels
print("nickels: ", nickels)
nickelsChange = (dimesChange) % 0.05

pennies = (nickelsChange) // 0.01  #num of pennies
print("pennies: ", pennies)

numOfCoins = toonies + loonies + dimes + nickels + pennies
print("number of coins: ", numOfCoins)

numOfDime = change / 0.1  #b)
print("number of dimes: ", numOfDime)