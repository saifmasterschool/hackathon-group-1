from config import AVAILABLE_CHANNELS
from database.extension import Session
from schemas import Channel


def init_database():
    session = Session()

    # Guard-clause
    if len(session.query(Channel).all()) > 0:
        return

    for channel in AVAILABLE_CHANNELS:
        session.add(
            Channel(channel_name=channel)
        )
    session.commit()
    session.close()
