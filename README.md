# Commands
### command_1(dbCursor)

    Purpose: Allows the user to search for stations by a partial station name using wildcards (_ and %).
    Steps:
        Prompts the user for partial station name input.
        Executes a SQL query to retrieve matching station names and IDs.
        Prints the results.
        Closes the database cursor.

### command_2(dbCursor)

    Purpose: Displays total ridership for all stations, sorted by station name.
    Steps:
        Executes a SQL query to get the total ridership for each station.
        Prints the station names and their ridership totals, including percentages.
        Closes the database cursor.

### command_3(dbCursor)

    Purpose: Displays the top 10 stations by ridership.
    Steps:
        Executes a SQL query to get the top 10 stations by ridership.
        Prints the station names and their ridership totals, including percentages.
        Closes the database cursor.

### command_4(dbCursor)

    Purpose: Displays the least 10 stations by ridership.
    Steps:
        Executes a SQL query to get the bottom 10 stations by ridership.
        Prints the station names and their ridership totals, including percentages.
        Closes the database cursor.

### command_5(dbCursor)

    Purpose: Displays information about stops on a specific line.
    Steps:
        Prompts the user to enter a line color.
        Executes a SQL query to retrieve stop information for the specified line.
        Prints the stop names, directions, and ADA accessibility.
        Closes the database cursor.

### command_6(dbCursor)

    Purpose: Displays ridership data grouped by month.
    Steps:
        Executes a SQL query to get ridership totals for each month.
        Prints the monthly ridership data.
        Prompts the user to plot the data.
        If yes, plots the data using matplotlib.
        Closes the database cursor.

### command_7(dbCursor)

    Purpose: Displays ridership data grouped by year.
    Steps:
        Executes a SQL query to get ridership totals for each year.
        Prints the yearly ridership data.
        Prompts the user to plot the data.
        If yes, plots the data using matplotlib.
        Closes the database cursor.

### command_8(dbCursor)

    Purpose: Compares daily ridership data for two stations in a given year.
    Steps:
        Prompts the user for a year and two station names.
        Executes SQL queries to retrieve and validate the stations.
        Fetches ridership data for the specified stations and year.
        Prints the ridership data for the first and last five days of the year.
        Prompts the user to plot the data.
        If yes, plots the data using matplotlib.
        Closes the database cursor.

### command_9(dbCursor)

    Purpose: Displays and optionally plots station locations for a specified line color.
    Steps:
        Prompts the user to enter a line color.
        Executes a SQL query to retrieve station locations for the specified line.
        Prints the station names and their coordinates.
        Prompts the user to plot the data.
        If yes, plots the data using matplotlib, overlaying it on a map of Chicago.
        Closes the database cursor.
