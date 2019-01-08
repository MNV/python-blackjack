"""
The module to handle bet errors.
"""


class BetException(ValueError):
    """The exception to handle bet errors."""
    def __init__(self, previous):
        self.previous = previous
        ValueError.__init__(self, previous)
