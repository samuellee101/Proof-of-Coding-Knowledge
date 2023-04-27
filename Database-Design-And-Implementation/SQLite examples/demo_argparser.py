import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--table', type=str, default='musician',help="the target table")
parser.add_argument('--record', type=str, default='none',help="the add/del record")
parser.add_argument('--add', action = 'store_true', default=False, help="action add")
parser.add_argument('--delete', action = 'store_true', default=False, help="action del")

args = parser.parse_args()

print("This is print function in demo_argparser.py:")
print(args.table)
print(args.record)
print(args.add)
print(args.delete)
