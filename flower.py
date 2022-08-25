import utils

class Flower:
    def __init__(self, image, position, size):
        self.image = image
        self.position = position
        self.size = size
        self_half_size = self.size / 2
        self.center = (self.position[0] + self_half_size / 2, self.position[1] + self_half_size / 2)
        # self.diagonal = 1.41421356237 * self.size
        self.half_diagonal = 0.75 * self.size
        # self.half_diagonal = 0,707106781185 * self.size
        
    def overlap(self, other_center, other_half_diagonal):
        distance = utils.compute_distance(self.center, other_center)

        # print(distance,self.half_diagonal + other_half_diagonal)
        return distance <= self.half_diagonal + other_half_diagonal 