# from luma.core.interface.serial import spi, noop
# from luma.core.render import canvas
# from luma.led_matrix.device import max7219
# import numpy as np
# from time import sleep

# serial = spi(port=0, device=0, gpio=noop())
# device = max7219(serial, block_orientation=-90, cascaded=6)

# device.contrast(4)
# device.clear()

with open("expressions.dat") as file:
    expressions = eval(file.read())
    
class Expression:
    def __init__(self, points=None, animated=False, 
                 OnlyEyes=False, preclear=True):
        self.expression = points
        self.isanimated = animated
        self.onlyUpdateEyes = OnlyEyes
        self.needClearBeforeRender = preclear
    
    def __str__(self):
        return "Expression(%s,%s,%s,%s)"%(self.points,
                                          self.animated,
                                          self.OnlyEyes,
                                          self.preclear)
    def demo(self):
        for points in self.expression:
            device.clear()
            with canvas(device) as draw:
                for point in points:
                    draw.point(point, fill="white") 
            sleep(.4)

Expressions = {i:Expression(points=e) for i,e in enumerate(expressions)}