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
@click.version_option(prog_name='cli-passthrough', version=version)
@click.pass_context
def cli(ctx):
    '''Entry point
    '''
    utils.write_to_log('\nNEW CMD')
    utils.write_to_log(' '.join(sys.argv))

    utils.write_to_log('\nNEW CMD', 'stderr')
    utils.write_to_log(' '.join(sys.argv), 'stderr')

    passthrough.passthrough(' '.join(ctx.args))

main = cli
