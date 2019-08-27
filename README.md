# Crocobot - An intelligent slackbot
Crocobot is an intelligent (eventually) slackbot.  Definitely parses commands better than v1

## Getting your API Key
*Currently the api token should be stored in ./data/apitoken.  I have it stored as raw text; however, you can add pickling or encryption if you need.*

1. You can create a bot by visiting https://api.slack.com/apps.  Choose a name and a workspace.
2. Once the app is created, click it in the apps list.
3. Your key will be located under the Features > OAuth & Permissions tab.  It is the "Bot User OAuth Access Token" that begins with "xoxb".

## Requirements
Requires Python 3.7+
Install required modules with the following command in the project directory:
```
pip install -r requirements.txt
```

## Run
```
python cb.py
```

## FYI: The help function pulls the docstring of the local function in cb.py, so make sure to add it to any new function!

# TODO
- More commands
- Refactoring modules
- Add better store for api token
- More descriptive logging
- I currently have the bot running as a systemctl service on a CentOS server.  I plan to add Docker integrations as well as instructions on each platform.
