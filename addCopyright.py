#
#***************************************************************************
#
#*        File name: addCopyright.py                                             
#
#*        File description:
#
#*        Revision history: 
#
#*        Copyright Dagar1994 2018-2019               
#
#***************************************************************************
import os
import subprocess
import fileinput

def Command_Execute(Command):
                process = subprocess.Popen(Command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                (stdout, stderr) = process.communicate()
                SUCCESS_OUTPUT=stdout
                ERROR_OUTPUT=stderr
                return (SUCCESS_OUTPUT)

def String_to_List(STRING):
                LIST=STRING.split()
                return LIST

def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)



def Find_files(EXTENSION,LOCATION):
	Command = "find "+ LOCATION + " -name '*." + EXTENSION + "' -type f"
	out = Command_Execute(Command)
	out = String_to_List(out)
	return out

def Insert_Comment(LOCATION,EXTENSION,Comment_Start,Comment_End):
	File_List=Find_files(EXTENSION,LOCATION)



	for index_f in range(len(File_List)):
             file_name = os.path.basename(File_List[index_f])
	     Copyright_text = "\n***************************************************************************\n\n*        File name: " + file_name + "                                             \n\n*        File description:\n\n*        Revision history: \n\n*        Copyright Dagar1994 2018-2019               \n\n***************************************************************************\n"
             if (Comment_End.strip() == "" ):
		Copyright_text = Copyright_text.splitlines()
		Final_Text = ""
		for index in range (len(Copyright_text)):
			Final_Text = Final_Text + Comment_Start +  Copyright_text[index] + "\n"
	     else :
		Final_Text = Comment_Start + Copyright_text + Comment_End
	     line_prepender(File_List[index_f],Final_Text)
	     print "Adding Copyright to file: " + File_List[index_f]

LOCATION = "."
Insert_Comment(LOCATION,"c","/*","*/")
Insert_Comment(LOCATION,"h","/*","*/")
Insert_Comment(LOCATION,"cs","/*","*/")
Insert_Comment(LOCATION,"css","/*","*/")
Insert_Comment(LOCATION,"cpp","/*","*/")
Insert_Comment(LOCATION,"java","/*","*/")
Insert_Comment(LOCATION,"sql","/*","*/")
Insert_Comment(LOCATION,"php","<?php/*","*/?>")
Insert_Comment(LOCATION,"js","/*","*/")
Insert_Comment(LOCATION,"py","#","")
Insert_Comment(LOCATION,"pl","#","")
Insert_Comment(LOCATION,"vb","'","")
Insert_Comment(LOCATION,"sh","#","")
Insert_Comment(LOCATION,"html","<!--","-->")
Insert_Comment(LOCATION,"xml","<!--","-->")
Insert_Comment(LOCATION,"bat","::","")
