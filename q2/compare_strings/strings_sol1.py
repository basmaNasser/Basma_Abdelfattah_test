def strings(s1,s2):
            s1,s2=check_input(s1,s2)
  
            if s1>s2:
                print ("string1 ("+str(s1)+") greater than string2("+str(s2)+")")
            elif s1< s2:
                print ("string1 ("+str(s1)+") less than string2("+str(s2)+")")
            else:
                print ("string1 ("+str(s1)+") equal string2("+str(s2)+")")
        
#function check if the input is string or not
# if the input is string with one integer it will send  integer value
def check_input(s1,s2):
    try:
        if len(s1)>1 and len(s2)>1:
            return (s1,s2)
        elif len(s1)>1 or len(s2)>1:
             return (s1,s2)
        else:
            return(int(s1),int(s2))
    except TypeError:
          print("one of the values you entered was not a string")        

strings('1.2.3.0','1.2.3')
"""
test cases:
'1.0','1.0'
'1.1','1.2'
'1.2', '-1.4'
'1.2.1', '1.2.0'
'1.5.1.0', '1.2.0'
'1.5.1.0', '1.2.0.6'
'2','10'
'1.1', '0'
'1.1', 9
"""
