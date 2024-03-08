from utilities.configurations import *


def addBookPayload(isbn,aisle):
    body = {

        "name": "Alice's Adventure In Wonderland",
        "isbn": isbn,
        "aisle": aisle,
        "author": "John foe"
    }
    return body


def buildPayLoadFromDB(query):

    addBody = {}
    tp = getQuery(query)
    addBody['name'] = tp[0]
    addBody['isbn'] = tp[1]
    addBody['aisle'] = tp[2]
    addBody['author'] = tp[3]
    return addBody
