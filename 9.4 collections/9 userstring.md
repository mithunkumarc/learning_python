#### The class, UserString acts as a wrapper around string objects.
#### wrapper around string objects for easier string subclassing


        from collections import UserString
        class MyString(UserString):
            def __init__(self,data):
                self.data = data
            def upper(self):
                return self.data.upper()


        m = MyString("hello")
        print(m.upper())


          output : HELLO
