from flask import Flask, escape, request, render_template
from models.game import *

app = Flask(__name__)

@app.route('/')
def solve():
    #g = game(0, 5)
    #g.move_up1(0)
    #g.move_right(1)

    name = request.args.get("name", "World")
    return render_template("game.html", game=move_left(game_state(0, 5), 0))
