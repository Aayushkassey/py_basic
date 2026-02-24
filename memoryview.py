# my_bytearray = bytearray(b"Hello World!")
# my_memoryview = memoryview(my_bytearray)
# byte_array = bytearray('XYZ', 'utf-8')
# mv = memoryview(byte_array)
# print(mv[0])  # Output: 88 (ASCII value of 'X')
# print(mv[1])  # Output: 89 (ASCII value of 'Y')
# print(mv[2])  # Output: 90 (ASCII value of 'Z')
# print(bytes(mv[0:2]))

# def fn():
#     pass
# a = fn()
# if a == None:
#     print("a is None")

# def fn():
#     pass
# a= fn()
# if a is None:
#     print("a is None")  


a=int('100000')
b=int('100000')

print(a is b)
print (a == b)
