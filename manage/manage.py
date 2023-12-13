from sqlalchemy import Integer, String, ForeignKey, Column, Boolean, DateTime, Text

from sqlalchemy.orm import declarative_base, relationship, backref

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    full_name = Column(String(50), nullable=False)
    email = Column(String(70), nullable=False)

    hashed_password = Column(String(length=1024), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)


class Categories(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    category_name = Column(String(50), nullable=False)


class Articles(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey('user.id'))
    article_name = Column(String(70), nullable=False)
    article_text = Column(Text)

    categories = relationship('Categories', secondary='categories_articles',
                              backref=backref('articles', lazy='dynamic'))


class Categories_Articles(Base):
    __tablename__ = 'categories_articles'

    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    article = Column(Integer, ForeignKey('articles.id'))


class Comments(Base):
    __tablename__ = 'comments'
    # metadata = metadata_obj
    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey('user.id'))
    article = Column(Integer, ForeignKey('articles.id'))


class Liked_Articles(Base):
    __tablename__ = 'liked_articles'

    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey('user.id'))
    article = Column(Integer, ForeignKey('articles.id'))
