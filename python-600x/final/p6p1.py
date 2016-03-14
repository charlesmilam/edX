class Person(object):
    def __init__(self, name):
        self.name = name
    def say(self, stuff):
        return self.name + ' says: ' + stuff
    def __str__(self):
        return self.name

class Lecturer(Person):
    def lecture(self, stuff):
        return 'I believe that ' + Person.say(self, stuff)

class Professor(Lecturer):
    def say(self, stuff):
        return 'Prof. ' + self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor):
    def say(self, stuff):
        return self.name + ' says: It is obvious that I believe that ' + Person.say(self, stuff)

    def lecture(self, stuff):
        return 'It is obvious that I believe that ' + Person.say(self, stuff)

# class ArrogantProfessor(Professor):
#     def say(self, stuff):
#         return self.name + ' says: It is obvious that I believe that' + self.name + ' says: ' + stuff
#
#     def lecture(self, stuff):
#         return 'Prof. ' + self.name + ' say: It is obvious that I believe that ' + Person.say(self, stuff)

e = Person('eric')
le = Lecturer('eric')
pe = Professor('eric')
ae = ArrogantProfessor('eric')

# Test - Person
print 'Person say'
print 'Expected: eric says: the sky is blue'
print 'Actual:', e.say('the sky is blue')
print
print '-' * 15
print

# Test - Lecturer say
print 'Lecturer say'
print 'Expected: eric says: the sky is blue'
print 'Actual:', le.say('the sky is blue')
print
print '-' * 15
print

# Test - Lecturer lecture
print 'Lecturer lecture'
print 'Expected: I believe that eric says: the sky is blue'
print 'Actual:', le.lecture('the sky is blue')
print
print '-' * 15
print

# Test - Professor say
print 'Professor say'
print 'Expected: eric says: I believe that eric says: the sky is blue'
print 'Actual:', pe.say('the sky is blue')
print
print '-' * 15
print

# Test - Professor lecture
print 'Professor lecture'
print 'Expected: eric says: I believe that eric says: the sky is blue'
print 'Actual:', pe.say('the sky is blue')
print
print '-' * 15
print

# Test - Arrogant Professor say
print 'Arrogant Professor say'
print 'Expected: eric says: It is obvious that I believe that eric says: the sky is blue'
print 'Actual:', pe.say('the sky is blue')
print
print '-' * 15
print

# Test - Arrogant Professor lecture
print 'Arrogant Professor lecture'
print 'Expected: It is obvious that I believe that eric says: the sky is blue'
print 'Actual:', pe.say('the sky is blue')
print
print '-' * 15
print
