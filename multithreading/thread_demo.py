"""
The _thread Module
The _thread module, also known as the low-level thread module, has been a part of Python's standard library since version 2.
 It offers a basic API for thread management, supporting concurrent execution of threads within a shared global data space. The module includes simple locks (mutexes) for synchronization purposes.

The threading Module
The threading module, introduced in Python 2.4, builds upon _thread to provide a higher-level and more comprehensive threading API.
It offers powerful tools for managing threads, making it easier to work with threads in Python applications.
"""

# This thread module is having limited capability as compare to threading
import _thread
import time

def print_name(name, *arg):
   print(name, *arg)

name="Coding..."
_thread.start_new_thread(print_name, (name, 1))
_thread.start_new_thread(print_name, (name, 1, 2))

time.sleep(0.5)