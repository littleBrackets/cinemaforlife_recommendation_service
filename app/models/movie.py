from sqlalchemy import Column, String, Integer, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TitleBasics(Base):
    __tablename__ = "title_basics"
    tconst = Column(String, primary_key=True)
    titletype = Column(String)       # lowercase column names match DB
    primarytitle = Column(String)
    originaltitle = Column(String)
    isadult = Column(Boolean)
    startyear = Column(Integer)
    endyear = Column(Integer)
    runtimeminutes = Column(Integer)
    genres = Column(String)

class TitleRatings(Base):
    __tablename__ = "title_ratings"
    tconst = Column(String, primary_key=True, index=True)
    averagerating = Column(Float)
    numvotes = Column(Integer)
