from app import db
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import String, Column, Integer
from datetime import datetime

class Flights(db.Model):

    __tablename__ = 'flight_table'
    id = Column(Integer, primary_key=True)
    carrier = Column('carrier', String())
    created_at = Column(String, default=datetime.now().strftime("%Y-%m-%d"))
    date = Column('date', String)
    start = Column('start', String())
    stop = Column('stop', String())
    #śflight_number = Column('flight_number', String())
    start_time = Column('start_time', String())
    stop_time = Column('end_time', String())
    price = Column('price', String())


    def __init__(self, carrier, date, start, stop, start_time, stop_time, price):
        self.carrier = carrier
        self.date = date
        self.start = start
        self.stop = stop
        #self.flight_number = flight_number
        self.start_time = start_time
        self.stop_time = stop_time
        self.price = price


    def __repr__(self):
        return '<id {}>'.format(self.id)