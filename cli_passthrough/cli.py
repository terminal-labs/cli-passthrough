import os
import pkg_resources
import sys

import click

import cli_passthrough.passthrough as passthrough
import cli_passthrough.utils as utils

version = pkg_resources.get_distribution('cli-passthrough').version

CONTEXT_SETTINGS = {
    'ignore_unknown_options': True,
    'allow_extra_args': True,
}

### CLI entry point
@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('-i', '--interactive', is_flag=True,
              help='Prefixes command with "/bin/bash -i -c", '
              'effectively sourcing the .bashrc file. '
              'This may use any aliases set in your current env.')
@click.version_option(prog_name='cli-passthrough', version=version)
@click.pass_context
def cli(ctx, interactive):
    '''Entry point
    '''
    utils.write_to_log('\nNEW CMD = {}'.format(' '.join(sys.argv)))
    utils.write_to_log('\nNEW CMD = {}'.format(' '.join(sys.argv)), 'stderr')

    exit_status = passthrough.passthrough(' '.join(ctx.args), interactive)
    sys.exit(exit_status)

main = cli
