#commands to demonstrate how to access and perform operations on a main file

import code as x 
#importing the main file as a library 

x.create("nivedita",25)
x.create("src",70,3600) 
x.read("nivedita")
x.read("src")
x.create("nivedita",50)
x.modify("nivedita",55)
x.delete("nivedita")


t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
t2.start()
t2.sleep()
