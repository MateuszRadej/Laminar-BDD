Feature: Payments

    Scenario: successful payment payu
        Given user is on the registration page
        When user clicks "Accept" button
        When user fills the email address
        When user clicks singup button
        When user provides "password"
        When user clicks "Continue" button
        When user choose "test123" plan
        When user clicks "Continue" button
        When user clicks checkbox
        When user clicks "Pay" button
        When user provides valid payu card data
        When user provides AXIS
        When user clicks PAY
        Then "In progress" loader is visible
        Then Page title should contain "Home"

   Scenario: successful payment stripe
        Given user is on the registration page
        When user fills the email address
        When user clicks singup button
        When user provides "password"
        When user clicks "Continue" button
        When user choose "laminar.testing.stripe.plan.name" plan
        When user clicks "Continue" button
        When user clicks checkbox
        When user clicks "Pay" button
        When user provides valid stripe card data
        Then "In progress" loader is visible
        Then Page title should contain "Home"


