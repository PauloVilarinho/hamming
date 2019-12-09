from handler import *


parity = True if input("chose parity(p=pair,o=odd)  ") == "o" else False
bits = input("enter the bits to get decoded  ")

x = BitHandler(parity,bits)

print(x.error)
