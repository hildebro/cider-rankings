from cider_ranking.db import session_wrapper
from cider_ranking.models import Cider
from .db import base, engine


def init_db():
    base.metadata.create_all(engine)


@session_wrapper
def add_ranking(session, name, sweetness_level, natural_level, score):
    cider = Cider(name, sweetness_level, natural_level, score)
    session.add(cider)
    session.commit()


@session_wrapper
def has_ranking(session, name):
    result = session.query(Cider).filter(Cider.name == name).all()
    return len(result) > 0


@session_wrapper
def get_all(session):
    return session.query(Cider).all()
