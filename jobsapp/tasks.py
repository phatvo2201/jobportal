from __future__ import absolute_import,unicode_literals
from celery import task

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from .models import *

def sendEmail(email,subject,to_email):
    from_email = settings.EMAIL_HOST_USER
    text_content="""
    {}
    
    {}

    

    """.format(email['shortDescription'],email['subtitle'])
    html_c=get_template('job-email.html')
    d={'email':email}
    html_content=html_c.render(d)
    
    msg= EmailMultiAlternatives(subject,text_content,from_email,to_email)
    msg.attach_alternative(html_content,'text/html')
    msg.send()


@task()
def scheduledTask():
    notifications= Notification.objects.all()
    for nx in notifications:
        if nx.status=='activate':

            selection=nx.sub_tags
            the_company='phat'
            jobs=Job.objects.filter(company_name=the_company,tags=selection)[:]
            subject='weekly job notication'
            email_jobs={
                "title":"job notication",
                "shortDescription":"thank you for subcrible this job",
                "subtitle":"job portal",
                "jobs":jobs,
            }

    sendEmail(email_jobs,subject,[nx.user.email])