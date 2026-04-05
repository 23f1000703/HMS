from controllers.database import db
from flask_security import UserMixin,RoleMixin
from datetime import datetime

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(100),unique = True,nullable = False)
    password = db.Column(db.String(255),nullable = False)
    active = db.Column(db.Boolean,default = True)
    fs_uniquifier = db.Column(db.String(255),nullable=False,unique =True )
    fs_token_uniquifier = db.Column(db.String(255),nullable =False,unique =True)

    roles = db.relationship("Role",secondary='user_role')

class Role(db.Model,RoleMixin):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    description = db.Column(db.String(255))

class UserRole(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    role_id = db.Column(db.Integer,db.ForeignKey('role.id'))

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    name= db.Column(db.String(250),nullable =False)
    specialization = db.Column(db.String(150),nullable = False)
    experience_years = db.Column(db.Integer,nullable = False)

    user = db.relationship('User', backref='doctor_profile')

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(250),nullable = False)
    dob = db.Column(db.DateTime,nullable =False)

    phone_no = db.Column(db.String(15),nullable = False)
    gender = db.Column(db.String(20),nullable = False)
    blood_group = db.Column(db.String(10))
    address = db.Column(db.Text,nullable = False)

    user = db.relationship('User', backref='patient_profile')

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)

    appointment_date = db.Column(db.Date)
    appointment_time = db.Column(db.Time)

    status = db.Column(db.String(20), default="Pending")
    # Pending / Approved / Completed / Cancelled

    doctor = db.relationship('Doctor', backref='appointments')
    patient = db.relationship('Patient', backref='appointments')

class MedicalRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    appointment_id = db.Column(db.Integer, db.ForeignKey('appointment.id'))
    diagnosis = db.Column(db.Text)
    notes = db.Column(db.Text)

    appointment = db.relationship('Appointment', backref='medical_record')

class Prescription(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    medical_record_id = db.Column(db.Integer, db.ForeignKey('medical_record.id'))
    medicine_name = db.Column(db.String(200))
    dosage = db.Column(db.String(100))
    duration = db.Column(db.String(100))

    medical_record = db.relationship('MedicalRecord', backref='prescriptions')

class Bill(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    appointment_id = db.Column(db.Integer, db.ForeignKey('appointment.id'))
    amount = db.Column(db.Float)
    payment_status = db.Column(db.String(20), default="Unpaid")

    appointment = db.relationship('Appointment', backref='bill')


    
