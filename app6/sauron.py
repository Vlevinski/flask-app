from app6 import db
from datetime import datetime


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return '<Post %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.name


class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    currency_name = db.Column(db.String(3), nullable=False)
    value = db.Column(db.Float)

    def __repr__(self):
        return '<Cur %r>' % self.currency_name

class TransferFrom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    bank = db.Column(db.String(40))
    currency = db.Column(db.String(40))
    bank_address = db.Column(db.String(100))
    notes = db.Column(db.String(100))

    def __repr__(self):
        return '<Trsf %r>' % self.name

class Trustee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trust_name = db.Column(db.String(40),  nullable=False)
    trustee_name = db.Column(db.String(40))
    type = db.Column(db.String(40))
    address = db.Column(db.String(100))
    tax_id = db.Column(db.String(40))
    base_currency = db.Column(db.String(40))
    phone = db.Column(db.String(40))
    email = db.Column(db.String(40))
    website = db.Column(db.String(40))
    notes = db.Column(db.String(100))

    def __repr__(self):
        return '<Trustee %r>' % self.trust_name

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    type = db.Column(db.String)
    trustee = db.Column(db.String)
    address = db.Column(db.String)
    tax_id = db.Column(db.String)
    base_currency = db.Column(db.String)
    phone = db.Column(db.String)
    email = db.Column(db.String)
    website = db.Column(db.String)
    notes = db.Column(db.String)

    def __repr__(self):
        return '<Vhcl %r>' % self.name


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String)
    address = db.Column(db.String)
    tax_id = db.Column(db.String)
    base_currency = db.Column(db.String)
    phone = db.Column(db.String)
    email = db.Column(db.String)
    website = db.Column(db.String)
    notes = db.Column(db.String)

    def __repr__(self):
        return '<Company %r>' % self.company_name


class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    company = db.relationship('Company', backref=db.backref('transactions', lazy=True))
    transaction_type = db.Column(db.String)
    #purchase_id = db.Column(db.Integer, db.ForeignKey('transactions.id'))
    #purchase = db.relationship('Transactions', backref=db.backref('purchases', lazy=True))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))
    vehicle = db.relationship('Vehicle', backref=db.backref('vechicles', lazy=True))
    currency_id = db.Column(db.Integer, db.ForeignKey('currency.id'))
    currency = db.relationship('Currency', backref=db.backref('currencies', lazy=True))
    unit_price = db.Column(db.Float)
    costs = db.Column(db.Float)
    units = db.Column(db.Integer)
    paid_with = db.Column(db.String)
    transfer_from = db.Column(db.Integer)
    transfer_date = db.Column(db.String)
    label = db.Column(db.String)
    notes = db.Column(db.String)

    def __repr__(self):
        return '<Transaction %r>' % self.transaction_type

class Investments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transactions_id = db.Column(db.Integer, db.ForeignKey('transactions.id'))
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    transaction_type_id = db.Column(db.Integer, db.ForeignKey('transfer_from.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))
    currency_id = db.Column(db.Integer, db.ForeignKey('currency.id'))
    purchase_date = db.Column(db.String)
    currency_price = db.Column(db.Float)
    aud_price = db.Column(db.Float)
    brokerage_price = db.Column(db.Float)
    full_costs = db.Column(db.Float)
    shares = db.Column(db.Float)
    currency_cost = db.Column(db.Float)
    aud_cost = db.Column(db.Float)

    def __repr__(self):
        return '<Cur %r>' % self.id

class Summary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    investments_id = db.Column(db.Integer, db.ForeignKey('investments.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))
    currency_id = db.Column(db.Integer, db.ForeignKey('currency.id'))
    first_purchase_date = db.Column(db.String)
    current_share_price = db.Column(db.Float)
    shares = db.Column(db.Float)
    weighted_cost_per_share = db.Column(db.Float)
    total_cost = db.Column(db.Float)
    current_asset_value = db.Column(db.Float)

    def __repr__(self):
        return '<Summary %r>' % self.id

class Settings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    my_name = db.Column(db.String)
    my_location = db.Column(db.String)
    my_language = db.Column(db.String)
    my_timezone = db.Column(db.String)
    my_currency = db.Column(db.String)
    my_email = db.Column(db.String)

    def __repr__(self):
        return '<Settings %r>' % self.my_name
