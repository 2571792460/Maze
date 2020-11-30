from flask import Flask, render_template
from models.score_manager import ScoreManager

app = Flask(__name__)

score_manager = ScoreManager()
score_manager.load_from_json()


@app.route('/')
def list_all_products():
    return render_template("player_rank.html", players=score_manager.items)


if __name__ == "__main__":
    app.run(debug=True)
