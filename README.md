## animoteBot

A Discord Bot/Cog to use animated emotes, even if you don't have Nitro!

This bot takes advantage of the fact that Discord bots technically have access to all Discord Nitro features except for animated profile pictures.

## Installation

If you have an existing bot, put the `animotes.py` file in your cogs/plugins folder and use `bot.load_extension(<cogfolder>.animotes)` in the on_ready() call. This might vary slightly depending on your bot/loader used.

If you want to use the bot framework, download the repository and edit config.yaml to include your token at the token line. The prefix line does not matter as the bot doesn't use commands.

## Limitations

- This also works on multiple servers (creating a fake global emote system), since the bot checks for _all_ the emotes it has access to, rather than the ones in the current Guild/server.
- No wumboji.

## License

GPLv3
