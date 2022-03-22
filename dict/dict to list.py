# Write a Python program to convert a given dictionary into a list of lists. Go to the editor



a = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}


b = [[i,a[i]] for i in a]
print(b)









#
# Original Dictionary2 = {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
#
#



# output = [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
#output2 = [['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']]
