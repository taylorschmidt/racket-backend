import models
from flask import Blueprint, jsonify, request, session, g
from playhouse.shortcuts import model_to_dict

doubles = Blueprint('doubles', 'doubles')

@doubles.route('/', methods=['POST'])
@login_required
def create_doubles_match():
    payload = request.get_json()
    try:
        payload['person_id'] = current_user.id
        match = models.Doubles.create(**payload)
        match_dict = model_to_dict(match)
        return jsonify(data=match_dict, status={"code": 201, "message":"Successfully created a new doubles match."})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message":"Did not create doubles match."})

@doubles.route('/', methods=['GET'])
@login_required
def get_doubles_matches():
    try:
        matches = [model_to_dict(doubles) for doubles in models.Doubles.select()\
                .join_from(models.Doubles, models.Person)\
                .where(models.Person.id==current_user.id)]
        return jsonify(data=matches, status={"code": 200, "message": "Successfully pulled all doubles matches for this user."})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message":"Error getting the doubles matches."})