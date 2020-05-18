NAMES = ['arnold SchwArzenegger', 'alEc Baldwin', 'Bob belderbos',
         'julian sequeira', 'Sandra Bullock', 'keAnu reeves',
         'julbob pybites', 'Bob Belderbos', 'julian sequeira',
         'Al Pacino', 'brad pitt', 'matt damon', 'brad pitt']

def surname(inputStr):
         return inputStr.split()[1]

def firstname(inputStr):
         return len(inputStr.split()[0])

def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    names = [x.title() for x in names]
    return list(set(names))
    

def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    print (type(sorted(names,key=surname)))
    return sorted(names,key=surname,reverse=True)
    # ...


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    return ( sorted(names,key=firstname)[0].split()[0])
    # ...

print (sort_by_surname_desc(NAMES))
print (shortest_first_name(NAMES))
