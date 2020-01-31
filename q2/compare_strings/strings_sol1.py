def strings(s1,s2):
    
            s1,s2 = check_input(s1,s2)
  
            if s1>s2:
               return("string1 ("+str(s1)+") greater than string2 ("+str(s2)+")")
            elif s1< s2:
               return("string1 ("+str(s1)+") less than string2 ("+str(s2)+")")
            else:
                return ("string1 ("+str(s1)+") equal string2 ("+str(s2)+")")
        
#function check if the input is string or not
# if the input is string with one integer it will send  integer value

def check_input(s1,s2):
    try:
        #if both strings are not int will return them as strings
        if len(s1)>1 and len(s2)>1:
            return (s1,s2)
        
         #if one of the strings are not int will return them as strings
        elif len(s1)>1 or len(s2)>1:
             return (s1,s2)
            
        #if both strings are int will return them as integers
        else:
            return(int(s1),int(s2))
        
    except TypeError:
         return("one of the values you entered was not a string")        


