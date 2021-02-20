*** Settings ***
Library  SeleniumLibrary
*** Test Cases ***
FramesTest
    open browser    https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html   Safari
    maximize browser window

    select frame    packageListFrame
    click link    org.openqa.selenium
    unselect frame

    select frame  packageFrame
    click link  AcceptedW3CCapabilityKeys
    unselect frame

    close browser