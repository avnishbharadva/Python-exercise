import numpy

a = numpy.char.add(['avnish'],['bharadva'])
# print(a, type(a))

print(numpy.char.add(['avnish','shivam'],[' hey',' hm']))

c = numpy.char.multiply('hey',3)
# print(c,type(c))

print(numpy.char.center("Avnish",30,fillchar='-'))

print(numpy.char.capitalize("avnish hry mkef"))

print(numpy.char.title("avnish hey hto nwkrn"))

print(numpy.char.lower(['AVNISH','BHARADVA']))

print(numpy.char.upper(['avnihs','wjdkw']))

print(numpy.char.split('avnish-jjb-jndn-kf-knd',sep='-'))

print(numpy.char.splitlines('hry jeb nej jnef\nfe\nrgr\ngr'))

print(numpy.char.strip('avnish avkns ajbfa','a'))

print(numpy.char.join(':','avnish'))
print(numpy.char.join([':','-'],['egf','htcd']))

print(numpy.char.replace('avnish hey ho','vni','hihi'))

