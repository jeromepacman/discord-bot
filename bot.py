import asyncio
import json
import os
import discord
import requests
from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
SCORE_URL = os.getenv('SCORE_URL')
UP_URL = os.getenv('UP_URL')
QUESTION_URL = os.getenv('QUESTION_URL')
board = f'**•´¯• Quizz Board •´¯•**'
userboard = f'ıllıllı Quizz Board ıllıllı\n'
# test_ServerID = 95856084817401036

client = discord.Client()


def get_score():
    leaderboard = ""
    id = 1
    r = requests.get(SCORE_URL)

    json_data = json.loads(r.text)
    for item in json_data:
        leaderboard += (
                str(id)
                + "  —> "
                + item["name"].split("#")[0]
                + "  "
                + str(item["points"])
                + " "
                + " \n"
        )
        id += 1
    return f'*{board}* \n\n {leaderboard}'


def update_score(user, points):
    url = UP_URL
    new_score = {"name": user, "points": points}
    requests.post(url, data=new_score)
    return


def get_question():
    qs = ""
    id = 1
    answer = 0
    r = requests.get(QUESTION_URL)
    json_data = json.loads(r.text)

    difficulty = json_data[0]["get_difficulty_display"]
    question_points = json_data[0]["question_points"]
    chrono = json_data[0]["chrono"]

    qs += (
            "**— Question —** "
            + " Niveau :   "
            + difficulty
            + "    💠 "
            + str(question_points)
            + " points   ⌚ ️"
            + str(chrono)
            + " _sec.._"
            + "\n\n"
    )

    qs += json_data[0]["title"] + "\n\n"

    for item in json_data[0]["answer"]:
        qs += str(id) + " – " + item["answer"] + "\n"
        if item["is_correct"]:
            answer = id
        id += 1
    return qs, answer, question_points, chrono, difficulty


@client.event
async def on_ready():
    print("logged in {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!ok"):
        await message.channel.send(f'Hey {message.author}')

    if message.content.startswith("!score"):
        leaderboard = get_score()
        await message.channel.send(leaderboard)

    if message.content.startswith("!quiz"):
        (qs, answer, question_points, chrono, difficulty) = get_question()
        await message.channel.send(qs)

        def check(m):
            return m.author == message.author and m.content.isdigit()

        try:
            guess = await client.wait_for("message", check=check, timeout=chrono)
        except asyncio.TimeoutError:
            return await message.channel.send("\n\n *Trop tard* 💤")

        await guess.delete(delay=10)
        if int(guess.content) == answer:
            user = guess.author
            msg = (
                    "Bonne réponse  ✅\n"
                    + str(guess.author.name)
                    + " valide "
                    + str(question_points)
                    + " points 😎")
            points = question_points
            await message.channel.send(msg)
            update_score(user, points)

        else:
            user = guess.author
            msg = (
                    "Mauvaise réponse 🔻\n"
                    + str(guess.author.name)
                    + " perd " +
                    str(question_points)
                    + " points 🥴")
            points = -question_points
            await message.channel.send(msg)
            update_score(user, points)


client.run(BOT_TOKEN)