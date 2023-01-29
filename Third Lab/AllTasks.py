import python_weather
import asyncio
import os
import sys

async def GetWeather():
    async with python_weather.Client(format=python_weather.IMPERIAL) as client:

    # fetch a weather forecast from a city
        weather = await client.get("Tel Aviv")
  
    # returns the current day's forecast temperature (int)
        return weather
  
    # get the weather forecast for a few days
        for forecast in weather.forecasts:
            print(forecast)
  
      # hourly forecasts
        for hourly in forecast.hourly:
            print(f' --> {hourly!r}')

def FirstTask():
    cnt = 0
    num = 3
    while num <= 96:
        num += 3
        cnt +=1
    print(cnt)

def SecondTask():
    inpStr = str(input("What are the numbers?"))
    nums = inpStr.split(",")
    for i in range(len(nums)):
        if nums[i][0] == nums[i][2]:
            print(str(nums[i]) + " is a palindrome!")

def ThirdTask():
    for i in range(1,30,1):
        money = int(input("How much money did student " + str(i) + " donate? "))
        if money > 50:
            print("!יישר כוח")

def FourthTask():
    weather = asyncio.run(GetWeather())
    weather.format = "C"
    forecasts = weather.forecasts
    for forecast in forecasts:
        temp = forecast.temperature
        date = forecast.date
        print("At",date,"it will be",str(temp)+"°C!")

def FifthTask():
    for i in range(1,10,1):
        school = int(input("How much money did student " + str(i) + " donate? "))
        if school >= 250:
            print("שילם דמי שכלול")
        elif school > 0:
            print("!!!עליך לשלם את חובותיך")
        else:
            sys.exit()

def SixthTask():
    for i in range(1,10,1):
        grade = int(input("What is student " + str(i) + "'s grade? "))
        if grade >= 250:
            print("שילם דמי שכלול")
        else:
            print("!!!עליך לשלם את חובותיך")

