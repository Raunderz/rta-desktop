"""Init command - scaffold a new project."""
import os
import sys


def init(args):
    project_name = args[0] if args else None
    if not project_name:
        print("error: project name required", file=sys.stderr)
        print("Usage: rta init <project-name>", file=sys.stderr)
        sys.exit(1)

    if os.path.exists(project_name):
        print(f"error: '{project_name}' already exists", file=sys.stderr)
        sys.exit(1)

    os.makedirs(project_name, exist_ok=True)
    print(f"Initialized project '{project_name}'")
