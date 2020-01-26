# https://docs.python.org/3.7/library/datetime.html

import datetime
#import pytz

# Naive - not aware of things such as Timezone and DST
d = datetime.date(2019, 1, 21) # dont use 01 - that gives an error back
print(d)

tday = datetime.date.today()

# weekday() - Monday is 0 and Sunday is 6
print('weekday:', tday.weekday())

# isoweekday() - Monday is 1 and Sunday is 7
print('isoweekday', tday.isoweekday())

print('today year:', tday.year, 'today month:', tday.month, 'today day:', tday.day)

# datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
tdelta = datetime.timedelta(hours=12)
print('12 hrs from now: {}'.format(tday + tdelta))
tDelta25HrsAgo = datetime.timedelta(hours=25)
print('25 hrs back from now: {}'.format(tday - tDelta25HrsAgo))
tDelta2DaysAgo = datetime.timedelta(days=2)
print('2 days back from now: {}'.format(tday - tDelta2DaysAgo))

# date2 = date1 + timedelta
# timedelta = date1 + date2

bday = datetime.date(2019, 3, 18)
till_bday = bday - tday
print("Days till B'Day:{}".format(till_bday.days))
print("Seconds till B'Day:{}".format(till_bday.total_seconds()))

# lets work with time now
time = datetime.time(9, 30, 45, 100000)
print("Time:", time)
print('Hour:{} Minute:{} Seconds:{}'.format(time.hour, time.minute, time.second))

dtTime = datetime.datetime(2019, 3, 18, 9, 30, 45, 100000)
print('Year:{} Month:{} Day:{} Hour:{} Minute:{} Seconds:{}'.format(dtTime.year, dtTime.month, dtTime.day, dtTime.hour, dtTime.minute, dtTime.second))
dtTime12HrsFromNow = dtTime + tdelta
print("Date time 12 hrs from now:{}".format(dtTime12HrsFromNow))

dt = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utc_now = datetime.datetime.utcnow()
#print(dir(datetime.datetime))
print("Date Today:", dt)
print("Date time now:", dt_now)
print("Date time UTC now:", dt_utc_now)



#dt = datetime.datetime(2016, 7, 24, 12, 30, 45, tzinfo=pytz.UTC)
# print(dir(dt))

#dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)

#dt_utcnow2 = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(dt_utcnow2)

# dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
# print(dt_mtn)

dt_mtn = datetime.datetime.now()

#mtn_tz = pytz.timezone('US/Mountain')
#dt_mtn = mtn_tz.localize(dt_mtn)

# print(dt_mtn)

#dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
# print(dt_east)

print(dt_mtn.strftime('%B %d, %Y'))

dt_str = 'July 24, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

# strftime - Datetime to String
# strptime - String to Datetime