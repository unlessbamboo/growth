from flask import Blueprint, make_response, current_app, request, jsonify

bp = Blueprint('api', __name__)

from . import views
from . import socket_views
