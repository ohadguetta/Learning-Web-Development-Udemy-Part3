import requests

def get_poke(user_input):
    req = requests.get('https://pokeapi.co/api/v2/pokemon/'+user_input)
    req = req.json()
    print(type(req))
    print(req)


while True:
    user_input = input('Please write pokemon: ')
    user_input = user_input.lower()
    if user_input == '':
        print('Please write something...')
        continue
    else:
        get_poke(user_input)
    
