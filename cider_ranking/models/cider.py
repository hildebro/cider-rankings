from sqlalchemy import Column, String, Integer

from ..db import base


class Cider(base):
    __tablename__ = 'cider'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    sweetness_level = Column(Integer)
    natural_level = Column(Integer)
    score = Column(Integer)

    def __init__(self, name, sweetness_level, natural_level, score):
        self.name = name
        self.sweetness_level = sweetness_level
        self.natural_level = natural_level
        self.score = score

    def __str__(self):
        return f'name: {self.name}, sweetness_level: {self.sweetness_level}, natural_level: {self.natural_level}, ' \
               f'score: {self.score} '
