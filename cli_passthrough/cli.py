import sys

import click
import pkg_resources

from . import cli_passthrough

version = pkg_resources.get_distribution("cli-passthrough").version
CONTEXT_SETTINGS = {"ignore_unknown_options": True, "allow_extra_args": True}


# CLI entry point
@click.command(context_settings=CONTEXT_SETTINGS)
@click.option(
    "-i",
    "--interactive",
    is_flag=True,
    help='Prefixes command with "/bin/bash -i -c", '
    "effectively sourcing the .bashrc file. "
    "This may use any aliases set in your current env.",
)
@click.option(
    "-s",
    "--silent",
    is_flag=True,
    help="Supress stdout and stderr. This will only remove display coming from stdout. "
    "Some commands may still alter the display.",
)
@click.version_option(prog_name="cli-passthrough", version=version)
@click.pass_context
def cli(ctx, interactive, silent):
    """Entry point
    """
    exit_status = cli_passthrough(" ".join(ctx.args), interactive, silent)
    sys.exit(exit_status)


main = cli
