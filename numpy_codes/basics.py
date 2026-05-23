import numpy as np 


def array_example():
    a = np.arange(15)
    print(a)
    a = a.reshape(3,5)
    print(a)

    print(a.shape)
    print(a.ndim)
    print(a.dtype)
    print(a.size)
    print(type(a))
    

def create_array():
    a = np.array([1,2,3])
    print(a)
    print(type(a))

    a[2] = 3.4
    print(a)

    c = np.array([[1,3],[2,3]], dtype=np.complex128)
    print(c)

    d = np.empty((3,2,2), dtype=np.float64)
    print(d)

    e = np.zeros((2,3), dtype=np.int32)
    print(e)

    f = np.arange(10,31,5)
    print(f)
    
    g = np.linspace(0, 10, 5)
    print(g)

    h = np.logspace(0, 10, 5)
    print(h)
    

    i = np.eye(3)
    print(i)

    
    


def main():
    create_array()
    # array_example()



if __name__ == "__main__":
    main()