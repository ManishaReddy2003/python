
##variable##
# which will store value or address value 

##SYNTAX##
# Variable = value
  #for example ;  x = 100  here x= variable,100 = value,213001= memeory location we can find memory location id()

##RULES IN VARIBLES ##
''' 1.Dont start with numbers & symbols  
        # example : 123ab=c , @123=abc 
    2.starting letter with  be alphabets and underscore  
       # example : _abc=0 , _ab12=1 ,  
    3. case sensitive 
        # example : a=python we call with python only in small letetrs if we call a=PYTHON it shoud be not accepted '''
x=5
print(x)

# multiple variables not stored in single value
a,b,c=1,2,3
print(a,b,c)

#multiple values can be stored in single variable 
c=1,2,3
print(c)

#single value can be stored in multiple variables
c=y=v=22
print(c)
print(v)
print(y)

abc=4
print(id(abc))