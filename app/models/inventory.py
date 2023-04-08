from .db import db, environment, SCHEMA, add_prefix_for_prod

class Inventory(db.Model):
    __tablename__ = 'inventory'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
    date = db.Column(db.Integer, nullable=False, unique=True)
    upc = db.Column(db.String(20), nullable=True, unique=True)
    asin = db.Column(db.String(20), nullable=False, unique=True)
    item_name = db.Column(db.String(255), nullable=False)
    buy_qty = db.Column(db.Integer, nullable=False)
    qty_received = db.Column(db.Integer, nullable=False)
    discrepencies = db.Column(db.Integer, nullable=False)

    user = db.relationship('User', back_populates='item', foreign_keys=[user_id])

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date,

        }
