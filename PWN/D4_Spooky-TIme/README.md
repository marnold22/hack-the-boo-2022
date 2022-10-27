# SPOOKY-TIME

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: YES
+ DOWNLOADABLE: YES

Description: Everyone loves a good jumpscare, especially kids or the person who does it.. Try to scare them all!
Submit flag & press enter

## NOTES

1. > file ./spooky_time
   1. spooky_time: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter ./glibc/ld-linux-x86-64.so.2, BuildID[sha1]=29a41183e07159f8444eb964aae5ea33d743a20d, for GNU/Linux 3.2.0, not stripped

2. > strings ./spooky_time > spooky.txt
3. > ./spooky_time
   1. You know what time it is? It's SPOOKY time!
   2. It's your chance to scare those little kids, say something scary!
   3. > RAH
   4. Seriously?? I bet you can do better than
   5. Anyway, here comes another bunch of kids, let's try one more time..
   6. >ARHAHAH
   7. Ok, you are not good with that, do you think that was scary?? Better luck next time!
4. Let's open this up in ghidra

    ```c
        void main(void)

        {
        long in_FS_OFFSET;
        char local_154 [12];
        char local_148 [312];
        long local_10;
        
        local_10 = *(long *)(in_FS_OFFSET + 0x28);
        setup();
        banner();
        puts("It\'s your chance to scare those little kids, say something scary!\n");
        __isoc99_scanf(&DAT_00102963,local_154);
        puts("\nSeriously?? I bet you can do better than ");
        printf(local_154);
        puts("\nAnyway, here comes another bunch of kids, let\'s try one more time..");
        puts("\n");
        __isoc99_scanf("%299s",local_148);
        puts("\nOk, you are not good with that, do you think that was scary??\n");
        printf(local_148);
        puts("Better luck next time!\n");
        if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                            /* WARNING: Subroutine does not return */
            __stack_chk_fail();
        }
        return;
        }
    ```

5. In the code we see that both of our input variables have set buffers
   1. The first local_154 = 12 bytes
   2. The second local_148 = 312 bytes
   3. Maybe we can leak past this

6. Let's run this in GDB
   1. If we send 12 A's (exact ammount of buffer) the program finishes running but skips the second input and uses one of our A's as the "second input"
   2. So we need to pass only 11 A's or 11 bytes
   3. Next we create a cyclical pattern of 312 ytes and pass that in for the second argument
      1. > gdb pattern create 312
      2. "aaaaaaaabaaaaaaacaaaaaaadaaaaaaaeaaaaaaafaaaaaaagaaaaaaahaaaaaaaiaaaaaaajaaaaaaakaaaaaaalaaaaaaamaaaaaaanaaaaaaaoaaaaaaapaaaaaaaqaaaaaaaraaaaaaasaaaaaaataaaaaaauaaaaaaavaaaaaaawaaaaaaaxaaaaaaayaaaaaaazaaaaaabbaaaaaabcaaaaaabdaaaaaabeaaaaaabfaaaaaabgaaaaaabhaaaaaabiaaaaaabjaaaaaabkaaaaaablaaaaaabmaaaaaabnaaaaaab"
   4. When we send this pattern through we get the response
      1. Undefined command: "aaaabnaaaaaab"
   5. If we look at the pattern we can see that 13 bytes are "overflowed"
      1. Let's subtract 13 from our original 312 meaning we have 299 bytes and then 13 free bytes to potentially exploit
7. Let's now craft a payload
   1. First send through 11 A's
   2. Next send 299 characters followed by " cat flag.txt" *NOTE: make sure to have the space before cat*
   3. Run this locally
   4. SUCCESS, now time to try remotely
8. Did not work on remote but lets try sending using a python script where we get the output of the "error"
9. Create solve.py
