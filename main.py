from flask import Flask, escape, request, render_template
from models.game import *

app = Flask(__name__)

games = []

@app.route('/')
def menu():
    return render_template("index.html", id=len(games))

@app.route('/game/<int:game_id>', methods=['GET', 'POST'])
def solve(game_id):
    global games
    if request.method == 'POST':
        if request.form.get('size') is not None:
            tmp_size = int(request.form['size'])
            if tmp_size < 3 or tmp_size > 15:
                tmp_size = 3
            games.append(game_state(len(games), tmp_size))
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
    if is_game_solved(games[game_id]):
        return render_template('win.html', moves = games[game_id].moves_count)
    return render_template("game.html", game=games[game_id])
