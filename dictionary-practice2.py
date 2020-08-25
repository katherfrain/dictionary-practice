def countFriends(friendly_dictionary):
    friendscount = 0
    if 'friends' in friendly_dictionary.keys():
        for friendkeys in friendly_dictionary['friends']:
            friendscount = friendscount + 1
    friendly_dictionary['friends-count'] = friendscount
    return friendly_dictionary

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


print(countFriends(ramit))

