![](https://media.discordapp.net/attachments/523253670700122144/694301358018396202/dp_maybee.png)

Discordopole takes what [Worldopole](https://github.com/brusselopole/Worldopole) left behind and puts it into Discord. The goal is to allow your users to get easy access to useful data.

- Supports **MAD** and **RDM**
- Written with language support in mind. Supports **English**, **German**, **French**, **Spanish** and **Polish**

### Links
- [**Wiki**](https://github.com/ccev/Discordopole/wiki) - Getting started, detailed feature overview and more.
- [**Discord**](https://discord.gg/cnT8Dmz) - Support, announcements and planned features.

### Features
There are two types of frontend features:
- Boards: messages that always stay updated with latest information
- Commands: allow users to get useful information they want

Screenshots and more information: [Board Wiki Page](https://github.com/ccev/Discordopole/wiki/Boards) and [Command Wiki Page](https://github.com/ccev/Discordopole/wiki/Commands)

### Added Features in this branch
You will need to change emote repo in config/config.ini to `emote_repo = https://raw.githubusercontent.com/alexmartz710/dp_emotes/master/` and use `!get emote` again in your trash server to get those new emotes

Stat Boards:
- lure_amount: total amount of active lures
- lure_types: amount of different lure types

![](https://i.imgur.com/sJESVBr.png)

- raid_lvl_1_active: amount of active lvl 1 raids
- raid_lvl_3_active: amount of active lvl 3 raids
- raid_lvl_4_active: amount of active lvl 4 raids
- raid_lvl_5_active: amount of active lvl 5 raids
- raid_lvl_6_active: amount of active lvl 6 raids
- raid_lvl_7_active: amount of active lvl 7 raids
- raid_lvl_8_active: amount of active lvl 8 raids

You can use `!board create stats area raid lvl all` instead of `!board create stats area raid lvl 1, raid lvl 3, raid lvl 4, raid lvl 5, raid lvl 6, raid lvl 7, raid lvl 8,` to show level 1-8 raids

- egg_lvl_1_active: amount of active lvl 1 eggs
- egg_lvl_3_active: amount of active lvl 3 eggs
- egg_lvl_4_active: amount of active lvl 4 eggs
- egg_lvl_5_active: amount of active lvl 5 eggs
- egg_lvl_6_active: amount of active lvl 6 eggs
- egg_lvl_7_active: amount of active lvl 7 eggs
- egg_lvl_8_active: amount of active lvl 8 eggs

You can use `!board create stats area egg lvl all` instead of `!board create stats area egg lvl 1, egg lvl 3, egg lvl 4, egg lvl 5, egg lvl 6, egg lvl 7, egg lvl 8` to show level 1-8 eggs

![](https://i.imgur.com/IWy0nzN.png)

- scanned_active: amount of active scanned mons
- scanned_today: total amount of scanned mons today
- average_iv_active: average iv of alle scanned active mons
- average_iv_today: average iv of alle scanned mons of the day
- hundos_active: amount of active hundos
- hundos_today: total amount of hundos today
- iv0_active: amount of active mon with 0% iv
- iv0_today: total amount of mon with 0% iv

![](https://i.imgur.com/TiplrNK.png)

other:
- Neutral gyms for gym_teams ![](http://puu.sh/FKtrr/d7ff1ccf4c.png)
- Select timeframe without area for command !pokemon
- You can use an alternative pokemon table for pokemon command. you will have to expand your `config.ini`. see `config_example/config.ini`. Pokemon command will use alternative table, if timespan start is older than oldest pokemon in main table. 
- New config option `show_used_timespan_in_footer`. If True, footer will show everytime used timespan and area for pokemon command
