import uuid

from flask import jsonify, request

from app import db
from patients import patient_blueprint
from patients.models import Patient_DIH, pats_dih_schema, pat_dih_schema
from flask_api import status


# Version 2:
# !DONE!: get all patients_dih  from New Base
@patient_blueprint.route('/', methods=['GET'])
def get_pat_dih():
    pat = Patient_DIH.query.all()
    return jsonify(pats_dih_schema.dump(pat))


#  !DONE!:  get patient by TRC_patient_id New Base
@patient_blueprint.route('/<int:TRC_patient_id>', methods=['GET'])
def get_patient_by_trct_id(TRC_patient_id):
    patient = Patient_DIH.query.filter_by(TRC_patient_id=TRC_patient_id).first()
    if patient:
        pat = pat_dih_schema.dump(patient)
        return jsonify(pat), status.HTTP_200_OK
    return jsonify("patients doesn't exist"), status.HTTP_404_NOT_FOUND


# Version 1:

# !DONE!: get All patients
# @patient_blueprint.route('/', methods=['GET'])
# def get_all_patients():
#     patients = patients_schema.dump(Patient.query.all())
#     return jsonify(patients)


# !DONE!: add new patient
@patient_blueprint.route('/', methods=['POST'])
def add_patient():
    if request.is_json:
        UID = "generated"
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        phone_number = request.json['phone_number']
        treatment_id = 3
        rendered_treatment_id = 2
        patient = Patient_DIH(
            UID=UID,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            treatment_id=treatment_id,
            rendered_treatment_id=rendered_treatment_id

        )
        db.session.add(patient)
        db.session.commit()
        return jsonify(response='patient created '), status.HTTP_201_CREATED
    return jsonify(message='an error was occurred patient Not saved'), status.HTTP_400_BAD_REQUEST
