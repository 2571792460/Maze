import json
from operator import itemgetter


class Score:
    """
    This is the Score Class
    """
    def __init__(self, player_name, score, date):
        """
        add player information to a dic and append it to the list
        :param1: player_name: str
        :param2: score: int
        :param3: date: str
        """
        self.player_name = player_name
        if type(score) != int:
            raise TypeError
        else:
            self.score = score
        self.score_list = []
        self.score_dic = {}
        self.date = date
        # Create a dic which contains player information
        self.score_dic["player_name"] = self.player_name
        self.score_dic["score"] = self.score
        self.score_dic["date"] = self.date
        # Append the dic into list
        self.score_list.append(self.score_dic)

    def from_json(self, filename):
        """
        Import data from a json file and put it into player_list
        :param1: filename: path
        :return: list
        """
        with open(filename) as f:
            data = json.load(f)
            for i in data:
                new_player = Score(i["player_name"], i["score"], i["date"])
                self.score_list.append(new_player.score_dic)
            return self.score_list

    def to_json(self, file):
        """
        Put data stored in self.score_list into a json file
        :param1: file: path
        """
        data = json.load(open(file))
        data.append(self.score_dic)
        # Sort the player information in score_list from high to low based on score
        new_list = sorted(data, reverse=True, key=itemgetter('score'))
        with open(file, 'w') as json_file:
            json.dump(new_list, json_file)

    def to_dict(self):
        """
        Convert a class instance into a dic
        :return: dic
        """
        self.score_dic["player_name"] = self.player_name
        self.score_dic["score"] = self.score
        self.score_dic["date"] = self.date
        return self.score_dic

    def from_dict(self, dic):
        """
        Convert a dic instance into a class instance
        :param1: dic: dic
        :return: class
        """
        player_name = dic["player_name"]
        score = dic["score"]
        date = dic["date"]
        return Score(player_name, score, date)


