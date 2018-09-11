""" Starts Twitch chat bot """
import threading
import config
import twitch

def main():
    """ Main loop """
    chat_config = config.ChatConfig()
    chat_config.silent = False
    chat = twitch.ChatTwitch(chat_config)

    print("Connecting to https://www.twitch.tv/{}".format(chat_config.channel))
    chat.connect_chat()
    print("  Echoing chat:\n")
    chat_child = threading.Thread(target=chat.read_chat)
    chat_child.start()
    while chat_config.run_flag:
        try:
            ans = input('>')
            if ans == 'exit':
                chat_config.run_flag = False
                print('Closing...')
                chat_child.join()
            else:
                chat_config.config_commands(ans)
        except KeyboardInterrupt:
            chat_config.run_flag = False

if __name__ == '__main__':
    main()
