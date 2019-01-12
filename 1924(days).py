A, B = map(int, input().split())
list = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
import datetime
dt1 = datetime.datetime(A, B)
dt2 = datetime.datetime(1, 1)
td = dt1 - dt2
dt1
