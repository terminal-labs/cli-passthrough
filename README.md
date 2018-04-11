# README

This project provides an entry point `cli-passthrough` in the terminal that accepts any amount of parameters, and runs those parameters as it's own command. Except in a few special cases, this will output to the terminal exactly what the command would have, including any formatting done with escape sequences. Both the combined stdout and stderr are logged, with order preserved, in `logs/history.log`, and the stderr by itself is logged in `/logs/stderr.log`. These log files are written to in realtime. The output to the terminal is also in realtime.

This project was motivated by the desire to have a cli-passthrough that does all of the following:

1. Run any command given to it.
2. Capture stdout and stderr independently for flexible logging.
3. Preserve order of stdout and stderr
4. Output to the screen in realtime, i.e. don't wait for the command to exit before dumping to the screen.
5. Capture exit code
6. Preserve ANSI escape sequences so most things are still formatted as if not run through this passthrough.
