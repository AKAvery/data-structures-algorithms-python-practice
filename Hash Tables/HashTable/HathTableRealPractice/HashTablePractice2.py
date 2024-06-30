weather_dict = {}

with open('nyc_weather.csv', 'r') as f:
    for line in f:
        tokens = line.split(',')
        try: 
            day = tokens[0]
            temperature = int(tokens[1])
            weather_dict[day] = temperature
        except: 
            print("Invalid temperature. Ignore the row")
print(weather_dict['Jan 9'])   
print(weather_dict['Jan 4']) 