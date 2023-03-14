from collections import defaultdict


def tuples_to_tree(source: list[tuple[str, str]]) -> dict:
    res = defaultdict(dict)
    
    for parent, child in source:
        res[parent][child] = res[child]
    
    return res[None]
