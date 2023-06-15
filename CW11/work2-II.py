import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument("path", type=str)
parser.add_argument("--size", action="store_true", required=False)

args=parser.parse_args()

for i in os.listdir(args.path):
    if args.size:
        if os.path.isfile(i):
            print(i,", size: ",os.path.getsize(i)/1024," KB")
        else:
            print(i)
    else:
        print(i)
