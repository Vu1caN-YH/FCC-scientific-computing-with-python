import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.total_balls = sum(k for k in kwargs.values())
        self.contents = [colour for colour, quantity in kwargs.items() for _ in range(quantity)]

    def draw(self, number):   
        removed_list = []
        if number > len(self.contents):
            removed_list = copy.copy(self.contents)
            self.contents = []
            return removed_list
        while number >0:
            removed_ball = self.contents.pop(
                random.randint(0, len(self.contents) - 1)
                )
            removed_list.append(removed_ball)
            number -= 1
            
        return removed_list
          

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M=0
    number_of_times_ran = num_experiments

    while number_of_times_ran > 0:
        hat_copy = copy.deepcopy(hat)
        removed_balls = hat_copy.draw(num_balls_drawn)
        ball_dict = {}
        for ball in removed_balls:
            if ball in ball_dict:
                ball_dict[ball] += 1
            else:
                ball_dict[ball] = 1

        success = True
        for ball, qty in expected_balls.items():
            if ball_dict.get(ball, 0) < qty:
                success = False
                break
            
        if success:
            M += 1
        number_of_times_ran -= 1

    #return number_of_times_ran, M, num_experiments, M/num_experiments
    return M/num_experiments

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)

print(probability)
