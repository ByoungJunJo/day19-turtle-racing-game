# day19-turtle-racing-game
Main lesson: Understanding x and y coordinates using the Turtle Python library.
## Project Descriptions
There are 2 parts in the day 19 lessons:
1. Make an Etch-A-Sketch game
```
def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_counterclockwise():
    tim.circle(radius=50, extent=60, steps=10)

def move_clockwise():
    tim.circle(radius=-50, extent=60, steps=10)

def clear_drawing():
    tim.reset()

screen.listen()

# Function as inputs (higher order functions); Use keyword arguments
screen.onkey(fun=move_forwards, key="W")
screen.onkey(fun=move_backwards, key="S")
screen.onkey(fun=move_counterclockwise, key="A")
screen.onkey(fun=move_clockwise, key="D")
screen.onkey(fun=clear_drawing, key="C")
```
### Key lessons from Make an Etch-A-Sketch Game
  - Create funcitons for each movement: move forward, backward, turn clockwise and counterclockwise.
  - Use the keyword arguments (called higher order functions).\
  According to Angela, this is common in Python, but some other languages do not support this.
  - Sometimes using the keyword arguments is more straightforward than the positional arguments because they show what exactly I'm calling.
2. Make a turtle racing game
This was the main project for the day. Bascially, I needed to create multiple turtles to race each other.
To do so, I used functions to create multiple "Turtle" objects:
```
def create_turtle(x, y, color):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x, y)
    return new_turtle

```
Then I created multiple turtles with different colors: `colors = ["red", "orange", "yellow", "green", "blue", "purple"]`.\
To know where each turtle was located, I used this method from Screen class: `screen.setup(width=500, height=400)`.\
This allowed me to figure out x and y coordinate much easier.Simply the Turtle library uses the [Cartesian coordinate system](https://en.wikipedia.org/wiki/Cartesian_coordinate_systems).
```
# Fixed x position
x = -230

# Starting y postion
y = -100
```

Now it's time to create multiple turtles using the function I created ealier `create_turtle`.
```
# Create multiple turtles and append them into the all_turtles list
i = 0
while i < len(colors):
    new_turtle = create_turtle(x=x, y=y, color=colors[i])
    all_turtles.append(new_turtle)
    i += 1
    y += 30
```
Then we're going to repeate `forward`moves until any turtle reaches to the end of the screen (`width > 230`)
```
# Once user has bet, change the 'is_race_on' to True
if user_bet:
    is_race_on = True

# Each turtle go random amount forwards from 0 to 10
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if user_bet == winning_turtle:
                print("You'won!")
            else:
                print("You lost!")
            print(f"You chose the {user_bet} turtle, and the winning turtle was the {winning_turtle} turtle.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
```

### Key lessons from the turtle racing project:
1. I can use functions to create multiple objects. I checked some other resources online, but I couldn't understand the code written.\
It's better to write my own which I can understand.
2. Don't be afraid of trying something new. Keep testing and printing out stuff and see how it goes--"what's the worst case scenario?"
3. Consitency, repeatability, and simplicity both in programming and life.
