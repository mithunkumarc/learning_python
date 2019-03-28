#### built in constants : 

          False :           type bool
          True :            type bool
          None :            type NoneType
          NotImplemented : <class 'NotImplementedType'>
          Ellipsis : <class 'ellipsis'>

         useful for the interactive interpreter shell and should not be used in programs.
        
          quit : <class '_sitebuiltins.Quitter'>
          exit : <class '_sitebuiltins.Quitter'>

                
#### quit() exit() : used in interpreter mode
            # exits from interpreter : exact difference , to be updated here
            
            
            print("hello")
            #quit()
            exit()
            print("world")


            for i in range(11):
                if i == 5:
                    quit()
                    #exit()
                print(i)

