# В этой задаче вам необходимо воспользоваться API сайта numbersapi.com
#
# Вам дается набор чисел. Для каждого из чисел необходимо узнать,
# существует ли интересный математический факт об этом числе.
#
# Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
# Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.
#
# Пример запроса к интересному числу:
# http://numbersapi.com/31/math?json=true
#
# Пример запроса к скучному числу:
# http://numbersapi.com/999/math?json=true


# import requests
#
# with open('dataset_24476_3.txt') as f:
#     for line in f:
#         line = line.strip()
#         api_url = f'http://numbersapi.com/{line}/math?json=true'
#         res = requests.get(api_url)
#         print('Interesting' if res.json()['found'] else 'Boring')

# второй вариант

# import requests
# import json
#
# def is_interesting(x):
#     url = "http://numbersapi.com/" + str(x) + "/math?json=true"
#     resp = requests.get(url).text
#     js = json.loads(resp)
#     return js["found"]
#
# with open("dataset_24476_3.txt") as fi:
#     for line in fi:
#         print("Interesting" if is_interesting(line.rstrip()) else "Boring")

# В этой задаче вам необходимо воспользоваться API сайта artsy.net
#
# API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.
#
# В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).
#
# Вам даны идентификаторы художников в базе Artsy.
# Для каждого идентификатора получите информацию о имени художника и годе рождения.
# Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый год рождения,
# выведите их имена в лексикографическом порядке.

# import requests
# import json
#
# client_id = 'db311cfe37ec4bc74a61'
# client_secret = 'ba1d22427d386b0b79ce4403c063b2ec'
#
# r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
#                   data={
#                       "client_id": client_id,
#                       "client_secret": client_secret
#                   })
# j = json.loads(r.text)
# token = j["token"]
#
# artists = []
#
# with open('dataset_24476_4.txt') as file:
#     for artist_id in file:
#         artist_id = artist_id.strip()
#         url = f'https://api.artsy.net/api/artists/{artist_id}'
#         params = {'xapp_token': token}
#         resp = requests.get(url, params=params).text
#         data = json.loads(resp)
#         artists.append({'name': data['sortable_name'], 'birthday': data['birthday']})
#
# for artist in sorted(artists, key=lambda x: (x['birthday'], x['name'])):
#     print(artist['name'])

# Второй вариант

# import requests
# import json
#
# # put your id and secret here
# client_id = '...'
# client_secret = '...'
#
# resp = requests.post("https://api.artsy.net/api/tokens/xapp_token", data={"client_id" : client_id, "client_secret" : client_secret}).text
# token = json.loads(resp)["token"]
#
# def get_json(url):
#     headers = {"X-Xapp-Token" : token}
#     resp = requests.get(url, headers=headers).text
#     return json.loads(resp)
#
# ans = []
#
# with open("input.txt") as inp:
#     for id in inp:
#         id = id.rstrip()
#         js = get_json("https://api.artsy.net/api/artists/"; + id)
#         ans.append((js["birthday"], js["sortable_name"]))
#
# ans.sort(key=lambda x: (int(x[0]), x[1]))
#
# print("\n".join(map(lambda x: x[1], ans)))
