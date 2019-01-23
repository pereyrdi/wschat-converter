#!/usr/bin/python
"""
To replace white spaces with underscore
find -name "* *" -type f | rename 's/ /_/g'

I like to remove this and leave just name in txt file
rename 's/WhatsApp_Chat_con_//' *.txt
rename 's/WhatsApp-Chat_con_//' *.txt
rename 's/WhatsApp_Chat_con-//' *.txt
rename 's/WhatsApp_Chat_//' *.txt
rename 's/WhatsApp-Chat-con-//' *.txt
rename 's/WhatsApp_Chat_con_//' *.txt

"""
import sys
import glob
import datetime

def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%d/%m/%Y')
    except ValueError:
        return False
    return True 

for fname in glob.glob("txt/*.txt"):
    print(fname)

#print(len(sys.argv))
#print(str(sys.argv))
#if len(sys.argv) > 1:
    #fname=sys.argv[1]
    name=fname.split("/")[1]
    name=name.split(".")
    #name=fname.replace("_"," ")

    fhtml = open('/destiny_path/'+name[0]+'.html', 'w+')

    fhtml.write("<!DOCTYPE html><head><meta http-equiv='Content-Type' content='text/html; charset=UTF-8'><link rel='stylesheet' type='text/css' href='wassap.css'></head><body>\n")
    fhtml.write("<div class='page'><div class='screen'><div class='screen-container'><div class='chat'><div class='chat-container'><div class='user-bar'><div class='back'><i class='zmdi zmdi-arrow-left'></i></div>\n")
    fhtml.write("<div class='name'><span>{}</span></div></div>".format(name[0].replace("_"," ").replace("-"," ")))


    fhtml.write("<div class='conversation'>\n")
    fhtml.write("<div class='conversation-container'>\n")


    with open(fname) as f:
        for line in f:
            if not (line.startswith("Los mensajes y llamadas")):
                line = line.strip('\n')
                if (len(line) > 0):
                    if validate(line[0:10]):
                        #print(line)
                        timestamp=line[0:24]
                        k = line[26:].split(':')
                        name=k[0]
                        message=k[1].rstrip().replace("<", "-").replace(">", "-")
                        
                        if name == "Diego":
                            fhtml.write("<div class='message sent'>\n")
                            fhtml.write("{}\n".format(message))
                            fhtml.write("<span class='metadata'><span class='time'>{}</span></span>\n".format(timestamp))
                            fhtml.write("</div>\n")

                        else:
                            fhtml.write("<div class='message received'>\n")
                            fhtml.write("{}\n".format(message))
                            fhtml.write("<span class='metadata'><span class='time'>{}<br>{}</span></span>\n".format(timestamp,name))
                            fhtml.write("</div>\n")
                    else:
                        #print(line)
                        fhtml.write("<div class='message received'>\n")
                        fhtml.write("{}\n".format(line))
                        fhtml.write("</div>\n")

    fhtml.write("</div></div></div></div></div></div></div>\n</body>\n</html>\n")
    fhtml.close() 
