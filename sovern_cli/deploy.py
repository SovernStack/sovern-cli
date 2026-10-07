import typer

def deploy(
    model_path: str = typer.Argument(..., help="Path to your .onnx model file"),
    name: str = typer.Option(..., "--name", help="Name for the deployed model"),
):
    """Deploy an ONNX model to Triton and get a live API endpoint."""
    typer.echo(f"Deploying {model_path} as '{name}'...")