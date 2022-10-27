# ENCODED-PAYLOAD

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: NO
+ DOWNLOADABLE: YES

Description: Buried in your basement you've discovered an ancient tome. The pages are full of what look like warnings, but luckily you can't read the language! What will happen if you invoke the ancient spells here?

## NOTES

1. > file ./encodedpayload
   1. encodedpayload: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), statically linked, no section header

2. > strings ./encodedpayload
   [SYIIIIIIIIICCCCCCC7QZjAXP0A0AkAAQ2AB2BB0BBABXP8ABuJI01iKzWHcScW3F3Pj6bOyHax0cVZmK0MCpYh0WO8Mk0PIbYYibHsOS0wp7qqxUReP5UfYmYhaLpCVV0PQF3LsfcOyIqZmMPF2ax0ndo1cE8e8fOvORBCYMYHcF2PSOyHaNPFkJmopRJ4KChmI3bU6e8Tme3ni8gCXFO2S1xC0U8VOsR59RNK9KSaByx4ZS0EPUPauPcphrOq0bh0Tg2cK2p0LSJso1ct43B51e31uSormFSGCTsSMgpV7rsLI9qJmmPAA

3. > Run the file
   1. ./encodedpayload
   2. RESPONSE: ERROR PIPE

4. Open the file up in ghidra
   1. Incredibly difficult to read

5. > ltrace ./encodedpayload
   1. Couldn't find .dynsym or .dynstr in "/proc/1092/exe"
6. > strace ./encodedpayload

   ```c
        execve("./encodedpayload", ["./encodedpayload"], 0x7ffe6027a4d0 /* 31 vars */) = 0
        [ Process PID=1096 runs in 32 bit mode. ]
        socket(AF_INET, SOCK_STREAM, IPPROTO_IP) = 3
        dup2(3, 2)                              = 2
        dup2(3, 1)                              = 1
        dup2(3, 0)                              = 0
        connect(3, {sa_family=AF_INET, sin_port=htons(1337), sin_addr=inet_addr("127.0.0.1")}, 102) = -1 ECONNREFUSED (Connection refused)
        syscall_0xffffffffffffff0b(0xffae1818, 0xffae1810, 0, 0, 0, 0) = -1 ENOSYS (Function not implemented)
        execve("/bin/sh", ["/bin/sh", "-c", "echo HTB{PLz_strace_M333}"], NULL) = 0
        [ Process PID=1096 runs in 64 bit mode. ]
        brk(NULL)                               = 0x55e423763000
        mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f8467e83000
        access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
        openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 4
        newfstatat(4, "", {st_mode=S_IFREG|0644, st_size=70242, ...}, AT_EMPTY_PATH) = 0
        mmap(NULL, 70242, PROT_READ, MAP_PRIVATE, 4, 0) = 0x7f8467e71000
        close(4)                                = 0
        openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 4
        read(4, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\300\223\2\0\0\0\0\0"..., 832) = 832
        pread64(4, "\6\0\0\0\4\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0"..., 784, 64) = 784
        pread64(4, "\4\0\0\0\20\0\0\0\5\0\0\0GNU\0\2\200\0\300\4\0\0\0\1\0\0\0\0\0\0\0", 32, 848) = 32
        pread64(4, "\4\0\0\0\24\0\0\0\3\0\0\0GNU\0q\247\307\271{\300\263\343I\243\330d\2ReU"..., 68, 880) = 68
        newfstatat(4, "", {st_mode=S_IFREG|0755, st_size=2061320, ...}, AT_EMPTY_PATH) = 0
        pread64(4, "\6\0\0\0\4\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0"..., 784, 64) = 784
        mmap(NULL, 2109328, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 4, 0) = 0x7f8467c6e000
        mmap(0x7f8467c96000, 1507328, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 4, 0x28000) = 0x7f8467c96000
        mmap(0x7f8467e06000, 360448, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 4, 0x198000) = 0x7f8467e06000
        mmap(0x7f8467e5e000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 4, 0x1f0000) = 0x7f8467e5e000
        mmap(0x7f8467e64000, 53136, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7f8467e64000
        close(4)                                = 0
        mmap(NULL, 12288, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f8467c6b000
        arch_prctl(ARCH_SET_FS, 0x7f8467c6b740) = 0
        set_tid_address(0x7f8467c6ba10)         = 1096
        set_robust_list(0x7f8467c6ba20, 24)     = 0
        rseq(0x7f8467c6c0e0, 0x20, 0, 0x53053053) = 0
        mprotect(0x7f8467e5e000, 16384, PROT_READ) = 0
        mprotect(0x55e421ceb000, 8192, PROT_READ) = 0
        mprotect(0x7f8467eb8000, 8192, PROT_READ) = 0
        prlimit64(0, RLIMIT_STACK, NULL, {rlim_cur=8192*1024, rlim_max=RLIM64_INFINITY}) = 0
        munmap(0x7f8467e71000, 70242)           = 0
        getuid()                                = 1000
        getgid()                                = 1000
        getpid()                                = 1096
        rt_sigaction(SIGCHLD, {sa_handler=0x55e421ce0d80, sa_mask=~[RTMIN RT_1], sa_flags=SA_RESTORER, sa_restorer=0x7f8467cabaa0}, NULL, 8) = 0
        geteuid()                               = 1000
        getppid()                               = 1093
        getrandom("\x17\xb0\x31\x50\xc7\x9d\xb4\x66", 8, GRND_NONBLOCK) = 8
        brk(NULL)                               = 0x55e423763000
        brk(0x55e423784000)                     = 0x55e423784000
        getcwd("/mnt/c/Users/marnold/CODE/CTF/htb/hack-the-boo-2022/REVERSE/D2_Encoded-Payload/rev_encodedpayload", 4096) = 98
        geteuid()                               = 1000
        getegid()                               = 1000
        rt_sigaction(SIGINT, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
        rt_sigaction(SIGINT, {sa_handler=0x55e421ce0d80, sa_mask=~[RTMIN RT_1], sa_flags=SA_RESTORER, sa_restorer=0x7f8467cabaa0}, NULL, 8) = 0
        rt_sigaction(SIGQUIT, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
        rt_sigaction(SIGQUIT, {sa_handler=SIG_DFL, sa_mask=~[RTMIN RT_1], sa_flags=SA_RESTORER, sa_restorer=0x7f8467cabaa0}, NULL, 8) = 0
        rt_sigaction(SIGTERM, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
        rt_sigaction(SIGTERM, {sa_handler=SIG_DFL, sa_mask=~[RTMIN RT_1], sa_flags=SA_RESTORER, sa_restorer=0x7f8467cabaa0}, NULL, 8) = 0
        write(1, "HTB{PLz_strace_M333}\n", 21)  = -1 EPIPE (Broken pipe)
        --- SIGPIPE {si_signo=SIGPIPE, si_code=SI_USER, si_pid=1096, si_uid=1000} ---
        +++ killed by SIGPIPE +++
    ```

7. > nm ./encodedpayload
    1. nm: encodedpayload: no symbols

8. > readelf -a encodedpayload

    ```text
        ELF Header:
        Magic:   7f 45 4c 46 01 01 01 00 00 00 00 00 00 00 00 00
        Class:                             ELF32
        Data:                              2's complement, little endian
        Version:                           1 (current)
        OS/ABI:                            UNIX - System V
        ABI Version:                       0
        Type:                              EXEC (Executable file)
        Machine:                           Intel 80386
        Version:                           0x1
        Entry point address:               0x8048054
        Start of program headers:          52 (bytes into file)
        Start of section headers:          0 (bytes into file)
        Flags:                             0x0
        Size of this header:               52 (bytes)
        Size of program headers:           32 (bytes)
        Number of program headers:         1
        Size of section headers:           0 (bytes)
        Number of section headers:         0
        Section header string table index: 0

        There are no sections in this file.

        There are no section groups in this file.

        Program Headers:
        Type           Offset   VirtAddr   PhysAddr   FileSiz MemSiz  Flg Align
        LOAD           0x000000 0x08048000 0x08048000 0x00193 0x002d2 RWE 0x1000

        There is no dynamic section in this file.

        There are no relocations in this file.
        No processor specific unwind information to decode

        Dynamic symbol information is not available for displaying symbols.

        No version information found in this file.
    ```
