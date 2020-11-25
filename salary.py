class Salary:
    initial_salary=0
    TA=0
    DA=0
    HRA=0
    EPF=0
    def accept(self):
         print("Enter the initial_salary");
         self.initial_salary=int(input())
         self.TA=(18/100)*self.initial_salary
         print("The TA value is ",self.TA);
         self.DA=(17/100)*self.initial_salary
         print("The DA value is ",self.DA);
         self.HRA=(25/100)*self.initial_salary
         print("The HRA value is ",self.HRA);
         self.EPF=(10/100)*self.initial_salary
         print("The EPF value is ",self.EPF);
        

class Total_salary(Salary):
    def __init__(self):
         accept. __init__(self)
         print("Net salary=")
    def printsal(self):
         self.Net_salary=self.initial_salary+self.TA+self.DA+self.HRA+self.EPF
         print(Net_salary)

Sal_obj=Salary()
Sal_obj.accept()
Sal_1obj=Total_salary()
Sal_1obj.printsal()











        
    
    
