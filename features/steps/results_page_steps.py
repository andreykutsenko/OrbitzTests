from behave import then

@then('Our search results for {city_from}, {city_to} and the date with {start_trip_week} and {back_trip_week} are displayed correctly')
def verify_result(context, city_from, city_to, start_trip_week, back_trip_week):
    context.app.results_page.verify_search_result(city_from, city_to, start_trip_week, back_trip_week)