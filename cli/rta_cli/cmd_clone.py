"""Clone command - clone a git repository."""
import sys


def clone(args):
    if not args:
        print("error: repository URL required", file=sys.stderr)
        print("Usage: rta clone <repo-url> [dir]", file=sys.stderr)
        sys.exit(1)

    repo_url = args[0]
    print(f"Cloning {repo_url} - to be implemented")
