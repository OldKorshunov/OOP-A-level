import sys
import traceback


from datetime import datetime
from datetime import date
from datetime import timedelta


import models


if __name__ == '__main__':
    try:
        recruiter = models.Recruiter('Oksana', 50, 'oksigen15@gmail.com')
        pr1 = models.Programmer("Danil", 70, 'Django MySQL CSS')
        pr2 = models.Programmer("Ihor", 3.4, 'Dgango ReasctJS HTML')
        candidate1 = models.Candidate('Hvan', 'Python JS HTML', 'Python', 'middle')
        candidate2 = models.Candidate('Huvan', 'C# Unity UnrealEngine4', 'C#', 'senior')
        candidate3 = models.Candidate('Ahvan', 'Ruby Go', 'Go', 'junior')
        vacancy1 = models.Vacancy('developer', 'py', 'middle')
        vacancy2 = models.Vacancy('frontend', 'js', 'senior')

    except Exception as err:
        with open("logs.txt", 'a+') as f:
            f.write(f"{datetime.now()}\n\n")
            traceback.print_exc(file=f)

