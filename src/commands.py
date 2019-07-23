""" Commands for twich chat messages """
import random
from datetime import datetime

do g:colors_namef display_timestamp(_):
    """ Display current time """
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    msg = 'Current Time: {}\r\n'.format(now)
    return msg

def display_uptime(args):
    """ Display script uptime """
    now = datetime.now()
    delta = now-args['uptime']
    msg = 'Uptime: {}\r\n'.format(delta)
    return msg

def roll_d6(_):
    """ Roll a 6 sided dice """
    roll = random.randint(1, 6)
    msg = 'Rolled a d6 with result: {}'.format(roll)
    return msg

def roll_d20(_):
    """ Roll a 20 sided dice """
    roll = random.randint(1, 20)
    msg = 'Rolled a d20 with result: {}'.format(roll)
    return msg

# args = (config.start_time, msg_user)
COMMANDS = {'time':display_timestamp\
    , 'uptime':display_uptime\
    , 'dice':roll_d6\
    , 'roll':roll_d20}
