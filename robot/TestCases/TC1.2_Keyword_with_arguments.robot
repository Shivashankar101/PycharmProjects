*** Settings ***

Library  SeleniumLibrary


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
    get notification number
    close browser

*** Keywords ***
logIntoTwitter
    [Arguments]     ${username}     ${password}
    input text    name:session[username_or_email]       ${username}
    input text    name:session[password]    ${password}
    click element    xpath://*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span
    sleep   2

get notification number
    ${unread_msg}=    get text   xpath://*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[3]/div/div[1]/div
    [Return]    ${unread_msg}
    log to console   ${unread_msg}
#   this below command will save it to log.html
    log     ${unread_msg}
