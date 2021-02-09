import requests
import json
import pprint

# api 받는 주소
# https://developer.riotgames.com/
api_key = 'RGAPI-3563187d-587c-4773-8299-d1b77a46f5c4'
summon_url = 'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/'
summonerName = '신사 갱플랭크'
summoner = summon_url + summonerName + '?api_key=' + api_key

r = requests.get(summoner)
#print(r.json())

tier_url = 'https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/'
tier = tier_url + r.json()['id'] + '?api_key=' + api_key

r2 = requests.get(tier)
#print(r2.json()[0]['tier'])

matchlist_url = 'https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/'
season = str(13)
matchlist = matchlist_url + r.json()['accountId'] + '?season=' + season + '&api_key=' + api_key

r3 = requests.get(matchlist)
#print(r3.json()['matches'][-1]['gameId'])

match_url = 'https://kr.api.riotgames.com/lol/match/v4/matches/'
match_Num = -1
match_Id = str(r3.json()['matches'][match_Num]['gameId'])
match = match_url + match_Id + '?api_key=' + api_key

r4 = requests.get(match)
print(r4.json())