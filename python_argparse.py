import argparse

parser = argparse.ArgumentParser(description="this is what this program does")
parser.add_argument("-i", "--input", help="input file name")
parser.add_argument("-o", "--output", help="output file name",
					default="out")

args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

#====================================================
import sys

print("This is the name of the program:", sys.argv[0]) 
print("Argument List:", str(sys.argv))
