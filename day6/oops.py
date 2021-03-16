# ---------------------------------CLASS---------------------------------------

# class MyClass:
# 	pass

# myObject = MyClass()
# print(type(myObject))
# print(myObject)	

# always give 1 parasmeter i.e. (self) to method

# class MyClass:
# 	def myMethod(self,value):
# 		print("this is my method")
# 		print(value)


# # whenevr you call method it attach it to the instance of method
# myObject = MyClass()
# myObject.myMethod("valurrrrr")		

# class used directly without using object are called study classes
# PASSING VALUE


# - -------------------------------constructor--------------------------

''' object is always out of class '''


# class MyClass2:
# 	x=1;y=2
# 	def myMethod(self,y):
# 		print("value of y is :", y)
# 		print("value of y is :", self.y)
        
          
# 	def __init__(self,x):
# 		print("value of x is : ",x)
# 		print("value of x is : ",self.x)
    
  

# myObject = MyClass2(100)
# myObject.myMethod(100)


# ------------------------------------there is no destructor in python----------------------------


# -----------------------------------encaptulatio-------------------------------------

# class ClassA:
# 	__privateVariable =""  
# 	#variable start with __ are private variable
#     _protectedVariable =""
#     #variable starts with _ are protected variable
    
#     publicVariable =""
#     # its a basic variable

#     # object should never created inside the class its a good approch because that object can acess any thing

#     def __init__(self,__privateVariable,_protectedVariable,publicVariable):
#     	self.__privateVariable = __privateVariable
#     	self._protectedVariable = _protectedVariable
#     	self.publicVariable = publicVariable
#     def setValues(self,__privateVariable,_protectedVariable,publicVariable):
#     	self.__privateVariable = __privateVariable
#     	self._protectedVariable = _protectedVariable
#     	self.publicVariable = publicVariable
#     def getValue(self):
#     print("private Value :  ",self.__privateVariable)
#     print("protected Value :  ",self._protectedVariable)	
#     print("public Value :  ",self.publicVariable)	



# obj = ClassA("yo","no","do")
# obj.getValue()


class BankDetail:
	__CustomerId= "",
	_AccountNo= "",
	customerName ="",
	

	def __init__(self,bankName):
		print("bank name: ",bankName)
		
	def setValues(self,__CustomerId,_AccountNo,customerName):
		self.__CustomerId = __CustomerId
		self._AccountNo = _AccountNo
		self.customerName= customerName
	def getValue(self):
		print("customerName : ",self.__CustomerId)
		print("AccountNo : ",self._AccountNo)
		print("customerName : ",self.customerName)


obj= BankDetail("HDFC")
obj.setValues("0225IT181023","48631354987204654","shivam")
obj.getValue()


	     	
	     	
	

		

