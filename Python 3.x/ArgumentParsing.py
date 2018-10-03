import argparse
import sys

def get_args():
	
	parser = argparse.ArgumentParser()
	parser.add_argument('--a1', required=True, dest='a1', help='First argument, mandatory')
	parser.add_argument('--a2', required=False, dest='a2', help='Second arg, optional')
	parser.add_argument('--a3', required=True, dest='a3', choices=['x', 'y'], type=str, help='Limited choices, type checking')

	parsed_args = parser.parse_args()
	return parsed_args

def main(parsed_args):
	print(parsed_args)

if __name__ == '__main__':
	main(get_args())
	sys.exit(0)
