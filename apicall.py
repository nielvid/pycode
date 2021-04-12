import requests
import json
try:
    res = requests.get('https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow')
    for data in res.json()['items']:
        print(data['title'])
except:
    print('Error occured')
class Person:

    def behavior(self):
        print('Good looking')
        
shade = Person()

print(shade.behavior())