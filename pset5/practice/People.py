import datetime

class Person(object):
    def __init__(self, name):
        """create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]
    def setBirthday(self, month, day, year):
        """sets self's birthday to birthDate"""
        self.birthday = datetime.date(year, month, day)
    def getAge(self):
        """returns self's current age in days"""
        if selef.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    def getLastName(self):
        """return self's last name"""
        return self.lastName
    def __lt__(self, other):
        """return True if self's name is lexicographically less than other's name, and Flase
           otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        """retrun self's name"""
        return self.name

class MITPerson(Person):
    nextIdNum = 0

    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum
    def __lt__(self, other):
        return self.idNum < other.idNum
    def speak(self, utterance):
        return (self.name() + " says: " + utterance)

class Professor(MITPerson):
    def __init__(self, name, department):
        MITPerson.__init__(self, name)
        self.department = department
    
    def speak(self, utterance):
        new = 'In course ' + self.department + ' we say '
        return MITPerson.speak(self, new + utterance)
    def lecture(self, topic):
        return self.speak('it is obvious that ' + topic)

class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year
    def speak(self, utterance):
        return MITPerson.speak(self, " Yo bro, " + utterance)

class Grad(Student):
    pass

class TransferStudent(Student):
    pass

def isStudent(obj):
    return isinstance(obj, Student)
