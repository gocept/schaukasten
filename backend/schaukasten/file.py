from schaukasten.db import Object, GUID
from sqlalchemy import Column, Integer, String, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship, backref
import hashlib
import mimetypes
import uuid


class File(Object):
    """Represents the central entity of the voting process."""

    id = Column(GUID(), primary_key=True)
    filename = Column(String(255), nullable=False)
    mimetype = Column(String(100), nullable=False)
    content_id = Column(
        Integer(), ForeignKey('content.id', ondelete='cascade'))
    content = relationship('Content', backref=backref("file", uselist=False))

    def __init__(self, **kw):
        self.id = uuid.uuid4()
        self.mimetype = mimetypes.guess_type(kw['filename'])
        super().__init__(**kw)


class Content(Object):
    """Represents the actual content of a File."""

    id = Column(Integer(), primary_key=True)
    hash = Column(GUID(), nullable=False)
    raw_content = Column(LargeBinary())

    def __init__(self, raw_content, **kw):
        m = hashlib.md5()
        try:
            m.update(raw_content)
        except TypeError:
            raw_content = bytes(raw_content, 'utf-8')
            m.update(raw_content)
        self.hash = uuid.UUID(m.hexdigest())
        self.raw_content = raw_content
        super().__init__(**kw)
