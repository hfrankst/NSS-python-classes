class Company(object):
    """This represents a company in which people work"""

    def __init__(self, name):
    	self.name = name
    	self.employees = set()

    def get_company_name(self):
        """Returns the name of the company"""
        
        return self.name

    def hire_employees(self, employee):
    	'''connecting the employee with the company'''

    	self.employees.add(employee)

    def list_employees(self):
    	'''listing the employees hired by this company'''

    	[print("These are the current employees: {} is the {} and they started on {}".format(employee.name, employee.title, employee.start_date)) for employee in self.employees]

class Employee:

	def __init__(self, name, title, start_date):
		self.name = name
		self.title = title
		self.start_date = start_date

	def set_employee_name(self):
		'''setting the employee's name'''

		return self.name 

	def get_title(self):
		'''returns the employee's job title'''

		return self.title

	def get_start_date(self):
   		'''returns the employee's start date'''

   		return self.start_date

'''creating a company'''
Corporation = Company('Corporation')

'''creating employees'''
james = Employee('James', 'CEO', '3-15-17')
sarah = Employee('Sarah', 'CTO', '4-10-17')
terrel = Employee('Terrel', 'VP of Sales', '2-20-16')

Corporation.hire_employees(james)
Corporation.hire_employees(sarah)
Corporation.hire_employees(terrel)

Corporation.list_employees()