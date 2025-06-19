import re
from typing import Optional, Callable


def filter_rows(rows: list[dict[str, str]], column: str, operator: str, value: str) -> list[dict[str, str]]:
    numeric = False
    if re.fullmatch(r'\d+(\.\d+|,\d+)?', value):
        value = float(value)
        numeric = True
    if operator == "=":
        if numeric:
            return [row for row in rows if float(row[column]) == value]
        else:
            return [row for row in rows if row[column] == value]
    try:
        value = float(value)
    except ValueError:
        raise ValueError(f"Column {column} must be numeric for filter")

    if operator == '<':
        return [row for row in rows if float(row[column]) < value]
    elif operator == '>':
        return [row for row in rows if float(row[column]) > value]
    else:
        raise ValueError(f"Unsupported operator: {operator}")


AGG_FUNCTIONS: dict[str, Callable[[list[float]], float]] = {
    'avg': lambda values: sum(values) / len(values),
    'min': min,
    'max': max,
}


def aggregate(rows: list[dict[str, str]], column: str, func: str) -> Optional[float]:
    try:
        values = [float(row[column]) for row in rows]
    except ValueError:
        raise ValueError(f"Column {column} must be numeric for aggregation")
    except KeyError:
        raise KeyError(f"Column {column} is not exist")

    agg_func = AGG_FUNCTIONS.get(func)
    if not agg_func:
        raise ValueError(f"Unsupported aggregation function: {func}")

    return round(agg_func(values), 3) if values else None
