import typer
from sovern_cli import auth, gpu, deploy

app = typer.Typer(help="SovernStack CLI — manage GPU compute from your terminal.")
app.add_typer(gpu.app, name="gpu")

app.command(name="login")(auth.login)
app.command(name="deploy")(deploy.deploy)

BANNER = r"""
 ____                            ____  _             _
/ ___|  _____   _____ _ __ _ __ / ___|| |_ __ _  ___| | __
\___ \ / _ \ \ / / _ \ '__| '_ \\___ \| __/ _` |/ __| |/ /
 ___) | (_) \ V /  __/ |  | | | |___) | || (_| | (__|   <
|____/ \___/ \_/ \___|_|  |_| |_|____/ \__\__,_|\___|_|\_\

  Fractional GPU compute, billed by the hour.
"""

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        typer.echo(BANNER)
        typer.echo(ctx.get_help())
        raise typer.Exit()

if __name__ == "__main__":
    app()