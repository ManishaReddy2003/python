#datatypes#
''' 1.int (-1 +1)
    2.float(2.33 decimal points)
    3.boolean(0 flase,1 true)
    4.string('python life')
    5.complex(i+5j)
    6.list[]
    7.tuple()
    8.set{}
    9.dictionary{}
    10.frozen set
    11.none '''

##INTEGER##
a=1
b=-1
print(type(a),type(b))

##FLOAT##
a=5.23
print(type(a))

##boolean##
a=True
b=False
print(type(a),type(b))
print(True==1)
print(False==0)

##complex##
a=2+3j ##real part 2 imaginary part 3##
print(type(a))


###TYPE CONVERSION###
##converting from one data type to another##
#int to float
a=3
print(float(a))
#float to boolean
a=0
print(bool(a))
#float to int
a=5.36
print(int(a))
#int to complex
a=5
print(complex(a))

#data lose----Explicity type conversion
# no data lose---implicity type conversion