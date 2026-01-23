STUDENTS = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
PLANTS = {'G':'Grass', 'C': 'Clover', 'R': 'Radishes', 'V':'Violets'}

class Garden:
    def __init__(self, diagram, students = STUDENTS):
        self.diagram = diagram.splitlines()
        students.sort()
        self.students = students

    def plants(self, stud):
        if stud not in set(self.students):
            return None    
        ind = self.students.index(stud)
        return [PLANTS[x] for line in self.diagram for x in [line[2*ind], line[2*ind+1]]]
        
            