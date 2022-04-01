#Sri Tarun Gulumuru
#duration:20 mins
#Question 3

def encrypt(s):

    f=open("textfile.txt","r")
    encrypt=open("encrypt.txt","w")

    data=f.read()

    for i in range(len(data)):
        val=ord(data[i])

        if data[i].isalpha() and data[i].isupper():
            val= val+s

            if val>90:
                val=64+(val-90)

        elif data[i].isalpha() and data[i].islower():
             val= val-s

             if val<97:
                 val=123-(97-val)

        elif data[i].isdigit():
            val=val-s

            if val<48:
                val=58-(48-val)

        encrypt.write(chr(val))

    f.close()
    encrypt.close()

def decrypt(s):

    encrypt=open("encrypt.txt","r")

    f=open("textfile.txt","w")

    data=encrypt.read()

    for i in range(len(data)):
        val=ord(data[i])

        if data[i].isalpha() and data[i].isupper():
            val=val-s

            if val<65:
                val=91-(65-val)

        elif data[i].isalpha() and data[i].islower():
            val=val+s

            if val>122:
                val=96+(val-122)

        elif data[i].isdigit():
            val=val+s

            if val>57:
                val= 47+(val-57)

        f.write(chr(val))

    encrypt.close()
    f.close()


encrypt(1)
decrypt(1)














        
