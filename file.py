def mangInasal(dictValue):
    sentence = "My name is %s and my mang inasal rice record is %d" % (dictValue['name'], dictValue['count'])
    print(sentence)

lolTuple = ({'name': 'Ryan', 'count': 3}, {'name': 'DJ(noob', 'count': 1})
lolList = [{'name': 'Ryan', 'count': 3}, {'name': 'DJ(noob', 'count': 1}]

for x in lolTuple:
    mangInasal(x)

for x in lolList:
    mangInasal(x)