import models
from flask import Blueprint, jsonify, request, session, g
from playhouse.shortcuts import model_to_dict
from flask_login import login_user, logout_user, current_user, login_required

singles = Blueprint('singles', 'singles')

@singles.route('/', methods=['POST'])
@login_required
def create_singles_match():
    payload = request.get_json()
    try:
        payload['person_id'] = current_user.id
        match = models.Singles.create(**payload)
        match_dict = model_to_dict(match)
        return jsonify(data=match_dict, status={"code": 201, "message":"Successfully created a new singles match."})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message":"Did not create singles match."})

@singles.route('/', methods=['GET'])
@login_required
def get_singles_matches():
    try:
        matches = [model_to_dict(singles) for singles in models.Singles.select()\
                .join_from(models.Singles, models.Person)\
                .where(models.Person.id==current_user.id)]
        return jsonify(data=matches, status={"code": 200, "message": "Successfully pulled all signals matches for this user."})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message":"Error getting the singles matches."})

@singles.route('/<singles_id>', methods=["PUT"])
@login_required
def update_singles_match(singles_id):
    try:
        payload = request.get_json()
        query = models.Singles.update(**payload)\
                .where(models.Singles.id==singles_id)
        query.execute()
        updated_match = model_to_dict(models.Singles.get_by_id(singles_id))
        return jsonify(data=updated_match, status={"code": 200, "message": "Successfully updated the singles match."})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 404,\
                                        "message": "Error getting the singles match."})


@singles.route('/<singles_id>', methods=["DELETE"])
@login_required
def delete_singles_match(singles_id):
    try:
        delete_match = models.Singles.get_by_id(singles_id)
        delete_match.delete_instance()
        return jsonify(data={}, status={"code": 200, "message": "Singles match successfully deleted"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 404,\
                                        "message": "Singles match does not exist"})