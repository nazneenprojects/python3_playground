def this_fails():
    x = 1/0

def my_data():
    data = int('abs')

try:
    #this_fails()
    my_data()
except ZeroDivisionError as err:
    print('Handling run time error:', err)
except ValueError as err:
    print("Handling run time exception from function" , err)
else :
    print("something went wrong")



