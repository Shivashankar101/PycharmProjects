*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://twitter.com/login
${browser}  Safari

*** Test Cases ***
InputBoxTest
#   to get default speed of selenium
    ${selenium_default_speed}=  get selenium speed
#   to print this default speed
    log to console  ${selenium_default_speed}

    open browser    ${url}  ${browser}
    maximize browser window
#   implicit wait  ---> applicable to all lines and declared ONCE at beginnining
    set selenium implicit wait  10 seconds

#   wait conditions (default it waits max 5 secods)
#   if we want selenium to wait for more time we have to set the timeout, as below
    set selenium timeout  10 seconds
#   above wait condition is only applicable to below line
    wait until page contains    Log in to Twitter


#   to set every statemet delay time for 1 sec
    set selenium speed  1
#   now the selenium speed is set to 1 sec, below statement will print it
    ${selenium_default_speed2}=  get selenium speed
    log to console  ${selenium_default_speed2}


    ${login_tab}    set variable    name:session[username_or_email]
    ${pass_tab}    set variable    name:session[password]

    element should be visible  ${login_tab}
    element should be visible  ${pass_tab}
    element should be enabled  ${login_tab}
    element should be enabled  ${pass_tab}

    clear element text  ${login_tab}
    input text  ${login_tab}    shivashankarawati@gmail.com
    clear element text  ${pass_tab}
    input text  ${pass_tab}    Pgpgpgagj100.

#   this puts the script to halt for 5 sec
    sleep   5 seconds

    close browser

*** Keywords ***
