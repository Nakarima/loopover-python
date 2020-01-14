from flask import Flask, escape, request, render_template
from models.game import *

app = Flask(__name__)

@app.route('/')
def solve():
    g = game(0, 5)
    g.move_left(0)
    g.move_right(1)

    name = request.args.get("name", "World")
    return render_template("game.html", game=g)