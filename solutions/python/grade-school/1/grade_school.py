from collections import defaultdict

class School:
    def __init__(self, name = ''):
        self.school = defaultdict(list)
        self.result = []

    def add_student(self, name, grade):
        val = True
        if name in self.roster():
            val = False
        else:
            self.school[grade].append(name)
        self.result.append(val)
        return val

    def grade(self, num):
        return sorted(self.school[num])

    def roster(self):
        lst = [self.grade(num) for num in sorted(self.school.keys())]
        return [stud for grad in lst for stud in grad]

    def added(self):
        return self.result

        

          

        
