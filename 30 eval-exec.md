#### eval() : eval is used to evaluate a single dynamically generated Python expression, returns value

      eval('print(2+2)')  # must be expression , must give output
      print(eval('5 * 5'))    # eval : returns output    
      eval('a = 10')      # error : a = 10 , does't give any output



#### exec() : is used for executing a dynamically created statement or program, no return value

      exec('print(47 + 47)')   #
      exec('a = 10')    # works fine
      print(a)          # output : 10


#### Python AST – Abstract Syntax Tree

      In computer science, an abstract syntax tree (AST), or just syntax tree, 
      is a tree representation of the abstract syntactic structure of source code written in a programming language.


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

#### parsing abstract syntax tree : 

      import ast
      code = ast.parse("print('hello world')")
      print(code)
      exec(compile(code,filename="",mode="exec"))
      #eval(compile(code,filename="",mode="exec"))

#### creating abstract syntax tree : 


            import ast

            tree = ast.parse('''
            fruits = ['grapes', 'mango']        # assign statement
            name = 'peter'                      # assign statement

            for fruit in fruits:                            # for statement
                print('{} likes {}'.format(name, fruit))          # body of for loop : print statemenet : format
            ''')

            print(ast.dump(tree))

            
            output : 
            Module(body=[Assign(
            ## fruits = ['grapes', 'mango']        
            targets=[Name(id='fruits', ctx=Store())], value=List(elts=[Str(s='grapes'), Str(s='mango')], ctx=Load())), 
            ## name = 'peter'
            Assign(targets=[Name(id='name', ctx=Store())], value=Str(s='peter')), 
            ## for loop            
            For(target=Name(id='fruit', ctx=Store()), iter=Name(id='fruits', ctx=Load()),
            body=[Expr(value=Call(func=Name(id='print', ctx=Load()), 
            args=[Call(func=Attribute(value=Str(s='{} likes {}'), attr='format', ctx=Load()), 
            args=[Name(id='name', ctx=Load()), Name(id='fruit', ctx=Load())], keywords=[])], keywords=[]))], orelse=[])])

