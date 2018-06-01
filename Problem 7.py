class Human(object):
    def __init__(self, name = "",gender =""):
        self.name = name
        self.gender = gender
    #Can use setter getters butwill take time
    #def set_gender(self, gender = ""):
    #   self.gender = gender
    #def get_gender(self):
    #    return self.gender
    #def set_name(self, newname = ""):
    #    self.name = newname
    #def get_name(self):
    #    return self.name

class Employee(Human):
    
    def __init__(self, name = "", gender = "", salary = 0, idnum = 0, company = "" ):
        Human.__init__(self, name, gender)
        self.salary = salary
        self.idnum = idnum
        self.company = company
        #self.setname(name)
        #self.setgender(gender)
    def get_salary(self):
        return self.salary 
        
    def __str__(self):
        return "name:"+str(self.name)+" company:"+str(self.company)
    #Can use setter getters butwill take time
    #def set_gender(self, id = ""):
    #   self.id = id
    #def get_id(self):
    #    return self.id
    #def set_salary(self, salary = 0):
    #    self.salary= salary
    #def set_company(self, company = ""):
    #    self.name = newname
    #def get_company(self):
    #    return self.name
    
    
if __name__ == "__main__":
    #Can take in one data at a time from the user and verify the values to make the program more efficient and effective but need  hour or so do make it a much better interactive program"
    no_of_employees = 3
    el = []
    el.append(Employee("Sandeep","Male",10000000, 1, "Quantiphi"))
    el.append(Employee("RandomNameFemale","Female",1000000000000, 2, "Quantiphi"))
    el.append(Employee("RandomNameMale","Male",10000, 3, "Quantiphi"))
    for i in range(no_of_employees):
        l = sorted(el, key = lambda a:a.get_salary(), reverse = True)
    
    for i in range(no_of_employees):
        print(l[i])
          