import discord
import json

from datetime import datetime

from dp.utils.util import get_loading_footer, get_message
from dp.utils.emotes import DPEmote
from dp.utils.area import Area
from dp.pogo import Stop, Gym, Mon, Item
from dp.dp_objects import dp

class Board():
    def __init__(self, board):
        self.original_board = board.copy()
        self.board = board.copy()
        self.embed = discord.Embed()
        self.area = Area(board["area"])
        self.static_map = ""

        self.old_ids = ["also update empty boards on start :)"]
        self.new_ids = []
        self.is_new = True

    async def get_message(self):
        self.channel = await dp.bot.fetch_channel(self.board["channel_id"])
        self.message = await self.channel.fetch_message(self.board["message_id"])
    
    def embed_details(self, text):
        self.embed.description = text
        self.embed.title = self.board.get("title", "")
        self.embed.timestamp = datetime.utcnow()
        self.embed.set_footer(text=self.area.name)
        self.embed.set_image(url=self.static_map)

    def generate_text(self, objs, template):
        text = ""
        for obj in objs:
            entry = template.get(obj)
            if len(text) + len(entry) >= 2048:
                break
            text += entry

        if len(objs) == 0:
            text = dp.files.locale["empty_board"]
            self.static_map = ""

        self.embed_details(text)
    
    def standard_dict(self):
        for k, v in self.standard_format.items():
            if k not in self.board.keys():
                self.board[k] = v
    
    async def get(self):
        await self.get_objs()
        self.is_new = self.old_ids != self.new_ids
        self.old_ids = self.new_ids
        if self.is_new:
            await self.generate_embed()

        return self.embed

#######################################################################################
# Grunt BOARD
#######################################################################################


#######################################################################################
# STAT BOARD
#######################################################################################

class StatBoard(Board):
    def __init__(self, bot, board):
        super().__init__(bot, board)
        self.all_stats = []
        self.templates = {
            "default": "{emote} {lang}"
        }

        self.standard_format = {
            "channel_id": "",
            "message_id": "",
            "title": self.bot.locale["stats"],
            "area": "",
            "wait": 2,
            "type": []
        }
        self.standard_dict()

    def gen(self, stat, template, lang, emote=""):
        t = template.format(emote=emote, lang=lang)
        return t.format(x=self.vals[stat][0][0])

    async def get_stats(self):
        mon_block = ""
        gym_block = ""
        stop_block = ""
        text = ""
        stats = ["gym_amount", "raid_active", "egg_active"]
        self.vals = {}
        for stat in self.all_stats:
            if stat in self.board["type"]:
                stats.append(stat)

        for stat in stats:
            val = await self.bot.queries.execute(stat, sql_fence=self.area.sql_fence)
            self.vals[stat] = val

        for stat in stats:    
            if "mon" in stat:
                continue

            elif stat == "gym_amount":
                g = self.gen(stat, self.templates["default"], self.bot.locale["total_gyms"], self.bot.custom_emotes["gym_white"]) + "\n"
            elif stat == "raid_active":
                g = self.gen(stat, self.templates["default"], self.bot.locale["active_raids"], self.bot.custom_emotes["raid"])
                if "egg_active" in stats:
                    g += " | " + self.bot.locale["eggs"].format(x=self.vals["egg_active"][0][0]) + "\n"
                    stats.remove("egg_active")
            elif stat == "egg_active":
                g = self.gen(stat, self.templates["default"], self.bot.locale["active_eggs"], self.bot.custom_emotes["raid"]) + "\n"
            gym_block += g
        text = mon_block + "\n" + gym_block + "\n" + stop_block
        self.embed_details(text)

#######################################################################################
# HUNDO BOARD
#######################################################################################

class HundoBoard(Board):
    def __init__(self, bot, board):
        super().__init__(bot, board)
        self.mons = []

    async def get_objs(self):
        hundos = await self.bot.queries.get_active_hundos(self.bot.config, self.area.sql_fence)
        for mid, form, atk, defe, sta in hundos:
            mon = Mon(self.bot, mid, form=form)
            self.mons.append(mon)

    async def generate_embed(self):
        self.bot.templates.hundo_board()
        template = self.bot.templates.template
        self.static_map = await self.bot.static_map.hundo(self.mons)
        self.generate_text(self.mons, template)

#######################################################################################
# QUEST BOARD
#######################################################################################