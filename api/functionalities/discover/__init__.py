from flask import Blueprint

discover_bp = Blueprint('discover', __name__, url_prefix='/discover')

from .bands_flowchart import bands_flowchart