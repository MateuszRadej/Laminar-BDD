Feature: Sign up

    Scenario: no email provided 
        Given user is on the registration page
        When user clicks "Accept" button
        When user clicks singup button
        Then Error message "This field is required" appears

    Scenario: too short email provided 
        Given user is on the registration page
        When user provides invalid "userEmail"
        When user clicks singup button
        Then Error message "Please enter a valid email address" appears


    Scenario: no password provided
        Given user is on the registration page
        When user fills the email address
        When user clicks singup button
        When user clicks "Continue" button
        Then Error message "Password must meet the requirements" appears
 
    Scenario: too short password provided 
        Given user is on the registration page
        When user fills the email address
        When user clicks singup button
        When user provides invalid "password"
        When user clicks "Continue" button
        Then Error message "Password must meet the requirements" appears

    Scenario: successful signup wihtout buiyng a plan
        Given user is on the registration page
        When user fills the email address
        When user clicks singup button
        When user provides "password"
        When user clicks "Continue" button
        When user clicks "Skip this step" button
        Then Page title should contain "Home"


