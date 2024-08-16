import sys

# print(sys.argv)                     # Common utility scripts often need to process command line arguments.
                                    # These arguments are stored in the sys module’s argv attribute as a list

"""
Run  from command line as below and get output
 >> python CommandLineArg.py hello world 123
>> ['CommandLineArg.py', 'hello', 'world', '123']
"""

# ----------------------------------------------------------------------------
import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)

""""
When run at the command line with python top.py --lines=5 alpha.txt beta.txt, 
the script sets args.lines to 5 and args.filenames to ['alpha.txt', 'beta.txt'].
"""