# UnComment one by one example and run

# Simple finally example
# try:
#     raise KeyboardInterrupt
# finally:
#     print("Good Bye!!")


# return from finally
# def bool_return():
#     try:
#         return True
#     finally:
#         return False
#
#
# print(bool_return())



def div(x, y):
    try:
       result = x / y
    except ZeroDivisionError:
        print("div by zero")
    else :
        print("Result", result)
    finally:
        print("executing finally...")

print("------------")
div(12, 0)
print("------------")
div(12, 134)
print("------------")
div("1", "2")


