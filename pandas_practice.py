import pandas as pd

data = {
    'chicken': [3, 5, 6, 9],
    'fish': [5, 3, 9, 6]
}

eaten = pd.DataFrame(data, index=['cat', 'dog', 'cheetah', 'wolf'])

def switch(value):
    match value:
        case 'cat':
            return eaten.loc['cat']
        case 'dog':
            return eaten.loc['dog']
        case 'cheetah':
            return eaten.loc['cheetah']
        case 'wolf':
            return eaten.loc['wolf']
        case _:
            return

animal = input('Enter animal: ')
selected_row = switch(animal)

if selected_row is None:
    print('The options are: cat, dog, cheetah, wolf')
else:
    print('chicken:' + str(selected_row['chicken']) + '\nfish:' + str(selected_row['fish']))
