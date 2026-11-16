*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  matti  matti123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ma  matti123
    Output Should Contain  Username must be at least three characters long and consist of letters only

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  matti123  matti123
    Output Should Contain  Username must be at least three characters long and consist of letters only

Register With Valid Username And Too Short Password
    Input Credentials  matti  lyhyt
    Output Should Contain  Password must be at least eight characters long and NOT consist of letters only

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  matti  aakkosia
    Output Should Contain  Password must be at least eight characters long and NOT consist of letters only

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command
