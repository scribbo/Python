import time
import turtle


def circle_draw(x, y, r, color):

    turtle.up()
    turtle.goto(x, y - r)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r, 360)
    turtle.end_fill()

    return


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    def running(self):

        while True:
            circle_draw(15, -55, 15, 'white')
            circle_draw(15, -20, 15, 'white')
            circle_draw(15, 15, 15, TrafficLight.__color[0])
            time.sleep(7)
            circle_draw(15, 15, 15, 'white')
            circle_draw(15, -20, 15, TrafficLight.__color[1])
            circle_draw(15, -55, 15, 'white')
            time.sleep(2)
            circle_draw(15, 15, 15, 'white')
            circle_draw(15, -20, 15, 'white')
            circle_draw(15, -55, 15, TrafficLight.__color[2])
            time.sleep(5)


tl = TrafficLight()
tl.running()
