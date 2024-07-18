import klayout.db as db
import matplotlib.pyplot as plt
import numpy as np

centerx = 0
centery = 0


width = 1000
height = 400

new_layout = db.Layout()

box = db.DBox(centerx-width/2, centery-height/2, centerx+width/2, centery+height/2)

top = new_layout.create_cell("TOP")


l1 = new_layout.layer(1, 0)

top.shapes(l1).insert(box)

arm = db.DBox(-100, -200, 100, 200)
contact = db.DBox(-200, 200, 200, 600)
shift = db.DCplxTrans.new(300, height)
top.shapes(l1).insert(shift*arm)
top.shapes(l1).insert(shift*contact)


shift = db.DCplxTrans.new(-300, height)
top.shapes(l1).insert(shift*arm)
top.shapes(l1).insert(shift*contact)


shift = db.DCplxTrans.new(1, 180, False, -300, -height)
top.shapes(l1).insert(shift*arm)
top.shapes(l1).insert(shift*contact)


shift = db.DCplxTrans.new(1, 180, False, 300, -height)
top.shapes(l1).insert(shift*arm)
top.shapes(l1).insert(shift*contact)



shift = db.DCplxTrans.new(1, -90, False, 600, 0)
top.shapes(l1).insert(shift*arm)
top.shapes(l1).insert(shift*contact)

shift = db.DCplxTrans.new(1, 90, False, -600, 0)
top.shapes(l1).insert(shift*arm)
top.shapes(l1).insert(shift*contact)

new_layout.write("bar.gds")
