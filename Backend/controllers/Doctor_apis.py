from flask_restful import Resource
from flask import request,jsonify,make_response
from controllers.user_database import user_datastore
from controllers.model import Doctor,Appointment,Patient
from controllers.database import db
from datetime import datetime

class DoctorList(Resource):
    def get(self):
        doctor = Doctor.query.all()
        response = []
        for doc in doctor:
          response.append({
            "id":doc.id,
            "user_id":doc.user_id,
            "active":doc.user.active,
            "name":doc.name,
            "qualification":doc.qualification,
            "specialization":doc.specialization,
            "experience_year":doc.experience_years,
             }
          )
        return make_response(jsonify(response))
    
    def post(self):
        data = request.get_json()
        Id = data.get('id',None)
        doc = Doctor.query.get(Id)
        response = []
        response.append({
            "id":doc.id,
            "name":doc.name,
            "qualification":doc.qualification,
            "specialization":doc.specialization,
            "experience_year":doc.experience_years,
             }
          )
        return make_response(jsonify(response))
    

class AppointmentData(Resource):
    def post(self):
        data = request.get_json()
        docid = data.get('doc_id')
        schedule = data.get('schedule')
        appoint =Appointment.query.filter_by(doctor_id = docid,status ='Pending').all()
        for sche in schedule:
            print(sche['date'])
            for i in appoint:
                print(i.appointment_date)
                if str(i.appointment_date) == sche['date']:
                    print('True')
                    if i.appointment_time == sche['shift'][0]:
                        sche['shift'][0] = 'Avail'
                    if i.appointment_time == sche['shift'][1]:
                        sche['shift'][1] = 'Avail'

        return make_response(jsonify(schedule),200)

class BookSlot(Resource):
    def post(self):
        data = request.get_json()
        doc_id =data.get('doc_id')
        pat_id =data.get('pat_id')
        date = data.get('date')
        shift = data.get('shift')

        appointment_date = datetime.strptime(date, "%Y-%m-%d").date()
        new_appointment = Appointment(
                doctor_id=doc_id,
                patient_id=pat_id,
                appointment_date=appointment_date,
                appointment_time = shift
        )

        db.session.add(new_appointment)
        db.session.commit()
        return {"message": "Appointment booked successfully"}, 200

    
class Complete(Resource):
    def put(self):
        data = request.get_json()
        docid = data.get('id')

        appointments = Appointment.query.filter_by(id=docid).all()
        for appt in appointments:
            appt.status = "Complete"

        db.session.commit()

        return {"message": "Appointment marked as Complete"}, 200
    
class Ids(Resource):
    def post(self):
        data = request.get_json()

        ID = data.get('Id')
        role = data.get('role')

        if role == "doctor":
            doc = Doctor.query.filter_by(user_id=ID).first()

            if not doc:
                return {"message": "Doctor not found"}, 404

            return {
                "doc_id": doc.id,
                "name": doc.name
            }

        elif role == "patient":
            pat = Patient.query.filter_by(user_id=ID).first()
            print(pat.id)

            if not pat:
                return {"message": "Patient not found"}, 404

            return {
                "pat_id": pat.id,
                "name": pat.name
            }

        else:
            return {"message": "Invalid role"}, 400

class Deleteappoint(Resource):
         def delete(self,id):
          user=Appointment.query.filter_by(id =id).first()
          print(user)
          db.session.delete(user)
          db.session.commit()
          return{"message":"Deleted"},200