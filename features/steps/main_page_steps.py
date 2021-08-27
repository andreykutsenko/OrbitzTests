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

@then('Select "Departing" date to be {start_trip_week} weeks from today and "Returning" date to be {back_trip_week} weeks from today')
def select_date_trip(context, start_trip_week, back_trip_week):
    context.app.main_page.input_date(start_trip_week, back_trip_week)

@then('Click on Search')
def click_search_icon(context):
    context.app.main_page.click_icon()