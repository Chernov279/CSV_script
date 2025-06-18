import re


def parse_condition(where_clause: str):
    match = re.match(r'^(.+?)([=<>])(.+)$', where_clause)
    if not match:
        raise ValueError(f"incorrect condition : {where_clause}")
    column, operator, value = match.groups()
    return column, operator, value
