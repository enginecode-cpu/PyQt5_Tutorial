# 날짜와 시간 표시하기

from PyQt5.QtCore import QDate, Qt, QTime, QDateTime

# 현재 날짜를 가져온다.
now = QDate.currentDate()
print(now.toString()) # # 월 3 23 2020

# 날짜 형식
print(now.toString('d.M.yy')) # 23.3.20
print(now.toString('dd.MM.yyyy')) # 23.03.2020
print(now.toString('ddd.MMMM.yyyy')) # 월.3월.2020
print(now.toString(Qt.DefaultLocaleLongDate)) # 2020년 3월 23일 월요일

print("\n-----------------\n")

# 현재 시간 출력하기
time = QTime.currentTime()
print(time.toString()) # 00:42:43

# 시간 형식
print(time.toString('h.m.s')) # 0.42.43
print(time.toString('hh.mm.ss')) # 00.42.43
print(time.toString('hh.mm.ss.zzzz')) # 00.42.43.729729
print(time.toString(Qt.DefaultLocaleLongDate)) # 오전 12:42:43
print(time.toString(Qt.DefaultLocaleShortDate)) # 오전 12:42

print("\n-----------------\n")

# 현재 날짜와 시간 출력하기
datetime = QDateTime.currentDateTime()
print(datetime.toString()) # 월 3 23 00:44:52 2020

print(datetime.toString('d.M.yy hh:mm:ss')) # 23.3.20 00:46:28
print(datetime.toString('dd.MM.yyyy hh:mm:ss')) # 23.03.2020 00:47:09
print(datetime.toString(Qt.DefaultLocaleLongDate)) # 2020년 3월 23일 월요일 오전 12:47:35
print(datetime.toString(Qt.DefaultLocaleShortDate)) # 2020-03-23 오전 12:48

