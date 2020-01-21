from flask import Flask, escape, request, render_template
from models.game import *

app = Flask(__name__)

games = []

@app.route('/')
def menu():
    global games
    games.append(game_state(len(games), 5))
    return render_template("index.html")

@app.route('/game/<int:game_id>', methods=['GET', 'POST'])
def solve(game_id):
    global games
    if is_game_solved(games[game_id]):
        return redirect('/win', moves = games[game_id].moves_count)
    if request.method == 'POST':
        tmp = games[game_id]
        if request.form.get('up'):
            tmp = move_up(tmp, int(request.form['up']))
        elif request.form.get('down') is not None:
            tmp = move_down(tmp, int(request.form['down']))
        elif request.form.get('left') is not None:
            tmp = move_left(tmp, int(request.form['left']))
        elif request.form.get('right') is not None:
            tmp = move_right(tmp, int(request.form['right']))
        games[game_id] = tmp
    return render_template("game.html", game=games[game_id])
