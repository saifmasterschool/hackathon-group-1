from database.extension import Base
from utils.to_dict_mixin_schema import ToDictMixin


class BaseClass(Base, ToDictMixin):
    """
        Custom Parent-class to extend from, easily extendable, especially useful
        for scalability. Inherits to_dict functionality.
        """
    __abstract__ = True
