import sys
import traceback


from datetime import datetime
from datetime import date
from datetime import timedelta


import models


if __name__ == '__main__':
    try:
        candidate = models.Candidate.new_candidates()
        #recruiter = models.Recruiter('Oksana', 50, 'oksigen15@gmail.com')
        #pr1 = models.Programmer("Danil", 70, 'Django MySQL CSS')
        #pr2 = models.Programmer("Ihor", 3.4, 'Dgango ReasctJS HTML')
        #candidate1 = models.Candidate('Sanya', 'Python JS HTML', 'Python', 'middle', 'sanya228@gmail.com')
        #candidate2 = models.Candidate('Jeka', 'C# Unity UnrealEngine4', 'C#', 'senior', 'jeka1998@gmail.com')
        #candidate3 = models.Candidate('KeREAL', 'Ruby Go', 'Go', 'junior', 'kiryusha77@gmail.com')
        #vacancy1 = models.Vacancy('developer', 'py', 'middle')
        #vacancy2 = models.Vacancy('frontend', 'js', 'senior')

    except Exception as err:
        with open("logs.txt", 'a+') as f:
            f.write(f"{datetime.now()}\n\n")
            traceback.print_exc(file=f)

