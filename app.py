import dbcreds
import mariadb

# functions for each selection
def MakeBlogPost(): 
  content = input("Add blog content: ")
  conn = mariadb.connect(user = dbcreds.user, password = dbcreds.password, host = dbcreds.host, port = dbcreds.port, database = dbcreds.database)
  cursor = conn.cursor()
  cursor.execute("INSERT INTO blog_post(username, content, id) VALUES(?, ?, NULL)", [username, content])
  conn.commit()
  print("Your blog post has been added!")
  cursor.close()
  conn.close()

def AllBlogPosts():
  conn = mariadb.connect(user = dbcreds.user, password = dbcreds.password, host = dbcreds.host, port = dbcreds.port, database = dbcreds.database)
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM blog_post")
  rows = cursor.fetchall()
  print(rows)
  cursor.close()
  conn.close()

# prompt user to add username and make selection
print("Welcome to Command Line Blog! Add username and select a number: ")
username = input("Username: ")
userSelection = input("1. Write a new blog post \n2. View all blog posts ")

if userSelection == "1":
  MakeBlogPost()
elif userSelection == "2":
  AllBlogPosts()
else:
  print("There was an error, please start again")