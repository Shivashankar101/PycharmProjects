*** Settings ***

Library    SeleniumLibrary
Resource    ../Resources/r.robot

*** Variables ***
${url}  https://twitter.com/login
${browser}  Safari


*** Test Case ***
LoginTest
#    create webdriver    Firefox    executable_path=/Users/shiv/Desktop/drivers/gecko/geckodriver
    open browser    ${url}    ${browser}
    maximize browser window
    set selenium implicit wait  5
    logIntoTwitter      shivashankarawati@gmail.com     Pgpgpgagj100.
    get twitter notifications count
    close browser


