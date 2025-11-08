from flask import request, jsonify, render_template

from database import *


async def index():
    return render_template('index.html')


async def fetch_data():
    return jsonify(
        {
            "MySQLClient.check_access": MySQLClient.check_access(),
            "RedisClient.check_access": RedisClient.check_access()
        }
    ), 200


async def process_data():
    if not request.is_json:
        return jsonify({"Error": "Request must be JSON"}), 400
    
    url_args: dict = request.args.to_dict()
    print(f'{url_args = }')
    
    data = request.get_json()
    print(f'{data = }')

    return jsonify({}), 200


def register_endpoints(app) -> None:
    """Register all endpoints"""
    app.add_url_rule(rule='/', endpoint='index', view_func=index, methods=['GET'])
    app.add_url_rule(rule='/fetch_data', endpoint='fetch_data', view_func=fetch_data, methods=['GET'])
    app.add_url_rule(rule='/process_data', endpoint='process_data', view_func=process_data, methods=['POST'])
