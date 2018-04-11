# README

This project provides an entry point `cli-passthrough` in the terminal that accepts any amount of parameters, and runs those parameters as it's own command. Except in a few special cases, this will output to the terminal exactly what the command would have, including any formatting done with escape sequences. Both the combined stdout and stderr are logged, with order preserved, in `logs/history.log`, and the stderr by itself is logged in `/logs/stderr.log`. These log files are written to in realtime. The output to the terminal is also in realtime.

This project was motivated by the desire to have a cli-passthrough that does all of the following:

1. ANY COMMAND: Run nearly any command given to it.
2. FLEXIBLE LOGGING: Capture stdout and stderr independently for flexible logging.
3. ORDER PESERVATION: Preserve order of stdout and stderr
4. REALTIME OUTPUT: Output to the screen in realtime, i.e. don't wait for the command to exit before dumping to the screen.
5. EXIT STATUS: Capture exit code
6. FORMATTING PRESERVED: Preserve ANSI escape sequences so most things are still formatted as if not run through this passthrough.
7. INTERACTIVE, i.e. allow prompting for input.


|                              | 1 | 2 | 3 | 4 | 5 | 6 | 7 | note |
|------------------------------|---|---|---|---|---|---|---|------|
| os.system                    | Y | N | Y | Y | Y | Y | Y | Doesn't capture output at all |
| os.popen                     | N | N | Y | N | N | Y | N | Deprecated & obsolete |
| os.exec*                     | Y | N | - | N | N | N | N | Really not the intended use |
| pexpect                      | Y | N | Y | Y | Y | Y | Y |     |
| stdbuf                       |   |   |   |   | Y | Y |   |     |
| subprocess.popen + threads   | Y | Y | Y | N | Y |   | N |     |
| subprocess.popen + pty       | Y | Y | Y | Y | Y | Y | Y |     |
