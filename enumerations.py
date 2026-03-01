# Written by: Christopher Gholmieh
# Imports:

# Enum:
import enum


# Education:
class Education(enum.Enum):
    # College:
    COLLEGE = enum.auto()

    # School:
    HIGH_SCHOOL = enum.auto()

    # Below:
    BELOW_HIGH_SCHOOL = enum.auto()


# Race:
class Race(enum.Enum):
    # Black:
    BLACK = enum.auto()

    # Other:
    OTHER = enum.auto()