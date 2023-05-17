import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="input file name")
parser.add_argument("-o", "--output", help="output file name",
					default="out")
args = parser.parse_args()
