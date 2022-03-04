from flask import request, current_app, jsonify
from app.models.lead_model import LeadModel
from datetime import datetime
from sqlalchemy.exc import IntegrityError, NoResultFound
import re

def create_lead():
    try:
        data = request.get_json()

        if(re.fullmatch("^\([1-9]{2}\)(?:[2-8]|9[0-9])[0-9]{3}\-[0-9]{4}$", data["phone"]) != None):
            for key, value in data.items():
                if type(value) != str:
                    return jsonify({"msg": "fields must be strings"}), 400
                if key != "name" and key != "email" and key != "phone":
                    return jsonify({"msg": "wrong fields"}), 400
                
            new_data = {
                        "name": data["name"], 
                        "email": data["email"],
                        "phone": data["phone"],
                        "creation_date": str(datetime.now().strftime("%d/%m/%Y %H:%M")),
                        "last_visit": str(datetime.now().strftime("%d/%m/%Y %H:%M")),
                        "visits": 1
                    }    

            new_lead = LeadModel(**new_data)

            current_app.db.session.add(new_lead)
            current_app.db.session.commit()

            return jsonify(new_lead), 201
        return jsonify("msg: Phone must be in the format (xx)xxxxx-xxxx"), 400
    
    except IntegrityError:
        return jsonify({"msg": "Email or phone already exists"}), 409

def get_leads():
    data = LeadModel.query.order_by(LeadModel.visits.desc()).all()

    if(len(data) > 0):
      return jsonify(data), 200
    return jsonify({"msg": "No data found"}), 404

def update_lead():
    try:
        data = request.get_json()

        for key, value in data.items():
            if(key != "email"):
                return jsonify({"msg": "request must be passsed only email"}), 400
            if(type(value) != str):
                return jsonify({"msg": "field must be string"}), 400

        lead = LeadModel.query.filter_by(email = data["email"]).one()

        setattr(lead, "last_visit", str(datetime.now().strftime("%d/%m/%Y %H:%M")))
        setattr(lead, "visits", lead.visits+1)

        current_app.db.session.add(lead)
        current_app.db.session.commit()

        return "", 204
    except NoResultFound:
        return jsonify({"msg": "No data found"}), 404

def delete_lead():
    try:
        data = request.get_json()
        for key, value in data.items():
            if(key != "email"):
                return jsonify({"msg": "request must be passsed only email"}), 400
            if(type(value) != str):
                return jsonify({"msg": " field must be string"}), 400

        lead = LeadModel.query.filter_by(email = data["email"]).one()

        current_app.db.session.delete(lead)
        current_app.db.session.commit()

        return "", 204
    except NoResultFound:
        return jsonify({"msg": "No data found"}), 404