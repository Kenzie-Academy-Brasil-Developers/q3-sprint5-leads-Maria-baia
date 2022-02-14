from flask import Blueprint
     
from app.routes.lead_blueprint import bp_leads

bp_api = Blueprint("bp_api", __name__)

bp_api.register_blueprint(bp_leads)
