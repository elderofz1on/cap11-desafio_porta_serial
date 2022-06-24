def on_forever():
    serial.write_value("x", input.acceleration(Dimension.X))
    basic.pause(500)
basic.forever(on_forever)
