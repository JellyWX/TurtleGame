import turtle

class Element():
  def __init__(self, scale=1, pos=(0,0)):
    self.turtle = turtle.Turtle()

    self.instructions = []
    self.scale = scale
    self.x = pos[0]
    self.y = pos[1]

    self.turtle.ht()
    self.turtle.speed(0)

  def from_file(self, fileN : str): ## method to form a turtle path from a file
    with open(fileN,'r') as f:
      instr = []
      for line in f:
        line = line.replace(' ','').replace('\n','').split('>')

        if line[0].startswith('#'): # ignore hashed lines
          continue

        point = []
        for i in range(len(line)):
          point.append(
            tuple(
              map(float,line[i].split(','))
            )
          )

        instr.append(point)

    self.instructions = instr

  def from_list(self, instr : list): ## method to form a turtle path from a list of vertices
    self.instructions = instr

  def scale(self, s : int):
    self.scale = s

  def pos(self, p : tuple):
    self.x = p[0]
    self.y = p[1]

  def draw(self):

    for instruction in self.instructions:
      print('{}: instruction {}'.format(self,instruction))

      self.turtle.penup()
      self.turtle.goto(instruction[0][0] * self.scale + self.x, instruction[0][1] * self.scale + self.y)
      self.turtle.pendown()

      for coord in instruction:
        self.turtle.goto(coord[0] * self.scale + self.x, coord[1] * self.scale + self.y)
