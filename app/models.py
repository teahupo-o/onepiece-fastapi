from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
    nationality = Column(String(50))
    biography = Column(String(500))
    birthdate = Column(Date)

    mangas = relationship("Manga", back_populates="author")

class Publisher(Base):
    __tablename__ = "publishers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
    country = Column(String(50))

    mangas = relationship("Manga", back_populates="publisher")

class Manga(Base):
    __tablename__ = "mangas"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), unique=True, index=True)
    synopsis = Column(String(500))
    ongoing = Column(Boolean, default=True)

    author_id = Column(Integer, ForeignKey("authors.id"))
    publisher_id = Column(Integer, ForeignKey("publishers.id"))

    author = relationship("Author", back_populates="mangas")
    publisher = relationship("Publisher", back_populates="mangas")
    volumes = relationship("Volume", back_populates="manga")
    arcs = relationship("Arc", back_populates="manga")
    characters = relationship("Character", back_populates="manga")

class Volume(Base):
    __tablename__ = "volumes"
    id = Column(Integer, primary_key=True, index=True)
    manga_id = Column(Integer, ForeignKey("mangas.id"))
    volume_number = Column(Integer)
    title = Column(String(100))
    cover_image = Column(String(200))
    release_date = Column(Date)

    manga = relationship("Manga", back_populates="volumes")
    chapters = relationship("Chapter", back_populates="volume")

class Arc(Base):
    __tablename__ = "arcs"
    id = Column(Integer, primary_key=True, index=True)
    manga_id = Column(Integer, ForeignKey("mangas.id"))
    arc_name = Column(String(100))
    description = Column(String(500))
    start_chapter = Column(Integer)
    end_chapter = Column(Integer)

    manga = relationship("Manga", back_populates="arcs")
    chapters = relationship("Chapter", back_populates="arc")

class Chapter(Base):
    __tablename__ = "chapters"
    id = Column(Integer, primary_key=True, index=True)
    volume_id = Column(Integer, ForeignKey("volumes.id"))
    arc_id = Column(Integer, ForeignKey("arcs.id"))
    chapter_number = Column(Integer)
    title = Column(String(100))
    release_date = Column(Date)

    volume = relationship("Volume", back_populates="chapters")
    arc = relationship("Arc", back_populates="chapters")

class Character(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True, index=True)
    manga_id = Column(Integer, ForeignKey("mangas.id"))
    name = Column(String(100), unique=True, index=True)
    description = Column(String(500))
    role = Column(String(50))
    affiliations = Column(String(200))
    bounty = Column(Integer, nullable=True)
    power_level = Column(Integer, nullable=True)

    manga = relationship("Manga", back_populates="characters")
