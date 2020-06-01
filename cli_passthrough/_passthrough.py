import errno
import fcntl
import os
import pty
import shutil
import struct
import sys
import termios
from itertools import chain
from select import select
from subprocess import Popen

from cli_passthrough.utils import echo
from cli_passthrough.utils import write_to_log


_COLUMNS, _ROWS, = shutil.get_terminal_size(fallback=(80, 20))


def _set_size(fd):
    """Found at: https://stackoverflow.com/a/6420070"""
    size = struct.pack("HHHH", _ROWS, _COLUMNS, 0, 0)
    fcntl.ioctl(fd, termios.TIOCSWINSZ, size)


def cli_passthrough(cmd=None, interactive=False, silent=False):
    """Largely found in https://stackoverflow.com/a/31953436"""
    write_to_log(f"NEW_CMD={cmd}", "stderr.log")
    write_to_log(
        f"CMD_PARAMS: interactive={interactive}, silent={silent}", "stderr.log"
    )

    if interactive:
        cmd = ["/bin/bash", "-i", "-c"] + cmd.split()
    else:
        cmd = cmd.split()

    masters, slaves = zip(pty.openpty(), pty.openpty())
    for fd in chain(masters, slaves):
        _set_size(fd)

    with Popen(cmd, stdin=sys.stdin, stdout=slaves[0], stderr=slaves[1]) as p:
        for fd in slaves:
            os.close(fd)  # no input
        readable = {
            masters[0]: sys.stdout.buffer,  # store buffers seperately
            masters[1]: sys.stderr.buffer,
        }
        while readable:
            for fd in select(readable, [], [])[0]:
                try:
                    data = os.read(fd, 1024)  # read available
                except OSError as e:
                    if e.errno != errno.EIO:
                        raise  # XXX cleanup
                    del readable[fd]  # EIO means EOF on some systems
                else:
                    if not data:  # EOF
                        del readable[fd]
                    else:
                        if fd == masters[0]:  # We caught stdout
                            echo(data, silent=silent)
                        else:  # We caught stderr
                            echo(data, err=True, silent=silent)
                        readable[fd].flush()
    for fd in masters:
        os.close(fd)
    return p.returncode
