#
# header comment! Overview, name, etc.
# Daniyal Khokhar

import sqlite3
import matplotlib.pyplot as plt


def command_9(dbCursor):
  print("")
  color = input("Enter a line color (e.g. Red or Yellow): ")
  #sql = "Select Distinct Stations.Station_Name, Stops.Latitude, Stops.Longitude, Stops.ADA from Stations Join Stops On Stops.Station_ID = Stations.Station_ID Join StopDetails On StopDetails.Stop_ID = Stops.Stop_ID Join Lines on StopDetails.Line_ID = Lines.Line_ID where Lines.Color Like ? Order by Station_Name asc;"
  sql = "Select Stations.Station_Name, Stops.Latitude, Stops.Longitude, Stops.ADA from Stations Join Stops On Stops.Station_ID = Stations.Station_ID Join StopDetails On StopDetails.Stop_ID = Stops.Stop_ID Join Lines on StopDetails.Line_ID = Lines.Line_ID where Lines.Color Like ? Group by Stations.Station_Name Order by Station_Name asc;"
  dbCursor.execute(sql, [color])
  rows = dbCursor.fetchall()
  if (len(rows) == 0):
    print("**No such line...")
    return 0
  else:
    for row in rows:
      print(row[0], ":", f"({row[1]},", f"{row[2]})")
  print("")
  plot = input("Plot? (y/n) ")
  if (plot == "y"):
    x = []  # create 2 empty vectors/lists
    y = []

    for row in rows:  # append each (x, y) coordinate that you want to plot
      x.append(row[2])
      y.append(row[1])

    image = plt.imread("chicago.png")
    xydims = [-87.9277, -87.5569, 41.7012, 42.0868]  # area covered by the map:
    plt.imshow(image, extent=xydims)

    plt.title(color + " line")
    #
    # color is the value input by user, we can use that to plot the
    # figure *except* we need to map Purple-Express to Purple:
    #
    if (color.lower() == "purple-express"):
      color = "Purple"  # color="#800080"

    plt.plot(x, y, "o", c=color)
    #
    # annotate each (x, y) coordinate with its station name:
    #
    for row in rows:
      plt.annotate(row[0], (row[2], row[1]))

    plt.xlim([-87.9277, -87.5569])
    plt.ylim([41.7012, 42.0868])

    plt.show()

  dbCursor.close()


def command_8(dbCursor):
  year = input("Year to compare against? ")
  st1 = input("Enter station 1 (wildcards _ and %): ")
  st2 = input("Enter station 2 (wildcards _ and %): ")
  #year = 2020
  #st1 = "%uic%"
  #st2 = "%sox%"
  sql = "Select station_ID, Station_Name from Stations where Station_Name Like ?;"  #Collect station Id and Name
  dbCursor.execute(sql, [st1])
  st1IdName = dbCursor.fetchone()

  dbCursor.execute(sql, [st2])
  st2IdName = dbCursor.fetchone()

  if (len(st2IdName) > 2 or len(st1IdName) > 2):  #Check for errors in input
    print("**Multiple stations found...")
    return 0
  elif (len(st2IdName) == 0 or len(st1IdName) == 0):
    print("**No station found...")
    return 0

  sql2 = "Select date(ride_date), Ridership.Num_Riders from Ridership Join Stations On Stations.Station_ID = Ridership.Station_ID Where Stations.Station_Name Like ? And strftime('%Y', Ride_Date) = ? Order by date(Ride_Date) asc;"  #Collect date, riders

  dbCursor.execute(sql2, [st1, str(year)])
  st1data = dbCursor.fetchall()

  print("Station 1:", st1IdName[0],
        st1IdName[1])  #Print first Station Name and ID

  for i in range(5):  #get first 5
    print(st1data[i][0], st1data[i][1])

  for i in range(len(st1data) - 5, len(st1data)):  # last 5
    print(st1data[i][0], st1data[i][1])

  #Now for Station 2

  dbCursor.execute(sql2, [st2, str(year)])
  st2data = dbCursor.fetchall()

  print("Station 2:", st1IdName[0],
        st1IdName[1])  #Print first Station Name and ID

  for i in range(5):
    print(st2data[i][0], st2data[i][1])

  for i in range(len(st2data) - 5, len(st2data)):  # last 5
    print(st2data[i][0], st2data[i][1])

  plot = input("Plot? (y/n) ")
  if (plot == "y"):
    x = []  # create 2 empty vectors/lists
    y = []

    day = 1
    for row in st1data:  # append each (x, y) coordinate that you want to plot
      x.append(day)
      y.append(row[1])
      day += 1

    day = 1
    for row in st2data:  # append each (x, y) coordinate that you want to plot
      x.append(day)
      y.append(row[1])
      day += 1

    plt.ioff()
    plt.xlabel("Day")
    plt.ylabel("Number of Riders")
    plt.title("Daily Ridership Data")
    plt.legend([st1IdName[0], st2IdName[0]])
    plt.plot(x, y)
    plt.show()

  dbCursor.close()


def command_7(dbCursor):
  print("** ridership by year **")

  sql = "Select strftime('%Y', Ride_Date), sum(Num_Riders) from Ridership GROUP BY strftime('%Y', Ride_Date) Order by strftime('%y', Ride_Date) asc;"

  dbCursor.execute(sql)
  rows = dbCursor.fetchall()
  for row in rows:
    print(row[0], ":", f"{row[1]:,}")

  plot = input("Plot? (y/n) ")
  if (plot == "y"):
    x = []  # create 2 empty vectors/lists
    y = []

    for row in rows:  # append each (x, y) coordinate that you want to plot
      x.append(row[0])  #FIX HERE NUMBERS off
      y.append(row[1])

    plt.xlabel("Year")
    plt.ylabel("Number of Riders * 10^8")
    plt.title("Annual Ridership Data")
    plt.plot(x, y)
    plt.show()

  dbCursor.close()


def command_6(dbCursor):
  print("** ridership by month **")

  sql = "Select strftime('%m', Ride_Date), sum(Num_Riders) from Ridership GROUP BY strftime('%m', Ride_Date) Order by strftime('%m', Ride_Date) asc;"
  dbCursor.execute(sql)
  rows = dbCursor.fetchall()
  for row in rows:
    print(row[0], ":", f"{row[1]:,}")

  print("")
  plot = input("Plot? (y/n) ")
  if (plot == "y"):
    x = []  # create 2 empty vectors/lists
    y = []

    for row in rows:  # append each (x, y) coordinate that you want to plot
      x.append(row[0])
      y.append(row[1])

    plt.xlabel("Month")
    plt.ylabel("Number of Riders * 10^8")
    plt.title("Monthly Ridership Data")
    plt.plot(x, y)
    plt.show()

  dbCursor.close()


def command_5(dbCursor):
  print("")
  color = input("Enter a line color (e.g. Red or Yellow): ")

  sql = "Select Stops.Stop_Name, Stops.Direction, Stops.ADA from Stops Join StopDetails On Stops.Stop_ID = StopDetails.Stop_ID Join Lines On StopDetails.Line_ID = Lines.Line_ID where Lines.Color Like ? Order by Stops.Stop_Name asc;"

  dbCursor.execute(sql, [color])
  rows = dbCursor.fetchall()
  if (len(rows) == 0):
    print("**No such line...")
  else:
    for row in rows:
      if (row[2] == 1):
        ADA = "(accessible? yes)"
      else:
        ADA = "(accessible? no)"
      print(row[0], ":", "direction = ", row[1], ADA)

  dbCursor.close()


def command_4(dbCursor):
  print("** least-10 stations **")

  sql = "Select Station_Name, sum(Num_Riders) from Stations Join Ridership on Stations.Station_ID = Ridership.Station_ID Group by Station_Name Order By sum(Num_Riders) asc limit 10;"

  dbCursor.execute(sql)
  rows = dbCursor.fetchall()

  totalSQL = "Select sum(Num_Riders) from Ridership;"
  dbCursor.execute(totalSQL)
  total = dbCursor.fetchone()
  for row in rows:
    print(row[0], ":", f"{row[1]:,}", f"({row[1]/total[0]*100:.2f}%)")

  dbCursor.close()


def command_3(dbCursor):
  print("** top-10 stations **")

  sql = "Select Station_Name, sum(Num_Riders) from Stations Join Ridership on Stations.Station_ID = Ridership.Station_ID Group by Station_Name Order By sum(Num_Riders) desc limit 10;"

  dbCursor.execute(sql)
  rows = dbCursor.fetchall()

  totalSQL = "Select sum(Num_Riders) from Ridership;"
  dbCursor.execute(totalSQL)
  total = dbCursor.fetchone()
  for row in rows:
    print(row[0], ":", f"{row[1]:,}", f"({row[1]/total[0]*100:.2f}%)")

  dbCursor.close()


def command_2(dbCursor):
  print("** ridership all stations **")

  sql = "Select Station_Name, sum(Num_Riders) From Stations Join Ridership on Stations.Station_ID = Ridership.Station_ID Group by Station_Name Order By Station_Name asc;"
  dbCursor.execute(sql)
  rows = dbCursor.fetchall()

  totalSQL = "Select sum(Num_Riders) from Ridership;"
  dbCursor.execute(totalSQL)
  total = dbCursor.fetchone()
  for row in rows:
    print(row[0], ":", f"{row[1]:,}",
          f"({row[1]/total[0]*100:.2f}%)")  #NEEDS FIX, PERCENTAGE ISSUE

  dbCursor.close()
  #print(stationname, ":", f"{ridership:,}", f"({percentage:.2f}%)")


def command_1(dbCursor):
  print("")
  str = input("Enter partial station name (wildcards _ and %): ")
  sql = """Select Station_ID, Station_Name From Stations Where Station_Name Like ? Order By Station_Name asc;"""
  dbCursor.execute(sql, [str])
  rows = dbCursor.fetchall()
  if (len(rows) == 0):
    print("**No stations found...")
  else:
    for row in rows:
      print(row[0], ":", row[1])

  dbCursor.close()


##################################################################
#
# print_stats
#
# Given a connection to the CTA database, executes various
# SQL queries to retrieve and output basic stats.
#


def get_data_seg(sql):
  dbCursor = dbConn.cursor()
  dbCursor.execute(sql)
  row = dbCursor.fetchone()
  return row[0]


def print_stats(dbConn):
  dbCursor = dbConn.cursor()

  print("General stats:")

  dbCursor.execute("Select count(*) From Stations;")
  row = dbCursor.fetchone()
  print("  # of stations:", f"{row[0]:,}")

  sql = "Select count(Stop_ID) from Stops;"
  print("  # of stops:", f"{get_data_seg(sql):,}")

  sql = "Select count(Station_ID) from Ridership;"
  print("  # of ride entries:", f"{get_data_seg(sql):,}")

  dbCursor.execute(
    "Select MIN(date(Ride_Date)), '-' , MAX(date(Ride_Date)) from Ridership;"
  )  # date range
  row = dbCursor.fetchone()
  print("  date range:", f"{row[0]}", row[1], row[2])

  sql = "Select sum(Num_Riders) from Ridership;"
  print("  Total ridership:", f"{get_data_seg(sql):,}")
  tempTotal = get_data_seg(sql)
  #FIXES NEEDED, PERCENTAGE ISSUES
  sql = "Select sum(Num_Riders) from Ridership where Type_of_Day = 'W';"
  tempWkday = get_data_seg(sql)
  print("  Weekday ridership: "
        f"{get_data_seg(sql):,}", f'({tempWkday / tempTotal*100:.2f}%)')

  dbCursor.execute(
    "Select sum(Num_Riders) from Ridership where Type_of_Day = 'A';"
  )  # total num riders weekday
  sql = "Select sum(Num_Riders) from Ridership where Type_of_Day = 'A';"
  tempSat = get_data_seg(sql)
  print("  Saturday ridership: "
        f"{get_data_seg(sql):,}", f'({ tempSat / tempTotal*100:.2f}%)')

  sql = "Select sum(Num_Riders) from Ridership where Type_of_Day = 'U';"
  tempSun = get_data_seg(sql)
  print("  Sunday/holiday ridership: "
        f"{get_data_seg(sql):,}", f'({ tempSun / tempTotal*100:.2f}%)')

  #print("  # of stations:", f"{row[1]:,}")

  dbCursor.close()


##################################################################
#
# main
#
print('** Welcome to CTA L analysis app **')
print()

dbConn = sqlite3.connect('CTA2_L_daily_ridership.db')

print_stats(dbConn)
while (True):
  print("")
  val = input("Please enter a command (1-9, x to exit): ")
  dbCursor = dbConn.cursor()
  if (val.isdigit()):
    if (int(val) == 1):
      command_1(dbCursor)
    elif (int(val) == 2):
      command_2(dbCursor)
    elif (int(val) == 3):
      command_3(dbCursor)
    elif (int(val) == 4):
      command_4(dbCursor)
    elif (int(val) == 5):
      command_5(dbCursor)
    elif (int(val) == 6):
      command_6(dbCursor)
    elif (int(val) == 7):
      command_7(dbCursor)
    elif (int(val) == 8):
      command_8(dbCursor)
    elif (int(val) == 9):
      command_9(dbCursor)
    else:
      print("**Error, unknown command, try again...")
  else:
    if (val == "x"):  #Error here
      dbCursor.close()
      exit()
    else:
      print("**Error, unknown command, try again...")

#
# done
#
