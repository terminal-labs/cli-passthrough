import os
from pathlib import Path

import click


def echo(msg, err=False, silent=False):
    if err:
        write_to_log(msg, "stderr.log")
        if not silent:
            click.echo(msg, nl=False, err=err)
    else:
        write_to_log(msg)
        if not silent:
            click.echo(msg, nl=False)


def write_to_log(data, additional_log=None):
    """Write data to log files. Will append data to a single combined log called history.log.
    Additionally write data to a log with a custom name (such as stderr)
    for any custom logs.

    Args:
        data (str or bytes): Data to write to log file.
        additional_log (str): Used to create (or append to) an additional
                         log file with a custom name.
    """
    try:
        data = data.decode("utf-8")
    except AttributeError:
        pass  # already a string

    # strip possible eol chars and add back exactly one
    data = "".join([data.rstrip(), "\n"])

    logpath = Path("logs")
    if not os.path.exists(logpath):
        os.makedirs(logpath)

    with open(logpath / "history.log", "a+") as fp:
        fp.write(data)

    if additional_log:
        with open(logpath / additional_log, "a+") as fp:
            fp.write(data)
