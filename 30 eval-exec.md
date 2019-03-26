#### eval() : eval is used to evaluate a single dynamically generated Python expression

      eval('print(2+2)')  # must be expression , must give output
      print(eval('5 * 5'))    
      eval('a = 10')      # error : a = 10 , does't give any output



#### exec() : is used for executing a dynamically created statement or program

      exec('print(47 + 47)')
      exec('a = 10')    # works fine
      print(a)          # output : 10
