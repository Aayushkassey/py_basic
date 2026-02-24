my_bytes = bytearray(b"Hello World!")
print(my_bytes) 

# print(my_bytes[0])  # Output: 72 (ASCII value of 'H')

my_bytes[7] = my_bytes[7] - 32  # Change 'W' to 'w' (ASCII value of 'w' is 119)
print(my_bytes)  # Output: bytearray(b'Hello, world!')  

