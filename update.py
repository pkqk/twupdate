import sys
import json
from twython import Twython

def client():
    with open('config.json') as f:
        data = json.load(f)
        return Twython(data['CONSUMER_KEY'],
                data['CONSUMER_SECRET'],
                data['ACCESS_TOKEN_KEY'],
                data['ACCESS_TOKEN_SECRET'])

def profile_image(data):
    client().update_profile_image(image=data)

if __name__ == "__main__":
    filename = sys.argv[1]
    avatar = open(filename, 'rb')
    profile_image(avatar)
