[Base Branch](https://github.com/Rapptz/discord.py/tree/7f4c57dd5ad20b7fa10aea485f674a4bc24b9547)

* added to_dict() to channel, guild, message, ... objects

They appear as specified in the original documentation: https://discordapp.com/developers/docs/resources/channel

Ugly workaround for my specific niche case. Probably could have been written better but who cares it works.

Why?  
I need the data in its original form. Since the crossbar router I am building is supplying these very data. I don't want to create yet another arbitrary JSON format and let users wonder how those JSONs are built. The discord.py library doesn't expose the original JSON data so I edited the library.     
This way the JSON format I am providing is exactly as specified in the Discord's Developer Portal's Documentation.  
