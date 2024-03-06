from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from db import db
from models import Board

board_blp = Blueprint('Boards','boards',description='Operations on boards', url_prefix="'/board")

@board_blp.route('/')
class BoardList(MethodView):
    def get(self):
        boards = Board.query.all()
        return jsonify([{"user_id":boards.user_id,
                        "id":boards.id,
                        "title":boards.title,
                        "content":boards.content,
                        "author":boards.author.name} for board in boards])
        
    def post(self):
        data = request.json
        new_board = Board(title=data['title'],content=data)