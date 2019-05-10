"""Module for testing Forward Reference cache resolution across modules."""
import sys
from textwrap import dedent
from typing import Optional


if sys.version_info[:2] >= (3, 6):
    exec(dedent("""
    default_a: Optional['A'] = None
    class A():
        pass
    """))
else:  # This should stay in sync with the syntax above.
    __annotations__ = dict(
        default_a=Optional['A'],
    )
    default_a = None

    class A():
        pass
