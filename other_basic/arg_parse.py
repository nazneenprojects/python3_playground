
import argparse

parser = argparse.ArgumentParser(description='Greet the user.')
parser.add_argument('name', type=str, help='The name of the user.')

args = parser.parse_args()

print(f"Hello, {args.name}!")


"""
    Run this python script using 
    python arg_parse.py Flounder

"""
