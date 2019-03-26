#### @classmethod : Transform a method into a class method. 

        ## example for @classmethod
        
        
#### compile() : Compile the source into a code or AST object. Code objects can be executed by exec() or eval().

                import ast
                codeInString = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
                file_name = 'sumstring'# optional
                #eval doest work for assingnment, os using exec
                codeObejct = compile(ast.parse(codeInString), filename = "" ,mode='exec')
                exec(codeObejct)
                eval(codeObejct)

                or
                
                codeInString = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
                codeObejct = compile(codeInString, filename = "" ,mode='exec')
                exec(codeObejct)
                eval(codeObejct)


#### complex() : Return a complex number with the value real + imag*1j or convert a string or number to a complex number. 
       
                
                print(complex(23,45))   # (23+45j)
                print(complex('23+8j')) # (23+8j)
                print(complex(45))      # (45+0j)
                # when it comes to sting , only one parameter is allowed
                # complex('23','8') # error
                
                
