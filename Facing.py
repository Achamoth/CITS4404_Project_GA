from enum import Enum


class Facing(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    def rotateAnticlockwise(self):
        # type: () -> Facing
        if self == Facing.UP:
            return Facing.LEFT
        elif self == Facing.LEFT:
            return Facing.DOWN
        elif self == Facing.DOWN:
            return Facing.RIGHT
        else:
            return Facing.UP

    def rotateClockwise(self):
        # type: () -> Facing
        if self == Facing.UP:
            return Facing.RIGHT
        elif self == Facing.RIGHT:
            return Facing.DOWN
        elif self == Facing.DOWN:
            return Facing.LEFT
        else:
            return Facing.UP

    def rotateTowards(self, target):
        # type: (Facing) -> Facing
        if self.rotateAnticlockwise() == target or self.rotateClockwise() == target:
            return target
        return self.rotateAnticlockwise()
