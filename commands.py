
class BotManager:
    def __init__(self, bot):
        self.bot = bot
        self.commands = self._add_commands()

    def _add_commands(self):
        return {
            "/help": {
                'cmd': self._help,
                'desc': "Scrive i comandi disponibili"
            },
            "/ciao": {
                'cmd': self.cmd_ciao,
                'desc': "Saluta.. Salute!"
            },
        }

    def _help(self, chat_id, text, **kw):
        commands = [(k, v['desc']) for k, v in self._add_commands().items()]
        msg = ""
        for cmd, descr in commands:
            msg += f"{cmd} : {descr}\n"
        self.bot.sendMessage(chat_id, msg)

    def cmd_ciao(self, chat_id, text, **kw):
        username = kw.get('username', "carissimo")
        msg = f"Ma ciao {username}, benvenuto al CircuSpring 2020!"
        self.bot.sendMessage(chat_id, msg)
