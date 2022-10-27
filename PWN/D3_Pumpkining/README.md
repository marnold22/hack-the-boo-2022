# PUMPKINING

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: YES
+ DOWNLOADABLE: YES

Description: Long live the King! Pumpking is the king of our hometown and this time of the year, he makes wishes come true! But, you must be naughty in order to get a wish.. He is like reverse Santa Claus and way cooler!

## NOTES

1. > file pumpking
   1. pumpking: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter ./glibc/ld-linux-x86-64.so.2, BuildID[sha1]=fbd2ae75e4f0a999c62a92360d6a085e30637725, for GNU/Linux 3.2.0, not stripped

2. Run the file
   1. > ./pumpking
   2. First of all, in order to proceed, we need you to whisper the secret passphrase provided only to naughty kids:
   3. >> bad
   4. You seem too kind for the Pumpking to help you.. I'm sorry!

3. So we need a passphrase, let's open this up in ghidra
4. In ghidra we see the main funtion

    ```c
        void main(void)
        {
        int iVar1;
        size_t sVar2;
        long in_FS_OFFSET;
        ulong local_28;
        undefined8 local_1f;
        undefined4 local_17;
        undefined2 local_13;
        undefined local_11;
        undefined8 local_10;
        
        local_10 = *(undefined8 *)(in_FS_OFFSET + 0x28);
        setup();
        local_1f = 0;
        local_17 = 0;
        local_13 = 0;
        local_11 = 0;
        write(1,
                "\nFirst of all, in order to proceed, we need you to whisper the secret passphrase provided  only to naughty kids: "
                ,0x70);
        read(0,&local_1f,0xe);
        local_28 = 0;
        while( true ) {
            sVar2 = strlen((char *)&local_1f);
            if (sVar2 <= local_28) break;
            if (*(char *)((long)&local_1f + local_28) == '\n') {
            *(undefined *)((long)&local_1f + local_28) = 0;
            }
            local_28 = local_28 + 1;
        }
        iVar1 = strncmp((char *)&local_1f,"pumpk1ngRulez",0xd);
        if (iVar1 == 0) {
            king();
        }
        else {
            write(1,"\nYou seem too kind for the Pumpking to help you.. I\'m sorry!\n\n",0x3e);
        }
                            /* WARNING: Subroutine does not return */
        exit(0x16);
        }
    ```

5. In here we see a string comparison ran strncmp() against 'pumpk1ngRulez'
6. let's re-run the file with the password
   1. > ./pumpking
   2. First of all, in order to proceed, we need you to whisper the secret passphrase provided only to naughty kids:
   3. >> pumpk1ngRulez
   4. [Pumpkgin]: Welcome naughty kid! This time of the year, I will make your wish come true! Wish for everything, even for tha flag!
   5. >>
7. Let's go back to ghidra

    ```c
        iVar1 = strncmp((char *)&local_1f,"pumpk1ngRulez",0xd);
        if (iVar1 == 0) {
            king();
        }
    ```

8. In this check we see that if we pass the correct string 'pumpk1ngRulez' then the king() function is called
9. Let's look at king()

    ```c
        void king(void)
        {
        long in_FS_OFFSET;
        undefined8 local_a8;
        undefined8 local_a0;
        undefined8 local_98;
        undefined8 local_90;
        undefined8 local_88;
        undefined8 local_80;
        undefined8 local_78;
        undefined8 local_70;
        undefined8 local_68;
        undefined8 local_60;
        undefined8 local_58;
        undefined8 local_50;
        undefined8 local_48;
        undefined8 local_40;
        undefined8 local_38;
        undefined8 local_30;
        undefined8 local_28;
        undefined8 local_20;
        undefined4 local_18;
        undefined2 local_14;
        long local_10;
        
        local_10 = *(long *)(in_FS_OFFSET + 0x28);
        write(1,
                "\n[Pumpkgin]: Welcome naughty kid! This time of the year, I will make your wish come true!  Wish for everything, even for tha flag!\n\n>> "
                ,0x88);
        local_a8 = 0;
        local_a0 = 0;
        local_98 = 0;
        local_90 = 0;
        local_88 = 0;
        local_80 = 0;
        local_78 = 0;
        local_70 = 0;
        local_68 = 0;
        local_60 = 0;
        local_58 = 0;
        local_50 = 0;
        local_48 = 0;
        local_40 = 0;
        local_38 = 0;
        local_30 = 0;
        local_28 = 0;
        local_20 = 0;
        local_18 = 0;
        local_14 = 0;
        read(0,&local_a8,0x95);
        (*(code *)&local_a8)();
        if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                            /* WARNING: Subroutine does not return */
            __stack_chk_fail();
        }
        return;
        }
    ```

10. The 0x28 is '40' when converted
