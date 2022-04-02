import asyncio
import json
import os
from tkinter.messagebox import QUESTION
import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
#test_ServerID = 958560848174010368

client = discord.Client()

def get_score():
    leaderboard = ' '
    id = 1
    r = requests.get(url="http://127.0.0.1:8000/api/score/leaderboard/")

    json_data = json.loads(r.text)
    for item in json_data:
        leaderboard += str(id) + "  —> " + \
            item['name'] + "  " + str(item['points']) + " points" + "\n\n"
        id += 1
    return leaderboard


def update_score(user, points):
    url = "http://127.0.0.1:8000/api/score/update/"
    new_score = {'name': user, 'points': points}
    x = requests.post(url, data=new_score)
    return


def get_question():
    qs = ''
    id = 1
    answer = 0
    r = requests.get("http://127.0.0.1:8000/api/random/?format=api")
    json_data = json.loads(r.text)

    question_points = json_data[0]['question_points']
    chrono = json_data[0]['chrono']

    qs += "Question — " + str(question_points) + \
        " points -  " + str(chrono) + " sec " + "\n\n\n"
    qs += json_data[0]['title'] + "\n\n"

    for item in json_data[0]['answer']:
        qs += str(id) + " – " + item['answer'] + "\n"
        if item['is_correct']:
            answer = id
        id += 1
    return qs, answer, question_points, chrono


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('!score'):
        leaderboard = get_score()
        await message.channel.send(leaderboard)

    if message.content.startswith('!quiz'):
        qs, answer, points, chrono = get_question()
        await message.channel.send(qs)

        def check(m):
            return m.content.isdigit() == True

        try:
            guess = await client.wait_for('message', check=check, timeout=chrono)
        except asyncio.TimeoutError:
            return await message.channel.send('Temps écoulé!')
        if int(guess.content) == answer:
            user = guess.author
            msg = str(guess.author.name) + ' valide ' + str(points) + ' points'
        else:
            await message.channel.send('mauvaise réponse')
            user = guess.author
            points = -points
            msg = str(guess.author.name) + ' ' + str(points) + ' points'

        await message.channel.send(msg)
        update_score(user, points)

client.run(BOT_TOKEN)
