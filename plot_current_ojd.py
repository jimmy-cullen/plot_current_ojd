import urllib, json, datetime
import matplotlib.pyplot as plt


url = "http://130.88.9.19:8080/ojd/current"

response = urllib.urlopen(url)

data = json.loads(response.read())

# look at the data we have:
#
# In [38]: for a in data[0].keys():
#    ....:     print a
#    ....:
# scheduleDetail
# endTime
# name
# startTime
# id


# all the interesting stuff is in scheduleDetail
#
# In [39]: for a in data[0]['scheduleDetail'][0].keys():
#     print a
#    ....:
# startEl
# src
# driveReversedForStops
# endAz
# driveDuration
# observedThroughStops
# startAz
# stopsDirection
# driveDirection
# experiment
# subArrayConfig
# startTime
# obsId
# endEl
# endTime
# 
# In [40]

# plot data


start_time_list = [scan['startTime'] for scan in data[0]['scheduleDetail']]
end_time_list = [scan['endTime'] for scan in data[0]['scheduleDetail']]
startEl_list = [scan['startEl'] for scan in data[0]['scheduleDetail']]
endEl_list = [scan['endEl'] for scan in data[0]['scheduleDetail']]
startAz_list = [scan['startAz'] for scan in data[0]['scheduleDetail']]
endAz_list = [scan['endAz'] for scan in data[0]['scheduleDetail']]


stl = [datetime.datetime.strptime(item, '%Y-%m-%dT%H:%M:%S.%fZ') for item in start_time_list]
etl = [datetime.datetime.strptime(item, '%Y-%m-%dT%H:%M:%S.%fZ') for item in end_time_list]



# create a list of lists containing start and end times
time_list = []

for a in range(len(start_time_list)):
  time_list.append([stl[a], etl[a]])


# create a list of lists containing start and end elevations
el_list = []

for a in range(len(startEl_list)):
  el_list.append([startEl_list[a], endEl_list[a]])


# create a list of lists containing start and end azimuth
az_list = []

for a in range(len(startEl_list)):
  az_list.append([startAz_list[a], endAz_list[a]])



for a in range(len(time_list)):
  ax1 = plt.subplot(211)
  plt.plot(time_list[a],az_list[a])
  plt.grid(True)
  plt.ylabel('Azimuth (Degrees)')
  plt.xlabel('UT')
  plt.title('Azimuth vs Time')

  plt.subplot(212, sharex=ax1)
  plt.plot(time_list[a],el_list[a])
  plt.grid(True)
  plt.ylabel('Elevation (Degrees)')
  plt.xlabel('UT')
  plt.title('Elevation vs Time')
  

plt.suptitle(data[0]['name'], fontsize=16)
plt.show()
