import copy
import random
# Consider using the modules imported above.


class Hat:

  def __init__(self, **kwargs):
    self.contents = []

    for color, count in kwargs.items():
      for _ in range(count):
        self.contents.append(color)

  def draw(self, num_balls_to_draw):
    # if the number of balls to draw exceeds the available quantity, return all the balls
    if num_balls_to_draw > len(self.contents):
      return self.contents
    else:
      balls_to_draw = random.sample(self.contents, num_balls_to_draw)

      for ball in balls_to_draw:
        self.contents.remove(ball)

      return balls_to_draw


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  # num_successful_experiments is the number of times the balls drawn meets the expected_balls
  num_successful_experiments = 0

  for _ in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    balls_drawn = hat_copy.draw(num_balls_drawn)
    success = False

    # check if the balls drawn meets the expected_balls
    for expected_color, expected_count in expected_balls.items():
      # if the balls drawn meet the expected_balls
      if balls_drawn.count(expected_color) >= expected_count:
        success = True
      else:
        success = False
        break

    if success:
      num_successful_experiments += 1

  return num_successful_experiments / num_experiments
