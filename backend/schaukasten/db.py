# encoding=utf-8
from sqlalchemy import Column, Integer
import risclog.sqlalchemy.model

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
