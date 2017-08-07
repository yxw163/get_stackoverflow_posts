# -*- coding: utf-8 -*-

import requests
from flask import Flask, request, render_template, url_for
from flask_restful import Api, reqparse
from resources import GetUserPosts

app = Flask(__name__)
api = Api(app)

@app.route('/')
def show_index():
	return render_template('index.html')

api.add_resource(GetUserPosts, '/userposts')

app.jinja_env.variable_start_string = '{[ '
app.jinja_env.variable_end_string = ' ]}'
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

if __name__ == '__main__':
    app.run(debug=True)