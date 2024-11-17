import numpy as np

np1=np.array([1,2,3,4,5,6])

print(np1.shape)
print(np1) # length


# Range 
np2 = np.arange(0,10,2)
print(np2)

# Zeros 
np3 = np.zeros(10)
print(np3)

np4 = np.zeros((2,10))
print(np4)

# Full
np5 = np.full((10),6)
print(np5) 

# sqrt each element

print(np.sqrt(np1))


# abs value of each element

print(np.absolute(np1))

#exponents of each element

print(np.exp(np1))

# min / max 

print(np.min(np1),np.max(np1))

# Sign of each element

print(np.sign(np1))

# Triangular sin cos log

np6=np1.copy()

print(np6)
