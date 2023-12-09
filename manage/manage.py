from sqlalchemy import MetaData, Integer, String, ForeignKey, Column, Boolean, DateTime, Text

from datetime import datetime

from sqlalchemy.orm import declarative_base, relationship, backref


Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    full_name = Column(String(50), nullable=False)
    email = Column(String(70), nullable=False)
    password = Column(String(50), nullable=False)
    admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow())


class Categories(Base):
    __tablename__ = 'categories'
    # metadata = metadata_obj
    id = Column(Integer, primary_key=True)
    category_name = Column(String(50), nullable=False)


class Articles(Base):
    __tablename__ = 'articles'
    # metadata = metadata_obj
    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey('users.id'))
    article_name = Column(String(70), nullable=False)
    article_text = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow())
    categories = relationship('Categories', secondary='categories_articles', backref=backref('articles', lazy='dynamic'))


class Categories_Articles(Base):
    __tablename__ = 'categories_articles'
    # metadata = metadata_obj
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    article = Column(Integer, ForeignKey('articles.id'))


class Comments(Base):
    __tablename__ = 'comments'
    # metadata = metadata_obj
    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey('users.id'))
    article = Column(Integer, ForeignKey('articles.id'))
    created_at = Column(DateTime, default=datetime.utcnow())


class Liked_Articles(Base):
    __tablename__ = 'liked_articles'
    # metadata = metadata_obj,
    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey('users.id'))
    article = Column(Integer, ForeignKey('articles.id'))
    created_at = Column(DateTime, default=datetime.utcnow())


