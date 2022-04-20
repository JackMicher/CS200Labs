# Module for Course class item
# Designed for use with transcript_manager
# By Jack Micher

class Course:
    """ A Course Item Object to store and return information about one course """
    def __init__(self, coursecode, coursename, ccredits, grade, semester, instructor):
        self._coursecode = coursecode
        self._coursename = coursename
        self._ccredits = int(ccredits)
        self._grade = grade
        self._semester = semester
        self._instructor = instructor
        
    # ============ setter methods ============
    def setcode(self, coursecode):
        self._coursecode = coursecode
    
    def setname(self, coursename):
        self._coursename = coursename
    
    def setcredits(self, ccredits):
        self._ccredits = ccredits
    
    def setgrade(self, grade):
        self._grade = grade
    
    def setsemester(self, semester):
        self._semester = semester
    
    def setinstructor(self, instructor):
        self._instructor = instructor

    # ============ return methods ============
    def getcode(self):
        return self._coursecode
    
    def getname(self):
        return self._coursename
    
    def getcredits(self):
        return self._ccredits
    
    def getgrade(self):
        return self._grade
    
    def getsemester(self):
        return self._semester
    
    def getinstructor(self):
        return self._instructor
    
    def __str__(self):
        return self._coursecode + "\t" + str(self._ccredits) + "\t" + self._grade + \
               "\t" + self._semester + "\t" + self._instructor + "\t\t" + self._coursename