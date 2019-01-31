# README

## Install

Install with `pip install cli-passthrough` / `pip install -e .` if you have this repo.


## How to Use


From the terminal:

```bash
$ cli-passthrough echo 'hi'
hi
$ echo 'hi'
hi
$ cli-passthrough python --error
Unknown option: --
usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
Try `python -h' for more information.
$ python --error
Unknown option: --
usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
Try `python -h' for more information.
```

From Python:
```ipython
In [1]: from cli_passthrough import cli_passthrough

In [2]: cli_passthrough("echo 'hi'")
hi
Out[2]: 0

In [3]: cli_passthrough("python --error")
Unknown option: --
usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
Try `python -h' for more information.
Out[3]: 2

```

## What does it do?


This project provides an entry point `cli-passthrough` in the terminal that accepts any amount of parameters, and runs those parameters as it's own command. Except in a few special cases, this will output to the terminal exactly what the command would have, including any formatting done with escape sequences. Both the combined stdout and stderr are logged, with order preserved, in `logs/history.log`, and the stderr by itself is logged in `/logs/stderr.log`. These log files are written to in realtime. The output to the terminal is also in realtime. The original intent was to dump all output back to the screen, while saving both stdout and stderr. Future work will be to return those outputs to Python as well.

This project was motivated by making a wrapper on another application which needed to be used over the CLI. I wanted to also use the wrapper from the CLI as well. I wanted to see the output of the program I was invoking in real-time, in the same formatting, and log everything. In other words, I wanted the following:

1. ANY COMMAND: Run nearly any command given to it.
2. FLEXIBLE LOGGING: Capture stdout and stderr independently for flexible logging.
3. ORDER PESERVATION: Preserve order of stdout and stderr
4. REALTIME OUTPUT: Output to the screen in realtime, i.e. don't wait for the command to exit before dumping to the screen.
5. EXIT STATUS: Capture exit code
6. FORMATTING PRESERVED: Preserve ANSI escape sequences so most things are still formatted as if not run through this passthrough.


|                              | 1 | 2 | 3 | 4 | 5 | 6   | note |
|------------------------------|---|---|---|---|---|-----|------|
| os.system                    | Y | N | Y | Y | Y | Y   | Doesn't capture output at all |
| os.popen                     | N | N | Y | N | N | Y   | Deprecated & obsolete |
| os.exec*                     | Y | N | - | N | N | N   | Really not the intended use |
| pexpect                      | Y | N | Y | Y | Y | Y   | Bad logging |
| subprocess.popen + threads   | Y | Y | Y | N | Y | Y/N | Doesn't have real-time output because it's often dependent on buffer flushes of blocks. |
| subprocess.popen + pty       | Y | Y | Y | Y | Y | Y   | We got it! |


## Known Limitations

This implementation of subprocess.popen + pty currently has the following limitations:

1. It doesn't run *every* command. Commands that need input from the user do not work, such as `ssh` or `ipython`.

1. It makes assumptions about the terminal size. It would be better if it detected the terminal the python is ran in, and use the same dimensions.

This is very much largely adapted (copied) from [this SO post](https://stackoverflow.com/a/31953436). I just wrapped it up into an importable function, gave it a CLI itself, and made basic logging to illustrate the point. Feel free to copy/paste/tweek it yourself.

**If you find something better** please let me know! I'd be more than happy to upgrade or replace this. This is simply the best I've found so far.
