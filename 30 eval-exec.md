#### eval() : eval is used to evaluate a single dynamically generated Python expression, returns value

      eval('print(2+2)')  # must be expression , must give output
      print(eval('5 * 5'))    # eval : returns output    
      eval('a = 10')      # error : a = 10 , does't give any output



#### exec() : is used for executing a dynamically created statement or program, no return value

      exec('print(47 + 47)')   #
      exec('a = 10')    # works fine
      print(a)          # output : 10


#### Python AST – Abstract Syntax Tree


      Abstract Syntax Tree is a very strong features in Python. 
      Python AST module allows us to interact with Python code itself and modify it.
      
      With Python AST module, we can do a lot of things like modifying Python code and inspect it. 
      The code can be parsed and modified before it is compiled to bytecode form. 
      
      
      Modes for Code Compilation

      As we mentioned mode in the last script above, there are three modes in which Python code can be compiled. 
      They are:

          exec: We can execute normal Python code using this mode.
          eval: To evaluate Python’s expressions, this mode will return the result fo the expression after evaluation.
          single: This mode works just like Python shell which execute one statement at a time.


#####
