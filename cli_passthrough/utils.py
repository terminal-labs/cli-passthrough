import os

import click

def echo(msg, err=None):
    if err:
        write_to_log(msg, 'stderr')
        click.echo(msg, err=err)
    else:
        write_to_log(msg)
        click.echo(msg)

def write_to_log(data=None, file_name=None):
    '''Write data to log files. Will append data to a single combined log.
    Additionally write data to a log with a custom name (such as stderr)
    for any custom logs.

    Args:
        data (str or bytes): Data to write to log file.
        file_name (str): Used to create (or append to) an additional
                         log file with a custom name. Custom name always gets
                         `.log` added to the end.
    '''
    try:
        data = data.decode('utf-8')
    except AttributeError:
        pass # already a string

    # strip possible eol chars and add back exactly one
    data = ''.join([data.rstrip(), '\n'])
    logpath = 'logs'
    if not os.path.exists(logpath):
        os.makedirs(logpath)

    fd_path = os.path.join(logpath, 'history.log')
    fd = open(fd_path, 'a+')
    fd.write(data)
    fd.close()
    if file_name:
        fd_custom_path = os.path.join(logpath, ''.join([file_name, '.log']))
        fd_custom = open(fd_custom_path, 'a+')
        fd_custom.write(data)
        fd_custom.close()
