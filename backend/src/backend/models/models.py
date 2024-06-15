import datetime
from typing import List

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from flask_sqlalchemy import SQLAlchemy


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


# Supplier, 
#     Reliable gutter material suppliers. Will be used to:
#         - Plan material pickup/delivery routes
#         - Track material pricing via web scraping through url
class Supplier(Base):
    __tablename__ = "suppliers"

    id: Mapped[int] = mapped_column(primary_key=True)
    supplier: Mapped[str] = mapped_column(String(120), unique=True)
    street: Mapped[str] = mapped_column(String(200))
    street_2: Mapped[str] = mapped_column(String(200), nullable=True)
    city: Mapped[str] = mapped_column(String(120))
    state: Mapped[str] = mapped_column(String(20))
    zip: Mapped[str] = mapped_column(String(20))
    website_url: Mapped[str] = mapped_column(String(500), nullable=True)


# ColorOption 
    # Have the color, and a FK to a Supplier obj. 
class ColorOption(Base):
    __tablename__ = "color_options"

    id: Mapped[int] = mapped_column(primary_key=True)
    color: Mapped[str] = mapped_column(String(80), nullable=False)
    supplier_id: Mapped[int] = mapped_column(ForeignKey("suppliers.id"), nullable=False)

    coil_options: Mapped[List["CoilOption"]] = relationship(back_populates="color")
    accessories: Mapped[List["Accessory"]] = relationship(back_populates="color")

    def __repr__(self) -> str:
        return self.color


# CoilOption, 
#     takes a supplier FK to later pack into GutterCoil obj for where you can get 
#     a specific gutter coil profile. 
#         Ex: Round, 5" Square, 5" K-Style
class CoilOption(Base):
    __tablename__ = "coil_options"

    id: Mapped[int] = mapped_column(primary_key=True)
    style: Mapped[str] = mapped_column(String(100))
    size: Mapped[str] = mapped_column(String(100))
    color_id: Mapped[int] = mapped_column(ForeignKey("color_options.id"))

    color: Mapped["ColorOption"] = relationship(back_populates="coil_options")
    accessories: Mapped[List["Accessory"]] = relationship(back_populates="coil")

    def __repr__(self) -> str:
        return "{}-{}".format(self.size, self.profile)



class Accessory(Base):
    __tablename__ = "accessories"

    id: Mapped[int] = mapped_column(primary_key=True)
    color_id: Mapped[int] = mapped_column(ForeignKey("color_options.id"))
    coil_id: Mapped[int] = mapped_column(ForeignKey('coil_options.id'))
    accessory: Mapped[str] = mapped_column(String)
    
    color: Mapped["ColorOption"] = relationship(back_populates="accessories")
    coil: Mapped["CoilOption"] = relationship(back_populates="accessories")

    def __repr__(self) -> str:
        return self.accessory




class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)




class Cart(Base):
    __tablename__ = "carts"

    id: Mapped[int] = mapped_column(primary_key=True)




class CartItem(Base):
    __tablename__ = "cart_items"

    id: Mapped[int] = mapped_column(primary_key=True)




class ContactRequest(Base): 
    __tablename__ = "contact_requests"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=func.now())
    deleted_at: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True) 
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    phone: Mapped[str] = mapped_column(String(10), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=True)
    messsage: Mapped[str] = mapped_column(String(666), nullable=True)    
    

    def __repr__(self) -> str: 
        return "{} / {}-{}-{} / {}".format(self.name, self.phone[0:3], self.phone[3:6], self.phone[6:], self.email)

