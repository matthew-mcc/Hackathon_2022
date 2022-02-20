# Calgary Hacks Hackathon - 2022

--------------------------------

# Go-Go Eco! - A Sustainable Car-Pool Scheduler for businesses.

Introducing Go-Go Eco!, a sustainable solution to commercial commuting. Go-Go Eco! is a web based carpool scheduler aimed at providing companies a way to keep their employees connected, we accomplish this by reducing their carbon footprint and help their employees find a safe and easy ride to work. Our project is designed in a way that allows a multitude of companies to access our features using our website and SQL database, with the end goal of licensing one project to many clients. Go-Go Eco! allows employees to opt in or out of the carpool program, or even choose to be the driver. There is an authentication system for employees which is stored in our database. Once logged into the system, employees can see the pickup schedule and locations that have been generated and see who the current driver is for that day. All of the groups are color coordinated and the driver node is increased in size for legibility. There is also a drop down box showing all groups, the members of the group with their respective pickup order and the driver for the current day. Drivers rarely have to veer far from home. The pickup schedule is generated in a way to maximize occupancy, and spend the least amount of time commuting to the company headquarters, shown in green. All of the features are conveniently displayed on a three dimensional, interactive, easy on the eyes map. Go-Go Eco! strives to reduce the carbon footprint of commuting heavy companies, while maintaining efficiency and employee relations all at an extremely low cost of entry.


# Software / libraries used:
- Python 3.9
- Django Web Framework - _python, CSS, HTML, JS_
- Geopy - _python_
- MySQL
- SQLLite
- Pandas - _python_
- Numpy - _python_

# __USAGE__
1. Clone this repository on to your hard drive.
2. To start up the website, simply navigate to the manage.py file located in website/setup.
3. Run the command "python manage.y runserver"
4. Connect to the local host in your browser, the correct ip address will be located in the terminal at launch.
5. Change the SQL database to add your employees and schedules, and press the refresh button to start the scheduling.
Note: Sometimes the Geopy library is being used by many users at once, and as such it can take as much as 20 seconds to run properly.

# Further Implementation:
Ideas include:
- Ranking system to provide rewards to employees who offer the most drives.
- Better group selector/visualizer.
- Including more modes of transportation such as busses, planes etc...
- Add a visualizing path / route line.

# Version
Currently in Version Alpha 1.0.

# Collaborators:
Matthew McConnell,
Kevin Van,
Vanessa Chen,
Kenny Jeon,
Gustavo Bravo

Made for the 2022 Calgary Hacks Hackathon competition.
