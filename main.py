print("Hello World!")

a = 1234
print( a // 1000)
print( a // 100 - a // 1000 * 10)
print( a // 10 - a // 100 * 10)
print( a // 1 - a // 10 * 10)

print ("----")
b = 12345
print( b % 10 )
print( (b % 100 - b % 10)//10)
print( (b % 1000 - b % 100)//100)
print( (b % 10000 - b % 1000)//1000)
print( (b % 100000 - b % 10000)//10000)
