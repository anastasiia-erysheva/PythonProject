import csv
import datetime
from collections import namedtuple
Meeting = namedtuple('Meeting', ('surname', 'name', 'meeting_date', "meeting_time"))
meetings_list = []
with open("meetings.csv", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        meeting_data = Meeting(*row)
        meetings_list.append(meeting_data)
sorted_meetings = sorted(meetings_list, key=lambda x: (datetime.datetime.strptime(x.meeting_date, "%d.%m.%Y"), datetime.datetime.strptime(x.meeting_time,  "%H:%M")))
for meeting in sorted_meetings:
    print(meeting.surname, meeting.name)

