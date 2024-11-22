print("Hello World!")

r = None
print(id(r))
r =1
print(r)
print(id(r))
r = "it"
print(r)
print(id(r))

import sys
z = complex(0, 0)
print(sys.getsizeof(z))
