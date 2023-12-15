class Healthbar:
    """
        A class that represents the cursor on the screen
        ...

        Attributes
        x : int
            position of the healthbar in the x-axis of the screen
        y : int
            position of the healthbar in the y-axis of the screen
        width : int
            width of the healthbar in pixels
        height : int
            height of the healthbar in pixels
        hp : int
            starting healthpoints of the player
        max_hp : int
            maximum value of health points of player
        -------
        """

    def __init__(self, x, y,  max_hp):
        self.x = x
        self.y = y
        self.width = 300
        self.height = 40
        self.hp = max_hp
        self.max_hp = max_hp
