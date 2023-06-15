import argparse

parser=argparse.ArgumentParser()

parser.add_argument('x', type=float)
parser.add_argument('y', type=float)
args = parser.parse_args()

result= args.x + args.y
print(f'The sum of {args.x} and {args.y} is {result}')


