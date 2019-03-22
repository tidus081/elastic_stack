"""

RUN

Entry point code for management manager server (flask)

Copyright 2018, Ikigai Labs.
All rights reserved.

"""
from server import application

HOST="0.0.0.0"
PORT="7000"

if __name__ == "__main__":
    application.run(host=HOST, port=PORT)
