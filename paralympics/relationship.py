from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from paralympics import db


# non-Key/relations`hip column details have been omitted from the classes below for brevity
# one-to-many relationship from Region to Event 
# https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#one-to-many

class Region(db.Model):
    __tablename__ = "region"
    # Primary key attribute
    NOC: Mapped[str] = mapped_column(db.Text, primary_key=True)
    # Add a relationship to Event. The Region then has a record of the Events associated with it. 
    # This references the relationship 'region' in the Event table.
    events: Mapped[List["Event"]] = relationship(back_populates="region")


class Event(db.Model):
    __tablename__ = "event"
    # add ForeignKey that maps to the primary key of the Region table
    NOC: Mapped[str] = mapped_column(ForeignKey("region.NOC"))
    # add relationship to Region, this references the relationship 'events' that is in the Region table
    region: Mapped["Region"] = relationship(back_populates="events")