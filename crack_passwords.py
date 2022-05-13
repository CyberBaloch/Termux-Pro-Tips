#! /usr/bin/env python

import crypt
from time import sleep
import argparse
import os

# clear the screen, use cls for windows
os.system("clear")

# Receiving command line arguments
parser = argparse.ArgumentParser()

parser.add_argument('-e', '--encrypted', help="encrypted passwords")
parser.add_argument('-w', '--word', help="word list")

# parsing Received arguments
args = parser.parse_args()

print("""

##      ## ########## #######  ##    ##
##      ## ##      ## #######  ##   ##
##      ## ##      ## ##       ##  ##
########## ########## ##       ## ##
########## ########## ##       ## ##
##      ## ##      ## ##       ##  ##
##      ## ##      ## #######  ##   ##
##      ## ##      ## #######  ##    ##
""")

sleep(1)
print(" by TERMUX PRO TIPS\n\n")
sleep(1)

print(" [:] initializing script")
sleep(1)
print(" [:] loading passwords's files")
sleep(1)
print(" [:] start cracking")
sleep(1)

print()
sleep(2)


found_passwords_count = 0 # num of found passwords
tested_passwords = 0  # tested passwords
found_list = []

common = open(args.raw, "r").readlines()
encrypted = open(args.encrypted, "r").readlines()

flag = None

# Trying each password on wordlist
for enc_pass in encrypted:
    if flag == "break":
        break
    for com_pass in common:
        test = crypt.crypt(com_pass, " ") + "\n"
        if test == enc_pass:
            found_list.append(com_pass)
            found_passwords_count += 1
            if found_passwords_count > 10:
                flag = "break"
                break
        tested_passwords += 1

        print(f" [:] Tested: {tested_passwords} found: {found_passwords_count}", end="\r")
        sleep(0.00005)


sleep(0.5)
print("\n\n")
print(" [:] XXXXXXX RESULTS XXXXXXX\n")
sleep(1)
print(" [:] List of found passwords\n")
sleep(1)

# print the list of found passwords
for p in found_list:
    sleep(0.5)
    print(" => " + p, end="")

print()
exit(0)
