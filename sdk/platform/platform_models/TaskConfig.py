"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *





from .TaskParam import TaskParam


class TaskConfig(Schema):

    
    name = fields.Str(required=False)
    
    task_config_id = fields.Int(required=False)
    
    task_params = fields.List(fields.Nested(TaskParam, required=False), required=False)
    

