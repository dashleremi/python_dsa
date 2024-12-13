# dictionaries
my_dictionary = {'name': 'emi', 'course':'python'}

phone_dict = {'emi': '123-456-7890',
              'zoolander': '098-765-4321',
              'jon_snow': '019-283-4756'}

word_dict = {'a':
             {
                 'apple': 'the round fruit of a tree of the rose family',
                 'ant': 'an insect which cleans up the floor',
             },
             'b':{
                 'bad': 'of poor quality or low standard',
                 'business': 'season 8 of GOT'
             }}
print(my_dictionary)
print(word_dict['a'])
print(word_dict['b'])

print(my_dictionary.get('name'))

my_dictionary['job'] = 'python programmer'
print(my_dictionary.get('job'))
for k, v in my_dictionary.items():
    print(k, v)
print(my_dictionary.values())

# keys have be immutable
