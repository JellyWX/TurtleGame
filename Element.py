import math
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

  def _toPolar(self):
    instr = []
    for instruction in self.instructions:

      point = []
      for coord in instruction:
        new_coord = (math.hypot(coord[0], coord[1]), math.atan2(coord[1], coord[0]))
        point.append(new_coord)

      instr.append(point)

    return instr

  def _toCartesian(self, polar):
    instr = []
    for instruction in polar:

      point = []
      for coord in instruction:
        new_coord = (
          round(coord[0] * math.cos(coord[1]),4),
          round(coord[0] * math.sin(coord[1]),4)
        )
        point.append(new_coord)

      instr.append(point)

    return instr


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

  def scale(self, s : int): ## re-scale the drawing (soft)
    self.scale = s

  def pos(self, p : tuple): ## re-position the drawing (soft)
    self.x = p[0]
    self.y = p[1]

  def rotate(self, d : float):
    r = math.radians(d)

    polar = self._toPolar()

    instr = []
    for instruction in polar:

      point = []
      for coord in instruction:
        new_coord = (coord[0], coord[1] + r)
        point.append(new_coord)

      instr.append(point)

    self.instructions = self._toCartesian(instr)

  def shift(self, p : tuple): ## hard-shift the vertices by user-provided values
    instr = []
    for instruction in self.instructions:

      point = []
      for coord in instruction:
        new_coord = (coord[0] + p[0], coord[1] + p[1])
        point.append(new_coord)

      instr.append(point)

    print('Performing shift: {} to {}'.format(self.instructions, instr))

    self.instructions = instr

  def draw(self): ## get the turtle to draw the vertices

    for instruction in self.instructions:
      print('{}: instruction {}'.format(self,instruction))

      self.turtle.penup()
      self.turtle.goto(instruction[0][0] * self.scale + self.x, instruction[0][1] * self.scale + self.y)
      self.turtle.pendown()

      for coord in instruction:
        self.turtle.goto(coord[0] * self.scale + self.x, coord[1] * self.scale + self.y)

  def reset(self):
    self.turtle.clear()
