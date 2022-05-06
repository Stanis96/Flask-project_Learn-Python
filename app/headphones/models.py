from sqlalchemy.orm import relationship

from app.db import db

class Brand(db.Model):
    __tablename__ = 'brands'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Brand {}>'.format(self.name)

class HeadphoneType(db.Model):
    __tablename__ = 'types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return '<HeadphoneType {}>'.format(self.name)

class Color(db.Model):
    __tablename__ = 'colors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Color {}>'.format(self.name)


class AddImage(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String, nullable=False)
    image_path = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<AddImage {}>'.format(self.file_name)

    @property
    def get_image(self):
        img = AddImage.query.get(self.image_id)
        return f'{img.image_path}/{img.file_name}'


class Headphone(db.Model):
    __tablename__ = 'headphones'
    
    id = db.Column(db.Integer, primary_key=True)
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'))
    type_id = db.Column(db.Integer, db.ForeignKey('types.id'))
    color_id = db.Column(db.Integer, db.ForeignKey('colors.id'))
    image_id = db.Column(db.Integer, db.ForeignKey('images.id'))
    model_name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float)
    lifetime = db.Column(db.Integer)
    max_power = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    impedance = db.Column(db.Integer)
    sensitivity = db.Column(db.Integer)
    lifetime_case = db.Column(db.Integer)
    is_nc = db.Column(db.Boolean)
    is_deleted = db.Column(db.Boolean)

    brand = db.relationship('Brand', lazy='joined')
    type = db.relationship('HeadphoneType', lazy='joined')
    color = db.relationship('Color', lazy='joined')
    image = db.relationship('AddImage', lazy='joined')


    def __repr__(self):
        return '<Headphone {}>'.format(self.model_name)


