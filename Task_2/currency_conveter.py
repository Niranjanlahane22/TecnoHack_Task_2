with open('Currency.txt') as f:lines = f.readline()
currencyDict = {}
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]

amount = int(input("Enter Amount : \n"))
print("Enter the name of the currency you want to convert this amount to ? Available option : \n")
[print(item) for item in currencyDict.keys()]
currency = input("please enter one of these values :")
print(
    f"{amount}INR is equal to {amount *float (currencyDict[currency])}{currency}")
