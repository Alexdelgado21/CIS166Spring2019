#Alex Delgado
#Extra Credit




def poundsTo():
    g = number * 452.592
    kilo = number / 0.453592
    ounces = number * 16

    gramsbox.setText(g)
    kilobox.setText(kilo)
    ouncebox.setText(ounces)

win = GraphWin("Conversions", 800, 600)

poundstext = Text(Point(180, 60), "Pounds:")
poundstext.draw(win)

poundsbox = Entry(Point(win.getWidth() / 2, 60), 25)
poundsbox.setFill("blue")
poundsbox.draw(win)

gramstext = Text(Point(190, 130), "Grams:")
gramstext.draw(win)

gramsbox = Text(Point(win.getWidth() / 2, 100), "")
gramsbox.draw(win)

kilotext = Text(Point(170, 160), "Kilograms:")
kilotext.draw(win)

kilobox = Text(Point(win.getWidth() / 2, 150), "")
kilobox.draw(win)

ouncetext = Text(Point(180, 220), "Ounces:")
ouncetext.draw(win)

ouncebox = Text(Point(win.getWidth() / 2, 200), "")
ouncebox.draw(win)

button = Text(Point(win.getWidth() / 2, 300), "Convert")
button.draw(win)

while True:
    win.getMouse()

    number = int(poundsbox.getText())
    poundsTo()
