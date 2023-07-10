import json
result = '{"id": "1","name": "Johnny Galecki","photo": "https://m.media-amazon.com/images/M/MV5BNzQ2ODY0MTIwMV5BMl5BanBnXkFtZTcwNDQ2NzMzMw@@._V1_UX266.jpg","charName": "Leonard Hofstadter"}'
result = json.loads(result)
print(result['name'])
print('---------')
result = json.dumps(result)
print(result)
