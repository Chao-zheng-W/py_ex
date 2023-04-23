import schedule
import time
def job():
    print('哈哈————————')

schedule.every(3).seconds.do(job)  #定时每3秒执行一次job函数
while True:
    schedule.run_pending()         #中间休息1秒
    time.sleep(1)

#可用于办公自动化