import json
import datetime


class Score:
    def __init__(self, player_name, score, date):
        self.player_name = player_name
        self.score = score
        self.score_list = []
        self.score_dic = {}
        self.date = date

    def add_score(self):
        self.score_dic["player_name"] = self.player_name
        self.score_dic["score"] = self.score
        self.score_dic["date"] = self.date
        self.score_list.append(self.score_dic)

    def from_json(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            for i in data:
                self.score_dic["player_name"] = i["player_name"]
                self.score_dic["score"] = i["score"]
                self.score_dic["date"] = i["date"]
                self.score_list.append(self.score_dic)
            return self.score_dic

    def to_dict(self):
        self.score_dic["player_name"] = self.player_name
        self.score_dic["score"] = self.score
        self.score_dic["date"] = self.date
        return self.score_dic

    def from_dict(self, dic):
        player_name = dic["player_name"]
        score = dic["score"]
        date = dic["date"]
        return Score(player_name, score, date)

    def to_json(self):
        string = json.dumps(Score.__dict__)
        return string

    def print_data(self):
        print(self.score_list)
