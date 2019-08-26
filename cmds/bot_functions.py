import random


class TextResponse:
    def __init__(self, channel, path="", username="crocobot", emoji=":crocoduck:", text=""):
        if path:
            if text:
                val_test = BotFunctions().check_number(text)
                total_lines = BotFunctions().file_len(path)
                if val_test == 0 or val_test > total_lines:
                    text = BotFunctions().random_line(path)
                elif val_test > 0:
                    with open(path, encoding="utf8") as fp:
                        for i, line in enumerate(fp):
                            if i == (val_test - 1):
                                text = line
                                break
            if not text:
                text = BotFunctions().random_line(path)
        if not path:
            if text:
                text = f"{text}"
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

    def get_payload(self):
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
        # jsonData = json.dumps(data)
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
