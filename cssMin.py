"""
"""

print("Minimizador de CSS!")

import os
import tempfile

filePath = 'arquivo.css'

def removeComments(filePath):
    file = open(filePath,'r')
    text = file.readlines()
    file.close()
    
    blockComment = False 
    line = ""
    for f in text:
        #line = ""
        lineComment = False 
        mark = False
        blockMark = False
        for let in f:
            if lineComment:
                break
            else:
                if let == '/':
                    if mark:
                        if not blockMark:
                            lineComment = True
                            mark = False
                    elif not blockMark:
                        mark = True
                elif let == "*":
                    if blockComment:
                        blockMark = True;
                        blockComment = False
                    else:
                        blockComment = True
                else:
                    if not blockComment:
                        line = line + let
                        
    fileTmp = open(filePath+'-temp','w' )
    fileTmp.write(line)
    fileTmp.close()
    

def removeSpacesLineBreakers(filePath):
    fileTmp = open(filePath+'-temp','r' )
    text = fileTmp.readlines()    
    fileTmp.close()
    os.remove(filePath+'-temp')
    
    oneLine = ""
    for f in text:
        f = f.replace('\n',' ')
        f = f.replace('} ','}')
        f = f.replace('{ ','{')
        f = f.replace('; ',';')
        f = f.replace(' .','.')
        f = f.replace(' #','#')

        oneLine = oneLine + f
        
    file2 = open(os.path.splitext(filePath)[0] + ".min.css",'w')
    file2.write(oneLine)
    file2.close()

##############################################################

#Removendo Comentarios 
print("Removendo Comentarios")
removeComments(filePath)


#removendo quebras de linha
print("Removendo quebras de linha")
removeSpacesLineBreakers(filePath)

print("Minimizador de CSS!")


