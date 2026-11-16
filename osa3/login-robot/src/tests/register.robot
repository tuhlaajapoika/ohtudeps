*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Register Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  matti  matti123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

#Register With Too Short Username And Valid Password
# ...

#Register With Enough Long But Invalid Username And Valid Password
# ...

#Register With Valid Username And Too Short Password
# ...

#Register With Valid Username And Long Enough Password Containing Only Letters
# ...


*** Keywords ***
Create User And Input Register Command
    Create User  kalle  kalle123
    Input Register Command
