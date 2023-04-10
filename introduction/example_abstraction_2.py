import requests

params = dict(q='Sausages', format='json')
parsed = requests.get(url='http://api.duckduckgo.com', params=params).json()
results = parsed['RelatedTopics']
for r in results:
    print(r['FirstURL'] + ' - ' + r['Text'])