import python_weather
import asyncio
import os

location = str(input("Enter the name of a city: "))

def temp(city):
    async def getweather(city):
        async with python_weather.Client(format=python_weather.METRIC) as client:
  
            weather = await client.get(city)
            print(weather.current.temperature)
    def temperature(city):
        if __name__ == "__main__":
            print()
        if os.name == "nt":
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(getweather(city))
    temperature(city)

temp(location)