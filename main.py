from telepot import Bot
from telepot.loop import MessageLoop
from time import sleep

from commands import BotManager
from exceptions import CircuSpringInitBotError
from utils import init_logger, read_config


log = init_logger()
conf = read_config()

try:
    bot = Bot(conf['api_key'])
    manager = BotManager(bot)
except Exception as e:
    err = "Error while initing Bot. Details: {e}".format(e=e)
    log.critical(err)
    raise CircuSpringInitBotError(err)


def handle(msg):
    chat_id = msg['chat']['id']
    text = msg['text']
    username = msg['from']['username']
    log.debug("input: {text}".format(text=text))

    cmd = text.split()[0] if len(text.split()) else None
    text = text[len(cmd):] if cmd else ''

    callback = manager.commands.get(cmd, {}).get('cmd')
    if callable(callback):
        callback(chat_id, text, username=username)


# start main routine
msg = "Starting CircuSpringBot ..."
log.info(msg)
print(msg)
MessageLoop(bot, handle).run_as_thread()
while True:
    sleep(10)
