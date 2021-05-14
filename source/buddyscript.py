#!/opt/naumen/nauphone/bin/python2.7

import subprocess

bashCommand = "naucore service naubuddy screen show sessions"

process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)

