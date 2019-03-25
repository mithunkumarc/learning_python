

                1.open() returns a file object, and is most commonly used with two arguments: open(filename, mode).
                2.The first argument is a string containing the filename. 
                3.The second argument is another string containing a few characters describing the way in which the file will be used. 
                4.mode can be 'r' when the file will only be read, 
                5.'w' for only writing (an existing file with the same name will be erased), 
                and 
                6.'a' opens the file for appending; any data written to the file is automatically added to the end.
                doubt : 7.'r+' opens the file for both reading and writing. 
                8.The mode argument is optional; 'r' will be assumed if it’s omitted.

---

#### Example : mode : 'w' (write) , creates new file if it doesnt exists. if exists replaces with new file      
                
                
                # create cities file 
                    f = open('cities','w')
                    cities = ['bangalore','mysore','tumkur']
                    for city in cities:
                        f.write(city+'\n')
                    f.close()


#### Example : mode : (r) : read, default mode is read
                
                # read() function will read single character at a time , readLine() read line by line
                # read(number) : number  : number of characters to be read
                
                f = open('cities','r')
                for i in f.readlines():         
                    print(i)

---    
    
#### Example : mode w will delete old file, to udate file use mode 'a' for appending file

                f = open('cities','a')
                cities = ['itanagar','portblair','shimla']
                for city in cities:
                    f.writelines(city+'\n')


#### mode r+ used for both reading and writing into file
                
                
                f = open('cities','r+')

                # for writing
                # cities = ['itanagar','portblair','shimla']
                # for city in cities:
                #     f.writelines(city+'\n')

                # for reading
                # for city in f.readlines():
                #     print(city)


#### mode w+ (write), because w+ repaces existing file with new emtpy file , reading always returns empty

                # use w+ mode for writing




#### mode (x) : used to create file : may raises FileExistsError

            # cant execute this code twice as you will get error, if output.txt file already exists
            
            with open("output.txt",'x') as file:
                file.write("hello world")



#### printing multiple line with next line character


                file = open('input.txt','w')
                file.writelines('\n'.join(['first line','second line']))
                # or file.writelines(['first line\n', 'second line\n','third line'])                
                file.close()

#### FileNotFoundError : Raised when a file or directory is requested but doesn’t exist.


                try:
                   file = open("demo.txt",'r')
                except FileNotFoundError as f:
                   print(f)


                Output : [Errno 2] No such file or directory: 'demo.txt'

#### FileExistsError : Raised when trying to create a file or directory which already exists. 

                  try:
                     file = open("file.txt",'x')
                  except FileExistsError as f:
                     print(f)
                  Output : [Errno 17] File exists: 'file.txt'



#### with statement : scope of variable ends when block ends. similar to auto cleanup/autocloseble
#### similar to try with resources in java,  autoclose at end



        The with statement clarifies code that previously would use 
        try...finally blocks to ensure that clean-up code is executed. 
        
        
        
          with open("output.txt",'x') as file:
              file.write("hello world")
          
          # scope of file variable ends here, so reference count declreases by 1 and autoclean up of file object may start
        
