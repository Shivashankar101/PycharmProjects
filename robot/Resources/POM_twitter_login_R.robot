*** Settings ***
Library  SeleniumLibrary
Variables  ../PageObjects/POM_twitter_locators.py

*** Keywords ***
Go to twitter page
    [Arguments]    ${url}     ${browser}
    open browser    ${url}     ${browser}
    set browser implicit wait  10
    maximize browser window

Enter Username and Password and login
    [Arguments]     ${username}     ${password}

    clear element text      ${username_locator}
    input text      ${username_locator}     ${username}

    clear element text      ${password_locator}
    input text      ${password_locator}     ${password}

    click element   ${login_button_xpath}

Check Error Message
    page should contain element     ${Error_message_xpath}

Verify successful login
    page should contain  Home

Log out
    scroll element into view    xpath://header/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]
    click element  xpath://header/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]
    sleep   3
    click element  xpath://*[@id="layers"]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/a[2]
    click element  xpath://*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div


Close my browser
    close all browsers



