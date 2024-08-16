"""
Python does automatic memory management (reference counting for most objects and garbage collection to eliminate cycles).
The memory is freed shortly after the last reference to it has been eliminated.

The weakref module provides tools for tracking objects without creating a reference. When the object is no longer needed,
it is automatically removed from a weakref table and a callback is triggered for weakref objects.
"""

# applications include caching objects that are expensive to create

import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

if __name__ == "__main__":
    a = A(10)  # create a reference
    d = weakref.WeakValueDictionary()
    d['primary'] = a  # does not create a reference

    print(d['primary'])  # fetch the object if it is still alive
    del a
    gc.collect()
    try:
        print(d['primary'])
    except Exception as e:
        raise e


