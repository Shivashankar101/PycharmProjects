*** Settings ***
Library  SeleniumLibrary
Library  DataDriver     ../Testdata/robot_data_twitter.csv      #sheet_name=robot_data_twitter
Resource  ../Resources/login_twitter.robot

Suite Setup  Go to twitter login page
Suite Teardown  Close my browser
Test Template  Invalid input test


*** Test Cases ***
TC with ${username} and ${password}




*** Keywords ***
Invalid input test
    [Arguments]      ${username}         ${password}
    set selenium implicit wait  10
    set browser implicit wait  10
    Username tab should be enabled
    Enter User Name     ${username}
    Password tab should be enabled
    Enter Password      ${password}
    Login button should be enabled
    Click Login
    sleep  2
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


