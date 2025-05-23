import configparser

config = configparser.ConfigParser()
config.read('config.ini')
accountID = config.getint('Credentials', '8043832960')
accountHash = config.get('Credentials', '12efef2ba448d268459dc136427d1ba0')
Token = config.get('Credentials', '8064617516:AAFHdzKwdJ39rOhPXuKeePW2yVJ8gP8kJTw')
DebugId=config.get('Credentials', '8043832960')
