# STUDENT NAME: SHRUTI PAGHADAL
# STUDENT ID: 20CE065
# AIM: SWAP CASE
print ("\n------------------------------------PRACTICAL 5-----------------------------------\n")
def swap_case(s): # The string s is the string which is to be modified.
    Output = "";
    #traversing each element of string and converting them to lowercase if they are in uppercase and vice-versa.
    for char in s:
        if(char.isupper()==True):
            Output += (char.lower());
        elif(char.islower()==True):
            Output += (char.upper());
        else:
            Output += char;
    return Output;

if __name__ == '__main__':
    s = input("Enter the string in which you want to swap cases:")
    result = swap_case(s)
    print("The output string after swapping the cases is:", result)
print("\n------------------------------------------END OF PRACTICAL 5-------------------\n")