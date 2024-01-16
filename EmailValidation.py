email= input ("Enter Your Email ID: ")
space = 0
uppercase =0
#putting in several conditions that should be met in order for it to be called a valid email id
if len(email)>= 8 : #making sure the email id is atleast of 8 characters in order to ba valid
    if email[0].isalpha(): #making sure first character is an alphabet
        if ("@" in email) and (email.count("@")==1): #ensuring there is not more than one @ used
            #if (email[-4]=="." ^ (email[-3]==".")):
            if (email[-4] == "." or email[-3] == "."):

                for i in email:
                    if i== i.isspace():
                        space=1
                    elif i.isalpha():
                        if i== i.upper():
                            uppercase=1
                        elif i.isdigit():
                            continue
                        elif i=="_" or i=="." or i=="@": #ensuring email contains the mentioned character(s)
                            continue
                        elif (i =="#" or i=="!" or i=="$" or i=="%" or i=="^" or i=="&" or i=="*" or i=="(" or i==")"):
                            print(" Invalid Email ID , ID musn't contain any special charcter apart from '@' , '.' , '_' ")
                        if (uppercase==1):
                            print ("Invalid Email Id , ID musn't contain any uppercase character")
                if (space==1):
                    print("Invalid Email Id , email musn't contain any space character ")

            else:
                print(' Invalid Email Id , must have a \'.\' at 4th or 3rd position from the back ')
        else:
            print("Invalid Email Id, musn't use more than 1 @ ")
    else:
        print("Invalid Email ID, first character must be an alphabet")
else:
    print ("Invalid Email ID, enter atleast 8 characters ")