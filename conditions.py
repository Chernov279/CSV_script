import re


def filter_rows(rows, column, operator, value: str):
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


def aggregate(rows, column, func):
    try:
        values = [float(row[column]) for row in rows]
    except ValueError:
        raise ValueError(f"Column {column} must be numeric for aggregation")
    except KeyError:
        raise KeyError(f"Column {column} is not exist")

    if func == 'avg':
        return round(sum(values) / len(values), 3) if values else None
    elif func == 'min':
        return round(min(values), 3) if values else None
    elif func == 'max':
        return round(max(values), 3) if values else None
    else:
        raise ValueError(f"Unsupported aggregation function: {func}")