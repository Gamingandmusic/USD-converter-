print("""
io_project_1.py
by Gamingandmusic
Currency converter, converts usd$ to another Currency.
""")
# inputs
name = input("name: ")
date = input("what's the date in mm/dd/yyyy: ")
usd = input("amount of money in USD$: ")

# Currency conversions

usd = float(usd)

cad = usd * 1.40

cad = float(cad)

gbp = usd * 1.27

gbp = float(gbp)

euro = usd * 0.94

euro = float(euro)

# print
print(name)

print("thanks for using this program")

print(date)

print("-------------------------------")

print("$")

print(usd)

print("€")

print(euro)

print("C$")

print(cad)

print("£")

print(gbp)

# ends program

input("press enter to quit")
