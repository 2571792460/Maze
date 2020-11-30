class Player():
    """
    This is a class of player list
    """
    def __init__(self):
        self._backpack = []


    @property
    def backpack(self):
        return self._backpack

    def pick_up_item(self, item):
        # player backpage list append an item
        self._backpack.append(item)

