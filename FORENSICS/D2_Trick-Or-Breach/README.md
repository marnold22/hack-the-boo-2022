# TRICK-OR-BREACH

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: NO
+ DOWNLOADABLE: YES

Description: Our company has been working on a secret project for almost a year. None knows about the subject, although rumor is that it is about an old Halloween legend where an old witch in the woods invented a potion to bring pumpkins to life, but in a more up-to-date approach. Unfortunately, we learned that malicious actors accessed our network in a massive cyber attack. Our security team found that the hack had occurred when a group of children came into the office's security external room for trick or treat. One of the children was found to be a paid actor and managed to insert a USB into one of the security personnel's computers, which allowed the hackers to gain access to the company's systems. We only have a network capture during the time of the incident. Can you find out if they stole the secret project?

## NOTES

1. > file capture.pcap
   1. capture.pcap: pcap capture file, microsecond ts (little-endian) - version 2.4 (Ethernet, capture length 262144)

2. Get all of the DNS values that were attempted (tryu and convert these values from hex to string)
   1. > strings capture.pcap > strings.txt

3. Text file magic
   1. Remove all the 'pumpkincorp' lines from the text file
   2. Remove all the 

