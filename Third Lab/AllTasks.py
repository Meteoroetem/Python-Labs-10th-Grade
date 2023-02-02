import python_weather, asyncio, os, sys, statistics

async def GetWeather():
    async with python_weather.Client(format=python_weather.METRIC) as client:
    # fetch a weather forecast from a city
        weather = await client.get("Tel Aviv")
    # returns the weather
        return weather

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
        print("At",date,"it will be", end=' ')
        if temp > 30:
            print(str(temp)+"°C! Flaming hot!")
        elif temp > 25:
            print(str(temp)+"°C! Averege Israeli weather!")
        elif temp > 17:
            print(str(temp)+"°C! Nice!")
        elif temp > 10:
            print(str(temp)+"°C! Unusually cold!")
        else:
            print(str(temp)+"°C! Are you sure your in Israel?")


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
        if grade == 999:
            sys.exit()
        elif grade >= 85:
            print("ןייטצמ דימלת")
        elif grade >= 65:
            print("הפי דמול")
        else:
            print("ךיגישה רפש")

def SeventhTask():
    h = int(input("What's the height?"))
    heights = [h]
    while h >= 0:
        h = int(input("What's the height?"))
        if h>0:
            heights.append(h)
    avrg = statistics.mean(heights)
    print(avrg)

def EighthTask():
    inp = str(input("Type something: "))
    for char in inp:
        print( 2 * char, end="")
def NinthTask():
    inp = str(input('Type something: '))
    print(inp.count(' ') + 1)