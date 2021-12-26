# String includes use 'in', return a boolean 
str = 'abc1'
print("ab" in str)

# join() method
#Note: When using a dictionary as an iterable, the returned values are the keys, not the values.

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

# return value nameTESTcountry
print(x) 

# x = "Hello World"	str	
# x = 20	int	
# x = 20.5	float	
# x = 1j	complex	
# x = ["apple", "banana", "cherry"]	list	
# x = ("apple", "banana", "cherry")	tuple	
# x = range(6)	range	
# x = {"name" : "John", "age" : 36}	dict	
# x = {"apple", "banana", "cherry"}	set	
# x = frozenset({"apple", "banana", "cherry"})	frozenset	
# x = True	bool	
# x = b"Hello"	bytes	
# x = bytearray(5)	bytearray	
# x = memoryview(bytes(5))	memoryview








#########################
# what python cannot do #
#########################
# If you try to combine a string and a number, Python will give you an error
