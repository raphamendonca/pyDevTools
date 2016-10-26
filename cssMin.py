"""

"""

print("Minimizador de CSS!")

pen('arquivo.css','r')
file2 = open('arquivo2.css','w')


blockComment = False 

for f in file.readlines():
    line = ""
    lineComment = False 
    mark = False
    blockMark = False
    for let in f:
        
        if lineComment:
            #print("comentario linha")
            break
        else:
            if let == '/':
                if mark:
                    if not blockMark:
                        lineComment = True
                        mark = False
                        #print("mark")
                elif not blockMark:
                    #print("nao é comentario bloco")
                    mark = True
                    
            elif let == "*":
                if blockComment:
                    #print("comentario bloco fim")
                    blockMark = True;
                    blockComment = False
                    
                else:
                #    print("comentario bloco inicio")
                    blockComment = True
            else:
                if not blockComment:
                #    print(let)
                    line = line + let
            
    file2.write(line)

file.close()

file2.close()



