
# unhandled exception occurs  inside an except sections
# try:
#     open("database.sqlite")
# except OSError:
#     raise RuntimeError("unable to handle error")


#exce must be exception instance or none
def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc


# how to disable auomatic exception chaining
try:
    open('database.sqlite')
except OSError as ex:
    raise RuntimeError from None


