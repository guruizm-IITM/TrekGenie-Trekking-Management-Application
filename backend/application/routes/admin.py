from flask import Blueprint

from flask_jwt_extended import jwt_required

from application.auth_utils import role_required

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/admin/dashboard")
@jwt_required()
@role_required("admin")
def dashboard():

    return {
        "message": "Welcome Admin"
    }