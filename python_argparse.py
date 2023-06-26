import argparse
import sys

parser = argparse.ArgumentParser(description="this is what this program does")
parser.add_argument("-i", "--input", help="input file name")
parser.add_argument("-o", "--output", help="output file name",
					default="out")

args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])
