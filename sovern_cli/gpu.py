import typer

app = typer.Typer(help="Manage and view GPU resources.")

@app.command("list")
def list_gpus():
    """List available GPU capacity."""
    typer.echo("Fetching available GPUs...")