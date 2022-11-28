from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Pocet(Model):
    id = Column(Integer, primary_key=True)
    cislo = Column(Integer, nullable=True)

    def __repr__(self, min=-5.01, max=4.99, message="zadej jine cislo"):
        return self.cislo