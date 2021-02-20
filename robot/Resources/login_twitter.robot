*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url} =     https://twitter.com/login
${browser} =     Safari

*** Keywords ***

Go to twitter login page
    open browser    ${url}      ${browser}
    sleep   5

Username tab should be enabled
    element should be enabled    name:session[username_or_email]
#    clear element text    name:session[username_or_email]


Enter User Name
    [Arguments]     ${username}
    input text  name:session[username_or_email]   ${username}


Password tab should be enabled
    element should be enabled       name:session[password]
#    clear element text      name:session[password]

Enter Password
    [Arguments]     ${password}
    input text  name:session[password]  ${password}

Login button should be enabled
    element should be enabled   xpath://*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div


Click Login
    click element  xpath://*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div
    sleep   3

Error message should be present
    page should contain element  xpath://body/div[@id='react-root']/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]

Ensure Successful Login
    page should contain     Home

Log out
    scroll element into view    xpath://header/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]
    click element  xpath://header/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]
    click element  xpath://*[@id="layers"]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/a[2]
#    click element  xpath://*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div

Print Links on page
    ${links} =  get all links
    log to console  ${links}

Close my browser
    close all browsers





