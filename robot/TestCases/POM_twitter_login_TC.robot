*** Settings ***
Library  SeleniumLibrary
Resource  ../Resources/POM_twitter_login_R.robot
Suite Teardown  Close my browser

*** Variables ***
${url} =  https://twitter.com/login
${browser} =  Safari
${username} =   Shivashankarawati@gmail.com
${password} =  Pgpgpgagj100.

*** Test Cases ***
TC1
    Go to twitter page  ${url}  ${browser}
    set browser implicit wait  10
    Enter username and password and login  ${username}  ${password}
    Verify successful login
    sleep   5
    Log out
    sleep   5




