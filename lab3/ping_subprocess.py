'''
Created on 4 Jul 2016

@author: e05975
'''
import subprocess
import shlex

command_line = "ping -c 1 10.0.1.135"

if __name__ == '__main__':
    args = shlex.split(command_line)
    try:
        subprocess.check_call(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        print ("Your pc is up!")
    except subprocess.CalledProcessError:
        print ("Failed to get ping.")

