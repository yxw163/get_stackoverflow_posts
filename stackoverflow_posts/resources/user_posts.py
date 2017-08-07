# -*- coding: utf-8 -*-

import requests
import gunpg
from flask_restful import Resource, reqparse
from flask import request

BASEURL = "https://api.stackexchange.com/2.2/users/"

params = {
    "site": "stackoverflow",
    "sort": "creation"
}


class GetUserPosts(Resource):

    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('userId', type=str, required=True, location='json')
        args = parser.parse_args(strict=True)
        targetUrl = BASEURL + args['userId'] + '/posts'
        r = requests.get(targetUrl, params)
        return r.json()
