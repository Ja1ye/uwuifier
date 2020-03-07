import random
import discord
from discord.ext import commands


bot = commands.Bot(command_prefix="!")
chances = ["1", "2", "3", "4", "5", '6', '7', '8', '9', '10', '11', '12']
testchances = ["2"]
chances2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46"]
uwus = ['uwu', '(´・ω・｀)', '(*´∇｀)ﾉ', '(◕‿◕✿)', 'ღ(U꒳Uღ)', '(⁄˘⁄ ⁄ ω⁄ ⁄ ˘⁄)♡', 'ψ(｀∇´)ψ', " ", " ", " ", " "]
escapechances = ['1', '2']
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)



    async def on_message(self, message):
        if message.author == self.user:
            return


        if "!uwu".lower() in message.content:
            await message.delete()
            await message.channel.send(uwuify(message.content[5::]))
            await message.channel.send("- {0.author.mention}".format(message))


#uwuifies a player - 33% chance to escape
        role = str('uwu').lower()
        user = message.author
        if discord.utils.get(user.roles, name=role):
            biguwus = random.choice(uwus)
            await message.delete()
            await message.channel.send(uwuify(message.content))
            await message.channel.send("- {0.author.mention}".format(message))
        elif message.content == message.content:
            response = "{0.author.mention} has been uwu'd".format(message)
            shot = random.choice(range(55))
            if shot == 2:
                user = message.author
                role = str('uwu').lower()
                await message.channel.send(response)
                await user.add_roles(discord.utils.get(user.guild.roles, name=role))
        role = str('uwu').lower()
        user = message.author
        if discord.utils.get(user.roles, name=role):
            shot = random.choice(range(2))
            if shot == 1:
                await user.remove_roles(discord.utils.get(user.guild.roles, name=role))




client = MyClient()

client.run()
bot.run()