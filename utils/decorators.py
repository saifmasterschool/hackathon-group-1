from functools import wraps

from database.extension import Session


def with_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        session = Session()

        try:
            result = func(session, *args, **kwargs)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    return wrapper
