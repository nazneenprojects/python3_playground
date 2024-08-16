"""
#   Threading
An executable program.
The associated data needed by the program (variables, workspace, buffers, etc.)
The execution context of the program (State of the process)

imp definitions:
Thread Identifier: Unique id (TID) is assigned to every new thread
Stack pointer: Points to the thread’s stack in the process. The stack contains the local variables under the thread’s scope.
Program counter: a register that stores the address of the instruction currently being executed by a thread.
Thread state: can be running, ready, waiting, starting, or done.
Thread’s register set: registers assigned to thread for computations.
Parent process Pointer: A pointer to the Process control block (PCB) of the process that the thread lives on.
TCB-thread control block : all info is there in TCB

Multiple threads can exist within one process where:

Each thread contains its own register set and local variables (stored in the stack) .
All threads of a process share global variables (stored in heap) and the program code

Multithreading is defined as the ability of a processor to execute multiple threads concurrently.
In a simple, single-core CPU, it is achieved using frequent switching between threads. This is termed context switching . In context switching, the state of a thread is saved and the state of another thread is loaded whenever any interrupt (due to I/O or manually set) takes place. Context switching takes place so frequently that
all the threads appear to be running parallelly (this is termed multitasking ).
"""

import threading

def print_data(name):
    print(f"Happy Easter {name}")
def print_secret(key):
    print(f"Do not share {key}")

if __name__ == "__main__":
    t1 = threading.Thread(target=print_data("Flounder"),  args=(10,))
    t2 = threading.Thread(target=print_secret("Ariel"),  args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Now Done!")



