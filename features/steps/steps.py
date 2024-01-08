from behave import given, when, then
from selenium import webdriver

@given('I am on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.clinicorp.com/planos')

@when('I click speak to a consultant')
def step_when(context):
    button = context.driver.find_element(By.ID, "comp-lflbv20z")
    button.click()

@then('I see the talk to a consultant page ')
def step_then(context):
    talk_page_title = context.driver.find_element(By.ID, "comp-lflbv20z")
    assert talk_page_title.text == "Falar com um consultor", f'Expected: Talk to a Consultant Page, Actual: {talk_page_title.text}'
