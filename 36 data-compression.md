

          import zlib

          text = 'witch which has which withches wrist watches'
          # converts to bytearray of text similar to b''witch which has which withches wrist watches''
          s = str.encode(text)  
          print(len(s))

          c = zlib.compress(s)
          print(c)
          print(len(c))

          t = zlib.decompress(c)

          # -- below line prints characters in ascii code
          # print(type(t))
          # for x in t:
          #     print(x)

          # back from byte array to original text
          x = t.decode('utf-8')   
          print(x)
          print(len(x))
