"""
bot_functions.py

BotFunctions
    + check_number
        - Checks if the input is an integer.
    + check_string
        - Checks if the input is a string.
    + random_line
        - Takes a file as an input and returns a random line as a string.
    + indexed_line
        - Takes a file and an index as inputs and returns the line that coincides with the index. 
    + file_len
        - Takes a file as input and returns the number of lines in the file.

TextResponse
    + Builds a block for the Slack client (meant for text-only responses).
ImageResponse
    + Builds a block for the Slack client (meant responses that contain images).
FieldResponse
    - Not implemented, builds a block that shows a pretty list.

Interactive Block Kit Builder:
https://api.slack.com/tools/block-kit-builder?blocks=%5B%7B%22type%22%3A%22section%22%2C%22text%22%3A%7B%22type%22%3A%22mrkdwn%22%2C%22text%22%3A%22Hello%2C%20Assistant%20to%20the%20Regional%20Manager%20Dwight!%20*Michael%20Scott*%20wants%20to%20know%20where%20you%27d%20like%20to%20take%20the%20Paper%20Company%20investors%20to%20dinner%20tonight.%5Cn%5Cn%20*Please%20select%20a%20restaurant%3A*%22%7D%7D%2C%7B%22type%22%3A%22divider%22%7D%2C%7B%22type%22%3A%22section%22%2C%22text%22%3A%7B%22type%22%3A%22mrkdwn%22%2C%22text%22%3A%22*Farmhouse%20Thai%20Cuisine*%5Cn%3Astar%3A%3Astar%3A%3Astar%3A%3Astar%3A%201528%20reviews%5Cn%20They%20do%20have%20some%20vegan%20options%2C%20like%20the%20roti%20and%20curry%2C%20plus%20they%20have%20a%20ton%20of%20salad%20stuff%20and%20noodles%20can%20be%20ordered%20without%20meat!!%20They%20have%20something%20for%20everyone%20here%22%7D%2C%22accessory%22%3A%7B%22type%22%3A%22image%22%2C%22image_url%22%3A%22https%3A%2F%2Fs3-media3.fl.yelpcdn.com%2Fbphoto%2Fc7ed05m9lC2EmA3Aruue7A%2Fo.jpg%22%2C%22alt_text%22%3A%22alt%20text%20for%20image%22%7D%7D%2C%7B%22type%22%3A%22section%22%2C%22text%22%3A%7B%22type%22%3A%22mrkdwn%22%2C%22text%22%3A%22*Kin%20Khao*%5Cn%3Astar%3A%3Astar%3A%3Astar%3A%3Astar%3A%201638%20reviews%5Cn%20The%20sticky%20rice%20also%20goes%20wonderfully%20with%20the%20caramelized%20pork%20belly%2C%20which%20is%20absolutely%20melt-in-your-mouth%20and%20so%20soft.%22%7D%2C%22accessory%22%3A%7B%22type%22%3A%22image%22%2C%22image_url%22%3A%22https%3A%2F%2Fs3-media2.fl.yelpcdn.com%2Fbphoto%2Fkorel-1YjNtFtJlMTaC26A%2Fo.jpg%22%2C%22alt_text%22%3A%22alt%20text%20for%20image%22%7D%7D%2C%7B%22type%22%3A%22section%22%2C%22text%22%3A%7B%22type%22%3A%22mrkdwn%22%2C%22text%22%3A%22*Ler%20Ros*%5Cn%3Astar%3A%3Astar%3A%3Astar%3A%3Astar%3A%202082%20reviews%5Cn%20I%20would%20really%20recommend%20the%20%20Yum%20Koh%20Moo%20Yang%20-%20Spicy%20lime%20dressing%20and%20roasted%20quick%20marinated%20pork%20shoulder%2C%20basil%20leaves%2C%20chili%20%26%20rice%20powder.%22%7D%2C%22accessory%22%3A%7B%22type%22%3A%22image%22%2C%22image_url%22%3A%22https%3A%2F%2Fs3-media2.fl.yelpcdn.com%2Fbphoto%2FDawwNigKJ2ckPeDeDM7jAg%2Fo.jpg%22%2C%22alt_text%22%3A%22alt%20text%20for%20image%22%7D%7D%2C%7B%22type%22%3A%22divider%22%7D%2C%7B%22type%22%3A%22actions%22%2C%22elements%22%3A%5B%7B%22type%22%3A%22button%22%2C%22text%22%3A%7B%22type%22%3A%22plain_text%22%2C%22text%22%3A%22Farmhouse%22%2C%22emoji%22%3Atrue%7D%2C%22value%22%3A%22click_me_123%22%7D%2C%7B%22type%22%3A%22button%22%2C%22text%22%3A%7B%22type%22%3A%22plain_text%22%2C%22text%22%3A%22Kin%20Khao%22%2C%22emoji%22%3Atrue%7D%2C%22value%22%3A%22click_me_123%22%7D%2C%7B%22type%22%3A%22button%22%2C%22text%22%3A%7B%22type%22%3A%22plain_text%22%2C%22text%22%3A%22Ler%20Ros%22%2C%22emoji%22%3Atrue%7D%2C%22value%22%3A%22click_me_123%22%7D%5D%7D%5D

"""
import random


class BotFunctions:
    def check_number(self, args):
        val = 0
        for x in args:
            try:
                val = int(x)
                break
            except ValueError:
                continue
        return val

    def check_string(self, args):
        val = "null"
        for x in args:
            try:
                val = str(x)
                break
            except ValueError:
                continue
        return val

    def random_line(self, file):
        lines = open(file, encoding="utf8").read().splitlines()
        myline = random.choice(lines)
        return myline

    def indexed_line(self, file, index):
        lines = open(file, encoding="utf8").read().splitlines()
        myline = random.choice(lines)
        if index < len(lines):
            myline = lines[index]
        return myline

    def file_len(self, file):
        with open(file, encoding="utf8") as f:
            for i, _ in enumerate(f):
                pass
        return i + 1


class TextResponse:
    def __init__(self, channel, path="", username="crocobot", emoji=":crocoduck:", text=""):
        if path:
        # "path" is optional for testing purposes.  
        # I also omit it to feed raw messages to this class, such as in the help() in cb.py.
            if text:
            # "text" is present if a user is trying to get a specific line from a file.
                val_test = BotFunctions().check_number(text)
                # First we check if the text is a valid integer.
                total_lines = BotFunctions().file_len(path)
                # We count the number of lines in the file (I will improve this with BotFunctions().indexed_line() in the future).
                if val_test == 0 or val_test > total_lines:
                    text = BotFunctions().random_line(path)
                    # If text is beyond the range of the file lines or invalid, it is set to a random line.
                elif val_test > 0:
                    with open(path, encoding="utf8") as fp:
                        for i, line in enumerate(fp):
                            if i == (val_test - 1):
                                text = line
                                # If the text is within the range of the file lines, this sets the text to that line.
                                # I realize that this function could be vastly improved but the bot was created in haste and it currently works as intended!
                                # I will refactor this in the future.
                                break
            if not text:
                text = BotFunctions().random_line(path)
                # If a specific line is not specified by the user, text is set to a random line.
        if not path:
            if text:
                text = f"{text}"
                # By omitting "path," we can feed raw text into the block.
            if not text:
                text = "This is a test!"
        self.channel = channel
        self.username = username
        self.icon_emoji = emoji
        self.MAIN_BLOCK = {
            "type": "section",
            "text": {
                    "type": "mrkdwn",
                    "text": (
                        f"{text}"
                    ),
            },
        }
        # Block structure is in JSON format, or a dictionary of dictionaries.

    def get_payload(self):
    # This is the main function of the class, it returns the block from above in a JSON that is compatible with the client.
        return {
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.MAIN_BLOCK
            ],
        }


class ImageResponse:
    def __init__(self, channel, path, username='crocobot', emoji=':crocoduck:', title_text='Behold!', mouseover_text='Courtesy of Crocobot'):
    # This class is a less complicated clone of TextResponse() that builds blocks with images in the response
        image = BotFunctions().random_line(path)
        self.channel = channel
        self.username = username
        self.icon_emoji = emoji

        self.MAIN_BLOCK = {
            "type": "image",
            "title": {
                "type": "plain_text",
                "text": f'{title_text}'
            },
            "image_url": f'{image}',
            "alt_text": f'{mouseover_text}'
        }

    def get_payload(self):
        return {
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.MAIN_BLOCK
            ],
        }


class FieldResponse:
    def __init__(self, channel, title_text='Title text', dict={}, username='crocobot', emoji=':crocoduck:'):
    # This class is yet to be implemented because it has a limit in the amount of fields it can display.
        self.channel = channel
        self.username = username
        self.icon_emoji = emoji
        self.TITLE_BLOCK = {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f'{title_text}'
            }
        }
        data = []
        for k, _ in dict.items():
            field = {
                "type": "mrkdwn",
                "text": f'`{k}`'
            }
            data.append(field)
        # Originally, I created this to list all of the supported commands for the bot but the number of commands exceeds the number of fields we can display.
        self.MAIN_BLOCK = {
            "type": "section",
            "fields": data
        }

    def get_payload(self):
        return {
            'channel': self.channel,
            'username': self.username,
            'icon_emoji': self.icon_emoji,
            'blocks': [
                self.TITLE_BLOCK,
                self.MAIN_BLOCK
            ],
        }
