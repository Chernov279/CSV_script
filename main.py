import csv

from conditions import filter_rows, aggregate
from parse_condition import parse_condition
from parser import Parser
from tabulate import tabulate


def main():
    parser = Parser()
    parsed_args = parser.parse_args()

    with open(parsed_args.file, "r", encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    if parsed_args.where:
        col, op, val = parse_condition(parsed_args.where)
        rows = filter_rows(rows, col, op, val)

    if parsed_args.aggregate:
        col, _, func = parse_condition(parsed_args.aggregate)
        result = aggregate(rows, col, func)
        if result is not None:
            rows = [{col: result},]
        else:
            print("No data for aggregate")
            return
    print(tabulate(rows, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()
