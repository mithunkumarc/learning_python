#### pickling unpickling 

        # pickling , serialization, marshalling, flattening
        # it serializes objects so they can be saved to a file, and loaded in a program again later on.
        # pickling : serialization
        # unpickling : de serializtion

          import pickle
          dogs_dict = { 'Ozzy': 3, 'Filou': 8, 'Luna': 5, 'Skippy': 10, 'Barco': 12, 'Balou': 9, 'Laika': 16 }
          filename = 'dogs'
          outfile = open(filename,'wb')# writing in binary mode
          pickle.dump(dogs_dict,outfile)# writing obj to file
          outfile.close()


          # unpickling
          infile = open(filename,'rb')
          new_dict = pickle.load(infile)
          infile.close()

          # check data
          print(new_dict)     # {'Ozzy': 3, 'Filou': 8, 'Luna': 5, 'Skippy': 10, 'Barco': 12, 'Balou': 9, 'Laika': 16}
          print(new_dict==dogs_dict)  # True
          print(type(new_dict)) # <class 'dict'>
          
#### when not to use

          # if you want to use data across different programming languages, pickle is not recommended.
          # Its protocol is specific to Python, thus, cross-language compatibility is not guaranteed.
          # You should also try not to unpickle data from an untrusted source.
          # Malicious code inside the file might be executed

#### alternate for pickle : json

          # more secure and much faster than pickle.


#### pickling and unpickling of an object

                import pickle
                class Dog:
                    def __init__(self,name):
                        self.name = name

                dog = Dog("tex")

                filename = 'dogs'
                outfile = open(filename,'wb')# writing in binary mode
                pickle.dump(dog,outfile)# writing obj to file
                outfile.close()


                # unpickling
                infile = open(filename,'rb')
                new_dog = pickle.load(infile)
                infile.close()

                # check data
                print('new dog name',new_dog.name)
                print('old dog name',dog.name)
                print(new_dog==dog) # false because two of they point to two different copies
                print(type(new_dog))

                output : 
                new dog name tex
                old dog name tex
                False
                <class '__main__.Dog'>
