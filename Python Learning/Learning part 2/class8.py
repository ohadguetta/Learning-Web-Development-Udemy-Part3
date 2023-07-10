import requests

req = requests.get('https://big-bang-theory-api.lesalvucci.workers.dev/search?q=sheldon')
results = req.json()
print(results)