*** Settings ***
Library  SeleniumLibrary
Resource  ../Resources/login_twitter.robot
Suite Setup  Go to twitter login page
Suite Teardown  Close my browser
#Test Template  Invalid input test


*** Test Cases ***
TC1:Invalid username, Invalid password        123     123

*** Keywords ***

Invalid input test
    set selenium implicit wait  10
    set browser implicit wait  10
    [Arguments]      ${username}         ${password}
    Username tab should be enabled
    Enter User Name     ${username}
    Password tab should be enabled
    Enter Password      ${password}
    Login button should be enabled
    Click Login
    sleep  5
    Error message should be present



Valid Input test
    [Arguments]      ${username}         ${password}

    Username tab should be enabled
    Enter User Name     ${username}
    Password tab should be enabled
    Enter Password      ${password}
    Login button should be enabled
    Click Login
    Ensure Successful Login
    Log out


