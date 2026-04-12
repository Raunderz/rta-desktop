"""Rta CLI - Minimal, fast."""

__version__ = "0.1.0"


def main():
    """Entry point for rta CLI."""
    import sys
    from rta_cli.commands import dispatch

    dispatch(sys.argv[1:])
