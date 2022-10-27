# HALLOWEEN-INVITATION

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: NO
+ DOWNLOADABLE: YES

Description: An email notification pops up. It's from your theater group. Someone decided to throw a party. The invitation looks awesome, but there is something suspicious about this document. Maybe you should take a look before you rent your banana costume.

## NOTES

1. > file invitation.docm
   1. invitation.docm: Microsoft Word 2007+
2. > strings invitation.docm > strings.txt
   1. In here we can see different macros twords the end of the file

3. Let's run oledump.py to extract the macro data from the docm and save it to a text file
   1. NOTE: credit to <https://github.com/DidierStevens/DidierStevensSuite> for the oledump.py file
   2. > python3 oledump.py "invitiation.docm" -s a -v > oledump.txt
4. After inspection we can see that this code is most likely visual basic, so lets redump the file but with the vbs extension
   1. > python3 oledump.py "invitiation.docm" -s a -v > oledump.vbs

5. Tried running it as a powershell script inside windows vm
6. Let't try to deobfuscate the code

## - Deobfuscating

1. Dim - this just is a variable decleration
2. Chr() - this function converts the ANSI character code to a character
3. & - this concatenates two VALUES
4. Val() - this function converts the specified string expression to a number and returns it as a double
5. Mid() - this function returns a specified number of characters from a string ie. Mid(string,start[,length])
6. &H - this prefix indicates a hexadecimal value
