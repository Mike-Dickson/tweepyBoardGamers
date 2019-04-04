import pyodbc


server = '13.66.153.161'
database = 'russreed'
username = 'michaeldickson1'
password = 'SharingMyPassword2019*'


connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database
connection_string = connection_string + ';UID=' + username + ';PWD=' + password

openConnection = pyodbc.connect(connection_string, timeout=60)
openCursor = openConnection.cursor() ##This is our way of passing stuff to and from the database.

sqlString = 'SELECT PersonId, FullName from Application.People WHERE isEmployee = 1'
openCursor.execute(sqlString)
myDataset = openCursor.fetchall()

for row in myDataset:
    print(row.FullName)

UserName = 'Bob Donut'
UserLocation = 'California'
UserFriends = 341
UserFollowers = 13013
TweetText = 'Had a new donut today. Had gumballs and gummy worms on it. Wasnt my favorite.'

sqlString = 'INSERT Tweets (UserName, UserLocation, UserFriends, UserFollowers, TweetText) VALUES (?, ?, ?, ?, ?)'
args = Tweet, UserName

openConnection.execute(sqlString, args)
openConnection.commit()

openCursor.close()
openConnection.close()

