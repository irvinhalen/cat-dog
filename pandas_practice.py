import pandas as pd

data = {
    'apples': [3, 2, 5, 1],
    'oranges': [5, 3, 7, 2]
}

purchases = pd.DataFrame(data, index=['Diether', 'Bernard', 'Mikhael', 'David'])

def switch(value):
    match value:
        case 'Diether':
            return purchases.loc['Diether']
        case 'Bernard':
            return purchases.loc['Bernard']
        case 'Mikhael':
            return purchases.loc['Mikhael']
        case 'David':
            return purchases.loc['David']
        case _:
            return

guy = input('Enter name: ')
selected_row = switch(guy)

if selected_row is None:
    print('The options are: Diether, Bernard, Mikhael, David')
else:
    print('Apples:' + str(selected_row['apples']) + '\nOranges:' + str(selected_row['oranges']))
