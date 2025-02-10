# Validate bet
if bet not in colors:
    print("Invalid choice! Restart and choose a valid color.")
    screen.bye()

# Create turtles
turtles = []
y_positions = [-100, -60, -20, 20, 60, 100]

for i in range(6):
    t = turtle.Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=-350, y=y_positions[i])
    turtles.append(t)

# Start race
race_on = True

while race_on:
    for t in turtles:
        t.forward(random.randint(1, 10))  # Move each turtle randomly

        if t.xcor() >= 350:  # If any turtle reaches the finish line
            race_on = False
            winning_color = t.pencolor()

            # Announce result
            if winning_color == bet:
                print(f"Congratulations! The {winning_color} turtle won. You win!")
            else:
                print(f"Oops! The {winning_color} turtle won. You lose.")

            break  # Exit loop when race ends

# Close the game on click
screen.exitonclick()
