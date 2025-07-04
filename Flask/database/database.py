import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey, FLOAT
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

engine = create_engine('sqlite:///Flask/data/users_info.db')
Base = declarative_base()

class User(Base, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    number = Column(String, index=True, unique=True)
    hashed_password = Column(String, nullable=True)
    created_date = Column(DateTime, default=datetime.datetime.now().date())
    premium = Column(Integer, default=0)
    tasks_amount = Column(Integer, default=0)

    bike = Column(Boolean, default=False)
    swimming = Column(Boolean, default=False)

    tasks = relationship("Tasks", back_populates='user')
    statics = relationship("Statics", back_populates="user")
    premiums = relationship("Premium", back_populates="user")

    def __repr__(self):
        return f'Id: {self.id}; Name: {self.name}; Number: {self.number}; Premium: {self.premium}'

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)


class Tasks(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    task1 = Column(Boolean, default=False)
    text1 = Column(String)
    task2 = Column(Boolean, default=False)
    text2 = Column(String)
    task3 = Column(Boolean, default=False)
    text3 = Column(String)
    date = Column(String, default=datetime.datetime.now().date().strftime("%Y-%m-%d"))

    user = relationship('User')

    def __repr__(self):
        return f'Id: {self.id}; User_id: {self.user_id}; task1: {self.task1}; task2: {self.task2}; task3: {self.task3}'


class Statics(Base):
    __tablename__ = 'statics'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    kilometres = Column(FLOAT, default=0.0)
    kilometre_bicycle = Column(FLOAT, default=0.0)
    kilometre_swimming = Column(FLOAT, default=0.0)

    push_up = Column(Integer, default=0)
    pull_up = Column(Integer, default=0)
    press = Column(Integer, default=0)
    squats = Column(Integer, default=0)

    user = relationship('User', back_populates='statics')

    def __repr__(self):
        return f"user_id: {self.user_id}; address={self.kilometeers})>"


class Premium(Base):
    __tablename__ = 'premium'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    text = Column(String, nullable=True)
    user = relationship('User')
    date = Column(DateTime, default=datetime.datetime.now().date()  )

    def __repr__(self):
        return f"user_id: {self.user_id}; text={self.text}; date={self.date}"


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
