#How to raise exception
"""
This below line will show output as
Traceback (most recent call last):
  File "/....../raiseexceptiondemo.py", line 1, in <module>
    raise NameError('Moin! Moin!')
NameError: Moin! Moin!
"""
#raise NameError('Moin! Moin!')


# f an exception class is passed, it will be implicitly instantiated by calling its constructor with no arguments:
# shorthand for 'raise ValueError()'
"""
Traceback (most recent call last):
  File "/home/zermatt/Documents/python/errors&exception/raiseexceptiondemo.py", line 12, in <module>
    raise ValueError
ValueError
"""
#raise ValueError


# exception raised but dont intent to handle it
try:
    raise NameError('Hi There')
except NameError:
    print('An exception flew by')
    raise

