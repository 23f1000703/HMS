from flask_restful import Resource
from flask import request,jsonify,make_response
from flask_login import current_user
from controllers.user_database import user_datastore
from controllers.model import Patient, Appointment ,Prescription , MedicalRecord,Doctor
from controllers.task import generate_patient_csv
from controllers.database import db

class PatientList(Resource):
    def get(self):
        patients = Patient.query.all()
        print(patients)
        response = []
        for pat in patients:
            response.append({
                "user_id": pat.user_id,
                "active":pat.user.active,
               "name": pat.name,
               "dob": pat.dob,
               'phone no.': pat.phone_no,
               "gender" : pat.gender,
               "address" : pat.address,
               "blood_group" : pat.blood_group
            })
        return make_response(jsonify(response))
    
class YourAppointment(Resource):
    def post(self):
        data = request.get_json()

        doc_id = data.get('doc_id')
        pat_id = data.get('pat_id')
        print(pat_id)
        role =data.get('role')
        if role == 'patient':
            appointments = Appointment.query.filter_by(patient_id = pat_id , status="Pending").all()
        if role == 'doctor':
            appointments = Appointment.query.filter_by(patient_id = doc_id , status="Pending").all()
        print(appointments)

        response = []
        for a in appointments:
            print("this is a",a.doctor_id)
            response.append({
                "id": a.id,
                "patient": a.patient.name,
                'patient_id':a.patient.id,
                "doctor_id":a.doctor.id,  
                "doctor": a.doctor.name,
                "dept": a.doctor.specialization,
                "Date":a.appointment_date,
                "time":a.appointment_time
            })

        return make_response(jsonify(response))
    
class AppointmentDone(Resource):
    def get(self):
        appointments = Appointment.query.filter_by(status="Completed").all()
        print(appointments)

        response = []
        for a in appointments:
            print("this is a",a.doctor_id)
            response.append({
                "id": a.id,
                "patient": a.patient.name,
                'patient_id':a.patient.id,
                "doctor_id":a.doctor.id,  
                "doctor": a.doctor.name,
                "dept": a.doctor.specialization,
                "Date":a.appointment_date,
                "time":a.appointment_time
            })

        return make_response(jsonify(response))
    
class PatientAppointment(Resource):
    def get(self):
        appointments = Appointment.query.filter_by(status="Pending").all()
        print(appointments)

        response = []
        for a in appointments:
            print("this is a",a.doctor_id)
            response.append({
                "id": a.id,
                "patient": a.patient.name,
                'patient_id':a.patient.id,
                "doctor_id":a.doctor.id,  
                "doctor": a.doctor.name,
                "dept": a.doctor.specialization,
                "Date":a.appointment_date,
                "time":a.appointment_time
            })

        return make_response(jsonify(response))
    
    def post(self):
        data = request.get_json()
        Id = data.get('Id',None)
        role =data.get("role")
        print("ID AND ROLE",Id,role)
        response =[]
        if role =="doctor":
            doctor = Doctor.query.filter_by(user_id = Id).first()
            doc_id =doctor.id
            appoint = Appointment.query.filter_by(doctor_id = doc_id).all()
        elif role == 'patient':
            patient = Patient.query.filter_by(user_id = Id).first()
            pat_id =patient.id
            appoint = Appointment.query.filter_by(patient_id = pat_id).all()

        for a in appoint:
            print('Post',a.patient.id)
            response.append({
                "id":a.id,
                "pat_id":a.patient.id,
                "doc_id":a.doctor.id,
                "name": a.patient.name,
                "docname":a.doctor.name,
                "status":a.status
            })

        return make_response(jsonify(response))

class UpdatePatient(Resource):
    def post(self):
        data = request.get_json()
        patId = data.get('pat_id',None)
        print('patId',patId)
        appointments = Appointment.query.filter_by(patient_id=patId).all()

        response = []

        for a in appointments:
            print(a)
            if not a.medical_record:
                continue

            record = a.medical_record

            for p in record.prescriptions:
                response.append({
                    "appointment_id": a.id,
                    "diagnosis": record.diagnosis,
                    "medicine": p.medicine_name,
                    "dosage": p.dosage,
                    "duration": p.duration
                })

        return response, 200

class RecordPatient(Resource):
    def post(self):
        data = request.get_json()

        doctor_id = data.get('doctor_id')
        patient_id = data.get('patient_id')
        appointment_id = data.get('appointment_id')
        visit_type = data.get('visit_type')
        diagnosis = data.get('diagnosis')
        notes = data.get('notes')
        medicines_name = data.get('medicines_name')
        dosage = data.get('dosage')
        duration = data.get('duration')

        record = MedicalRecord(
            doctor_id=doctor_id,
            patient_id=patient_id,
            appointment_id=appointment_id,
            visit_type=visit_type,
            diagnosis=diagnosis,
            notes=notes
        )

        db.session.add(record)
        db.session.commit()

        pres = Prescription(
            medical_record_id=record.id,
            medicine_name=medicines_name,
            dosage=dosage,
            duration=duration
            )
        db.session.add(pres)
        db.session.commit()

        return {"message": "Data saved successfully"}, 201

class Name(Resource):
    def post(self):
        Ids =request.get_json()
        docid =Ids.get("doctor_id")
        patid = Ids.get("patient_id")
        print("Received:", patid, docid)
        response =[]
        patient = Patient.query.get(patid)
        print(patient)
        doctor = Doctor.query.get(docid)
        response.append({
            "Patient_name":patient.name,
            "Doctor_name":doctor.name,
            'Department':doctor.specialization
        })

        return make_response(jsonify(response), 200)
    
class PatientHistory(Resource):

    def post(self):
        data = request.get_json()
        docid = data.get('doc_id')
        patid = data.get('pat_id')
        print('pathist',docid,patid)
        doctor =Doctor.query.filter_by(id =docid).first()
        records = MedicalRecord.query.filter_by(doctor_id=docid,patient_id=patid).all()
        print('records',records)

        datarec = []

        for record in records:
            for p in record.prescriptions:

                datarec.append({
                    "record_id": record.id,
                    "visit_type": record.visit_type,
                    "diagnosis": record.diagnosis,
                    "notes": record.notes,
                    "appointment_id": record.appointment_id,

                    "medicine_name": p.medicine_name,
                    "dosage": p.dosage,
                    "duration": p.duration
                        
                })

        return make_response(jsonify(datarec),200)

class PatientFullRecord(Resource):
    def post(self):
        data = request.get_json()
        patid = data.get('pat_id')
        print('pathist',patid)
        records = MedicalRecord.query.filter_by(patient_id=patid).all()
        print('records',records)

        datarec = []

        for record in records:
            patient = Patient.query.filter_by(id = record.patient_id).first()
            doctor = Doctor.query.filter_by(id = record.doctor_id).first()
            for p in record.prescriptions:

                datarec.append({
                    "patient_name" : patient.name,
                    "doc_name": doctor.name,
                    "dep":doctor.specialization,
                    "record_id": record.id,
                    "visit_type": record.visit_type,
                    "diagnosis": record.diagnosis,
                    "notes": record.notes,
                    "appointment_id": record.appointment_id,

                    "medicine_name": p.medicine_name,
                    "dosage": p.dosage,
                    "duration": p.duration
                        
                })

        return make_response(jsonify(datarec),200)


class ExportCSV(Resource):
    def post(self):
        data = request.get_json()

        patient_id = data.get("patient_id")
        email = data.get("email")

        generate_patient_csv.delay(patient_id, email)

        return {"msg": "CSV generating... check mail"}