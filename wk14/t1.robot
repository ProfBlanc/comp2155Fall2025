*** Settings ***
Library    CustomConnectHandler.py

*** Variables ***
${DEVICE}       192.168.198.128
${USER}         ${EMPTY}
${PASS}         ${EMPTY}
${SECRET}       cisco1
${PORT}		30009
@{COMMANDS}   show version    show ip int brief

*** Test Cases ***
Test Connection
    ${output}=    Connect And Run Command    ${DEVICE}    ${USER}    ${PASS}    ${SECRET}    ${PORT}    show version

    FOR    ${cmd}    IN    @{COMMANDS}
            Log    Connect And Run Command    ${DEVICE}    ${USER}    ${PASS}    ${SECRET}    ${PORT}   ${cmd}
    END

    Log    ${output}
