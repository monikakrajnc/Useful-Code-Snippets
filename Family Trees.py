# Family Trees

# This procedure finds someone's ancestors,
# given a Dictionary that provides the parent relationships.

# An example of an input Dictionary:

ada_family = { 'Judith Blunt-Lytton': ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt'],
              'Ada King-Milbanke': ['Ralph King-Milbanke', 'Fanny Heriot'],
              'Ralph King-Milbanke': ['Augusta Ada King', 'William King-Noel'],
              'Anne Isabella Blunt': ['Augusta Ada King', 'William King-Noel'],
              'Byron King-Noel': ['Augusta Ada King', 'William King-Noel'],
              'Augusta Ada King': ['Anne Isabella Milbanke', 'George Gordon Byron'],
              'George Gordon Byron': ['Catherine Gordon', 'Captain John Byron'],
              'John Byron': ['Vice-Admiral John Byron', 'Sophia Trevannion'] }

def ancestors(genealogy, person):
    a = []
    for i in genealogy:
        if person == i:      #find the person in the dictionary
            b = genealogy[person]     #list of fist degree of ancestors
            a = a + b
        for j in a:                   #find second degree ancestors, 
            if j in genealogy:        #for every ancestor find his/her ancestors and
                c = genealogy[j]      #add them to the list with first degree ancestors
                    #print(c)
                a = a + c
                    #print(a)
    return a         #all the known ancestors of the person


# Here are some examples:

print ancestors(ada_family, 'Augusta Ada King')
#    ['Anne Isabella Milbanke', 'George Gordon Byron',
#    'Catherine Gordon','Captain John Byron']

print ancestors(ada_family, 'Judith Blunt-Lytton')
#    ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt', 'Augusta Ada King',
#    'William King-Noel', 'Anne Isabella Milbanke', 'George Gordon Byron',
#    'Catherine Gordon', 'Captain John Byron']

print ancestors(ada_family, 'Dave')
#    []
