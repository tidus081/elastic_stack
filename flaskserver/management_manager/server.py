"""

MANAGEMENT MANAGER SERVER

Management manager server code

Copyright 2018, Ikigai Labs.
All rights reserved.

"""
from flask import Flask, request, jsonify, render_template

from base_utils import get_logger
import requests

logger = get_logger("ServerLogger", "info")


application = Flask("ManagementManager")


"""
Server Methods
"""

@application.route('/data', methods=['POST'])
def data():
    if request.method == 'POST':
        logger.error("it's not server error, testing")
        return jsonify("congrats")

