class Healthbar:
    """
        A class that represents the cursor on the screen
        ...

        Attributes
        x : int
            #TODO
        y : int
            #TODO
        width : int
            #TODO
        height : int
            #TODO
        hp : int
            #TODO
        max_hp : int
            #TODO
        -------
        """

    def __init__(self, x, y,  max_hp):
        self.x = x
        self.y = y
        self.width = 300
        self.height = 40
        self.hp = max_hp
        self.max_hp = max_hp
