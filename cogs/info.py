import discord
# from discord import app_commands, Intents, Client, Interaction
from discord.ext import commands
from discord import app_commands
# others
import random
import re
import os
import requests
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://soren:cdD2_qWUYRk-d4G@orion.iztml.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
base = cluster["OrionDB"]

ign_cur = base["ign"]


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Info is Loaded ...")


    @app_commands.command(name="userinfo", description="Shows info about a user")
    async def userinfo(self,interaction:discord.Interaction, user:str = None):
        if user:
            try:
                # get the member IDs in the string
                guild = interaction.guild
                # returns list of strings
                matches = re.findall(r"<@!?([0-9]{15,20})>", user)
                # create list of discord.Member
                member = guild.get_member(int(matches[0]))
                user = member
            except:
                user = interaction.guild.get_member_named(user)
            if not user:
                try:
                    user = interaction.guild.get_member(int(name))
                except:
                    pass
            if not user:
                embed = discord.Embed(color = 0x5865F2,description = "Index ERROR!")
                embed.set_author(name = "ERROR", icon_url= self.bot.user.avatar)
                await interaction.response.send_message(embed = embed)
                return
        else:
            user = interaction.user

        if user.id != 815908097288962099:
            avi = user.avatar.replace(static_format='png')
            if isinstance(user, discord.Member):
                roles = roles = [role for role in user.roles]
                for role in roles:
                    if role.name=="@everyone":
                        roles.remove(role)
                        break

            
            if user.nick==None:
                nn=user.name
            else:
                nn=user.nick
            
            if user.id == 736818641907089520:
                em = discord.Embed(color = 0xfea0c3)
                em.set_author(name = "QUEEN's INFO", icon_url= self.bot.user.avatar)
                em.add_field(name="QUEEN's NAME",value=f"```\n{user}```", inline=True)
                em.add_field(name = "QUEEN's ID",value = f"```\n{user.id}```",inline= True)
                em.add_field(name="QUEEN's NICK NAME", value=f"```\n{nn}```", inline=False)
            else:
                em = discord.Embed(color = 0x5865F2)
                em.set_author(name = "USER INFO", icon_url= self.bot.user.avatar)
                em.add_field(name="USER NAME",value=f"```\n{user}```", inline=True)
                em.add_field(name = "USER ID",value = f"```\n{user.id}```",inline= True)
                em.add_field(name="NICK NAME", value=f"```\n{nn}```", inline=False)


            
            x = ign_cur.find_one({"dc_id":user.id})

            val_user_name = None
            chess_user_name = None
            lichess_user_name = None

            if x != None:
                if 'val_user' in x.keys():
                    val_user_name = x["val_user"]
                if 'chess_user' in x.keys():
                    chess_user_name = x["chess_user"]
                
                if 'lichess_user' in x.keys():
                    lichess_user_name = x["lichess_user"]
            
            lists = []
            emo = {"val":"<:valorant:814455293328228394>", "chess":"<:chess:830030544661119056>", "lichess":"<:lichess:837249373167026196>"}

            if val_user_name != None:
                try:
                    splited = val_user_name.split("#")
                    name = splited[0].replace(" ","%20")
                    tag = splited[1]
                    
                    s = f"{emo['val']} - [{val_user_name}](https://tracker.gg/valorant/profile/riot/{name}%23{tag}/overview)"
                except:
                    s = s = f"{emo['val']} - {val_user_name}"
                    
                lists.append(s)
            if chess_user_name != None:
                j = f"{emo['chess']} - [{chess_user_name}](https://www.chess.com/member/{chess_user_name})"
                lists.append(j)
            
            if lichess_user_name != None:
                k = f"{emo['lichess']} - [{lichess_user_name}](https://lichess.org/@/{lichess_user_name})"
                lists.append(k)
            
            if len(lists) != 0:
                text = "\n".join(lists)
                em.add_field(name = "IGNS", value = text, inline=True)
            else:
                em.add_field(name = "IGNS", value = "None", inline = True)

            if len(roles)>0:
                x = [role.name for role in roles]
                x.reverse()
                em.add_field(name=f"ROLES ({len(x)})", 
                            value=f"```\n{', '.join(x)}```", inline=False)
            elif len(roles)==0:
                em.add_field(name=f"ROLES ({len(roles)})", 
                            value="```\nNone```", inline=False)

            form='%d/%m/%Y %H:%M:%S'
            em.add_field(name='ACCOUNT CREATED ON (D/M/Y)', 
                        value=f"```\n{user.created_at.__format__(form)}```",inline=False)
            em.add_field(name='JOINED SERVER ON (D/M/Y)', 
                        value=f"```\n{user.joined_at.__format__(form)}```",inline=False)
            nitro=user.premium_since
            if nitro != None:
                em.add_field(name='BOOST STATUS (D/M/Y)', 
                            value='None' if nitro==None else f"```\n{nitro.__format__(form)}```",inline=False)
            em.set_thumbnail(url=avi)
            av=user.avatar.replace(static_format='png')
            await interaction.response.send_message(embed = em)

        else:
            avi = user.avatar.replace(static_format='png')
            if isinstance(user, discord.Member):
                roles = roles = [role for role in user.roles]
                for role in roles:
                    if role.name=="@everyone":
                        roles.remove(role)
                        break
            
            em = discord.Embed(color = 0x5865F2)
            em.set_author(name = "USER INFO", icon_url= user.avatar)
            em.add_field(name="USER NAME",value=f"```\n{user}```", inline=True)
            em.add_field(name = "USER ID",value = f"```\n{user.id}```",inline= True)
            
            if user.nick==None:
                nn=user.name
            else:
                nn=user.nick

            em.add_field(name='NICK NAME', value=f"```\n{nn}```", inline=False)

            em.add_field(name='VERSION', value= "`V3.1`", inline=True)
            dic = {"0":":zero:","1":":one:","2":":two:","3":":three:","4":":four:","5":":five:","6":":six:","7":":seven:","8":":eight:","9":":nine:","10":":one::zero:"}
            num = str(len(self.bot.guilds))
            if len(num) > 1:
                emo = ""
                for i in num:
                    emo = emo + dic[i]
            else:
                emo = dic[num]
            em.add_field(name='ACTIVE ON', value=f"{emo} servers", inline=True)


            mem1 = self.bot.get_user(693375549686415381)

            mem2 = self.bot.get_user(692066406384271451)

            mem3 = self.bot.get_user(736818641907089520)

            # def underline(x):
            #     x = str(x)
            #     j = []

            #     for i in x:
            #         if i == "_":
            #             j = x.split("_")

            #     if len(j) > 1:
            #         j = "\_".join(j)
            #         return j
            #     else:
            #         return x


            em.add_field(name='DEVELOPER TEAM', value=f"```diff\n> {mem1} \n-worked on design and development.\n\n> {(mem2)}\n-worked on development.\n\n> {mem3}\n-helped with ideas and suggestions.```", inline=False)

            if len(roles)>0:
                roles.reverse()
                em.add_field(name=f"ROLES ({len(roles)})", 
                            value=f"```\n{', '.join([role.name for role in roles])}```", inline=False)
            elif len(roles)==0:
                em.add_field(name=f"ROLES ({len(roles)})", 
                            value="```\nNone```", inline=False)

            form='%d/%m/%Y %H:%M:%S'
            em.add_field(name='ACCOUNT CREATED ON (D/M/Y)', 
                        value=f"```\n{user.created_at.__format__(form)}```",inline=False)
            em.add_field(name='JOINED SERVER ON (D/M/Y)', 
                        value=f"```\n{user.joined_at.__format__(form)}```",inline=False)

            em.set_thumbnail(url=avi)
            print(avi)
            av= user.avatar.replace(static_format='png')

            await interaction.response.send_message(embed = em)
    

    @app_commands.command(name="anime", description="Shows info about any anime")
    async def anime(self,interaction:discord.Interaction, name:str):
        try:
            url = f"https://api.jikan.moe/v4/anime?q={name}"
            req = requests.get(url)
            big_data = req.json()
            result_list = big_data["data"]
            result = result_list[0]
            id = result["mal_id"]
            all_data = requests.get(f"https://api.jikan.moe/v4/anime/{id}").json()['data']
            title = all_data['title']
            url = all_data['url']
            des = all_data['synopsis']

            x = des.split(" ")
            d = des.split(".")
            if x[0] == "Final":
                des = d[0] + "."


            anime_em = discord.Embed(title = title,url = url, description = des,color = 0x5865F2)
            
            anime_em.set_thumbnail(url = all_data['images']['jpg']['image_url'])

            if all_data['type'] != "Movie":
                air_from = all_data['aired']['from'][:10]
                air_to = all_data['aired']['to'][:10] if all_data['aired']['to'] != None else "unknown"
                anime_em.add_field(name = ":calendar_spiral: AIRED",
                    value = f"**FROM:** `{air_from}`\n**TO:** `{air_to}`",
                    inline = True)
            else:
                air_from = all_data['aired']['from'][:10]
                anime_em.add_field(name = ":calendar_spiral: AIRED",
                    value = f"**Released:** `{air_from}`")

            status = "Completed" if all_data['airing'] == False else "Airing"
            anime_em.add_field(name = ":page_facing_up: STATUS",
                value = f"{status}")

            anime_em.add_field(name = ":bookmark_tabs: TYPE",
                value = all_data['type'])

            if all_data['episodes'] != None:
                anime_em.add_field(name = ":cd: EPISODES",
                value = f"{all_data['episodes']} eps")
            else:
                anime_em.add_field(name = ":cd: EPISODES",
                value = "0 eps")

            anime_em.add_field(name = ":stopwatch: DURATION",
                value = f"{all_data['duration']}")

            anime_em.add_field(name = ":bar_chart: SCORE",
                value = f"**{all_data['score']} / 10 **")
            n = []
            for i in all_data["genres"]:
                n.append(i["name"])

            n = ", ".join(n)

            anime_em.add_field(name = ":scroll: GENRES",
                value = n,
                inline = False)
            
            await interaction.response.send_message(embed = anime_em)
        except:
            anime_em = discord.Embed(title = "Anime not found",color = 0x5865F2)
            await interaction.response.send_message(embed = anime_em)
    
    @app_commands.command(name="manga", description="Shows info about any manga")
    async def manga(self,interaction:discord.Interaction, name:str):
        try:
            url = f"https://api.jikan.moe/v4/manga?q={name}"
            req = requests.get(url)
            big_data = req.json()
            result_list = big_data["data"]
            result = result_list[0]
            id = result["mal_id"]
            all_data = requests.get(f"https://api.jikan.moe/v4/manga/{id}").json()['data']
            title = all_data['title']
            url = all_data['url']
            des = all_data['synopsis']

            x = des.split(" ")
            d = des.split(".")
            if x[0] == "Final":
                des = d[0] + "."

            manga_em = discord.Embed(color = 0x5865F2,title = title,url = url, description = des)
            
            manga_em.set_thumbnail(url = all_data['images']['jpg']['image_url'])

            air_from = all_data['published']['from'][:10]
            air_to = all_data['published']['to'][:10] if all_data['published']['to'] != None else "unknown"
            manga_em.add_field(name = ":calendar_spiral: PUBLISHED",
                value = f"**FROM:** `{air_from}`\n**TO:** `{air_to}`",
                inline = True)

            manga_em.add_field(name = ":page_facing_up: STATUS",
                value = all_data["status"])

            manga_em.add_field(name = ":bookmark_tabs: TYPE",
                value = all_data['type'])

            manga_em.add_field(name = ":book: LENGTH",
            value = f"**chapters:** {all_data['chapters']}\n**volumes:** {all_data['volumes']}")

            manga_em.add_field(name = ":chart_with_upwards_trend: RANK",
                value = f"TOP {all_data['rank']}")
            manga_em.add_field(name = ":bar_chart: SCORE",
                value = f"**{all_data['score']} / 10 **")
            n = []
            for i in all_data["genres"]:
                n.append(i["name"])
            n = ", ".join(n)
            manga_em.add_field(name = ":scroll: GENRES",
                value = n,
                inline = False)
            
            await interaction.response.send_message(embed = manga_em)
        except:
            manga_em = discord.Embed(title = "Manga not found",color = 0x5865F2)
            await interaction.response.send_message(embed = manga_em)
    

async def setup(bot):
    await bot.add_cog(Info(bot))