class Logbook:
    def __init__(self, climber_name):
        self.climber_name = climber_name
        self.ascents = []
    def add_ascent(self, ascent):
        self.ascents.append(ascent)

class Ascent:
    def __init__(self, climb_name, date, grade, climb_type, style, stars):
        # Could also be added: crag, partner, notes
        self.name = climb_name
        self.date = date
        self.grade = grade
        self.type = climb_type
        self.style = style
        self.stars = stars