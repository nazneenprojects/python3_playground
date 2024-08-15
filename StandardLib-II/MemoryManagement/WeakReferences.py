"""
Python does automatic memory management (reference counting for most objects and garbage collection to eliminate cycles).
The memory is freed shortly after the last reference to it has been eliminated.

The weakref module provides tools for tracking objects without creating a reference. When the object is no longer needed,
it is automatically removed from a weakref table and a callback is triggered for weakref objects.
"""