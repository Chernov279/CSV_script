import argparse


class Parser:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(
            description="CSV tool: filter and aggregate columns."
        )
        self._configure()

    def _configure(self):
        self.parser.add_argument(
            '--file',
            type=str,
            required=True,
            help='Path to CSV file, e.g. --file some_data.csv'
        )
        self.parser.add_argument(
            '--where',
            type=str,
            help='Filter rows, e.g. --where "price>1000"'
        )
        self.parser.add_argument(
            '--aggregate',
            type=str,
            help='Aggregate column, e.g. --aggregate "price=avg"'
        )

    def parse_args(self) -> argparse.Namespace:
        return self.parser.parse_args()
