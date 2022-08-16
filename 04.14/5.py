import random
from pprint import pprint
from collections import OrderedDict
iterable_obj = str([x*random.random() for x in range(-5, 5, 2)]).lstrip('[').rstrip(']') + ', ' + str([random.randint(-5, 5) for _ in range(1, 5, 1)]).lstrip('[').rstrip(']')


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
        
def calc_avg_val(iterable_obj: str or list or tuple):
    summa = 0
    squares_sum = 0
    multiplication = 1
    harmonic_sum = 0
    for el in iterable_obj:
        if el == ',':
            iterable_obj = iterable_obj.replace(el, '')
        elif el == '0':
            iterable_obj = iterable_obj.replace(el, '')
    if type(iterable_obj) == str or list or tuple:
        l = iterable_obj.split()
        if all(is_number(n) for n in l):
            for el in l:
                summa += float(el)
                squares_sum += float(el) ** 2
                multiplication *= float(el)
                harmonic_sum += 1/float(el)
            mean = summa / len(l)
            geometric_mean = (abs(multiplication) ** (1/len(l)))
            square_mean = (squares_sum*(1/len(l))) ** (0.5)
            harmonic_mean = len(l) / harmonic_sum
            d = {'mean': mean, 'geometric_mean': geometric_mean, 'square_mean': square_mean, 'harmonic_mean': harmonic_mean}
            res = OrderedDict(sorted(d.items(), key=lambda x: x[1]))
            return(res)
        else:
            return iterable_obj
    else:
        return None
    
pprint(calc_avg_val(iterable_obj)) 
print()       
pprint(iterable_obj)       

# OrderedDict([('mean', 0.3378619677916095),
             # ('geometric_mean', 1.522237266900699),
             # ('square_mean', 3.039911483776847),
             # ('harmonic_mean', 5.315524675536858)])