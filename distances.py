from dataclasses import dataclass, field

MEDIUM_JUMP_MULTIPLIER = 1.29
MEDIUM_RUN_MULTIPLIER = 1.40

LONG_JUMP_MULTIPLIER = 1.15
LONG_RUN_MULTIPLIER = 1.25

MULTIPLIERS = {'long': {'jump': LONG_JUMP_MULTIPLIER, 'run': LONG_RUN_MULTIPLIER},
               'medium': {'jump': MEDIUM_JUMP_MULTIPLIER, 'run': MEDIUM_RUN_MULTIPLIER}}

MEDIUM_DISTANCES = [38, 37, 36, 34, 33, 30, 27, 25, 23, 20, 17, 13, 11]
LONG_DISTANCES =   [67, 65, 62, 58, 56, 52, 49, 44, 40, 35, 30, 25, 18]


@dataclass
class Distance:
    distance: str
    still: list
    jump: list = field(init=False)
    run: list = field(init=False)

    def __post_init__(self) -> None:
        self.jump = [round(distance * MULTIPLIERS[self.distance]['jump'])
                     for distance in self.still]
        self.run = [round(distance * MULTIPLIERS[self.distance]['run'])
                    for distance in self.still]


medium_distances = Distance('medium', MEDIUM_DISTANCES)
long_distances = Distance('long', LONG_DISTANCES)
