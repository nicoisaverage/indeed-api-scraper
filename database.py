# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:28:42 2019

@author: Nick
"""
#open database connection
db = pymysql.connect(host="ourlocalhost",
                     user="nicoisaverage",
                     password="testing",
                     db="mydatabase",
                     charset="utf8",)
cursor = db.cursor 

#execute SQL command to add function to write offers into database
cursor.excecute("""INSERT INTO indeed(job_title,\
                                    location,\
                                    description, \ 
                                    offer_url,\
                                    offers_skills,\ 
                                    indeed_apply,\
                                    job_key, \
                                    proposal, \ 
                                    proposal_sent, \ 
                                    date) \
VALUES ('%s', '%s' '%s', 'Undefined', \
        '%s', '%s', 'None', 'False', '%s')""" % (offer))
#commit 
db.commit() 

except:
    db.rollback()