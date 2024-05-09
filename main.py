from canvas import Canvas
from shapes import Square, Rectangle

canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Enter canvas color (black or white)")

canvas = Canvas(canvas_width, canvas_height, colors[canvas_color])

while True:
    shape_type = input("What do you like to draw?(rectangle or square) Enter quit to quit. ")
    if shape_type.lower() == 'rectangle':
        rec_x = int(input("Enter x of the rectangle: "))
        rec_y = int(input("Enter y of the rectangle: "))
        rec_width = int(input("Enter width of the rectangle: "))
        rec_height = int(input("Enter height of the rectangle: "))
        red = int(input("How much red should the rectangle have?(0-255) "))
        green = int(input("How much green should the rectangle have?(0-255) "))
        blue = int(input("How much blue should the rectangle have?(0-255) "))

        rectangle1 = Rectangle(rec_x, rec_y, rec_width, rec_height, (red, green, blue))
        rectangle1.draw(canvas)

    if shape_type.lower() == 'square':
        sqr_x = int(input("Enter x of the square: "))
        sqr_y = int(input("Enter y of the square: "))
        sqr_side = int(input("Enter side of the square: "))
        red = int(input("How much red should the square have?(0-255) "))
        green = int(input("How much green should the square have?(0-255) "))
        blue = int(input("How much blue should the square have?(0-255) "))

        square1 = Square(sqr_x, sqr_y, sqr_side, (red, green, blue))
        square1.draw(canvas)

    if shape_type.lower() == "quit":
        break
canvas.make('canvas.png')
