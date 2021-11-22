"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .LaunchPage import LaunchPage










class LandingPageFeature(Schema):

    
    launch_page = fields.Nested(LaunchPage, required=False)
    
    continue_as_guest = fields.Boolean(required=False)
    
    login_btn_text = fields.Str(required=False)
    
    show_domain_textbox = fields.Boolean(required=False)
    
    show_register_btn = fields.Boolean(required=False)
    

