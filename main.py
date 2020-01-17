from flask import Flask, escape, request, render_template
from models.game import *

app = Flask(__name__)

g = game_state(0,5)

@app.route('/')
def solve():
    global g
    g = move_left(g, 0)
    print(is_game_solved(g))
    name = request.args.get("name", "World")
    return render_template("game.html", game=g)
