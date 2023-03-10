import datetime
from datetime import date
from dateutil.rrule import rrule, WEEKLY , MONTHLY, YEARLY
from datetime import timedelta
from mongoengine.errors import NotUniqueError
from remainder_model import Remainder
class RemainderAPI:
 # ================================================================================================= 
 # reaminder_post (Input):
 #      org_id = "0",
 #      title = "1st remainder",
 #      due_date = "2022-12-27 08:26:49.219717",             // till date our task want to generate
 #      repeat = "Every month",                              // days or month or year to genrate our task
 #      repeat_end_date = "2023-12-27 08:26:49.219717",      // stop the task in this repetation date
 #      response1  = "1st remainder's task"                              
 #      repeat_no  = "5"    
 #                                 
 #      remind_me = "1 day"                                 // How many days remainder notification to genrate
 #      remind_me_no = "5 times"                            // How many times remainder to genrate
 #      owner = " task generated Owner name"                // Which person to generate
 #         
 #      reapeat_type = "month"                              // this will applicable when the reapeat is "Custom"  or it not necessary                             
 #      end_date  = "2023-12-27 08:26:49.219717",           // this will applicable when the reapeat is "Custom"  when our custom date is ended                                
 #      end_occurance = "5"                                 // this will applicable when the reapeat is "Custom"  when our custom date is how many time to generate     
 # 
 #      Result will be :
 #
 #      notification_date = [ "2023-01-26 08:26:49.219717", "2023-02-26 08:26:49.219717",..........."2023-05-26 08:26:49.219717" ]                                                                   
 # ================================================================================================= 

    def reaminder_post(org_id,title,due_date,repeat,repeat_end_date,response1,repeat_no,reapeat_type,end_date,end_occurance,notification_date,remind_me,remind_me_no,owner):

        try:
            
            repeat_year = due_date[0]+due_date[1]+due_date[2]+due_date[3]
            repeat_month = due_date[5]+due_date[6]
            repeat_date = due_date[8]+due_date[9]
            
            repeat_hour = due_date[11]+due_date[12]
            repeat_min = due_date[14]+due_date[15]

            if repeat_end_date:
                repeat_end_year = repeat_end_date[0]+repeat_end_date[1]+repeat_end_date[2]+repeat_end_date[3]
                repeat_end_month = repeat_end_date[5]+repeat_end_date[6]
                repeat_end_date = repeat_end_date[8]+repeat_end_date[9]

            if end_date:
                reapeat_type_end_year = end_date[0]+end_date[1]+end_date[2]+end_date[3]
                reapeat_type_end_month = end_date[5]+end_date[6]
                reapeat_type_end_date = end_date[8]+end_date[9]

            if repeat == 'None':
                start_date = date(int(repeat_year),int(repeat_month),int(repeat_date))
                start_time = timedelta(hours=int(repeat_hour), minutes=int(repeat_min))
                for d in rrule(WEEKLY, dtstart=start_date, until=start_date):
                    d1 = d + timedelta(hours=int(repeat_hour), minutes=int(repeat_min)) - timedelta(days=int(remind_me_no))
                    d2 = d1 - timedelta(hours=5, minutes=28)
                    task = Remainder(org_id=org_id,title=title,due_date=d,remainder_id=response1,notification_date=d2,remind_me=remind_me,remind_me_no=remind_me_no,owner=owner)
                    response = task.save()
                    output1 = {'task_id' : response.id}

            if repeat == 'Every Week':
                start_date = date(int(repeat_year),int(repeat_month),int(repeat_date))
                end_date = date(int(repeat_end_year),int(repeat_end_month),int(repeat_end_date))
                for d in rrule(WEEKLY, dtstart=start_date, until=end_date):

                    d1 = d + timedelta(hours=int(repeat_hour), minutes=int(repeat_min)) - timedelta(days=int(remind_me_no))
                    d2 = d1 - timedelta(hours=5, minutes=28)
                    task = Remainder(org_id=org_id,title=title,due_date=d,remainder_id=response1,notification_date=d2,remind_me=remind_me,remind_me_no=remind_me_no,owner=owner)
                    response = task.save()
                    output1 = {'task_id' : response.id}
            if repeat == 'Every Month':
                start_date = date(int(repeat_year),int(repeat_month),int(repeat_date))
                end_date = date(int(repeat_end_year),int(repeat_end_month),int(repeat_end_date))
                for d in rrule(MONTHLY, dtstart=start_date, until=end_date):
                    d1 = d + timedelta(hours=int(repeat_hour), minutes=int(repeat_min)) - timedelta(days=int(remind_me_no))
                    d2 = d1 - timedelta(hours=5, minutes=28)
                    task = Remainder(org_id=org_id,title=title,due_date=d,remainder_id=response1,notification_date=d2,remind_me=remind_me,remind_me_no=remind_me_no,owner=owner)                    
                    response = task.save()
                    output1 = {'task_id' : response.id}
            if repeat == 'Every Year':
                start_date = date(int(repeat_year),int(repeat_month),int(repeat_date))
                # start_date = date(2023,1,2)
                end_date = date(int(repeat_end_year),int(repeat_end_month),int(repeat_end_date))
                for d in rrule(YEARLY, dtstart=start_date, until=end_date):
                    d1 = d - timedelta(days=int(remind_me_no))
                    d1 = d + timedelta(hours=int(repeat_hour), minutes=int(repeat_min)) - timedelta(days=int(remind_me_no))
                    d2 = d1 - timedelta(hours=5, minutes=28)
                    task = Remainder(org_id=org_id,title=title,due_date=d,remainder_id=response1,notification_date=d2,remind_me=remind_me,remind_me_no=remind_me_no,owner=owner)                    
                    response = task.save()
                    output1 = {'task_id' : response.id}

            if repeat == 'Custom':
                if reapeat_type == 'Week':
                    start_date = date(int(repeat_year),int(repeat_month),int(repeat_date))
                    if end_date:
                        end_date = date(int(reapeat_type_end_year),int(reapeat_type_end_month),int(reapeat_type_end_date))
                        for d in rrule(WEEKLY, dtstart=start_date, until=end_date,interval=int(repeat_no)):
                            d1 = d - timedelta(days=int(remind_me_no))
                            d1 = d + timedelta(hours=int(repeat_hour), minutes=int(repeat_min)) - timedelta(days=int(remind_me_no))
                            d2 = d1 - timedelta(hours=5, minutes=28)
                            task = Remainder(org_id=org_id,title=title,due_date=d,remainder_id=response1,notification_date=d2,remind_me=remind_me,remind_me_no=remind_me_no,owner=owner)                            
                            response = task.save()
                    if end_occurance:
                        for d in rrule(WEEKLY, dtstart=start_date, count=int(end_occurance),interval=int(repeat_no)):
                            d1 = d - timedelta(days=int(remind_me_no))
                            d1 = d + timedelta(hours=int(repeat_hour), minutes=int(repeat_min)) - timedelta(days=int(remind_me_no))
                            d2 = d1 - timedelta(hours=5, minutes=28)
                            task = Remainder(org_id=org_id,title=title,due_date=d,remainder_id=response1,notification_date=d2,remind_me=remind_me,remind_me_no=remind_me_no,owner=owner)                            
                            response = task.save()
                        output1 = {'task_id' : response.id}
                if reapeat_type == 'Month':
                    start_date = date(int(repeat_year),int(repeat_month),int(repeat_date))
                    if end_date:
                        end_date = date(int(reapeat_type_end_year),int(reapeat_type_end_month),int(reapeat_type_end_date))
                        for d in rrule(MONTHLY, dtstart=start_date, until=end_date,interval=int(repeat_no)):
                            d1 = d - timedelta(days=int(remind_me_no))
                            d1 = d + timedelta(hours=int(repeat_hour), minutes=int(repeat_min)) - timedelta(days=int(remind_me_no))
                            d2 = d1 - timedelta(hours=5, minutes=28)
                            task = Remainder(org_id=org_id,title=title,due_date=d,remainder_id=response1,notification_date=d2,remind_me=remind_me,remind_me_no=remind_me_no,owner=owner)                            
                            response = task.save()
                    if end_occurance:
                        for d in rrule(MONTHLY, dtstart=start_date, count=int(end_occurance),interval=int(repeat_no)):
                            d1 = d - timedelta(days=int(remind_me_no))
                            d1 = d + timedelta(hours=int(repeat_hour), minutes=int(repeat_min)) - timedelta(days=int(remind_me_no))
                            d2 = d1 - timedelta(hours=5, minutes=28)
                            task = Remainder(org_id=org_id,title=title,due_date=d,remainder_id=response1,notification_date=d2,remind_me=remind_me,remind_me_no=remind_me_no,owner=owner)                            
                            response = task.save()
                        output1 = {'task_id' : response.id}
                if reapeat_type == 'Year':
                    start_date = date(int(repeat_year),int(repeat_month),int(repeat_date))
                    if end_date:
                        end_date = date(int(reapeat_type_end_year),int(reapeat_type_end_month),int(reapeat_type_end_date))
                        for d in rrule(YEARLY, dtstart=start_date, until=end_date,interval=int(repeat_no)):
                            d1 = d - timedelta(days=int(remind_me_no))
                            d1 = d + timedelta(hours=int(repeat_hour), minutes=int(repeat_min)) - timedelta(days=int(remind_me_no))
                            d2 = d1 - timedelta(hours=5, minutes=28)
                            task = Remainder(org_id=org_id,title=title,due_date=d,remainder_id=response1,notification_date=d2,remind_me=remind_me,remind_me_no=remind_me_no,owner=owner)                            
                            response = task.save()
                    if end_occurance:
                        for d in rrule(YEARLY, dtstart=start_date, count=int(end_occurance),interval=int(repeat_no)):
                            d1 = d - timedelta(days=int(remind_me_no))
                            d1 = d + timedelta(hours=int(repeat_hour), minutes=int(repeat_min)) - timedelta(days=int(remind_me_no))
                            d2 = d1 - timedelta(hours=5, minutes=28)
                            task = Remainder(org_id=org_id,title=title,due_date=d,remainder_id=response1,notification_date=d2,remind_me=remind_me,remind_me_no=remind_me_no,owner=owner)                            
                            response = task.save()
                        output1 = {'task_id' : response.id}
                        return output1
        except NotUniqueError as e:
            return ''