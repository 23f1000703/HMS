from flask_restful import Resource
from flask import request,jsonify,make_response
from controllers.user_database import user_datastore
from controllers.model import Patient
from controllers.database import db

class PatientList(Resource):
    def get(self):
        patients = Patient.query.all()
        print(patients)
        response = []
        for pat in patients:
            response.append({
               "name": pat.name,
               "dob": pat.dob,
               'phone no.': pat.phone_no,
               "gender" : pat.gender,
               "address" : pat.address,
               "blood_group" : pat.blood_group
            })
        return make_response(jsonify(response))

