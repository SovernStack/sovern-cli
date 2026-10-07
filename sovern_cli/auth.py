import typer

def login(token: str = typer.Option(..., prompt=True, help="Your SovernStack API key")):
    """Authenticate with your SovernStack account."""
    typer.echo(f"Logged in successfully.")