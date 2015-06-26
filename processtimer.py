#!/usr/bin/env python

from apscheduler.schedulers.blocking import BlockingScheduler
import psycopg2
import sys
import xml.etree.ElementTree as ET
import urllib3
import codecs
from datetime import datetime, date, time

sched = BlockingScheduler()
@sched.scheduled_job('interval', minutes=2)
def timed_job():
    print('The jobsdata process is still running...')

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=10)
def scheduled_job():
    print('This job is run every weekday at 5pm.')

sched.start()
