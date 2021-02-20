*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
NavigationTest
    open browser    https://www.google.com   Safari
    maximize browser window
    print current location

    go to   https://twitter.com/login
    print current location

#    to take screen shot of an element / logo
    capture element screenshot    xpath://*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div    /Users/shiv/PycharmProjects/robot/TestCases/screenshots/login.png
#    to take full page screenshot
    capture page screenshot    /Users/shiv/PycharmProjects/robot/TestCases/screenshots/twitter_page.png


    go back
    print current location
    sleep  2


    close browser

*** Keywords ***
print current location
    ${location}     get location
    log to console      ${location}