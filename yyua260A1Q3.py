import math
hour = input("Enter hour: ")
hour0 = int(hour) + 100
hours = str(hour0)
hour1 = hours[1:]
minute = input("Enter minute: ")
minute0 = int(minute) + 100
minutes = str(minute0)
minute1 = minutes[1:]
second = input("Enter second: ")
second0 = int(second) + 100
seconds = str(second0)
second1 = seconds[1:]
Enter_time1 = hour1 + ":" + minute1 + ":" + second1

hour2 = input("Enter hour: ")
hour3 = int(hour2) + 100
hourx = str(hour3)
hour4 = hourx[1:]
minute2 = input("Enter minute: ")
minute3 = int(minute2) + 100
minutex = str(minute3)
minute4 = minutex[1:]
second2 = input("Enter second: ")
second3 = int(second) + 100
secondx = str(second3)
second4 = secondx[1:]
Enter_time2 = hour4 + ":" + minute4 + ":" + second4

int_hour1 = int(hour)
int_minute1 = int(minute)
int_second1 = int(second)
int_hour2 = int(hour2)
int_minute2 = int(minute2)
int_second2 = int(second2)


sum_hour = (int_hour1 + int_hour2)
sum_minute = (int_minute1 + int_minute2)
sum_second = (int_second1 + int_second2)

no_zero_second = sum_second % 60
minute = sum_second // 60 + sum_minute
no_zero_minute = minute % 60
no_zero_hour = sum_hour + (minute // 60)

total_hour0 = int(no_zero_hour) + 100
total_hours = str(total_hour0)
total_hour = total_hours[1:]
total_minute0 = int(no_zero_minute) + 100
total_minutes = str(total_minute0)
total_minute = total_minutes[1:]
total_second0 = int(no_zero_second) + 100
total_seconds = str(total_second0)
total_second = total_seconds[1:]

total_time = total_hour + ":" + total_minute + ":" + total_second

print("Enter_time:", Enter_time1)
print("Enter_time:", Enter_time2)
print("Total time:", total_time)
