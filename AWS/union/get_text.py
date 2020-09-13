import boto3,os
from _pdf import *
from _image import *


s3BucketName = "text-demo-peor-equipo"
#documentName = "ttt.png"
#s3BucketName = input()

name = "tarea"
#l = ".txt"
num = 0
while True:
    try:

        cad = input().split(".")
        num += 1
        n = name + str(num)
        os.chdir('tareas')
        #os.system('pwd')
        f= open(n,"w+")
        ext = cad[1]
        documentName = str(cad[0]+"."+cad[1])
        #print(documentName,ext)
        #print(name)
        print(cad)
        
        if ext == "png":
            text = get_textImage(s3BucketName,documentName)
            for i in text:
                f.write(i)
            #f.write("\n")
            #print(text)
        else:

            text = get_textPdf(s3BucketName,documentName)

            for i in text:
                f.write(i)

            #f.write("\n")
            #print(text)
        
        f.close()

        os.chdir('..')
    except EOFError:
        break

