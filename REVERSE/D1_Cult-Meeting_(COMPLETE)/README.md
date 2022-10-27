# CULT-MEETING

## FLAG: HTB{1nf1ltr4t1ng_4_cul7_0f_str1ng5}

## Status: Incomplete

+ DOCKER: YES
+ DOWNLOADABLE: YES

Description: After months of research, you're ready to attempt to infiltrate the meeting of a shadowy cult. Unfortunately, it looks like they've changed their password!

## NOTES

1. > file meeting
   1. meeting: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=72d8b06e4ca750d5c24395d3349c3121b9b95283, for GNU/Linux 3.2.0, not stripped

2. Run the file
   1. > ./meeting

3. > strings meeting
   1. /lib64/ld-linux-x86-64.so.2
    mgUa
    puts
    stdin
    fgets
    stdout
    system
    fwrite
    strchr
    __cxa_finalize
    setvbuf
    strcmp
    __libc_start_main
    libc.so.6
    GLIBC_2.2.5
    _ITM_deregisterTMCloneTable
    __gmon_start__
    _ITM_registerTMCloneTable
    u/UH
    []A\A]A^A_
    [3mYou knock on the door and a panel slides back
    [3m A hooded figure looks out at you
    "What is the password for this week's meeting?"
    sup3r_s3cr3t_p455w0rd_f0r_u!
    [3mThe panel slides closed and the lock clicks
    |      | "Welcome inside..."
    /bin/sh
    \/
    \| "That's not our password - call the guards!"
    ;*3$"
    GCC: (Debian 10.2.1-6) 10.2.1 20210110
    crtstuff.c
    deregister_tm_clones
    __do_global_dtors_aux
    completed.0
    __do_global_dtors_aux_fini_array_entry
    frame_dummy
    __frame_dummy_init_array_entry
    main.c
    __FRAME_END__
    __init_array_end
    _DYNAMIC
    __init_array_start
    __GNU_EH_FRAME_HDR
    _GLOBAL_OFFSET_TABLE_
    __libc_csu_fini
    _ITM_deregisterTMCloneTable
    stdout@GLIBC_2.2.5
    puts@GLIBC_2.2.5
    stdin@GLIBC_2.2.5
    _edata
    system@GLIBC_2.2.5
    strchr@GLIBC_2.2.5
    __libc_start_main@GLIBC_2.2.5
    fgets@GLIBC_2.2.5
    __data_start
    strcmp@GLIBC_2.2.5
    __gmon_start__
    __dso_handle
    _IO_stdin_used
    __libc_csu_init
    __bss_start
    main
    setvbuf@GLIBC_2.2.5
    fwrite@GLIBC_2.2.5
    __TMC_END__
    _ITM_registerTMCloneTable
    __cxa_finalize@GLIBC_2.2.5
    .symtab
    .strtab
    .shstrtab
    .interp
    .note.gnu.build-id
    .note.ABI-tag
    .gnu.hash
    .dynsym
    .dynstr
    .gnu.version
    .gnu.version_r
    .rela.dyn
    .rela.plt
    .init
    .plt.got
    .text
    .fini
    .rodata
    .eh_frame_hdr
    .eh_frame
    .init_array
    .fini_array
    .dynamic
    .got.plt
    .data
    .bss
    .comment

4. In the strings command we can see a string that says 'sup3r_s3cr3t_p455w0rd_f0r_u!'
5. Rerun the meeting but use the password: sup3r_s3cr3t_p455w0rd_f0r_u!
   1. > ./meeting
   2. "What is the password for this week's meeting?"
      1. sup3r_s3cr3t_p455w0rd_f0r_u!
   3. The panel slides closed and the lock clicks | "Welcome inside..." |
   4. NOTE: We now have bash

6. Let's open it up in ghidra just to look

### - DOCKER SPINUP TO GET ACTUAL FLAG

1. Now let's spin up the docker instance and run this against the server
2. > nc 206.189.117.93 32448
3. "What is the password for this week's meeting?"
   1. > sup3r_s3cr3t_p455w0rd_f0r_u!
   2. The panel slides closed and the lock clicks | "Welcome inside..." |
   3. WE NOW HAVE BASH
4. > ls
   1. flag.txt meeting.sh
5. > cat flag.txt
   1. HTB{1nf1ltr4t1ng_4_cul7_0f_str1ng5}
