class Logbook:
    def __init__(self, climber_name):
        self.climber_name = climber_name
        self.ascents = []
    def add_ascent(self, ascent):
        self.ascents.append(ascent)

class Ascent:
    def __init__(self, date, name, grade):
        self.date = date
        self.name = name
        self.grade = grade # This should be an instance of the Grade class

