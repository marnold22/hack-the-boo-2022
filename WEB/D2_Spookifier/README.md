# SPOOKIFIER

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: YES
+ DOWNLOADABLE: YES

Description: There's a new trend of an application that generates a spooky name for you. Users of that application later discovered that their real names were also magically changed, causing havoc in their life. Could you help bring down this application?

## NOTES

1. Upon first inspection I see a template ebeing used and instantly think potential template injection?
2. Running the application typing my name generates the table with my name in the corresponding fonts
3. However funning a template injection like this: `${6*6}` I get the response of 36 not `6*6`
4. This is a great resource for template injection: <https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection>

## - Template Injection Route

1. Detect
2. Identify the templating engine
   1. From the code we see it import Mako BUT wew also can verify that by the type of template we provided (ie. ${} vs {{}} vs <%= %>)
