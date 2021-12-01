"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema










class Access(BaseSchema):

    
    answer = fields.Boolean(required=False)
    
    ask_question = fields.Boolean(required=False)
    
    comment = fields.Boolean(required=False)
    
    rnr = fields.Boolean(required=False)
    

