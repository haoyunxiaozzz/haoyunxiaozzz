from datetime import datetime, timedelta

# 如用户不按照需求，在这里输入的格式是：03-04-2020呢，程序就会异常
birthday = input('enter your birthday (dd/mm/yyyy): ')

birthday_date = datetime.strptime(birthday, '%d/%m/%Y') 

print(f'Your birthday : {birthday_date}')

one_day = timedelta(days=5)
birthday_eve = birthday_date - one_day
print(f'Day before birthday : {birthday_eve}')          #打印出   生日前一天是birthday_eve（生日）

