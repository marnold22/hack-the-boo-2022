# GONNA-LEFT-EM-ALL

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: NO
+ DOWNLOADABLE: YES

Description: Quick, there's a new custom Pokemon in the bush called "The Custom Pokemon". Can you find out what its weakness is and capture it?

## NOTES

1. Examine chall.py
   1. In here we can see 'm' is the flag in bytes_to_long format so we will want to use the 'from_bytes' function inside of Crypto.Util
   2. Inside of the main function we see two values (c1 & c2) which are created in the 'encrypt()' function
   3. More importantly we can see that the message (m) is used in the calculation for c2, so let's try to undo that calculation

2. Undo c2 calculation to find m
   1. c2 = m * s mod p (where p is our 1024 bit prime integer)
