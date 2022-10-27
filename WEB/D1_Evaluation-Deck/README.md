# EVALUTATION-DECK

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: YES
+ DOWNLOADABLE: YES

Description: A powerful demon has sent one of his ghost generals into our world to ruin the fun of Halloween. The ghost can only be defeated by luck. Are you lucky enough to draw the right cards to defeat him and save this Halloween?

## NOTES

1. The first thing that sticks out to me after loading the webpage is that there is a jquery-migrate-1.2.1 library
2. The fact that they give the version number makes me think there could be a vulnerability
3. The other thing is once inspecting the page and going to console we have a warning with 'JQMIGRATE: jQuery.browser is deprecated'
4. After further exploration this article helped with the ideas behind the exploitation <https://chris.heald.me/2013/jquery-migrate-xss/>

## - TESTING

1. In the browser console let's run the following
   1. > ```$("a[href='<img src=x onerror=prompt(1) />']")```
   2. This should create an error popup with the value of 1
2. Let's try and exploit further - this will try to load the flag.txt file when the #row1 div is clicked

```js
    $(document).ready(function () {
        $("#row1").click(function (e) {
            e.preventDefault();
            window.location.href = "../flag.txt";
        });
    });
```
