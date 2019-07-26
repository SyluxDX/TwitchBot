""" Twitch chat functions """
# disabling general exception,too many attributes
# pylint: disable=W0702,R0902

import time
import socket
import commands

class ChatTwitch():
    """ Class for interecting with twitch chat """
    def __init__(self, config):
        self.config = config
        self.irc = None
        self.cmds = commands.COMMANDS

    @staticmethod
    def is_console(line):
        """ Check if message is from twicth console """
        if 'PRIVMSG' in line:
            return False
        return True

    @staticmethod
    def get_msg(line):
        """ Extract message from twicth chat """
        user = line.split('!')[0]
        aux = line[line.find('PRIVMSG'):]
        i = aux.find(':')
        msg = aux[i+1:]
        return user[1:], msg

    def check_command(self, msg):
        """ Check message for a command to execute """
        # generalize function with dic
        # check for specific user
        if self.config.checkuser and msg[0] != self.config.user:
            return
        if msg[1][0] == '!':
            args = {'uptime':self.config.start_time, 'user':msg[0]}
            cmd = msg[1][1:]
            if cmd in self.cmds:
                cmd_rsp = self.cmds[cmd](args)
                rsp = 'PRIVMSG #{} :{}'.format(self.config.channel, cmd_rsp)
                self.irc.send(rsp.encode())
        else:
            return

    def change_color(self):
        """ Change user's text color in chat """
        msg = 'PRIVMSG #{} :/color {}\r\n'.format(self.config.channel, self.config.color)
        self.irc.send(msg.encode())

    def connect_chat(self):
        """ Connect to a Channel's chat """
        # connect to twitch chat
        self.irc = socket.socket()
        self.irc.connect((self.config.server, self.config.port))
        # login to twitch chat
        msg = 'PASS {}\nNICK {}\nJOIN #{}\n'.format(self.config.pwd, \
            self.config.user, self.config.channel)
        self.irc.send(msg.encode())

        connecting = True
        while connecting:
            readbuffer = self.irc.recv(1024).decode()
            for line in readbuffer.split('\r\n'):
                if 'End of /NAMES list' in line:
                    print("Bot joinned %s's chat"%(self.config.channel))
                    connecting = False
                    break
        if not self.config.silent:
            msg = 'PRIVMSG #{} :bot joinned\r\n'.format(self.config.channel)
            self.irc.send(msg.encode())

    def read_chat(self):
        """ Read twicth chat.

        If timeout is defined and > 0 the function returns when
        no messages were recieved longer than timeout"""
        while self.config.run_flag:
            try:
                if self.config.chat_timeout > 0:
                    self.irc.settimeout(self.config.chat_timeout)
                readbuffer = self.irc.recv(1024)
            except KeyboardInterrupt:
                break
            except socket.timeout:
                #print('socket timeout..')
                continue
            except:
                print('general catch in read_chat')
                continue

            for line in readbuffer.decode().split('\r\n'):
                if line == '':
                    continue

                elif self.is_console(line) and 'PING' in line:
                    msg = 'PONG tmi.twitch.tv\r\n'
                    self.irc.send(msg.encode())
                    if self.config.display_ping:
                        if self.config.timestamp:
                            print('[%s]'%(time.strftime('%Y-%m-%d %H:%M:%S')), end='')
                        print(msg)

                else:
                    msg = self.get_msg(line)
                    self.check_command(msg)
                    if self.config.timestamp:
                        print('[%s]'%(time.strftime('%Y-%m-%d %H:%M:%S')), end='')
                    print('%s: %s'%(msg[0], msg[1]))
