 from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

db = SQLAlchemy()

class Comment(db.Model):
  __tablename__ = 'comments'
  id = Column(Integer, primary_key=True)
  user = Column(String(50))
  comment = Column(String(120))

  def __init__(self, user, comment):
    self.user = user
    self.comment = comment

  def __repr__(self):
    return '<Comment %r>' % (self.id)
