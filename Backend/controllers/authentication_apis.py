from flask_restful import Resource
from flask import request,jsonify,make_response
from flask_security import utils,auth_token_required

from controllers.user_database import user_datastore
from controllers.model import Doctor,Patient
from controllers.database import db
from datetime import datetime

class LoginApi(Resource):
    def post(self):

        login_credentials = request.get_json()

        if not login_credentials:
            result = {
                'message':'Login credential are required.'
            }
            return make_response(jsonify(result), 400)
        
        email = login_credentials.get('email',None)
        password = login_credentials.get('password',None)

        if not email or not password:
            result = {
                'message':'Email and Password required.'
            }
            return make_response(jsonify(result),400)
        
        user = user_datastore.find_user(email=email)

        if not user:
            result = {
                'message':'User not found.'
            }
            return  make_response(jsonify(result),404)
        
        
        if not utils.verify_password(password, user.password):
            result = {
                'message':'Invalid Password.'
            }
            return make_response(jsonify(result),401)
        
        auth_token = user.get_auth_token()

        utils.login_user(user) 

        response = {
            'message':'Login successful.',
            'user_details':{
                'email':user.email,
                'roles': [role.name for role in user.roles],
                'auth_token': auth_token
            }
        }
        return make_response(jsonify(response), 200)     


class LogoutApi(Resource):
    @auth_token_required
    #@role_required(['admin'])
    def post(self):
        utils.logout_user()

        response = {
            'message': 'logout successfully'
        }
        return make_response(jsonify(response),200)

class RegisterApi(Resource):
    def post(self):
        creds  = request.get_json()

        if not creds:
            result ={
                'message':"Registration credentials are required."
            }
            return make_response(jsonify(result),400)
        
        email =creds.get('email',None)
        password = creds.get('password',None)
        role_name = creds.get('role')

        if not email or not password:
            result = {
                'message':'Email and password required'
            }
            return make_response(jsonify(result), 400)
        
        if not role_name:
             result = {
                  'message':'role is required'
             }
             return make_response(jsonify(result))
        
        if user_datastore.find_user(email=email):
            result = {
                'message':'User already Exist.'
            }
            return make_response(jsonify(result), 409)
        
        role = user_datastore.find_role(role_name)
        print(role)

        user = user_datastore.create_user(
            email=email,
            password=password,
            roles = [role]
        )
        db.session.add(user)
        db.session.flush()

        if role_name == "doctor":
                specialization=creds.get("specialization")
                experience_years=creds.get("experience_years")
                name=creds.get("name")
                
                doctor = Doctor(
                user_id=user.id,
                name=name,
                specialization=specialization,
                experience_years=experience_years, 
                )
                db.session.add(doctor)

        elif role_name == "patient":
                dob_str=creds.get("dob")
                dob = datetime.strptime(dob_str, "%Y-%m-%d")
                name =creds.get("name")
                phone_no = creds.get("phone_no")
                gender=creds.get("gender")
                blood_group=creds.get("blood_group",None)
                address=creds.get("address")
                
                patient = Patient(
                user_id=user.id,
                name=name,
                phone_no = phone_no,
                dob=dob,
                gender=gender,
                blood_group=blood_group,
                address=address
            )

                db.session.add(patient)

        db.session.commit()


        response = {
            'message': 'Registration successful.',
            'user_details': {
                'email': email,
                'roles': [r.name for r in user.roles]
            }
        }
        return make_response(jsonify(response), 201)
    

    # def put(self):
    #     pass
    
    # def get(self):
    #     pass
