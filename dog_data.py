from typing import Dict

dog_data: Dict[str, str] = {'Fido': 'Bulldog', 'Kenny': 'Poodle',
                            'Goofy': 'Terrier', 'Sherry': 'Chihuahua',
                            'Derrick': 'German Shepherd', 'Rose': 'Husky',
                            'Danny': 'Pug'}


def get_dogs_under(dog_breed: str):
    count = 0
    print(f"\nDogs under category '{dog_breed}':")
    for (k, v) in dog_data.items():
        if v.startswith(dog_breed):
            print(k, ': ', v, sep="")
            count += 1

    if count == 0:
        print(f'No dogs was found under category {dog_breed}')


def driver():
    while (breed := input('\nEnter the dog breed (press \'@\' to quit): ')) != '@':
        if breed == '@':
            break
        get_dogs_under(breed.upper())

    print('Bye!')


driver()
