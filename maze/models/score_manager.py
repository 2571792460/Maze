import json
from maze.models.score import Score


class ScoreManager:
    """
    this class uses aggregation to manage a collection of 'Score' instances.
    """
    def __init__(self):
        """ uses a dictionary to store the player items """
        self._items = dict()

    @property
    def items_text(self):
        """ getter for the items_text property """
        return [f"{item.player_name}: {item.score} at {item.date}" for item in self._items.values()]

    @property
    def items(self):
        """ property items (list of players) """
        return list(self._items.values())

    def add_item(self, player):
        """
        add an item to the manager

        Args:
            player (Score): the item to add


        Returns:
            None
        """
        self._items[player.player_name] = player

    def load_from_json(self, f='./models/result.json'):
        """loads player items from a JSON file (default = result.json)"""
        with open(f, 'r') as fp:
            json_data = json.load(fp)
            for player in json_data:
                obj = Score(
                    player_name=player['player_name'],
                    score=player['score'],
                    date=player['date']
                )
                self.add_item(obj)
