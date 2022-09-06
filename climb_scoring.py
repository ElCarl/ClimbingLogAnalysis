import climb_grading
from abc import ABC, abstractmethod

class ScoringMethod(ABC):
    @classmethod
    @abstractmethod
    def score_ascent(cls, ascent, logbook):
        pass

# Take in ascent and return a score
# At some future point can be modified to include context such as climber's previous hardest climb/95th percentile climb or suchlike.
class FlatScoring(ScoringMethod):
    # Just give ascents a score based on difficulty. No other modifiers.
    
    # Doesn't actually use any class info, does this still need to be a classmethod if it inherits from something where
    # score_ascent is marked as a classmethod?
    @classmethod
    def score_ascent(cls, ascent, logbook):
        grade_base_score = ascent.grade.numerical_grade
        return grade_base_score

class ScaledScoring(ScoringMethod):
    # Doesn't scale based on previous ascents, but does care about style etc.
    # There should also be some attempt to normalise scores between different disciplines.

    @classmethod
    def score_ascent(cls, ascent, logbook):
        raise NotImplementedError

class AdjustedScaledScoring(ScoringMethod):
    # Should adjust scoring based on previous climbs. E.g. someone doing 3 7As in a day is worth a lot more if they've only done 7A+ rather than 7C!
    @classmethod
    def score_ascent(cls, ascent, logbook):
        raise NotImplementedError