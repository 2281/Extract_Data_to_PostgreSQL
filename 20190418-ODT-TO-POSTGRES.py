from ezodf import opendoc, Sheet
import psycopg2
#conn.autocommit = True

#TODO login/pass to config file
conn = psycopg2.connect(dbname='postgres', user='postgres',
                        password='12345', host='localhost')

cursor = conn.cursor()

conn.autocommit = True

#cursor.execute('SELECT * FROM twitter WHERE sentiment > 8')
#"INSERT INTO test (num, data) VALUES (%s, %s)",
#...      (100, "abc'def"))
#    print(row)

global listtowrite, resultfile, path, parameterlist, i

path = ("")
doc = opendoc("test.ods")
sheet = doc.sheets[0]

listtowrite = ["","","","",""]
field = 2
i = 0

parameterlist = [["configname","A"], ["modelname", "G"], ["hardwaretype","E"], ["hardwarename","F"], ["author","B"]]

def get(field):
    global i
    for param in parameterlist:
        catch(parameterlist[i][0], parameterlist[i][1], field)
        try:
            i <= len(parameterlist)
            i+=1
        except:
            pass
  
def catch(unit, column, field):
    position = sheet["{0}{1}".format(column, field)]
    if unit == "configname":
        listtowrite[i] = (" {0}{1}{2}".format("\n", position.value, "\n"))
    elif unit == "modelname":
        listtowrite[i] = (" {0}{1}".format(position.value, "\n"))
#    elif unit == "hardwaretype":
#        listtowrite[i] = ("{0}: ".format(position.value))
    elif unit == "hardwaretype":
        listtowrite[i] = ("{0}: ".format(position.value))

    elif unit == "hardwarename":
        listtowrite[i] = ("{0}{1}".format(position.value, "\n"))
    elif unit == "author":
        listtowrite[i] = (" {0}{1}{2}{3}".format( "Автор: ",position.value,"\n", "\n", "\n"))
    if (position.value_type) is None and unit == "hardwarename":
        listtowrite[i] = (" \n")
    if (position.value_type) is None and unit != "hardwarename":
        listtowrite[i] = (" ")

def writetopostgres():
#    INSERT INTO project_configs VALUES('PythonScript-ADD-TEST', '', 'hardwaretype: Materinka - 2242', 'Author: DSSL');
    try:
        cursor.execute("INSERT INTO project_configs VALUES('PythonScript-ADD-TEST', 'yyy', 'Materinka', 'Author: DSSL');")
    except ValueError:
        print("Error in function")

writetopostgres()
cursor.close()
conn.close()
