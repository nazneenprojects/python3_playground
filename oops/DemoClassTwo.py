class DemoClassTwo:
    """
    A Simple class to demo attribute references and instantiation
    """

    def __init__(self, author_name, email):
        self.author = author_name
        self.email = email


x = DemoClassTwo("Nazneen Mulani", 'naz18mulani@gmail.com')
print(x)
print(x.author, x.email)

