import sys


def dispatch(args):
    """Route CLI commands - lazy import for speed."""
    if not args:
        _print_help()
        return

    cmd = args[0]
    rest = args[1:]

    if cmd == "init":
        from rta_cli.cmd_init import init
        init(rest)
    elif cmd == "auth":
        from rta_cli.cmd_auth import auth
        auth(rest)
    elif cmd == "clone":
        from rta_cli.cmd_clone import clone
        clone(rest)
    elif cmd in ("--help", "-h", "help"):
        _print_help()
    else:
        print(f"error: unknown command '{cmd}'", file=sys.stderr)
        print("Run 'rta help' for usage.", file=sys.stderr)
        sys.exit(1)


def _print_help():
    print("rta - AI-assisted code editor CLI")
    print()
    print("Usage: rta <command> [args]")
    print()
    print("Commands:")
    print("  init        Initialize a new project")
    print("  auth        Authenticate with Rta backend")
    print("  clone       Clone a repository")
    print("  help        Show this help message")
