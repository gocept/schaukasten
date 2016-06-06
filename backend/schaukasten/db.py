# encoding=utf-8
from sqlalchemy import Column, Integer
from sqlalchemy.types import TypeDecorator, CHAR
from sqlalchemy.dialects.postgresql import UUID
import risclog.sqlalchemy.model
import uuid

ENGINE_NAME = 'schaukasten'


class ObjectBase(risclog.sqlalchemy.model.ObjectBase):

    _engine_name = ENGINE_NAME
    id = Column(Integer, primary_key=True)

    @property
    def identifier(self):
        "Value usable in the `get` method to retrieve the object from the DB."
        return self.id

Object = risclog.sqlalchemy.model.declarative_base(
    ObjectBase, class_registry=risclog.sqlalchemy.model.class_registry)


# according to sqlalchemy documentation
# http://docs.sqlalchemy.org/en/latest/core/custom_types.html#backend-agnostic-guid-type
class GUID(TypeDecorator):
    """Platform-independent GUID type.

    Uses Postgresql's UUID type, otherwise uses
    CHAR(32), storing as stringified hex values.

    """
    impl = CHAR

    def load_dialect_impl(self, dialect):
        if dialect.name == 'postgresql':
            return dialect.type_descriptor(UUID())
        else:
            return dialect.type_descriptor(CHAR(32))

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        elif dialect.name == 'postgresql':
            return str(value)
        else:
            if not isinstance(value, uuid.UUID):
                return "%.32x" % uuid.UUID(value).int
            else:
                # hexstring
                return "%.32x" % value.int

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        else:
            return uuid.UUID(value)
