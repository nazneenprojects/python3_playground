def fun1(self, x, y):
    print("You are going to find min here in fun1 for", x , " & ", y)
    return "Min is:", min(x, x + y)





class DemoClass:
    f = fun1

    def local_fun(self):
        return "you are inside local_fun function"

    def __init__(self):
        self.temp_var = self.local_fun()

if __name__ == '__main__':
        instance = DemoClass()
        print(instance.local_fun())  # Correct way to call an instance method
        print(instance.f(2, 3))  # Correct way to call an instance method
        print(instance.temp_var)
