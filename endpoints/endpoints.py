from flask import request, jsonify, render_template

from create import db


def index():
    return render_template('index.html')


def register_endpoints(app) -> None:
    """Register all endpoints"""
    app.add_url_rule(rule='/', endpoint='index', view_func=index, methods=['GET'])

