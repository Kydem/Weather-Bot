import os
import discord
import python_weather
from discord_slash import SlashCommand
from dotenv import load_dotenv
from discord_slash.utils.manage_commands import create_option

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = int(os.getenv('DISCORD_GUILD'))
client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)

async def get_weather(place=str):
    client = python_weather.Client(format=python_weather.IMPERIAL)
    # fetch a weather forecast from a city
    weather = await client.find(place)
    return weather


# Startup Information
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('with ur mom'))
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='your breathing'))
    
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

@slash.slash(name="uwu")
async def uwu(ctx):
    await ctx.send("I did something")

@slash.slash(name="potato")
async def get_potato(ctx):
    await ctx.send("https://po.ta.to")

@slash.slash(name="ping")
async def _ping(ctx):
    await ctx.send("Pong!")
    
@slash.slash(name="hack_time")
async def hack_time(ctx):
   await ctx.send("yeet!")

@slash.slash(name="weather", options=[create_option(
   name='input', description='place', option_type=3, required=True)])
async def getweather(ctx, input=str):

    weather = await get_weather(input)
    temperature_string = f'The temperature is {weather.current.temperature} degrees fahrenheit in {weather.location_name}\n'
    forecast = [f'Date: {forecast.date} Sky: {forecast.sky_text} Temp: {forecast.temperature}' for forecast in weather.forecasts]
    forecast_string = '```' + '\n'.join(forecast) + '```'
    await ctx.send('```WEATHER REPORT:\n' + temperature_string + forecast_string + '```')


client.run(TOKEN)