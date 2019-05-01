> xpath : singe element

> xpath expression : gets multiple elements


Selecting Nodes

XPath uses path expressions to select nodes in an XML document. The node is selected by following a path or steps. The most useful path expressions are listed below:


          Expression 	Description
          nodename 	  Selects all nodes with the name "nodename"
          / 	        Selects from the root node
          // 	        Selects nodes in the document from the current node that match the selection no matter where they are
          . 	        Selects the current node
          .. 	        Selects the parent of the current node
          @ 	        Selects attributes


In the table below we have listed some path expressions and the result of the expressions:


          Path Expression 	          Result

          bookstore 	          Selects all nodes with the name "bookstore"

          /bookstore 	          Selects the root element bookstore

          Note: If the path starts with a slash ( / ) it always represents an absolute path to an element!

          bookstore/book      	Selects all book elements that are children of bookstore
          
          //book 	              Selects all book elements no matter where they are in the document

          bookstore//book 	    Selects all book elements that are descendant of the bookstore element, no matter where they are under the bookstore element

          //@lang 	            Selects all attributes that are named lang
          
          
          
          
links : 

          https://www.w3schools.com/xml/xpath_syntax.asp
          https://docs.scrapy.org/en/xpath-tutorial/topics/xpath-tutorial.html
