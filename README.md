# Crocobot - An intelligent slackbot
Crocobot is an intelligent (eventually) slackbot.  Definitely parses commands better than v1

## Requirements
Requires Python 3.7+
Install required modules with the following command in the project directory:
```
pip install -r requirements.txt
```

## API Key
Currently the api token should be stored in ./data/apitoken as raw text; however, you can add pickling or encryption if you need.

## Run
```
python cb.py
```

## FYI: The help function pulls the docstring of the local function in cb.py, so make sure to add it to any new function!

# TODO
- More commands
- Refactoring modules
- Add better store for api token
