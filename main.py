import discord
import yaml
from heroku_git_fs import HerokuGitFS
from discord.ext import commands
import os

if 'ON_HEROKU' not in os.environ:
    config = yaml.safe_load(open('config.yaml'))
else:
    config = {
        'token': os.environ.get('TOKEN'),
        'prefix': os.environ.get('PREFIX'),
        'remote_url': os.environ.get('REMOTE_URL')
    }


bot = commands.Bot(command_prefix=commands.when_mentioned_or(
    config['prefix']),
    description='A bot to make non Nitro members use non-global Nitro emotes on the servers it is in.',
    pm_help=True)


def load_cog(cog):
    try:
        bot.load_extension(cog)
    except Exception as e:
        print('Could not load cog ' + cog)
        print(e)


@bot.event
async def on_ready():
    if config['remote_url']:
        bot.heroku_git_fs = HerokuGitFS(remote_url=config['remote_url'], directory='databases', branch='master')
    print('------------')
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('Using prefix:')
    print(config['prefix'])
    print('------------')
    load_cog('animotes')
    print('Loaded animotes cog...')
    await bot.change_presence(activity=discord.Game(name='Use ' + config['prefix'] + 'register to enable me'))

bot.run(config['token'])
