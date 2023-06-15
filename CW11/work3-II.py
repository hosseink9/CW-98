from datetime import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('date1',type=str)
parser.add_argument('date2',type=str)

args = parser.parse_args()
date_format='%Y-%m-%d'

a=datetime.strptime(args.date1,date_format)
b=datetime.strptime(args.date2,date_format)

c=a-b

print(f'The number of days between {a} and {b} is result {c}')
