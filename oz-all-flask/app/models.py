from .database import db
import pytz
from datetime import datetime


class Participants(db.Model):
    __tablename__ = "participant"
    participant_id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(
        db.DateTime, default=lambda: datetime.now(pytz.timezone("Asia/Seoul"))
    )


class Responses(db.Model):
    response_id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer)  # ForeignKey 제거, 정수 값으로 직접 저장
    answer = db.Column(db.Integer)
    participant_id = db.Column(db.Integer, db.ForeignKey("participant.id"))
    participant = db.relationship("Participant", backref="answers")