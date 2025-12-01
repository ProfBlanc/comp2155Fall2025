*** Settings ***
Library    NetmikoLibrary

*** Variables ***
${DEVICE}       192.168.198.128
${USER}         ${EMPTY}
${PASS}         ${EMPTY}
${DEVICE_TYPE}  cisco_ios_telnet
${PORT}         30009
${SECRET}       cisco1

*** Test Cases ***
Test Connection
    Open Connection    ${DEVICE}    ${USER}    ${PASS}    ${DEVICE_TYPE}    ${PORT}    ${SECRET}

    ${output}=    Execute Command    show version
    Log    ${output}

    Close Connection
