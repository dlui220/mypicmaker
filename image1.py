def createImage(xres,yres):
    switch = 1
    image = open("test1.ppm",'w')
    s = "P3 " + str(xres) + " " + str(yres) + " 255 "
    r = 255
    g = 0
    b = 0
    for i in range(yres):
        for j in range(xres):
            s += str(r) + " " + str(g) + " " + str(b) + " "
        r -= 1 * switch
        g += 1 * switch
        b += 1 * switch
        if (g == 255):
            switch = switch * -1
        if (switch == -1 and g == 0):
            switch = switch * -1

    image.write(s)
    image.close()

createImage(600,600)
