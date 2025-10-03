class Colours:
    dark_grey = (26, 31, 40)
    green = (47, 230, 23)
    red = (232, 18, 18)
    orange = (226, 116, 17)
    yellow = (237, 234, 4)
    purple = (166, 0, 247)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)
    white = (255, 255, 255)
    light_blue = (59, 85, 162)
    dark_orange = (186, 86, 17)

    #Allows to access attributes within the class as opposed to the instance
    #can be used to get return total count of classes or even higher level stuff
    @classmethod
    def get_cell_colours(cls):
        return [cls.dark_grey, cls.green, cls.red, cls.light_blue, cls.yellow, cls.purple, cls.cyan, cls.blue]