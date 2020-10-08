from .auth import login_required
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from .db import init_db


bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@login_required
@bp.route("/", methods=("GET", "POST"))
def dashboard():
  return render_template("dashboard/dashboard.html")
