import discord
from discord.ext import commands
from game.player import Bot, Player
from game.game import Game

bot = commands.Bot(command_prefix=".")

GAME: Game = None
PLAYER_BOT: Bot = None
PLAYER_CLIENT: Player = None
version = "V0.99 BETA"


# евенты
@bot.event
async def on_ready():
    print('Logged')


# @bot.event
async def on_message(message):
    print('{0.author} пишет: {0.content} в канале #'.format(message) + message.channel.name)


# команды
@bot.command(pass_context=True)
async def _math(ctx, a, b):
    await ctx.send(int(a) + int(b))


@bot.command(pass_context=True)
async def _send_embed(ctx, title, descr):
    embed = discord.Embed(
        title=title,
        description=descr
    )
    await ctx.send(embed=embed)


# крестики нолики
@bot.command(pass_context=True)
async def _help(ctx, game):
    if game not in "сервер крестики-нолики кн".split(" "):
        await ctx.send('Я вас не понимаю. Напишите "._help сервер", "._help крестики-нолики",'
                 ' "._help кн"(крестики-нолики) по обстоятельствам')
    elif game == "крестики-нолики":
        embed = discord.Embed(
            title="КРЕСТИКИ НОЛИКИ " + version,
            description="""**._start** - начать игру.
            **._game_stat** - статус игры пример:
            ```
              0 1 2
            0 -|x|- 
            1 -|o|o
            2 -|-|x```
            **._move [x y]** - походить своей фишкой пример: ._move 2 1"""
        )
        await ctx.send(embed=embed)
    elif game == "кн":
        embed = discord.Embed(
            title="КРЕСТИКИ НОЛИКИ " + version,
            description="""**._start** - начать игру.
                    **._rules** - правила игры
                    **._game-stat** - статус игры пример:
                    ```
              0 1 2
            0 -|x|- 
            1 -|o|o
            2 -|-|x```
                    **._move [x y]** - походить своей фишкой пример: ._move 2 1
                    **._end** - закончить игру"""
        )
        await ctx.send(embed=embed)
    elif game == "сервер":
        await ctx.send("сервер")


@bot.command(pass_context=True)
async def _start(ctx):
    global GAME
    GAME = Game(player_x_id=ctx.author.id, player_o_id='bot')
    GAME.new_game()
    await ctx.send("----! Добро пожаловать в КРЕСТИКИ НОЛИКИ " + version + " !----\n"
                   " Напишите ***._rules*** чтобы получит список правил игры. Напишите ***._help кн***"
                   " или ***._help крестики-нолики*** чтобы получить список команд в крестиках ноликах!")


@bot.command(pass_context=True)
async def _end(ctx):
    GAME.change_status(False)
    await ctx.send("Пока:sob:. Будем ждать вас ещё!")


@bot.command(pass_context=True)
async def _move(ctx, x: int, y: int):
    if GAME.get_status():
        await ctx.send(GAME.provide_player_move(x, y, ctx.author.id))
        await ctx.send(GAME.get_field().draw_field())
    else:
        await ctx.send("Запустите игру чтобы сделать ход! Напишите ._start чтобы начать игры."
                       " Напишите ._help для подробной информации.")


@bot.command(pass_context=True)
async def _game_stat(ctx):
    pass
    # if GAME.get_status():
    #     await ctx.send(functions.draw_field(functions.field))
    # else:
    #     await ctx.send("Запустите игру чтобы посмотреть статус игры! Напишите **.\_start** чтобы начать игры."
    #                    " Напишите **.\_help крестики_нолики** для подробной информации.")


@bot.command(pass_context=True)
async def _rules(ctx):
    embed = discord.Embed(
        title="ПРАВИЛА ИГРЫ КРЕСТИКИ НОЛИКИ(" + version + ")",
        description="""Начиается всё с того что вы пишите ***._start*** и начинаете игру.
Чтобы походить вам надо написать ***._move [x][y]***, сразу после вас ходит робот(пока он ходит на рандом). Пример игры:
```Ваш ход: x
  0 1 2
0 x|-|-
1 -|-|-
2 -|o|-```
Вы пишите: ._move 0 1
Следующая стадия:
```Ваш ход: x
  0 1 2
0 x|-|o
1 x|-|-
2 -|o|-```
Игра заканчивается в четерёх случаях: вы выиграли, вы проиграли, ничья, вы закончили игру.

*Вы выиграли*:
Чтобы выиграть надо поставить три своего хода(который написан над полем) по горизантали, вертикали или диаганали.

*Вы проиграли*:
Вы проигрываете в том случае, когда робот ставит три своих хода по горизантали, вертикали или диаганали.

*Ничья*:
Ничья объявляется тогда, когда на поле не осталось свободного хода и при этом никто не виыграл.

*Вы закончили игры*:
Вы можете принудительно закончить игры написав ***._end***.

Если вы потеряли текущий статус игры?
Можете написать ***._game_stat***, чтобы получить текущий статус игры если вы запуталиясь в сообщениях.

Полный список команд в крестиках-ноликах или на всём сервере напишите ***._help [крестики-нолики/кн/сервер]***
    для крестиков-ноликов - "крестики-нолики" или "кн"
    для сервера - "сервер\""""
    )
    await ctx.send(embed=embed)

bot.run("NzkwNTc5NDUzNTkxNjgzMTEy.X-CqfQ.LEoyOPgr582syFTMj61haMtQmEw")
