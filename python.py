'''for loop with else'''
'''endpoint in range is never reached, thus range(n) will give 0..n-1'''
'''TODO - slicing'''
for n in range(2,10):
	for x in range(2, n):
		if n%x == 0:
			print(n, 'equals', x, ' * ', n//x)
			break
	else:
		print (n, 'is prime')

def func(n):
	"""This is an example function. Good practice to keep first line a DocString"""
	'''lookup process - The execution of a function introduces a new symbol table used for the local variables of the function. More precisely, all variable assignments in a function store the value in the local symbol table; whereas variable references first look in the local symbol table, then in the local symbol tables of enclosing functions, then in the global symbol table, and finally in the table of built-in names. Thus, global variables cannot be directly assigned a value within a function (unless named in a global statement), although they may be referenced. Functions without a return statement returns None'''
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a+b
	return result

l = func(100)
print (l)

'''default values for a function - default values are evaluated only once, and are evaluated at the point of function definition in the defining scope'''
def f_defaultChange(a, L=[]):
    L.append(a)
    return L

'''if default values to not be shared for subsequent calls'''
def f_defaultSame(a, L=None):
	if L is None:
		L=[]
	L.append(a)
	return L

print(f_defaultChange(1))
print(f_defaultChange(2))
print(f_defaultChange(3))
	
print(f_defaultSame(1))
print(f_defaultSame(2))
print(f_defaultSame(3))


#KEYWORD ARGUMENTS, keyword arguments must follow positional arguments
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
	print("-- This parrot wouldn't", action)
	print("if you put", voltage, "volts through it.")
	print("-- Lovely plumage, the", type)
	print("-- It's", state, "!")


#Valid
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

#invalid, uncomment to try
'''
parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument
'''
'''final formal parameter of the form **name accepts a dictionary of keyword arguments except for those corresponding the formal parameters.'''
'''final formal parameter of the form *name accepts a tuple containing the positional arguments beyond the formal parameter list'''
print(range(3, 6))            # normal call with separate arguments
args = [3, 6]
print(range(*args))			#call with arguments unpacked from a list, for dictionary use **args


