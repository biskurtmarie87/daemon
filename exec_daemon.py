#!/usr/bin/env python3.11.2

import os
import subprocess
from time import sleep
import config

def check_and_execute():
    if os.path.exists(config.ldap_FS):
        print("File '/ldap_home' exists. Executing main script...")
        subprocess.run(['bash', config.script_path], check=True)
    else:
        print("File '/ldap_home' not found.")

def main():
    while True:
        check_and_execute()
        sleep(config.daemon_rotate)

if __name__ == "__main__":
    main()
