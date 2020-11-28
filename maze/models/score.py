import json
import datetime

class Score:
    def __init__(self, player_name, score, date):

        self.player_name = player_name

        self.score = score
        self.score_list = []
        self.score_dic = {}
        self.date = date

    def add_score_from_json(self, player_name, score, date):
        self.score_dic["player_name"] = player_name
        self.score_dic["score"] = score
        self.score_dic["date"] = date
        self.score_list.append(self.score_dic)

    def add_score_from_app(self):
        self.score_dic["player_name"] = self.player_name
        self.score_dic["score"] = self.score
        self.score_dic["date"] = self.date
        self.score_list.append(self.score_dic)

    def from_json(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            for i in data:
                self.add_score_from_json(i['player_name'], i["score"], i["date"])


    def print_1(self):
        print(self.score_list)


    # def to_dict(self):
    #
    #     # dictinary['player_name'] = self.player_name
    #     # dictinary['score'] = self.score
    #     # dictinary['data'] = self.date
    #     # return dictinary
    #
    # def from_dict(self, dictionary):
    #     json_file = json.dumps(dictionary)
    #     return json_file
    #
    # def to_json(self):
    #     string = json.dumps(Score.__dict__)
    #     return string

