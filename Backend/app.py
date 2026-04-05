from flask import Flask
from flask_security import Security
from flask_restful import Api
from flask_cors import CORS

from controllers.database import db
from controllers.user_database import user_datastore
from controllers.config import Config

def create_app():
    app=Flask(__name__)#----this create an Flask app
    app.config.from_object(Config) #---load settings of config class

    db.init_app(app)#----This bind app and database

    security= Security(app , user_datastore)#------This connect app for security

    api=Api(app, prefix='/api') #-----This activate app for using restful

    with app.app_context():#----this code ensure currently we are using this app
        db.create_all() #---this create all models

        admin_role = user_datastore.find_or_create_role(name='admin',description='Admin')
        doctor_role = user_datastore.find_or_create_role(name='doctor',description='Doctor')
        user_role = user_datastore.find_or_create_role(name = 'patient',description= 'Patient')

        if not user_datastore.find_user(email = 'admin@gmail.com'):
            user_datastore.create_user(
                email="admin@gmail.com",
                password ="admin@12345",
                roles =[admin_role]
            )
        db.session.commit()

    return app,api

app, api = create_app() #--- if we call app or api it will call function create app 
CORS(app, origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ])
@app.route('/')
def index():
    return {
        'message' : "this is my app"
    }

from controllers.authentication_apis import LoginApi,LogoutApi,RegisterApi
from controllers.Doctor_apis import DoctorList
from controllers.Patient_api import PatientList

api.add_resource(LoginApi,'/login')
api.add_resource(LogoutApi,'/logout')
api.add_resource(RegisterApi,'/register')
api.add_resource(DoctorList,'/doclist')
api.add_resource(PatientList,'/patlist')

if __name__ == "__main__":
    app.run(debug=True)