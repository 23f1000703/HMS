from celery_worker import celery
import csv
from flask_mail import Message
from controllers.model import MedicalRecord, Patient, Doctor
from flask_mail import Mail

mail = Mail()

@celery.task()
def generate_patient_csv(patient_id, email):
    from app import create_app
    app, _ = create_app()

    with app.app_context():

        records = MedicalRecord.query.filter_by(patient_id=patient_id).all()

        file_path = f"patient_{patient_id}.csv"

        # CSV write start
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # header
            writer.writerow([
                "Patient Name",
                "Doctor Name",
                "Visit Type",
                "Diagnosis",
                "Notes",
                "Appointment Date",
                "Medicines"
            ])

            for r in records:
                patient = Patient.query.get(r.patient_id)
                doctor = Doctor.query.get(r.doctor_id)

                appointment_date = r.appointment.appointment_date if r.appointment else ""

                medicines = []
                for p in r.prescriptions:
                    medicines.append(f"{p.medicine_name} ({p.dosage}, {p.duration})")

                writer.writerow([
                    patient.name,
                    doctor.name,
                    r.visit_type,
                    r.diagnosis,
                    r.notes,
                    str(appointment_date),
                    ", ".join(medicines)
                ])

        # Mail config
        app.config.update(
            MAIL_SERVER='localhost',
            MAIL_PORT=1025,
            MAIL_USE_TLS=False,
            MAIL_USE_SSL=False
        )

        mail.init_app(app)

        msg = Message(
            subject="Patient Report",
            sender="test@example.com",
            recipients=[email]
        )

        with open(file_path, "rb") as f:
            msg.attach(file_path, "text/csv", f.read())

        mail.send(msg)

        return "CSV sent"