from db import db
import datetime
from pytz import timezone 

class Remainder(db.Document):
    
    org_id = db.IntField(required=True)
    title = db.StringField(required=True)
    owner =  db.ObjectIdField(required=True)
    remainder_id = db.ObjectIdField()
    create_date = db.DateTimeField(default=datetime.datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.171Z'))
    modify_date = db.DateTimeField()
    postponded_date = db.DateTimeField()
    completed_date = db.DateTimeField()
    status = db.StringField(required=True,default='incomplete')
    postponded_status = db.StringField()
    remind_me = db.StringField()
    remind_me_no = db.StringField()
    due_date = db.DateTimeField()
    # if custom :
    repeat_no = db.StringField()
    reapeat_type = db.StringField()
    end_date = db.DateTimeField()
    end_occurance = db.StringField()
    notification_date = db.DateTimeField()
    notification =  db.StringField(required=True,default='0')