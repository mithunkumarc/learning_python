guide link : 

        https://docs.scipy.org/doc/numpy/reference/


quick start tutorial : 

        https://docs.scipy.org/doc/numpy/user/quickstart.html


some examples : 

        https://www.analyticsindiamag.com/the-most-important-numpy-functions-you-should-know-when-learning-python/



#### jupyter notebook install


        link : https://jupyter.org/install

        python3 -m pip install --upgrade pip
        python3 -m pip install jupyter
        jupyter notebook

        Note : if jupyter running on old python
        use
        
        pip3 install --upgrade pip jupyter ipython


#### understanding multile dimension array

                c = np.arange(24).reshape(2,3,4)
                
                        two times 3 * 4 matrix

                array([[[ 0,  1,  2,  3],
                        [ 4,  5,  6,  7],
                        [ 8,  9, 10, 11]],

                       [[12, 13, 14, 15],
                        [16, 17, 18, 19],
                        [20, 21, 22, 23]]])
