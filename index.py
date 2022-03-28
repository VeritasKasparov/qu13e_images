import requests


def array(letter):
    n = str(letter)
    array = ['http://www.qu13e.com/595/' + n + '00.jpg',
'http://www.qu13e.com/389/' + n + '01.jpg',
'http://www.qu13e.com/010/' + n + '03.jpg',
'http://www.qu13e.com/369/' + n + '05.jpg',
'http://www.qu13e.com/919/' + n + '07.jpg',
'http://www.qu13e.com/619/' + n + '09.jpg',
'http://www.qu13e.com/333/' + n + '11.jpg',
'http://www.qu13e.com/345/' + n + '13.jpg',
'http://www.qu13e.com/039/' + n + '15.jpg']  

    return array


def listar():
    x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    number_var = 0
    number_array = 0
    new_array = []
    
    while (number_array <= len(array(0))-1): 
        if (number_var <= len(x)-1):
            new_array.append(array(x[number_var])[number_array])
            number_var +=1
        
        else: 
            number_var = 0
            number_array += 1

    return new_array
new_array = listar()

r = lambda x: requests.get(x).content

def response(a):
    n = 0
    
    for b in a:
        
        file = open(b[25:][:4] + '.jpg', 'wb')
        file.write(r(b))
        file.close
        n +=1

response(new_array)
