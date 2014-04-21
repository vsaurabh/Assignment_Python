''' 1.) It is possible to do multiple assignments at once ? Give an example of one ?
	Ans.) Yes '''

def mul_assignment():
	'''function for multiple assignments'''
	a,b,c = 1,2,3
	print "problem 1 =>",a,b,c

'''2.) Write simple program to swapping values of 2 variables ?'''

def swapping_value(a,b):
	'''function for swapping values'''
	print "problem 2 =>"
	print "Before swapping=>" , a,b
	a,b = b,a
	print "After swapping=>" , a,b

'''3.) What will be the output of the following program ? : cube = lambda x: x ** 3
	Ans.) when we give any value of x than it will give cube of that number.
    Ex.) x=4 o/p : cube = 64'''

def lambda_fun(x):
    '''function for problem lambda function'''
    print "problem 3 =>"
    cube = lambda x: x ** 3
    print cube(x)

def main():
	mul_assignment()
	swapping_value(4,5)
	lambda_fun(7)


if __name__ == '__main__':
	main()
