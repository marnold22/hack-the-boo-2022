# POOF

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: YES
+ DOWNLOADABLE: YES *WARNING DON'T RUN THIS CODE IT CAN BE DANGEROUS*

Description: In my company, we are developing a new python game for Halloween. I'm the leader of this project; thus, I want it to be unique. So I researched the most cutting-edge python libraries for game development until I stumbled upon a private game-dev discord server. One member suggested I try a new python library that provides enhanced game development capabilities. I was excited about it until I tried it. Quite simply, all my files are encrypted now. Thankfully I manage to capture the memory and the network traffic of my Linux server during the incident. Can you analyze it and help me recover my files? To get the flag, connect to the docker service and answer the questions.
WARNING! Do not try to run the malware on your host. It may harm your computer! <http://138.68.188.84/forensics_poof.zip>

## NOTES

1. Let's open up the pcap file in wireshark
2. In here we see a GET request to <http://files.pypi-install.com/packages/a5/61/caf3af6d893b5cb8eae9a90a3054f370a92130863450e3299d742c7a65329d94/pygaming-dev-13.37.tar.gz>
3. This could be the malicious code/python library mentioned in the description
4. Let's analyze the mem.dmp file
5. > file mem.dmp
   1. mem.dmp: ELF 64-bit LSB core file, x86-64, version 1 (SYSV)
6. Let's open this in ghidra
7. Let's spawn the docker instance

### - DOCKER SPINUP TO GET ACTUAL FLAG

1. ```text
    +-----------+---------------------------------------------------------+
    |   Title   |                       Description                       |
    +-----------+---------------------------------------------------------+
    | Downgrade |          During recent auditing, we noticed that        |
    |           |     network authentication is not forced upon remote    |
    |           |       connections to our Windows 2012 server. That      |
    |           |           led us to investigate our system for          |
    |           |  suspicious logins further. Provided the server's event |
    |           |       logs, can you find any suspicious successful      |
    |           |                          login?                         |
    +-----------+---------------------------------------------------------+

    ```

2. Which is the malicious URL that the ransomware was downloaded from? (for example: <http://maliciousdomain/example/file.extension>)
3. > <http://files.pypi-install.com/packages/a5/61/caf3af6d893b5cb8eae9a90a3054f370a92130863450e3299d742c7a65329d94/pygaming-dev-13.37.tar.gz>
4. [+] Correct!
5. What is the name of the malicious process? (for example: malicious)
6. > Keep-Alive
7. [-] Wrong Answer!
8. > wget
9. [-] Wrong Answer!
10. > retransmission
11. [-] Wrong Answer!
12. > fast retransmission
13. [-] Wrong Answer!
