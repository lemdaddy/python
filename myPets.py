myPets = ['Jax', 'Toby', 'Roxy']
print('enter a name: ')
name = input()
if name not in myPets:
    print('i dont have a pet named '+ name)
else:
    print(name + ' is my pet')

