"""Auth command - login/logout with Rta backend."""
import sys


def auth(args):
    if not args:
        print("Usage: rta auth <login|logout|status>", file=sys.stderr)
        sys.exit(1)

    subcmd = args[0]
    if subcmd == "login":
        _login(args[1:])
    elif subcmd == "logout":
        _logout()
    elif subcmd == "status":
        _status()
    else:
        print(f"error: unknown auth subcommand '{subcmd}'", file=sys.stderr)
        sys.exit(1)


def _login(args):
    print("Auth login - to be implemented")


def _logout():
    print("Auth logout - to be implemented")


def _status():
    print("Auth status - to be implemented")
