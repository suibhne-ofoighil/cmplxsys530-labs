import matplotlib.pyplot as plt
import numpy as np


class LangstonsAnt:
    directions = ['^', '>', 'v', '<']

    def __init__(self, dimensions=11, direction=0, random_middle=False):
        plt.cla()
        self.config = np.zeros(shape=(dimensions, dimensions))
        (self.x, self.y) = (np.array((dimensions, dimensions)) / 2).astype(int)
        self.direction = direction
        self.dimensions = dimensions

        if random_middle:
            offsets = np.array([-1, 0, 1])
            Ys = offsets + self.y
            Xs = offsets + self.x
            for y in Ys:
                for x in Xs:
                    self.config[y, x] = np.random.randint(0, 2)


    def update(self):

        # if cell ant is on is black
        if self.config[self.x, self.y] == 1:

            # turn to right
            self.direction = (self.direction + 1) % 4

            # turn cell white
            self.config[self.x, self.y] = 0

            # move forward
            if self.direction == 0:
                self.y = (self.y - 1) % self.dimensions
            elif self.direction == 1:
                self.x = (self.x + 1) % self.dimensions
            elif self.direction == 2:
                self.y = (self.y + 1) % self.dimensions
            elif self.direction == 3:
                self.x = (self.x - 1) % self.dimensions

        # if ant on white cell
        else:

            # turn to left
            self.direction = (self.direction - 1) % 4

            # turn cell black
            self.config[self.x, self.y] = 1

            # move forward
            if self.direction == 0: #facing up
                self.y = (self.y - 1) % self.dimensions
            elif self.direction == 1: #facing right
                self.x = (self.x + 1) % self.dimensions
            elif self.direction == 2: #facing down
                self.y = (self.y + 1) % self.dimensions
            elif self.direction == 3: #facing left
                self.x = (self.x - 1) % self.dimensions

    def observe(self):
        # plot board
        plt.imshow(self.config, cmap=plt.cm.binary)

        # plot ant
        plt.scatter(self.y, self.x, c='red', marker=self.directions[self.direction])

        print(self.x, self.y)

        plt.show()


if __name__ == '__main__':

    # Game = LangstonsAnt(direction=3, dimensions=11)
    Game = LangstonsAnt(direction=2, dimensions=100, random_middle=True)
    [ Game.update() for i in range(1000000) ]
    Game.observe()

