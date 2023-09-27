from c_exam_class import Exams

class Subject:
    def __init__(self, subject, score) -> None:
        # inherited attributes
        self.subject = subject
        self.exam = []
        self.score = None

    def __str__(self) -> str:
        return f"SUBJECT: {self.subject}"

# array of objects (subjects)
subjects = [Subject("Algebra and Analitic Geometry"), Subject("Object Oriented Programming"), Subject("English Language")]
# each subject will have a number of objects of the exam class inside of it

# print(subjects[0])    [test (checked)]
