"""
This extracts used to get instragram users
"""
from flask import request
from flask_restful import Resource
import twitter_user_endpoint
import pandas as pd
from ast import literal_eval
#from schema import DataSchema
import json

#data_schema = DataSchema()

class Twitter(Resource):   

    def get(self, name):
        data= name
        
       # result=instagram_users.call_all_func(data)
        result=twitter_user_endpoint.process_metadata(data)

        return {
            'Username data': result
        }


