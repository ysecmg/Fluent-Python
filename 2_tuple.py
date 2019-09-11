colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]

'''
for tshirt in ('%s %s' % (c,s) for c in colors for s in sizes):
    print(tshirt)
'''

# lax_coordinates = (33.9425, -118.408056)
# latitude, longitude = lax_coordinates

# quotient, remainder = divmod(20,8)

from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889,77.208889)),
]
tokyo = City(*metro_areas[0])
