import argparse
import sys

def get_args():
	# create an instance of the ArgumentParser class	
	parser = argparse.ArgumentParser()
	# mandatory argument, inputted through --a1, stored in this script as 'a1'
	parser.add_argument('--a1', required=True, dest='a1', help='First argument, mandatory')
	# optional argument
	parser.add_argument('--a2', required=False, dest='a2', help='Second arg, optional')
	# mandatory argument, will be taken as a string, can be only one of 'x' or 'y'
	parser.add_argument('--a3', required=True, dest='a3', choices=['x', 'y'], type=str, help='Limited choices, type checking')
	# parse the args and store in parsed_args
	# -h can also be used to display the help values
	parsed_args = parser.parse_args()
	return parsed_args

# main function gets tuple of arguments from get_args()
def main(parsed_args):
	print(parsed_args)

if __name__ == '__main__':
	# call main with the return val of get_args
	main(get_args())
	sys.exit(0)
