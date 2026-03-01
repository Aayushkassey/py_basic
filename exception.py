# import numbers


# a= int(input("Enter a divident: "))
# b= int(input("Enter a divisor"))
# # c= int(input("Enter another divident: "))
# # d= int(input("Enter another divisor: "))

# # print("Result is:", a / b)
# numbers = [1, 2, 3, 4, 5]
# i = int(input("Enter an index: "))


# try:
#     print("Result is:", a / b)
#     print(numbers[i])

# # except Exception as e:
# #     print(e)

# except ZeroDivisionError:
#     print(f"Error: Cannot Divide {a} by zero")

# except IndexError:
#     print(f"Error: Index {i} is out of range for the list.")

# except Exception as e:
#     print(f"An unknown error occurred. error: {e}")

# print("This access has been logged")

import time
empty= []
count= 0
while True:
    try:
        print("Hello!")
        time.sleep(1) 
        empty.append(count)
    except KeyboardInterrupt:
        print("You entered ctrl + break, but I want break")