d = {
    'name' : 'Avnish',
    'rollno' : 2,
    'branch' : 'BCA'
}

print(d)
print(d['name'])
print(d['rollno'])
print(d['branch'])

d['rollno'] = 8
d['dish'] = 'Rotali nu sak'

print(d['rollno'])
print(d['dish'])

del d['dish']

print(d)

d.clear()

print(d)