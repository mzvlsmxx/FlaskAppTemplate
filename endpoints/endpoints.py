from flask import request, jsonify, render_template

from database import *


async def index():
    return render_template('index.html')


async def process_data():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            print(data)
            # Now we can process data from request
            return jsonify({"message": "Data received"}), 200
        else:
            return jsonify({"error": "Request must be JSON"}), 400

    elif request.method == 'GET':
        return jsonify(await get_all_entries())


def register_endpoints(app) -> None:
    """Register all endpoints"""
    app.add_url_rule(rule='/', endpoint='index', view_func=index, methods=['GET'])
    app.add_url_rule(rule='/process_data', endpoint='process_data', view_func=process_data, methods=['GET', 'POST'])
