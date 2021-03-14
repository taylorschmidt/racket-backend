import models
from flask import Blueprint, jsonify, request, session, g
from playhouse.shortcuts import model_to_dict

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