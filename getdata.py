
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# 출석율을 가져오는 함수
def scrape_attendancerate(browser):
    try:
    
        return 
    except:
        print('error!')



# 온라인 강의 수강 현황
def scrape_onlinelecture_cur_sit(browser):
    try:
    
        return 
    except:
        print('error!')




# 팀 프로젝트
def scrape_teamproject(browser):
    try:
    
        return 
    except:
        print('error!')





# 과제 

def scrape_assignmnet(browser):
    try:
    
        return 
    except:
        print('error!')





# 퀴즈
def scrape_quiz(browser):
    try:
    
        return 
    except:
        print('error!')

