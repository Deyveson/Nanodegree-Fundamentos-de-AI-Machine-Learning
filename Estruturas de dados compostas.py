elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}


elements['hydrogen'].get('is_noble_gas', 'yes')
elements['helium'].get('is_noble_gas', 'no')


print(elements)
