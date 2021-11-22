"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

class UserValidator:
    
    class loginWithFacebook(Schema):
        
        platform = fields.Str(required=False)
         
    
    class loginWithGoogle(Schema):
        
        platform = fields.Str(required=False)
         
    
    class loginWithGoogleOauth(Schema):
        
        platform = fields.Str(required=False)
        
        redirect_url = fields.Str(required=False)
         
    
    class loginWithGoogleAndroid(Schema):
        
        platform = fields.Str(required=False)
         
    
    class loginWithGoogleIOS(Schema):
        
        platform = fields.Str(required=False)
         
    
    class loginWithAppleIOS(Schema):
        
        platform = fields.Str(required=False)
         
    
    class loginWithOTP(Schema):
        
        platform = fields.Str(required=False)
         
    
    class loginWithEmailAndPassword(Schema):
        
        pass 
    
    class sendResetPasswordEmail(Schema):
        
        platform = fields.Str(required=False)
         
    
    class forgotPassword(Schema):
        
        pass 
    
    class sendResetToken(Schema):
        
        pass 
    
    class loginWithToken(Schema):
        
        pass 
    
    class registerWithForm(Schema):
        
        platform = fields.Str(required=False)
         
    
    class verifyEmail(Schema):
        
        pass 
    
    class verifyMobile(Schema):
        
        pass 
    
    class hasPassword(Schema):
        
        pass 
    
    class updatePassword(Schema):
        
        pass 
    
    class logout(Schema):
        
        pass 
    
    class sendOTPOnMobile(Schema):
        
        platform = fields.Str(required=False)
         
    
    class verifyMobileOTP(Schema):
        
        platform = fields.Str(required=False)
         
    
    class sendOTPOnEmail(Schema):
        
        platform = fields.Str(required=False)
         
    
    class verifyEmailOTP(Schema):
        
        platform = fields.Str(required=False)
         
    
    class getLoggedInUser(Schema):
        
        pass 
    
    class getListOfActiveSessions(Schema):
        
        pass 
    
    class getPlatformConfig(Schema):
        
        name = fields.Str(required=False)
         
    
    class updateProfile(Schema):
        
        platform = fields.Str(required=False)
         
    
    class addMobileNumber(Schema):
        
        platform = fields.Str(required=False)
         
    
    class deleteMobileNumber(Schema):
        
        platform = fields.Str(required=False)
        
        active = fields.Boolean(required=False)
        
        primary = fields.Boolean(required=False)
        
        verified = fields.Boolean(required=False)
        
        country_code = fields.Str(required=False)
        
        phone = fields.Str(required=False)
         
    
    class setMobileNumberAsPrimary(Schema):
        
        pass 
    
    class sendVerificationLinkToMobile(Schema):
        
        platform = fields.Str(required=False)
         
    
    class addEmail(Schema):
        
        platform = fields.Str(required=False)
         
    
    class deleteEmail(Schema):
        
        platform = fields.Str(required=False)
        
        active = fields.Boolean(required=False)
        
        primary = fields.Boolean(required=False)
        
        verified = fields.Boolean(required=False)
        
        email = fields.Str(required=False)
         
    
    class setEmailAsPrimary(Schema):
        
        pass 
    
    class sendVerificationLinkToEmail(Schema):
        
        platform = fields.Str(required=False)
         
    