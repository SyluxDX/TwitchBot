""" Configuration module """
from datetime import datetime

class ChatConfig():
    """ Configuration class """
    ### Variables to change
    # channel/stream name
    channel = None
    # username used for connect to chat
    user = None
    # oauth token, formated as 'oauth:<token>'
    pwd = None
    run_flag = True
    # Twitch chat
    start_time = datetime.now()
    server = 'irc.twitch.tv'
    port = 6667
    chat_timeout = 2.0
    timestamp = True
    checkuser = False
    display_ping = False
    silent = False
    color = 'HotPink'
    twitch_colors = {'blue':'Blue', 'coral':'Coral', 'dodgerblue':'DodgerBlue', \
        'springgreen':'SpringGreen', 'yellowgreen':'YellowGreen', 'green':'Green', \
        'orangered':'OrangeRed', 'red':'Red', 'goldenrod':'GoldenRod', 'hotpink':'HotPink', \
        'cadetblue':'CadetBlue', 'seagreen':'SeaGreen', 'chocolate':'Chocolate', \
        'blueviolet':'BlueViolet', 'firebrick':'Firebrick'}
    # Twitch API
    client_id = None
    api = 'https://api.twitch.tv/kraken/'
    stream = 'streams/'

    def __str__(self):
        line = '------------------------\nConfigs:\n'
        line += ' channel: '+self.channel+'\n'
        line += ' user: '+self.user+'\n'
        if self.timestamp:
            line += ' timestamp: on\n'
        else:
            line += ' timestamp: off\n'
        if self.checkuser:
            line += ' checkuser: on\n'
        else:
            line += ' checkuser: off\n'
        if self.display_ping:
            line += ' displayPing: on\n'
        else:
            line += ' displayPing: off\n'
        line += ' color: '+self.color+'\n'
        line += '------------------------'

        return line

    def set_timestamp(self, arg):
        """ Display timestamp set method """
        if arg.lower() == 'on':
            self.timestamp = True
        if arg.lower() == 'off':
            self.timestamp = False
        if arg.lower() == 'toggle':
            self.timestamp = not self.timestamp

    def set_checkuser(self, arg):
        """ Check message's username set method """
        if arg.lower() == 'on':
            self.checkuser = True
        if arg.lower() == 'off':
            self.checkuser = False
        if arg.lower() == 'toggle':
            self.checkuser = not self.checkuser

    def set_display_ping(self, arg):
        """ Display ping/pong message set method"""
        if arg.lower() == 'on':
            self.display_ping = True
        if arg.lower() == 'off':
            self.display_ping = False
        if arg.lower() == 'toggle':
            self.display_ping = not self.display_ping

    def set_color(self, arg):
        """ Username text color set method """
        aux = arg.lower()
        if aux in self.twitch_colors:
            self.color = self.twitch_colors[aux]

    def list_colors(self, _):
        """ Prety list all Twitch colors available """
        colors = self.twitch_colors.values()
        colors = list(colors)
        colors.sort()
        i = 0
        line = ''
        for clr in colors:
            aux = clr+' '*16
            line += aux[:16]
            i += 1
            if i == 3:
                line += '\n'
                i = 0
        print(line)

    def list_config(self, _):
        """  Print corrent configurations """
        print(self)

    def uptime(self, _):
        """ Print script uptime """
        elapse = datetime.now()-self.start_time
        print('Uptime: {}'.format(elapse))

    def config_commands(self, arg):
        """ Change config using command line """
        commands = {'timestamp':self.set_timestamp, 'checkuser':self.set_checkuser, \
        'displayping':self.set_display_ping, 'color':self.set_color, \
        'listcolors':self.list_colors, 'config':self.list_config, 'uptime':self.uptime}
        commands = {'timestamp':(self.set_timestamp, 'Set message timestamp display, usage: [on][off]'), \
            'checkuser':(self.set_checkuser, 'Set if username is checked with !commands, usage: [on][off]'), \
            'displayping':(self.set_display_ping, 'Set echoing of Twitch\'s ping messages, usage: [on][off]'), \
            'color':(self.set_color, 'Set bot username color, usage: color, usage: <colorname>'), \
            'listcolors':(self.list_colors, 'Prints list of username\'s colors'), \
            'config':(self.list_config, 'Prints current configurations, usage: config'), \
            'uptime':(self.uptime, 'Prints uptime, usage: uptime')}
        arg = arg.lower().split()
        arg.append('toggle')
        if arg[0] == 'help':
            if arg[1] != 'toggle':
                # display command help
                if arg[1] in commands:
                    print('{}\n    {}'.format(arg[1], commands[arg[1]][1]))
                else:
                    print('Unkown command')
            else:
                # list all commands
                cmd = list(commands.keys())
                cmd.sort()
                print('Available commands:\n  ', end='')
                print('\n  '.join(cmd))
                print('For more information on a command, use \'help <command>\'')
        elif arg[0] in commands.keys():
            commands[arg[0]][0](arg[1])
        else:
            print('Unsupported command. Type "help" for a list of available commands:')
