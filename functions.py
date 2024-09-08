#Function is a block of code which runs when it is called. 

def my_function_stock ():
    print('stock exchange are company sells shares typically to gain additional money to grow the company.')
my_function_stock()

#Adding arguments to functions - These are specific after function names inside the ()
def gender(last_name):
    print(last_name + ' lionel')
gender('israel')
gender('senwin')
gender('winnie')
gender('david')

def names(first_name, last_name):
    print(first_name + ' ' + last_name)
names('godwin', 'senwin')
names('israel', 'ehis')
name_instance = names
print(name_instance)

#Using * as argument 
def organization(*labour):
    print('all organizations are under government.e.g ' + labour[3])
organization('football', 'music', 'movie', 'finance', 'education', 'estate management', 'business admin', 'hospitality')

#Default parameter value 
def country(state = 'lagos'):
    print('i live in ' + state)
country('imo')
country('rivers')
country()
country('calabar')

#Recursion 
def sports(football):
    if (football > 0):
        result = football + sports(football - 1)
        print(result)
    else:
        result = 0 
    return result 
print('this is recursion example')
sports(6)

    
