from calendar import leapdays
from enum import Enum

class AllGrades:
    # TODO read this all from a config file, much neater
    # Also have a long and heated discussion about what is equivalent between disciplines! Absolutely no effort made to equalise it so far.

    winter_grades = {
        "I": 1,
        "I/II": 2,
        "II": 3,
        "II/III": 4,
        "III": 5,
        "IV": 6,
        "V": 7,
        "VI": 8,
        "VII": 9,
        "VIII": 10,
        "IX": 11,
        "X": 12,
        "XI": 13,
        "XII": 14
    }

    trad_grades = {
        "none": 1,
        "M":    1,
        "D":    2,
        "HD":   2.5,
        "VD":   3,
        "HVD":  4,
        "MS":   4.5,
        "S":    5,
        "HS":   6,
        "MVS":  6.5,
        "VS":   7,
        "HVS":  8,
        "E1":   9,
        "E2":   10,
        "E3":   11,
        "XS":   11, # ??
        "E4":   12,
        "E5":   13,
        "E6":   14,
        "E7":   15,
        "E8":   16,
        "E9":   17,
        "E10":  18,
        "E11":  19
    }

    boulder_grades = {
        "?":    1,
        "f?":   1,
        "VE":   1,
        "VM":   2,
        "VB":   3,
        "V0-":  3.5,
        "V0":   4,
        "V0+":  4.5,
        "V1":   5,
        "V2":   6,
        "V3":   7,
        "V3+":  7.5,
        "V4":   8,
        "V4+":  8.5,
        "V5":   9,
        "V5+":  9.5,
        "V6":   10,
        "V7":   11,
        "V8":   12,
        "V8+":  13,
        "V9":   14,
        "V10":  15,
        "V11":  16,
        "V12":  17,
        "V13":  18,
        "V14":  19,
        "V15":  20,
        "V16":  21,
        "V17":  22,
        "f2":   2,
        "f2+":  2.5,
        "f3":   3,
        "f3+":  3.5,
        "f4":   4,
        "f4+":  4.5,
        "f5":   5,
        "f5+":  6,
        "f6A":  7,
        "f6A+": 7.5,
        "f6B":  8,
        "f6B+": 8.5,
        "f6C":  9,
        "f6C+": 9.5,
        "f7A":  10,
        "f7A+": 11,
        "f7B":  12,
        "f7B+": 13,
        "f7C":  14,
        "f7C+": 15,
        "f8A":  16,
        "f8A+": 17,
        "f8B":  18,
        "f8B+": 19,
        "f8C":  20,
        "f8C+": 21,
        "f9A":  22
    }

    sport_grades = {
        "1":    1,
        "2a":   2,
        "2b":   2,
        "2c":   2,
        "3a":   3,
        "3b":   3,
        "3c":   3.5,
        "4a":   4,
        "4b":   4,
        "4c":   4.5,
        "5a":   5,
        "5b":   5.5, # It's all a bit messed up here, can fix later
        "5c":   6,
        "6a":   7,
        "6a+":  7.5,
        "6b":   8,
        "6b+":  8.5,
        "6c":   9,
        "6c+":  9.5,
        "7a":   10,
        "7a+":  11,
        "7b":   12,
        "7b+":  13,
        "7c":   14,
        "7c+":  15,
        "8a":   16,
        "8a+":  17,
        "8b":   18,
        "8b+":  19,
        "8c":   20,
        "8c+":  21,
        "9a":   22, # Top end is a bit skewed against bouldering, but not really an issue for how this gets used!!
        "9a+":  23,
        "9b":   24,
        "9b+":  25,
        "9c":   26
    }

class Grade:
    # Underlying grade will be some easy to use numerical value
    def __init__(self, text_grade):
        self.numerical_grade, self.climb_type = Grade._interpret_grade(text_grade)
    def _interpret_grade(text_grade):
        # Check bouldering grades
        try:
            grade = AllGrades.boulder_grades[text_grade]
        except KeyError:
            pass
        else:
            grade_type = "boulder"
            return (grade, grade_type)
        # Check trad grades
        try:
            grade = AllGrades.trad_grades[text_grade]
        except KeyError:
            pass
        else:
            grade_type = "trad"
            return (grade, grade_type)
        # Check sport grades
        try:
            grade = AllGrades.sport_grades[text_grade]
        except KeyError:
            pass
        else:
            grade_type = "sport"
            return (grade, grade_type)
        # TODO implement other grades (or more likely neaten this up to reduce code replication)
    def __str__(self):
        return f"{self.climb_type}: {self.numerical_grade}"

class Style:
    # E.g. lead/solo/boulder/TR, onsight/flash/RP/dog
    class MainStyle(Enum):
        NONE = 0
        LEAD = 1
        SECOND = 2
        SOLO = 3
        BOULDER = 4
        TOP_ROPE = 5
        ALT_LEAD = 6
        DWS = 7
    
    class SubStyle(Enum):
        NONE = 0
        ONSIGHT = 1
        FLASH = 2
        GROUND_UP = 3
        REDPOINT = 4
        REPEAT = 5
        DOG = 6
        DNF = 7
    
    def __init__(self, main_style, sub_style):
        self.main_style = main_style
        self.sub_style = sub_style
    
    def __str__(self):
        return f"{self.main_style.name.capitalize()} {self.sub_style.name.lower()}"