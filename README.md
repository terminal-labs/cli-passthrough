# README

## Install

Install with `pip install cli-passthrough` / `pip install -e .` if you have this repo.


## How to Use


From the terminal:

```bash
$ cli-passthrough echo hi
hi
$ echo hi
hi
$ cli-passthrough cat -asdf
cat: invalid option -- 'a'
Try 'cat --help' for more information.
$ cat -asdf
cat: invalid option -- 'a'
Try 'cat --help' for more information.
```

From Python:
```ipython
In [1]: from cli_passthrough import cli_passthrough

In [2]: cli_passthrough("echo 'hi'")
hi
Out[2]: 0

In [3]: cli_passthrough("cat -asdf")
cat: invalid option -- 'a'
Try 'cat --help' for more information.
Out[3]: 1
```

This should also handle some commands that provide interactivity, like `ssh`, `ipython`, and `passwd`.

## What does it do?


This project provides an entry point `cli-passthrough` in the terminal that accepts any amount of parameters, and runs those parameters as it's own command. Except in a few special cases, this will output to the terminal exactly what the command would have, including any formatting done with escape sequences. Both the combined stdout and stderr are logged, with order preserved, in `logs/history.log`, and the stderr by itself is logged in `logs/stderr.log`. These log files are written to in realtime. The output to the terminal is also in realtime. The original intent was to dump all output back to the screen, while saving both stdout and stderr. Future work will be to return those outputs to Python as well.

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

1. Not tested and probably doesn't work on Windows.

1. It doesn't run *every* command. E.g. Commands that repeatedly modify the display like `top` and `glances` aren't handled well.

This started with [this SO post](https://stackoverflow.com/a/31953436). It now has a few improvements, but the credit for the jumping off point is definitely that post. Thank you to all contributors.
