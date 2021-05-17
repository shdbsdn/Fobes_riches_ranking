from selenium import webdriver

url = 'https://www.forbes.com/?sh=352d50a52254'
options=webdriver.ChromeOptions()
#options.add_argument('headless')
driver = webdriver.Chrome('C:/Users/82104/chromedriver.exe',options=options)
driver.get(url)

click_menu=driver.find_element_by_xpath('/html/body/div[1]/header/nav/div[1]/button[1]')
click_menu.click()
click_billion=driver.find_element_by_xpath('/html/body/div[1]/header/nav/div[3]/ul/li[1]')
click_billion.click()
click_world=driver.find_element_by_xpath('/html/body/div[1]/header/nav/div[3]/ul/li[1]/div[2]/ul/li[2]/a')
click_world.click()
data = [[],[]]
name=driver.find_elements_by_class_name('personName')
k = 0
print(len(name))
for i in name:
    if k == 0:
        k += 1
        print('#')
        continue
    print(i.text)
    data[0].append(i.text)
    if k == 10:
        break
    k += 1

k = 0
net_worth=driver.find_elements_by_class_name('netWorth')
print(len(net_worth))

for i in net_worth:
    if k == 0:
        k += 1
        print('#')
        continue
    print(float(i.text.replace('$','').replace('B',''))*1000000000)
    data[1].append(float(i.text.replace('$','').replace('B',''))*1000000000)
    if k == 10:
        break
    k += 1
print(data)

import matplotlib.pyplot as plt

plt.rc('font',size = 5)
plt.bar(range(0,10), data[1])
plt.ylabel("dollar")
plt.xticks(range(0,10),data[0],rotation = 90)
plt.show()