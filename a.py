from weather import Weather, Unit
weather = Weather(unit=Unit.CELSIUS)

city=raw_input("Enter Location!")
location=weather.lookup_by_location(city)
condition = location.condition()
print(condition.text())

forecasts = location.forecast()

for forecast in forecasts:
    print(forecast.date())
    print(forecast.high())
    print(forecast.low())
