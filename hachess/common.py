from typing import Any
from pprint import pprint

from rich.console import Console


def vprint(
    s: Any,
    verbose: bool,
    pretty: bool = False,
    sort_dicts: bool = False,
    limit: int = None,
) -> None:
    if limit is not None:
        p = s[:limit]
    else:
        p = s
    if verbose:
        if pretty:
            pprint(p)
        else:
            Console().print(p)
