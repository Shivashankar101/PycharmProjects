*** Settings ***

Library  SeleniumLibrary


*** Variables ***


*** Test Case ***
LoginTest
#    create webdriver    Firefox    executable_path=/Users/shiv/Desktop/drivers/gecko/geckodriver
    open browser    https://twitter.com/login}    Safari
    input text    name:session[username_or_email]    Shivashankarawati@gmail.com
    input text    name:session[password]    Pgpgpgagj100.
    click element    xpath://*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span
    close browser

*** Keywords ***