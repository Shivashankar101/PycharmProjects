*** Settings ***

Library    SeleniumLibrary

*** Test Cases ***
#For Loop1
#    :For    ${i}    IN RANGE    1   10
#    \   log to console  ${i}
#
#For Loop2
#    :for    ${i}    IN    1 2 3 4 5
#    \   log to console  ${i}
#
#For Loop3
#    :for    ${i}    IN    1  2  3  4  5
#    \   log to console  ${i}

#For Loop4
#    @{list}  create list    1   2   3   4   5
#    :for    ${i}    IN    @{list}
#    \   log to console  ${i}

#For Loop5
#    :for    ${i}    IN    rama  shama   hari    krishna
#    \   log to console  ${i}

#For Loop6
#    :for    ${i}    IN    rama krishna
#    \   log to console  ${i}

For Loop7  ### this gives an ERROR ###
    :FOR    ${i}    IN    rama  shama   hari    krishna
    \   log to console  ${i}
    \   exit for loop if  ${i}==hari

#For Loop8
#    @{numlist}     create list     1   2   3   4   5
#    :for    ${i}    IN    @{numlist}
#    \   log to console  ${i}
#    \   exit for loop if  ${i}==3