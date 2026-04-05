from flask_restful import Resource
from flask import request,jsonify,make_response
from controllers.user_database import user_datastore
from controllers.model import Doctor
from controllers.database import db

class DoctorList(Resource):
    def get(self):
        doctor = Doctor.query.all()
        response = []
        for doc in doctor:
          response.append({
            "id":doc.id,
            "name":doc.name,
            "specialization":doc.specialization,
            "experience_year":doc.experience_years,
             }
          )
        return make_response(jsonify(response))