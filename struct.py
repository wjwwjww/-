#引入time模块，实现延时
from time import sleep
#引入selenium库中的webdriver模块，实现对网页的操作
from selenium import webdriver
#引入By Class，辅助元素定位
from selenium.webdriver.common.by import By
# #引入ActionChains Class，辅助鼠标移动
# from selenium.webdriver.common.action_chains import ActionChains
# #引入Keys Class，辅助键盘操作
# from selenium.webdriver.common.keys import Keys

#打开谷歌浏览器
driver = webdriver.Safari()
#打开网页
driver.get('https://yd.shuabu.cn/') #将URL替换为需要操作的网址
sleep(2)

el=driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div[2]/button/span') #找到确定按钮
el.click() #点击确定按钮
sleep(5)
account=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[3]/div[5]/div/div/div[1]/div[2]/input') #找到账号输入框
password=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[3]/div[5]/div/div/div[2]/div[2]/span/input') #找到密码输入框
step=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[3]/div[5]/div/div/div[3]/div[2]/input') #找到步数输入
account.send_keys('18279331349') #输入账号
password.send_keys('Wjw040307')
step.send_keys('54321')
confirm=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[3]/button/span') #找到确定按钮
confirm.click() #点击确定按钮
sleep(5)
driver.quit()
