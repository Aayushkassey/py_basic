# def my_generator():
#     for i in range(5):
#         print(i) 
 
# The reason you aren't seeing an output is that calling a '
# 'generator function does not actually run the code inside it. '
# 'It only creates the "engine," but it hasn't turned the key yet.
# When you write gen = my_generator(), 
# Python looks at the yield keyword and says: "Okay, this is a generator."
# " I won't run it now; I'll just hand back an object that knows how to run later."

def my_generator():
    for i in range(5):
        yield i  #yield is "See You in a Minute."
gen = my_generator()
print(dir(gen))
#step by step print
print(next(gen)) # print(gen) gives the object my_generator address location
print(next(gen))
print(next(gen))



#all printing that is in my_generator
# for j in gen:
#     print (j)


#here 0 is starting and 5 is ending and 2 is step , here is 0 included and 5 is excluded
for i in range(0,5,2):
    print(i)

