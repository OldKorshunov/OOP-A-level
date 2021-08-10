import re


regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


class Employee:
    def __init__(self, name, salary, email=None):
        self.name = name
        self.salary = salary
        self.email = email
        if self.email is not None:
            self.validate_email()
            self.save_email()
        
        
    def work(self):
        return "I come to the office."


    def check_salary(self, days):
        return self.salary * days


    def __str__(self):
        return self.name


    def save_email(self):
        with open('emails.txt', 'a+') as f:
            f.write(f'{self.name} : {self.email}\n')


    def validate_email(self):
        if(re.fullmatch(regex, self.email)):
            print("Valid Email")
 
        else:
            print("Invalid Email")


    def __lt__(self, other):
        return self.salary < other.salary


    def __gt__(self, other):
        return self.salary > other.salary


    def __ge__(self, other):
        return self.salary >= other.salary


    def __le__(self, other):
        return self.salary <= other.salary


    def __eq__(self, other):
        return self.salary == other.salary


class Recruiter(Employee):
    def work(self):
        return super().work()[:-1] + " and start to hiring."


    def __str__(self):
        print("Recruiter : " + super().__str__())
        return "Recruiter : " + super().__str__()


    
class Programmer(Employee):
    def __init__(self, name, salary, tech_stack=None):
        super().__init__(name, salary)
        if tech_stack is not None:
            self.tech_stack = tech_stack


    def work(self):
        return super().work()[:-1] + " and start to coding."


    def __str__(self):
        print("Programmer : " + super().__str__())
        return "Programmer : " + super().__str__()


    def __add__(self, other):
        stack = (set(self.tech_stack.split() + other.tech_stack.split()))
        return self.__class__("sup", 100, " ".join(stack))


    def __lt__(self, other):
        return len(self.tech_stack) < len(other.tech_stack)


    def __gt__(self, other):
        return len(self.tech_stack) > len(other.tech_stack)


    def __ge__(self, other):
        return len(self.tech_stack) >= len(other.tech_stack)


    def __le__(self, other):
        return len(self.tech_stack) <= len(other.tech_stack)


    def __eq__(self, other):
        return len(self.tech_stack) == len(other.tech_stack)


class Vacancy:
    def __init__(self, title, main_skill, main_skill_level):
        self.title = title
        self. main_skill = main_skill
        self.main_skill_level = main_skill_level



class Candidate:
    def __init__(self, full_name, technologies, main_skill, main_skill_grade, email=None):
        self.full_name = full_name
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

