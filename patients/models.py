import datetime
from dataclasses import dataclass

from app import db, ma
from marshmallow import fields


# ? patient Model

class Patient_DIH(db.Model):
    __tablename__ = 'Patient_DIH'

    TRC_patient_id: int
    treatment_id: int
    rendered_treatment_id: int
    first_name: str
    last_name: str

    TRC_patient_id = db.Column(db.Integer, primary_key=True)
    treatment_id = db.Column(db.Integer())
    rendered_treatment_id = db.Column(db.Integer())
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    phone_number = db.Column(db.String())
    UID = db.Column(db.String())


class Patient_Dih_Schema(ma.Schema):
        TRC_patient_id = fields.Field()
        treatment_id = fields.Field()
        rendered_treatment_id = fields.UUID()
        first_name = fields.String()
        last_name = fields.String()
        phone_number = fields.String()
        UID = fields.String()


pat_dih_schema = Patient_Dih_Schema()
pats_dih_schema = Patient_Dih_Schema(many=True)


# @dataclass
# class Patient(db.Model):
#     __tablename = 'patient'
#     # ! definition of patient fields
#
#     trc_patient_id = db.Column(db.Integer, primary_key=True)  # ? primary key
#     # ! identifier of user he will be generated automatically in route before storage in database
#     uid_patient = db.Column(db.String, unique=True)
#     first_name = db.Column(db.String)
#     last_name = db.Column(db.String)
#     phone_number = db.Column(db.String)
#     # has a
#     experience = db.relationship('Experience', backref='patients', lazy='joined')
#
# # * : Experience Schema definition based on Marshmallow to serialize object
# class PatientSchema(ma.Schema):
#     trc_patient_id = fields.Field()
#     uid_patient = fields.Field()
#     uid_patient = fields.UUID()
#     first_name = fields.String()
#     last_name = fields.String()
#     phone_number = fields.String()
#     # https://marshmallow.readthedocs.io/en/stable/nesting.html
#     # experience = fields.List(fields.Nested(ExperienceSchema()))
#     # we can use this methode if we don't have relationship
#     #class Meta:
#         #fields = ('trc_patient_id', 'uid_patient', 'first_name', 'last_name', 'phone_number')
#
#
# patient_schema = PatientSchema()
# patients_schema = PatientSchema(many=True)
# #
# class Experience(db.Model):
#     __tablename__ = 'experience'
#
#     id_experience = db.Column(db.Integer(), primary_key=True)
#     trc_patient_id = db.Column(db.Integer(), db.ForeignKey('patient.trc_patient_id'))
#     start_date = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
#     end_date = db.Column(db.DateTime(), nullable=True)
#     description = db.Column(db.String)
#     patient = db.relationship('Patient', backref='experiences')
#
#
# class Calory(db.Model):
#     __tablename__ = 'calory'
#
#     id = db.Column(db.Integer, primary_key=True)
#     id_experience = db.Column(db.Integer, db.ForeignKey('experience.id_experience'))
#     value = db.Column(db.Float)
#     start_mesured_datetime = db.Column(db.DateTime())
#     end_mesured_datetime = db.Column(db.DateTime())
#     created_at = db.Column(db.DateTime())
#     end_at = db.Column(db.DateTime())
#     experience = db.relationship('Experience', backref='calorys')
#
#
# class Step(db.Model):
#     __tablename__ = 'step'
#
#     id = db.Column(db.Integer, primary_key=True)
#     id_experience = db.Column(db.Integer, db.ForeignKey('experience.id_experience'))
#     value = db.Column(db.Integer)
#     start_mesured_datetime = db.Column(db.DateTime())
#     end_mesured_datetime = db.Column(db.DateTime())
#     created_at = db.Column(db.DateTime())
#     end_at = db.Column(db.DateTime())
#     experience = db.relationship('Experience', backref='steps')
#
#
#
#
#
#
#
#
