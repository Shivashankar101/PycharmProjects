*** Settings ***

Library  SeleniumLibrary


*** Variables ***
${url}  https://twitter.com/login
${browser}  Safari


*** Test Case ***
LoginTest
#    create webdriver    Firefox    executable_path=/Users/shiv/Desktop/drivers/gecko/geckodriver
    open browser    ${url}    ${browser}
    logIntoTwitter
    close browser

*** Keywords ***
logIntoTwitter
    input text    name:session[username_or_email]    Shivashankarawati@gmail.com
    input text    name:session[password]    Pgpgpgagj100.
    click element    xpath://*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span
