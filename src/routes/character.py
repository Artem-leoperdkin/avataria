from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from app import db

from models.character import Character


character = Blueprint('character', __name__)

@character.route('/character/create', methods=['GET'])
@login_required
def create():
    return render_template("character/create.html")

@character.route('/character/store', methods=['POST'])
@login_required
def store():
    data = request.get_json()
    hat = data.get('hat')
    shirt = data.get('shirt')
    pants = data.get('pants')
    shoes = data.get('shoes')
    character = Character(user_id=current_user.id, hat=hat, shirt=shirt, pants=pants, shoes=shoes)
    db.session.add(character)
    db.session.commit()
    return redirect(url_for('character.all'))


@character.route("/characters", methods=['GET'])
@login_required
def all():
    characters = Character.query.filter_by(user_id=current_user.id).all()
    return render_template('character/all_characters.html', characters=characters)


@character.route('/character/<int:id>/edit', methods=['GET'])
@login_required
def edit(id):
    character = Character.query.get_or_404(id)
    return render_template("character/edit.html", character=character)


@character.route('/character/<int:id>/update', methods=['POST'])
@login_required
def update(id):
    character = Character.query.get_or_404(id)
    data = request.get_json()
    character.hat = data.get('hat')
    character.shirt = data.get('shirt')
    character.pants = data.get('pants')
    character.shoes = data.get('shoes')
    db.session.commit()
    return "Персонаж обновлен"


@character.route('/character/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
    character = Character.query.get_or_404(id)
    db.session.delete(character)
    db.session.commit()
    
    return redirect(url_for("character.all"))
    
    




