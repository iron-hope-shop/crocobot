"""
cb.py

Crocobot
Made for #crocoducks

Author: Bradley Jackson
Version: 8.25.19
Maintainer: Bradley Jackson
E-mail: me@brad-jackson.com
Status: Production
"""
import logging
import slack
import re
from cmds.bot_functions import BotFunctions, TextResponse, ImageResponse
import time

start_time = time.time()
# This creates a timestamp which is retrieved by the uptime() function.

# The functions below are the supported chat commands of the bot.
# There are two main types of responses that streamline creating a new command:
#   + TextResponse()
#   + ImageResponse()
# These classes can be explored in greater detail the cmds package (./cmds/bot_functions).


def timfact(web_client, user_id, channel, **kwargs):
    # Note that any number of variables can be passed as keyword arguments.
    # The "text" variable is passed to almost every chat command; however, it is not always used.
    """
    *TimFact*
    Brings a Tim Fact into your life.

    *Arguments:*
    _number_ -- specify a number or leave it blank for a random Tim Fact.

    *Usage:*
    `timfact <number>`

    *Examples:*
    `cb Timfact 2`
    `crocobot tIMFaCT 99`
    `crocobot TIMfact`
    """
    # The docstrings are retrieved by the help() function and are formatted in Markdown for Slack.
    message = TextResponse(channel, username="Tim Fact 4 U", emoji=":timrobbins:",
                           text=kwargs['text'], path="./data/timfact").get_payload()
    # Note that text is used here to pass arguments given by the user.
    # For example, the user can choose to input "timfact" to get a random fact or "timfact 11" to retrieve the 11th Tim Fact.
    web_client.chat_postMessage(**message)
    # This class method unpacks the message block to be sent as a JSON to the Slack server.


def forrestfact(web_client, user_id, channel, **kwargs):
    """
    *Forrestfact*
    Tells you the Forrest Fact.

    *Usage:*
    `ff`

    *Examples:*
    `cb ff`
    `crocobot Ff `
    `crocobot FF`
    """
    message = TextResponse(channel, username="Forrest Fact",
                           emoji=":pepewhat:", path="./data/forrestfact").get_payload()
    # Note that there is no "text" passed to this function, so the response is always random.
    web_client.chat_postMessage(**message)


def phobias(web_client, user_id, channel, **kwargs):
    """
    *Phobias*
    Learn about your darkest fears.  Brought to you by Kevin Passmore.

    *Usage:*
    `phobias`

    *Examples:*
    `crocobot, phobias!  NOW!`
    `cb PhOBIAs!`
    `crocobot, phobias!`
    """
    message = TextResponse(channel, username="Phobias",
                           emoji=":scared:", path="./data/phobias").get_payload()
    web_client.chat_postMessage(**message)


def sharkattack(web_client, user_id, channel, **kwargs):
    """
    *Shark Attack*
    ShArK aTTACC!  Made for A-Ron.

    *Usage:*
    `sharkattack`

    *Examples:*
    `crocobot sharkattack`
    `cb sHARKatTACK!`
    `crocobot, sharkattack!`
    """
    message = TextResponse(channel, username="Shark Attack!",
                           emoji=":dancing-shark:", path="./data/sharkattack").get_payload()
    web_client.chat_postMessage(**message)


def pewpew(web_client, user_id, channel, **kwargs):
    """
    *Pew, pew.*
    Pewpew is brought to you by Jared Nesbit.

    *Usage:*
    `pewpew`

    *Examples:*
    `crocobot pewpew`
    `cb pewPEW!`
    `crocobot, pEwpEw!`
    """
    message = TextResponse(channel, "Pew, PEW!", ":bam:",
                           "./data/pewpew").get_payload()
    web_client.chat_postMessage(**message)


def chuckfact(web_client, user_id, channel, **kwargs):
    """
    *Chuck Fact*
    Chuck fact is brought to you by Jared Nesbit.
    
    *Usage:*
    `chuckfact`

    *Examples:*
    `crocobot chuckfact`
    `cb chuckfact!`
    `crocobot, chuckFACT!`
    """
    message = TextResponse(channel, username="Chuck Fact",
                           emoji=":chucknorris:", path="./data/chuckfact").get_payload()
    web_client.chat_postMessage(**message)


def uptime(web_client, user_id, channel, **kwargs):
    """
    *Uptime*
    Shows you how long the Crocobot has been online.  It may surprise you.
    
    *Usage:*
    `uptime`

    *Examples:*
    `crocobot uptime`
    `cb UPtime!`
    `crocobot, uPtIme!!`
    """
    uptime = f"I have been alive for {round(time.time() - start_time)} seconds.  Soon I will be reborn."
    message = TextResponse(channel, username="Crocobot",
                           emoji=":timer_clock:", text=uptime).get_payload()
    # The text can be manually passed to TextResponse() if we want specific text to be shown.
    # When doing this, a path should not be passed to TextResponse().  
    # See cmds.bot_functions for more details.
    web_client.chat_postMessage(**message)


def bfs(web_client, user_id, channel, **kwargs):
    """
    *Banana for Scale*
    Provides a banana for reference.

    *Example:*
    `cb bfs`
    `crocobot BFS!`
    """
    message = ImageResponse(channel, './data/bfs', username="Banana for Scale", emoji=":magic_banana:",
                            title_text="A banana.  For scale.", mouseover_text="Find more on r/BananasForScale!").get_payload()
    # This is the first instance of an ImageResponse(), which pulls a random image url from the data file.
    # See cmds.bot_functions for more details.
    web_client.chat_postMessage(**message)


def help(web_client, user_id, channel, **kwargs):
    """
    *Help*
    Explains the mighty powers of the crocoduck.  I am case/delimiter InSeNs1tIvE!@
    
    *Arguments:*
    _command_ -- specify a command or leave it blank for a full list of commands.
    
    *Usage:*
    `help <command>`
    
    *Examples:*
    `crocobot help`
    `cb hELPMe timFACT`
    `crocobot, help! img`
    """
    string = kwargs["text"]
    # In the case of the help function, the "text" variable is the intersection of the user-passed message and the keys in the "commands" dictionary.
    # See the examples in the docstring above.
    # There are more details of the logic in the message() function.
    val_test = BotFunctions().check_string(string)
    # The class method BotFunctions().check_string(arg) is used to make sure that "string" is the correct value type.
    if val_test in commands:
    # If/Else block checks if the user is querying a valid command and returns the doctring of that command's associated function.
        result = commands[val_test].__doc__
        message = TextResponse(channel, text=result).get_payload()
    else:
    # If the user did not query for a valid function, the bot replies with a list of its functions.
        result=[]
        for command in commands:
            result.append(command)
        result = f"*Here is a list of known commands:*\nType `cb help <command>` for more details.\n{result}"
        message = TextResponse(channel, text=result).get_payload()
    web_client.chat_postMessage(**message)


def bless(web_client, user_id, channel, **kwargs):
    """
    *Blessings, my son.*
    And to you.
    
    *Example:*
    `cb blessingsmyson`
    `crocobot ... blessingsmyson...`
    """
    message = ImageResponse(channel, path="./data/blessingsmyson", username="Blessings",
                            emoji=":timrobbins:", title_text="Blessings, my son.", mouseover_text="Tim").get_payload()
    web_client.chat_postMessage(**message)


def img(web_client, user_id, channel, **kwargs):
    """
    *Img*
    Spreads Crocoduck propaganda.
    
    *Example:*
    `cb img`
    `crocobot img!`
    """
    message = ImageResponse(channel, path="./data/imgs", username="Crocobot", emoji=":crocoduck:",
                            title_text="Behold, yonder crocoduck!", mouseover_text="qua-hissss...").get_payload()
    web_client.chat_postMessage(**message)


def cagemebro(web_client, user_id, channel, **kwargs):
    """
    *Cagemebro*
    Spreads Cage propaganda.
    
    *Example:*
    `cb cagemebro`
    `crocobot CAGEMEBRO!`
    """
    message = ImageResponse(channel, path="./data/cagemebro", username="Cage me, BRO!", emoji=":partycage:",
                            title_text="Why am I not in that image?", mouseover_text="A national treasure.").get_payload()
    web_client.chat_postMessage(**message)


def smashing(web_client, user_id, channel, **kwargs):
    """
    *Smashing*
    Smashing is brought to you by Jared Nesbit.
    
    *Usage:*
    `smashing`
    
    *Examples:*
    `crocobot smashing`
    `cb SMASHing!`
    `crocobot, sMaShInG!`
    """
    message = ImageResponse(channel, path="./data/smashing", username="Smashing", emoji=":smashing:",
                            title_text="The face.  The man.  The legend.", mouseover_text="Quite.").get_payload()
    web_client.chat_postMessage(**message)


def sanic(web_client, user_id, channel, **kwargs):
    """
    *Sanic*
    Gotta go fast!.
    
    *Example:*
    `cb sanic`
    `crocobot SANIC!`
    """
    message = ImageResponse(channel, path="./data/sanic", username="s4n1c", emoji=":sanic:",
                            title_text="COME ON, STEP IT UP!", mouseover_text="I am sped.").get_payload()
    web_client.chat_postMessage(**message)


def borismebro(web_client, user_id, channel, **kwargs):
    """
    *Borisme*
    Displays an aspect of Boris.
    
    *Example:*
    `cb borismebro`
    `cb borismebro 1`
    """
    message = ImageResponse(channel, path="./data/borismebro", username="BorisBro",
                            emoji=":chuckboris:", title_text=" ", mouseover_text=" ").get_payload()
    web_client.chat_postMessage(**message)


commands = {
    "timfact": timfact,
    "help": help,
    "img": img,
    "cagemebro": cagemebro,
    "sharkattack": sharkattack,
    "sanic": sanic,
    "pewpew": pewpew,
    "chuckfact": chuckfact,
    "smashing": smashing,
    "uptime": uptime,
    "bfs": bfs,
    "phobias": phobias,
    "bless": bless,
    "borismebro": borismebro,
    "ff": forrestfact
}


@slack.RTMClient.run_on(event="member_joined_channel")
def member_join(**payload):
    """member_join
    This function is run when a member joins a channel that the bot is in.
    When a member joins, the bot collects the JSON triggered from the event.
    The JSON is then unpacked into variables below.
    We are able to determine if the new member was invited or joined on their own and respond accordingly.
    """
    data = payload["data"]
    web_client = payload["web_client"]
    channel = data.get("channel")
    user_id = data.get("user")
    inviter = data.get("inviter")
    if inviter != None:
        result = f"Qua-hiss, <@{user_id}>!\n... <@{inviter}>, are you sure about this?"
    elif inviter == None:
        result = f"Qua-hiss, <@{user_id}>!\n... You found us!"
    message = TextResponse(channel, username="Crocobot",
                           emoji=":crocoduck:", text=result).get_payload()
    web_client.chat_postMessage(**message)


@slack.RTMClient.run_on(event="member_left_channel")
def member_leave(**payload):
    """member_leave
    Similar to the member_join function, this function is triggered when a member of the channel leaves.
    """
    data = payload["data"]
    web_client = payload["web_client"]
    channel = data.get("channel")
    user_id = data.get("user")
    result = f"R.I.P. in peace <@{user_id}>."
    message = TextResponse(channel, username="Crocobot",
                           emoji=":ripip:", text=result).get_payload()
    web_client.chat_postMessage(**message)


@slack.RTMClient.run_on(event="message")
def message(**payload):
    """message
    This function is triggered when someone send a message in a channel that the bot is in.
    Returns:
        A unpacked block to the RTM Client.
    """
    data = payload["data"]
    web_client = payload["web_client"]
    channel_id = data.get("channel")
    user_id = data.get("user")
    text = data.get("text")

    if user_id is not None and text is not "This content can\'t be displayed.":
    # Checks whether the message was sent by a bot or a user.
        regex_delim = re.sub("[^a-zA-Z0-9]", " ", str(text))
        # This regex grabs only alphanumeric characters from the message.
        split_text = regex_delim.split()
        # The words are then split and stored in a list.
        split_text_lower = [x.lower() for x in split_text]
        # The list is converted to lowercase.
        try:
            if split_text_lower[0] == "crocobot" or split_text_lower[0] == "cb":
            # Checks whether the bot was mentioned as the first word in the message.
                split_text_lower.pop(0)
                # If the bot was mentioned, we can remove the "crocobot" or "cb" from the beginning of the list to continue parsing
                intersection = [
                    x for x in split_text_lower if x in set(commands)]
                # Converts the commands dictionary to a list, checks whether each word is in the list of commands, and stores matching words in a list. 
                if intersection:
                    command = intersection[0]
                    # In the list of recognized commands, only the first command will be executed.
                    difference = [
                        x for x in split_text_lower if x not in commands]
                    if command == "help":
                        # Checks if the commands is "help" and runs the help() function with the list of commands as input.
                        intersection.pop(0)
                        # Removes "help" from the list.
                        return commands[command](web_client, user_id, channel_id, text=intersection)
                    else:
                        return commands[command](web_client, user_id, channel_id, text=difference)
                else:
                    return commands["help"](web_client, user_id, channel_id, text=[])
        except IndexError:
            pass


if __name__ == "__main__":
    on = True
    log_string = time.strftime("%H%M%S_%d%m%y")
    # Log nomenclature is HH:MM:SS_DDMMYY
    with open("./data/apitoken", "r") as file:
        global slack_token
        slack_token = file.read().replace("\n", "")
    # Fetches API token from store file
    # TODO: add encrypted store for API token
    logging.basicConfig(
        filename=f"./log/{log_string}.log",
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
    logger = logging.getLogger()
    logger.addHandler(logging.StreamHandler())
    rtm_client = slack.RTMClient(token=slack_token)
    # Initialize RTM Client
    while on:
        try:
            rtm_client.start()
        except KeyboardInterrupt as e:
            print(e)
            on = False
        except ValueError:
            logger.exception('Bot encountered ValueError')
        except KeyError:
            logger.exception('Bot encountered KeyError')
        except IndexError:
            logger.exception('Bot encountered IndexError')
        else:
            logger.exception('Bot encountered some other error...')
