from behave import given, when, then, step
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
import time
from environment import element_exists


def get_random_string():
    return ''.join(random.choice(string.ascii_letters) for _ in range(10))


@given(u'user is on the registration page')
def step_open_website(context):
    wait = WebDriverWait(context.driver, 10)
    context.driver.get('https://client.staging.laminar.video/register')


@when('user provides invalid "{text}"')
def step_impl(context, text):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.visibility_of_element_located((By.NAME, "{text}".format(text=text)))).send_keys("12")


@when('user fills the email address')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    random_string = get_random_string()
    email= random_string + "@laminar.laminar"
    wait.until(EC.visibility_of_element_located((By.NAME, "userEmail"))).send_keys(email)


@when('user clicks singup button')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Start your membership")]'))).click()


@when('user provides "{text}"')
def step_impl(context, text):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.visibility_of_element_located((By.NAME, "{text}".format(text=text)))).send_keys("12345678")


@when('user clicks "{text}" button')
def step_impl(context, text):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(text(), "{text}")]'.format(text=text)))).click()


@when('user clicks checkbox')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//span[contains(@class, "Checkbox_icon__fyzuz")]'))).click()


@when('user choose "{text}" plan')
def step_impl(context, text):
    wait = WebDriverWait(context.driver, 5)
    statement = element_exists(lambda: wait.until(EC.presence_of_element_located((By.XPATH, '//h2[contains(text(), "{text}")]/ancestor::div[contains(@class, "PlanCard_active")]'.format(text=text)))))
    while statement == False:
        statement = element_exists(lambda: wait.until(EC.presence_of_element_located((By.XPATH, '//h2[contains(text(), "{text}")]/ancestor::div[contains(@class, "PlanCard_active")]'.format(text=text)))))
        if statement:
            break
        else:
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, '//h2[contains(text(), "{text}")]'.format(text=text)))).click()
            except:
                wait.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@class, "rightNavigationButton")]'))).click()


@when('user provides valid payu card data')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    card_number = wait.until(EC.visibility_of_element_located((By.NAME, "ccard_number")))
    for x in range(0,4):
      card_number.send_keys("4242")
      time.sleep(0.005)

    wait.until(EC.visibility_of_element_located((By.NAME, "cname_on_card"))).send_keys("john")
    wait.until(EC.visibility_of_element_located((By.NAME, "ccvv_number"))).send_keys("123")
    wait.until(EC.visibility_of_element_located((By.NAME, "cexpiry_date_year"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//option[contains(text(), "2023")]'))).click()
    wait.until(EC.visibility_of_element_located((By.NAME, "cexpiry_date_month"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//option[contains(text(), "Feb (2)")]'))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//input[contains(@id, "pay_button")]'))).click()


@when('user provides valid stripe card data')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    card_number = wait.until(EC.visibility_of_element_located((By.NAME, "cardNumber")))
    for x in range(0,4):
      card_number.send_keys("4242")
      time.sleep(0.005)

    wait.until(EC.visibility_of_element_located((By.NAME, "billingName"))).send_keys("john")
    wait.until(EC.visibility_of_element_located((By.NAME, "cardCvc"))).send_keys("123")
    wait.until(EC.visibility_of_element_located((By.NAME, "cardExpiry"))).send_keys("1125")
    wait.until(EC.visibility_of_element_located((By.XPATH, '//span[contains(text(), "Zapisz kart")]/ancestor::button[contains(@class, "SubmitButton")]'))).click()


@when('user clicks PAY')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//input[contains(@value, "PAY")]'))).click()


@when('user provides AXIS')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//input[contains(@name, "password")]'))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//h3[contains(text(), "lease enter the Otp")]/following-sibling::input[contains(@name, "password")]'))).send_keys("123456")


@when('video is being played')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//span[(contains(@class, "current-time") and contains(text(), "0")]')))
    wait.until(EC.visibility_of_element_located((By.XPATH, '//h3[contains(text(), "lease enter the Otp")]/following-sibling::input[contains(@name, "password")]'))).send_keys("123456")


@then('Page title should contain "{text}"')
def step_impl(context, text):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.title_contains("{text}".format(text=text)))


@then('"In progress" loader is visible')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//h1[contains(text(), "In progress")]')))


@then('Error message "{text}" appears')
def step_impl(context, text):
    wait = WebDriverWait(context.driver, 10)
    assert element_exists(lambda: wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "{text}")]'.format(text=text)))))
