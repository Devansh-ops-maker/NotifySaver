import time,sched
from main import open_blackboard
from GetContent import parse_content
from notifier import notify_updates
import schedule

def job():
    content=open_blackboard()
    updates=[]
    deadlines={}
    updates,deadlines=parse_content(content)
    print(updates,deadlines)
    notify_updates(updates,deadlines)
schedule.every(60).minutes.do(job)


job()

while True:
    schedule.run_pending()
    time.sleep(60)



