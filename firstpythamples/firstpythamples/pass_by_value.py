# scope and passing

i = 1

def local():
    i = 2 # local

def local2(i):
    i = 2 # local parameter

def globalish():
    global i # kind of awkward
    i = 3 # changes the value of the global

def passing_params(a, b, c):
    print(c, a, b);

def passing_params_default_values(a, b, c='yellow'):
    # But do default values really change the world?
    print(c, a, b);


local()
print(i)
local2(i)
print(i)
globalish()
print(i)

passing_params(1, 'blue', {'dog': 'cat'})

# Unusual, is it useful? It certainly makes code more readable in terms
# of what the parameters are to any function call (when reading later.)
# Well we have to know it because python
passing_params(b='blue', c={'dog': 'cat'}, a=1)

# and default values can be added, which is kind of nice I guess.
passing_params_default_values(1, 'blue')
#passing_params(1, 'blue')

# functions are actually objects like everything else in python
def answer():
    print(42)

def run_something(func):
    func()


run_something(answer)
