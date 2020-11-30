import json
from operator import itemgetter


class Score:
    def __init__(self, player_name, score, date):
        self.player_name = player_name
        self.score = score
        self.score_list = []
        self.score_dic = {}
        self.date = date
        self.score_dic["player_name"] = self.player_name
        self.score_dic["score"] = self.score
        self.score_dic["date"] = self.date
        self.score_list.append(self.score_dic)

    def from_json(self, filename):
        with open(filename) as f:
            data = json.load(f)
            for i in data:
                new_player = Score(i["player_name"], i["score"], i["date"])
                self.score_list.append(new_player.score_dic)
            return self.score_list

    def to_json(self, file):
        data = json.load(open(file))
        data.append(self.score_dic)
        new_list = sorted(data, reverse=True, key=itemgetter('score'))
        with open(file, 'w') as json_file:
            json.dump(new_list, json_file)

    # def serialize(self):
    #     new_list = sorted(self.score_list, reverse=True, key=itemgetter('score'))
    #     print(new_list)
    #     return new_list

    def print_data(self):
        print(self.score_list)

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


