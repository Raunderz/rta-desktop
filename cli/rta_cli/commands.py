import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

app = typer.Typer(
    name="rta",
    help="AI-assisted code editor CLI",
    add_completion=False,
)
console = Console()


@app.command()
def chat():
    """Start the Rta chat interface"""
    from rta_cli.chat import start_chat
    start_chat()


@app.callback(invoke_without_command=True)
def callback(ctx: typer.Context):
    """Rta - AI-assisted code editor CLI"""
    if ctx.invoked_subcommand is None:
        from rta_cli.chat import start_chat
        start_chat()


@app.command()
def init():
    """Initialize a new project"""
    from rta_cli.cmd_init import init
    init([])


@app.command()
def auth():
    """Authenticate with Rta backend"""
    from rta_cli.cmd_auth import auth
    auth([])


@app.command()
def clone():
    """Clone a repository"""
    from rta_cli.cmd_clone import clone
    clone([])


if __name__ == "__main__":
    app()
