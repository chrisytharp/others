# String Test Timer

import time

print('Calculating the time difference between string concantenation and list appending' )
print('Please wait......')

startTime = time.time()
for trial in range(10000):
    building = ''
    for i in range(10000):
        building += 'x'
print('String concatenation: ', (time.time() - startTime))

startTime = time.time()
for trial in range(10000):
    building = []
    for i in range(10000):
        building.append('x')   #building is a list of 10,000 ['x','x',etc...
    building = ''.join(building)
#print(building)             #building is a string of 10,000 'xxxxxxxxxetc....
print('List appending:    ', (time.time() - startTime))
