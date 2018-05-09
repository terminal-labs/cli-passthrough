import errno
import os
import pty
import subprocess
import sys
from select import select
from subprocess import Popen

import click

import cli_passthrough.utils as utils

def passthrough(cmd=None, interactive=False):
    '''Largely found in https://stackoverflow.com/a/31953436'''
    masters, slaves = zip(pty.openpty(), pty.openpty())
    if interactive:
        cmd = ["/bin/bash", "-i", "-c"] + cmd.split()
    else:
        cmd = cmd.split()

    with Popen(cmd, stdin=slaves[0], stdout=slaves[0], stderr=slaves[1]) as p:
        for fd in slaves:
            os.close(fd) # no input
            readable = {
                masters[0]: sys.stdout.buffer, # store buffers seperately
                masters[1]: sys.stderr.buffer,
            }
        while readable:
            for fd in select(readable, [], [])[0]:
                try:
                    data = os.read(fd, 1024) # read available
                except OSError as e:
                    if e.errno != errno.EIO:
                        raise #XXX cleanup
                    del readable[fd] # EIO means EOF on some systems
                else:
                    if not data: # EOF
                        del readable[fd]
                    else:
                        if fd == masters[0]: # We caught stdout
                            utils.echo(data.rstrip())
                        else: # We caught stderr
                            utils.echo(data.rstrip(), err=True)
                        readable[fd].flush()
    for fd in masters:
        os.close(fd)
    return p.returncode
