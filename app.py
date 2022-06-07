import mariadb
from dbcreds import *

# def split_exploits():
#     if user_alias + user_pass != (alias,user_password):
        

conn = mariadb.connect(
                            user=user,
                            host=host,
                            password=password,
                            port=port,
                            database=database
                            )
cursor = conn.cursor

print('Youve Connected to exploit division!')
print('You must login to continue')
def login():
    user_alias = str(input('Please Enter ALIAS : '))
    user_pass = str(input('Please Enter PASSWORD : '))
login()



print('Select from the following options : ')
print('1 : Make an Exploit')
print('2 : See ALL Exploits')
print('3 : See EVERYONE ELSE Exploits')
print('4 : Exit Application')
print('Which will you choose')
user_selection = int(input('1 : ... 2 : ... 3 : ... 4 : '))


while True:
    if user_selection == 1:
        int(user_selection) == 1
        print('Make an Exploit!! ')
        exploit = input('... : ')
        cursor.execute('INSERT INTO exploits (content) VALUES (?)', [exploit])
        conn.commit()
        print('Nice !! Exploit Completed : {} '.format(post))
    elif user_selection == 2:
        int(user_selection) == 2
        print('See ALL Exploits! ')
        cursor.execute('SELECT content FROM exploits')
        allExploits = cursor.fetchall()
        print(allExploits)
    elif user_selection == 3 :
        int(user_selection) == 3
        print('See EVERYONE ELSE Exploits')
    elif user_selection == 4 :
        int(user_selection) == 4
        print('Exiting Application now')
    conn.close()