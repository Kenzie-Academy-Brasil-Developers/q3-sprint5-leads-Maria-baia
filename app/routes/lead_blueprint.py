from flask import Blueprint

from app.controllers.lead_controller import create_lead, get_leads, update_lead, delete_lead

bp_leads = Blueprint("bp_leads", __name__, url_prefix="/leads")

bp_leads.post("")(create_lead)
bp_leads.get("")(get_leads)
bp_leads.patch("")(update_lead)
bp_leads.delete("")(delete_lead)