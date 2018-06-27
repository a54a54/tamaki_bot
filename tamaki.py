# -*- coding: utf-8 -*-
import discord
import asyncio
import response

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('くふふ！')
    print('-------')

@client.event
async def on_member_join(member):
    ch_name = "welcome_channel_name" # 反応させたいチャンネル名を入れてください
    defchannel = discord.utils.get(member.server.channels, name=ch_name)
    m = """\
    たまきのひみつきちへようこそ！{0.mention}おやぶん！
    これから一緒に遊ぼうね！くふふっ！
    """
    await client.send_message(defchannel, m.format(member))
    # 付与させたい役職がなければここ以下3行は消してください
    name_role = "your_add_role_name" # 付与させたい役職があればここに書いてください
    addrole = discord.utils.get(member.server.roles, name=name_role)
    await client.add_roles(member, addrole)

@client.event
async def on_message(message):
    if client.user != message.author: # 自身のメッセージには反応しない
        if "環、じゃんけん" in message.content or "環、ジャンケン" in message.content: #じゃんけんする時
            m = response.janken(message.content)
            if type(m) is tuple:
                await client.send_message(message.channel, 'じゃんけん、' + m[0] + '！')
                await asyncio.sleep(1)
                await client.send_message(message.channel, m[1])
            else: # じゃんけんの手をちゃんと入力してない時
                await client.send_message(message.channel, m)
        else: # じゃんけん以外の応答
            m = response.res_message(message.content)
            if not m: # 応答できない時
                pass
            else:
                await client.send_message(message.channel, m.format(message))

client.run("BOT_TOKEN") # クライアント秘密鍵
