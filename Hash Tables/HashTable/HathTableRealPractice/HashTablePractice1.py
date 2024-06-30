import os

# Print the current working directory
print("Current working directory:", os.getcwd())

# List files in the current working directory
print("Files in the current directory:", os.listdir(os.getcwd()))

arr = []

with open("nyc_weather.csv", "r") as f:
    for line in f:
        tokens = line.split(',')
        try: 
            temperature = int(tokens[1])
            arr.append(temperature)
        except: 
            print("Invalid temperature. Ignore the row")

print(sum(arr[0:7])/7)

"""maximum = arr[0]
current = 0
for x in arr:
    if x > maximum:
        maximum = x
print(maximum)"""
print(max(arr[0:10]))