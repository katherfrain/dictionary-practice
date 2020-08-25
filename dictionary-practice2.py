ramit = {
    "name": "Ramit",
    'email': 'ramit@gmail.com',
    'interests': ['movies', 'tennis', 'friends'],
    'friends': [ 
        {
            'name': 'Jasmine',
            'email': 'jasmine@yahoo.com',
            'interests': ['tennis', 'ruling Agrabah']
        },
        {
            'name': 'Jan (sure it is)',
            'email': 'jan@hotmail.com',
            'interests': ['movies', 'tv', 'escaping family time']
        }
    ]

}

print(ramit['email'])
print(ramit['interests'][0])
print(ramit['friends'][0]['email'])
print(ramit['friends'][1]['interests'][1])