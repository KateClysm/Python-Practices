import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)
        if not self.contents:
            raise ValueError("A hat will always be created with at least one ball.")

    def draw(self, n_balls):
        if n_balls <= len(self.contents):
            balls = []
            for _ in range(n_balls):
                ball = random.choice(self.contents)
                balls.append(ball)
                self.contents.remove(ball) #removes the ball
            return balls #returns them as a list of strings
        else: 
            contents_copy = self.contents[:]
            self.contents.clear()
            return contents_copy


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
    
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls = hat_copy.draw(num_balls_drawn)
        frecuency = {}
        for ball in balls:
            if ball in frecuency:
                frecuency[ball] += 1 #ball as the key for the dictionary
            else:
                frecuency[ball] = 1

        if all(frecuency.get(ball, 0) >= expected_balls[ball] for ball in expected_balls):
            success_count += 1
            
        probability = success_count / num_experiments
    return probability
