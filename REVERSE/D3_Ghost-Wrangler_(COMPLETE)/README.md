# GHOST-WRANGLER

## FLAG: HTB{h4unt3d_by_th3_gh0st5_0f_ctf5_p45t!}

## Status: Complete

+ DOCKER: NO
+ DOWNLOADABLE: YES

Description: Who you gonna call?

## NOTES

1. > file ./ghost
   1. ghost: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=810d0f9271ec04d80a2eee6ff2afd9367da3c3dd, for GNU/Linux 3.2.0, not stripped
2. > strings ghost > ghost.txt
3. Let's run the file
4. > ./ghost
   1. |___________________________________________| I've managed to trap the flag ghost in this box, but it's turned invisible! Can you figure out how to reveal them?
5. Let's open ghidra
6. In the main() function we see

    ```c
        undefined8 main(void)
        {
        undefined8 uVar1;
        
        uVar1 = get_flag();
        printf("%s\r|\x1b[4m%*.c\x1b[24m| I\'ve managed to trap the flag ghost in this box, but it\'s turn ed invisible!\nCan you figure out how to reveal them?\n"
                ,uVar1,0x28,0x5f);
        return 0;
        }
    ```

    1. This function gets the flag and stores it as uVar1
    2. Then it printf()'s the description and passes the flag as well as 0x28 and 0x5f as parameters
    3. %s = string of characters
    4. \r = Carriage Return - move the cursor/print head to the beginning of the current line
    5. \x = hexidecimal character escape which is \x1b = ESC
    6. [4m = underline (mono only) and the 'm' signifies the end of that instruction
    7. %*.c  = The '*' after '%' in a format string signify that the input matching the format will be ignored
    8. \x = hexidecimal character escape which is \x1b = ESC
    9. [24m = ?
    10. This looks like printf(menu, flag, 40, 95) the 40 is th enumber of '_' characters

7. And in the get_flag() function we see

    ```c
        void * get_flag(void)
        {
        void *__s;
        uint local_c;
        
        __s = malloc(0x29);
        memset(__s,0,0x29);
        for (local_c = 0; local_c < 0x28; local_c = local_c + 1) {
            *(byte *)((long)__s + (long)(int)local_c) = _[(int)local_c] ^ 0x13;
        }
        return __s;
        }
    ```

    1. In here we see malloc(0x29) = 41 bytes of memory being allocated
    2. memset(pointer to 41bytes, 0 = value being set, memory address)
    3. for loop - loops staring at 0, up to 41, incremented by 1
    4. set the character to whatever the value is Bitwise exclusive OR 0x13 = (19)

8. So overall we can see that the flag gets set and called in main() and sent to printf()
9. That being said let's open this binary in GDB (with gef) and see if we can stepthrough each instruction to view the flag
10. > gdb ./ghost
    1. break *main
    2. r (to run)
    3. ni (for next instruction)
    4. Step through until we get to uVar where it calls get_flag()
       1. WOOHOO! "HTB{h4unt3d_by_th3_gh0st5_0f_ctf5_p45t!}"
