Python 3.7.3 (default, Mar 27 2019, 17:13:21) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
======================= RESTART: C:/Users/User/code.py =======================
>>> import code as x
>>> 
>>> x.create("kolkata",25)
>>> x.create("bangalore",50,120)
>>> 
>>> x.read("kolkata")
'kolkata:25'
>>> x.read("bangalore")
'bangalore:50'
>>> 
>>> x.read("kolkata")
'kolkata:25'
>>> x.read("bangalore")
error: time-to-live of bangalore has expired
>>> 
>>> x.delete("bangalore")
error: time-to-live of bangalore has expired
>>> 
>>> x.modify("kolkata",60)
>>> x.read("kolkata")
'kolkata:60'
>>> 
>>> x.delete("kolkata")
key is successfully deleted
>>> 
>>> x.read("kolkata")
error: given key does not exist in database. Please enter a valid key
>>> 
======================= RESTART: C:/Users/User/code.py =======================
>>> import code as x
>>> 
>>> x.create("delhi",25)
>>> 
>>> x.create("delhi",40)
error: this key already exists
>>> 
>>> x.read("dellhi")
error: given key does not exist in database. Please enter a valid key
>>> x.read("delhi")
'delhi:25'
>>> 
>>> x.create("pune62place",21)
error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers
>>> x.create("pune@place",45)
error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers
>>> x.create("pune place",78)
error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers
>>> x.create("puneplace",55)
>>> x.read("puneplace")
'puneplace:55'
>>> 
>>> 
>>> x.read("delhi")
'delhi:25'
>>> x.delete("delhi")
key is successfully deleted
>>> x.read("delhi")
error: given key does not exist in database. Please enter a valid key
>>> 
