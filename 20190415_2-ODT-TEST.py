import os, time
from ezodf import opendoc, Sheet

global listtowrite, resultfile, path, parameterlist, i

path = ("D:\CLEANME")
doc = opendoc("D:\CLEANME\parsme_SPECIAL_CONFIGURATIONS.ods")
resultfile = ("20190416-parsing_result.txt")
sheet = doc.sheets[0]

field = 2
i = 0
listtowrite = ["","","","",""]
parameterlist = [["configname","A"], ["modelname", "G"], ["hardwaretype","E"], ["hardwarename","F"], ["author","B"]]

def get(field):
	global i
	for param in parameterlist:
		print(parameterlist[i][0], parameterlist[i][1], field)
		catch(parameterlist[i][0], parameterlist[i][1], field)
		i+=1
	i = 0
	field+=1
	
def	catch(unit, column, field):
	position = sheet["{0}{1}".format(column, field)]
	if unit == "configname":
		listtowrite[i] = (" {0}{1}{2}{3}".format("\n------","Конфигурация: ", position.value, "\n"))
	elif unit == "modelname":
		listtowrite[i] = (" {0}{1}{2}".format("Название модели: ", position.value, "\n"))
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
	
def	write():
	global i
	filepath = os.path.join(path, resultfile)
	if not os.path.exists(path):
		os.makedirs(path)
	f = open(filepath,'a')
	f.writelines(listtowrite)
	f.close()
#	i+=1

i = 0	
while field < 725:
	get(field)
#	field+=1
	write()