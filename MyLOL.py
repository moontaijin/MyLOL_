import requests
import json
import pprint

api_key = '<API_KEY>'
summon_url = 'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/'
summonerName = '신사 갱플랭크'
summoner = summon_url + summonerName + '?api_key=' + api_key

r = requests.get(summoner)

tier_url = 'https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/'
tier = tier_url + r.json()['id'] + '?api_key=' + api_key

r2 = requests.get(tier)
#print(r2.json())
print(r2.json()[0]['tier'])