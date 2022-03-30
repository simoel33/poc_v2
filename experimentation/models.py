import datetime

from app import db, ma
from marshmallow import fields


########################## Experimentation Model With Mapper ##############################
# Model
class Experimentation(db.Model):
    __tablename__ = 'Experimentation'

    id = db.Column(db.Integer(), primary_key=True)
    TRC_patient_id = db.Column(db.Integer(), db.ForeignKey('Patient_DIH.TRC_patient_id'))
    start_date = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    end_date = db.Column(db.DateTime(), default=None)
    description = db.Column(db.String)
    patients = db.relationship('Patient_DIH', backref='experimentations')


# Mapper
class ExperimentationShema(ma.Schema):
    id = fields.Field()
    TRC_patient_id = fields.Field()
    start_date = fields.Field()
    end_date = fields.Field()
    description = fields.String()


experimentation_shema = ExperimentationShema()
experimentations_shema = ExperimentationShema(many=True)


########################## End Experimentation Model With Mapper ##############################


########################## Start Calory Models With Mappers ##############################

class Calorie(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    experimentation_id = db.Column(db.Integer(), db.ForeignKey('Experimentation.id'))
    value = db.Column(db.Float())
    start_measured_date = db.Column(db.Date())
    start_measured_time = db.Column(db.String())
    end_measured_date = db.Column(db.Date())
    end_measured_time = db.Column(db.String())
    created_date = db.Column(db.Date())
    created_date = db.Column(db.String())
    experience = db.relationship('Experimentation', backref='calories')


class CalorieShema(ma.Schema):
    id = fields.Integer()
    experimentation_id = fields.Integer()
    value = fields.Float()
    start_measured_date = fields.Field()
    # start_measured_time = fields.DateTime()
    end_measured_date = fields.Field()
    # end_measured_time = fields.Field()
    created_date = fields.Field()

calorie_shema = CalorieShema()
calories_shema = CalorieShema(many=True)

########################## END Calory Model With Mapper ##############################


########################## Start Step Model With Mapper ##############################

class Step(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    experimentation_id = db.Column(db.Integer(), db.ForeignKey('Experimentation.id'))
    value = db.Column(db.Float())
    start_measured_date = db.Column(db.Date())
    start_measured_time = db.Column(db.String())
    end_measured_date = db.Column(db.Date())
    end_measured_time = db.Column(db.String())
    created_date = db.Column(db.Date())
    created_date = db.Column(db.String())
    experience = db.relationship('Experimentation', backref='steps')


# class Experience(db.Model):
#     __tablename__ = 'experience'
#
#     id_experience: int
#     trc_patient_id: int
#     start_date: datetime
#     end_date: datetime
#     description = str
#
#     id_experience = db.Column(db.Integer(), primary_key=True)
#     # belongs to Patient
#     trc_patient_id = db.Column(db.Integer(), db.ForeignKey('patient.trc_patient_id'))
#     start_date = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
#     end_date = db.Column(db.DateTime(), default=None)
#     description = db.Column(db.String)
#     patient = db.relationship('Patient', backref='experiences')
#     #calories = db.relationship('Calory', backref='experiences', lazy='joined')
#     # steps = db.relationship('Step', backref='experiences', lazy='joined')


# * : Experience Schema definition based on Marshmallow to serialize object

#
# class ExperienceSchema(ma.Schema):
#     id_experience = fields.Field()
#     trc_patient_id = fields.Field()
#     start_date = fields.DateTime()
#     end_date = fields.DateTime()
#     description = fields.String()
#
#     # class Meta:
#     # fields = ('id_experience', 'trc_patient_id', 'start_date', 'end_date', 'description')
#
#
# experience_schema = ExperienceSchema()
# experiences_schema = ExperienceSchema(many=True)

#
# class Calory(db.Model):
#     __tablename__ = 'calory'
#
#     id = db.Column(db.Integer, primary_key=True)
#     id_experience = db.Column(db.Integer, db.ForeignKey('experience.id_experience'))
#     value = db.Column(db.Float)
#     start_mesured_datetime = db.Column(db.DateTime(), default=datetime.datetime.utcnow())
#     end_mesured_datetime = db.Column(db.DateTime(), default=None)
#     created_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow())
#     end_at = db.Column(db.DateTime(), default=None)
#     experience = db.relationship('Experience', backref='calories', lazy='joined')
#
#
# class CaloryShema(ma.Schema):
#     id = fields.Field()
#     id_id_experience = fields.Field()
#     value = fields.Float()
#     start_mesured_datetime = fields.DateTime()
#     created_at = fields.DateTime()
#     end_at = fields.DateTime()
#
#
# calory_shema = CaloryShema()
# calories_shema = CaloryShema(many=True)
#
#
# class Step(db.Model):
#     __tablename__ = 'step'
#
#     id = db.Column(db.Integer, primary_key=True)
#     id_experience = db.Column(db.Integer, db.ForeignKey('experience.id_experience'))
#     value = db.Column(db.Integer)
#     start_mesured_datetime = db.Column(db.DateTime(), default=datetime.datetime.utcnow())
#     end_mesured_datetime = db.Column(db.DateTime(), default=None)
#     created_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow())
#     end_at = db.Column(db.DateTime(), default=None)
#     experience = db.relationship('Experience', backref='steps', lazy='joined')
#
# class StepShema(ma.Schema):
#     id = fields.Field()
#     id_id_experience = fields.Field()
#     value = fields.Float()
#     start_mesured_datetime = fields.DateTime()
#     created_at = fields.DateTime()
#     end_at = fields.DateTime()
#
#
# step_shema = StepShema()
# steps_shema = StepShema(many=True)
