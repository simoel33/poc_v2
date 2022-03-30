from datetime import datetime

from app import db
from . import experimentation_blueprint
from flask import request
from experimentation.models import Experimentation, experimentations_shema, experimentation_shema, Calorie, \
    calories_shema
from flask import jsonify
from flask_api import status
from patients.models import Patient_DIH


# !DONE! get All experimentation's *V2*
@experimentation_blueprint.route('/', methods=['GET'])
def get_all_experimentations():
    experiementations = Experimentation.query.all()
    exps = experimentations_shema.dump(experiementations)
    return jsonify(exps)


# !DONE!: get experimentation by id *V2*
@experimentation_blueprint.route('/<int:id>', methods=['GET'])
def get_experimentation_by_exp_id(id):
    experience = Experimentation.query.filter_by(id=id).first()
    if experience:
        experimentation = experimentation_shema.dump(experience)
        return jsonify(experimentation), 200
    return jsonify("Experience not exist "), 404

# !DONE!: get all experimentations / Patient :V2:
@experimentation_blueprint.route('/patient/<int:TRC_patient_id>', methods=['GET'])
def get_all_experimentations_for_patient(TRC_patient_id):
    patient = Patient_DIH.query.filter_by(TRC_patient_id=TRC_patient_id).first()
    if patient:
        experimentation = experimentations_shema.dump(patient.experimentations)
        return jsonify(experimentation), 200
    return jsonify("Patient doesn't have anny Experience "), 404


# !ERROR! Can't insert Null i need to set auto increment TRC_patient_id :V2:
# !TODO!: add Experimentation to Patient_DIH :V2:
@experimentation_blueprint.route('/<int:TRC_patient_id>', methods=['POST'])
def add_experimentation(TRC_patient_id):
    patient = Patient_DIH.query.filter_by(TRC_patient_id=TRC_patient_id).first()
    if patient and request.is_json:
        description = request.json['description']
        experience = Experimentation(description=description,
                                     patients=patient,
                                     start_date=None,
                                     end_date=None,)
        db.session.add(experience)
        db.session.commit()
        return jsonify(message="created successfully"), 201
    return jsonify(message="an error was occurred"), 401


# !DONE!: End Experimentation :V2:
@experimentation_blueprint.route('/end/<int:id>', methods=['PUT'])
def end_experimentation(id):
    # ! to stop an experementation just we should chek if end_date has value else we add cuurent date
    experience = Experimentation.query.filter_by(id=id).first()
    if experience:
        if experience.end_date is None:
            experience.end_date = datetime.now()
            db.session.commit()
            return jsonify("Experience Was Stopped !!"), status.HTTP_201_CREATED
        return jsonify("Experience Already Stopped"), status.HTTP_409_CONFLICT
    return jsonify("Experience Not Exist"), status.HTTP_404_NOT_FOUND

# # ? Calories Operations

# TODO: get all from Calories
@experimentation_blueprint.route('/calories', methods=['GET'])
def get_all_calories():
    calories = Calorie.query.all()
    if calories:
        return jsonify(calories_shema.dump(calories)), 200
    return jsonify('NO Caloric Found'), 404
#
# # !DONE!: Add calories
# @experimentation_blueprint.route('/calories/add/<id_experience>', methods=['POST'])
# def add_calorie_to_experimentation(id_experience):
#     experience = Experience.query.filter_by(id_experience=id_experience).first()
#     print(experience)
#     if experience and request.is_json:
#         value = request.json['value']
#         calory = Calory(value=value, experience=experience)
#         db.session.add(calory)
#         db.session.commit()
#         return jsonify(data=f"{value} calories was add successfully"), status.HTTP_201_CREATED
#     return jsonify(data="an error was occurred"), status.HTTP_404_NOT_FOUND
#
#

# # !DONE!: Numbers of Calories :V2:
@experimentation_blueprint.route('/calories/<int:id>', methods=['GET'])
def get_nb_calories_for_experience(id):
    cal = Experimentation.query.filter_by(id=id).first()
    if cal:
        val = 0.0
        for i in cal.calories:
            val = val + float(i.value)
        return jsonify(val), 200
    return jsonify('No calories found for this Experimentation'), 404

# # ? Step Operations

# !DONE!: Numbers of steps
@experimentation_blueprint.route('/steps/<int:experimentation_id>', methods=['GET'])
def get_nb_steps_for_experience(experimentation_id):
    experience = Experimentation.query.filter_by(id=experimentation_id).first()
    if experience:
        val = 0
        for step in experience.steps:
            val = val + int(step.value)
        return jsonify(val), status.HTTP_200_OK
    return jsonify("No records found"), status.HTTP_404_NOT_FOUND


#
# # !DONE!: Add Steps
# @experimentation_blueprint.route('/steps/add/<id_experience>', methods=['POST'])
# def add_steps_to_experimentation(id_experience):
#     experience = Experience.query.filter_by(id_experience=id_experience).first()
#     if experience and request.is_json:
#         value = request.json['value']
#         step = Step(value=value, experience=experience)
#         db.session.add(step)
#         db.session.commit()
#         return jsonify(data="values of steps add successfully"), status.HTTP_201_CREATED
#     return jsonify(data="an error was occurend"), status.HTTP_404_NOT_FOUND
#
#
#
