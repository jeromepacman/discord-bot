import discord
import requests
import json
import asyncio
import os

from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

client = discord.Client()

def get_score():
    leaderboard = ''
    id = 1
    response = requests.get(url="http://127.0.0.1:8000/api/score/leaderboard/")

    json_data = json.loads(response.text)
    for item in json_data:
        leaderboard += str(id) + ' ' + item['name'] + ". " + str(item['points']) + "\n"
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
    response = requests.get("http://127.0.0.1:8000/api/random/")
    json_data = json.loads(response.text)
    qs += "Question: \n"
    qs += json_data[0]['title'] + "\n\n"

    for item in json_data[0]['answer']:
        qs += str(id) + "–" + item['answer'] + "\n"
        if item['is_correct']:
            answer = id
        id += 1

    points = json_data[0]['points']

    return qs, answer, points

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!score'):
        leaderboard = get_score()
        await message.channel.send(leaderboard)

    if message.content.startswith('!quiz'):
        qs, answer, points = get_question()
        await message.channel.send(qs)

        def check(m):
            return m.content.isdigit() == True

        try:
            guess = await client.wait_for('message', check=check, timeout=8.0)
        except asyncio.TimeoutError:
            return await message.channel.send('Temps écoulé !')

        if int(guess.content) == answer:
            user = guess.author
            msg = str(guess.author.name) + ' valide +' + str(points) + ' points'
            await message.channel.send(msg)
            update_score(user, points)
        else:
            await message.channel.send('tss tss, mauvaise réponse')


client.run(BOT_TOKEN)

