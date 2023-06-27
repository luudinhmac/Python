# Default dict

from collections import defaultdict
thisdict = {
    'brand': 'Ford',
    'model': 'msfd',
    'year': 1212
}

def define_value():
    return "not init"
thisdict = defaultdict(lambda : 'not init')
thisdict['brand']= 'Ford'
thisdict['model']= 'sdfdsf'
thisdict['year']= 12312

print(thisdict['a'])
