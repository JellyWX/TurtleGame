# TurtleGame
Python Turtle 'engine'
## What
It's a very basic renderer using Python Turtle
## How
Download and copy across `TurtleTools.py`.
## How #2
To read a vertex file, use `ReadVertex(filename)`. To then render the vertexes, use `PaintVertex(vertex)`.
## What's a vertex file?
A vertex file is a file containing all the points you need rendered. **We recommend you do all your vertexes as numbers less than or equal to 1, and that the start of the main instruction starts at 0,0**. It works something like this:
```
# Draw a square (fastest way)
0,0 > 0,1 > 1,1 > 1,0 > 0,0

# Draw half a square and then a triangle under it
0,0 > 0,1 > 1,1 > 1,0
0,0 > -1,0 > 0,-1 > 0,0
```

## Why < 1 and 0,0?
Because it means that scaling is working by the same amount for each object. You can scale up an object before you draw it with `PaintVertex(vertex,scale=10)`. Similarly, you can offset your shape using `PaintVertex(vertex,pos=(0,10))`
