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
def list_ranking(session):
    return session.query(Cider).filter(Cider.name == 'Sommersby').all()
