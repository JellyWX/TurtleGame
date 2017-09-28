import turtle

def ReadVertex(fileN):
  with open(fileN,'r') as f:
    instr = []
    for line in f:
      line = line.replace(' ','').replace('\n','').split('>')
      if line[0].startswith('#'):
        continue
      point = []
      for i in range(len(line)):
        point.append(
          tuple(map(float,line[i].split(',')))
        )

      instr.append(point)

  return instr

def PaintVertex(vertexes,scale=1,pos=(0,0)):
  T = turtle.Turtle()
  T.ht()
  T.speed(0)

  for instruction in vertexes:
    print('instruction ', instruction)

    T.penup()
    T.goto(instruction[0][0] * scale + pos[0],instruction[0][1] * scale + pos[1])
    T.pendown()

    for coord in instruction:
      T.goto(coord[0] * scale + pos[0],coord[1] * scale + pos[1])
