from behave import given, when, then

@given('Open main page')
def open_page(context):
    context.app.main_page.open()

@when('Select {tab_text} option')
def select_tab_option(context, tab_text):
    context.app.main_page.click_tab(tab_text)

@then('Enter "{city_field}": {city_text}')
def select_city(context, city_field, city_text):
    context.app.main_page.input_city(city_field, city_text)