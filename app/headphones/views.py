from flask import Blueprint, render_template, flash, redirect, url_for

from app.db import db
from app.users.decorators import admin_required
from app.headphones.models import Brand, HeadphoneType, Color, AddImage, Headphone
from app.headphones.forms import AddHeadphoneForm
from app.headphones.models import Headphone

blueprint = Blueprint('headphone', __name__, url_prefix='/')

@blueprint.route('/add_hp', methods=['GET', 'POST'])
@admin_required
def add_headphones():
    form = AddHeadphoneForm()
    form.brand_id.choices = [(brand.id, brand.name) for brand in Brand.query.order_by(Brand.name).all()]
    form.type_id.choices = [(type.id, type.name) for type in HeadphoneType.query.order_by(HeadphoneType.name).all()]
    form.color_id.choices = [(color.id, color.name) for color in Color.query.order_by(Color.name).all()]
    form.image_id.choices = [(image.id, image.file_name) for image in AddImage.query.order_by(AddImage.file_name).all()]
    if form.validate_on_submit():
        headphones = Headphone(
                    brand_id=form.brand_id.data,
                    type_id=form.type_id.data,
                    color_id=form.color_id.data,
                    image_id=form.image_id.data,
                    model_name=form.model_name.data,
                    price=form.price.data,
                    lifetime=form.lifetime.data,
                    max_power=form.max_power.data,
                    weight=form.weight.data,
                    impedance=form.impedance.data,
                    sensitivity=form.sensitivity.data,
                    lifetime_case=form.lifetime_case.data,
                    is_nc=form.is_nc.data,
                    is_deleted=form.is_deleted.data)                   
        db.session.add(headphones)
        db.session.commit()
        flash('Success! This headphone has been added!')
        return redirect(url_for('headphone.add_headphones'))
    return render_template('add_hp.html', title='Add headphones', form=form)
