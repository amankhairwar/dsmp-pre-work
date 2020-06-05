# --------------
##File path for the file 
file_path 
#Code starts here
def read_file(path):
 file = open(path, 'r')
 sentence = file.readline()
 file.close()
 return sentence
sample_message = read_file(file_path)
# --------------
#Code starts here

message_1 = read_file(file_path_1)
message_2 = read_file(file_path_2)

print(message_1, message_2)

def fuse_msg(message_a, message_b):
 quotient = int(message_b)//int(message_a)
 return str(quotient)

secret_msg_1 = fuse_msg(message_1, message_2) 
# --------------
#Code starts here
message_3 = read_file(file_path_3)
print(message_3)

def substitute_msg(message_c):
 sub = ""
 if message_c == "Red":
  sub = "Army General"
 elif message_c == "Green":
  sub = "Data Scientist"
 elif message_c == "Blue":
  sub = "Marine Biologist"

 return sub 

secret_msg_2 = substitute_msg(message_3)
 # --------------
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here
message_4 = read_file(file_path_4)
message_5 = read_file(file_path_5)

print(message_4, message_5)

def compare_msg(message_d, message_e):
 a_list = message_d.split(" ")
 b_list = message_e.split(" ")
 c_list = []
 c_list = [i for i in a_list if i not in b_list]
 final_msg = " ".join(c_list)
 return final_msg

secret_msg_3 = compare_msg(message_4, message_5)
# --------------
#Code starts here
message_6 = read_file(file_path_6)
print(message_6)
def extract_msg(message_f):
 a_list = message_f.split(" ")
 even_word = lambda x: len(x)%2 == 0
 b_list = list(filter(even_word, a_list))
 final_msg = " ".join(b_list)
 return final_msg

secret_msg_4 = extract_msg(message_6)



# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]


final_path= user_data_dir + '/secret_message.txt'

#Code starts here
secret_msg = " ".join(message_parts)
def write_file(secret_msg, path):
 fp = open(final_path, 'a+')
 fp.write(secret_msg)
 fp.close()

write_file(secret_msg, final_path)
print(secret_msg)

#Code starts here


# --------------
#Code starts here

#Function to fuse message
def fuse_msg(message_a,message_b):
    
    #Integer division of two numbers
    quot=(int(message_b)//int(message_a))
    
    #Returning the quotient in string format
    return str(quot)

#Calling the function to read file  
message_1=read_file(file_path_1)
print(message_1)
#Calling the function to read file
message_2=read_file(file_path_2)

#Calling the function 'fuse_msg'
secret_msg_1=fuse_msg(message_1,message_2)

#Printing the secret message 
print(secret_msg_1)

#Code ends here


# --------------
#Code starts here

#Code starts here

#Function to substitute the message
def substitute_msg(message_c):
    
    #If-else to compare the contents of the file
    if message_c=='Red':
        sub= 'Army General'
    elif message_c=='Green':
        sub= 'Data Scientist'
    elif message_c=='Blue':
        sub ='Marine Biologist'
    
    #Returning the substitute of the message
    return sub

#Calling the function to read file
message_3=read_file(file_path_3)

#Calling the function 'substitute_msg'
secret_msg_2=substitute_msg(message_3)   

#Printing the secret message
print(secret_msg_2)

#Code ends here


# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here

#Function to compare message
def compare_msg(message_d,message_e):
    
    #Splitting the message into a list
    a_list=message_d.split()
    
    #Splitting the message into a list
    b_list=message_e.split()
    
    #Comparing the elements from both the lists
    c_list = [i for i in a_list if i not in b_list]
    
    #Combining the words of a list back to a single string sentence
    final_msg=" ".join(c_list)
    
    #Returning the sentence
    return final_msg


#Calling the function to read file
message_4=read_file(file_path_4)

#Calling the function to read file
message_5=read_file(file_path_5)

#Calling the function 'compare messages'
secret_msg_3=compare_msg(message_4,message_5)

#Printing the secret message
print(secret_msg_3)

#Code ends here


# --------------
#Code starts here
#Code starts here

#Function to filter message
def extract_msg(message_f):
    
    #Splitting the message into a list
    a_list=message_f.split()
    
    #Creating the lambda function to identify even length words
    even_word=lambda x: (len(x)%2==0)
    
    #Splitting the message into a list
    b_list=(filter(even_word, a_list))
    
    #Combining the words of a list back to a single string sentence
    final_msg=" ".join(b_list)
    
    #Returning the sentence
    return final_msg

#Calling the function to read file
message_6=read_file(file_path_6)

#Calling the function 'filter_msg'
secret_msg_4=extract_msg(message_6)

#Printing the secret message
print(secret_msg_4)

#Code ends here


# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]


final_path= user_data_dir + '/secret_message.txt'

#Code starts here

#Combining the secret message parts into a single complete secret message
secret_msg=" ".join(message_parts)

#Function to write inside a file
def write_file(secret_msg,path):
       
#     #Opening a file named 'secret_message' in 'write' mode
    file = open(path, 'a+')

#     #Writing to the file
    file.write(secret_msg)

#     #Closing the file
    file.close()

# #Calling the function to write inside the file    
write_file(secret_msg, final_path)

#Printing the entire secret message
print(secret_msg)

#Code ends here


