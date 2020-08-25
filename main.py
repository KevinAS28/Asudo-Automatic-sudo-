#!/usr/bin/python3

import subprocess
import time
import sys

def start(executable_file):
    return subprocess.Popen(
        executable_file,
        stdin=subprocess.PIPE,
    )

def write1(process, msg):
    process.communicate(input=(msg+"\n").encode("utf-8"))

def write_read(process, msg):
    return process.communicate(input=(msg+"\n").encode("utf-8"))[0].decode("utf-8")

def terminate(process):
    process.stdin.close()
    process.terminate()
    process.wait(timeout=0.2)


process = start(["sudo"])
inp = ["password"]
for i in inp:
    write1(process, i)

# time.sleep(0.2)

terminate(process)

