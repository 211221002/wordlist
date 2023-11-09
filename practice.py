import requests

api_key = '1dd3cd56-61ad-47f2-a9b3-448df71f180f'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definitions in definitions:
    print(definitions)