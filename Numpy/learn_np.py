import numpy as np

# baic init and abo
arr = np.array([10, 20, 30])

arr_2d = np.array([[10, 20, 30, 40], [20, 43, 45, 67]])


print(np.shape(arr_2d))
print(arr_2d[1, 0:3])


'''
Definition of NumPy  
NumPy (Numerical Python) is a Python library used for numerical computing, providing support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on them.  

Characteristics of NumPy:  
1. N-Dimensional Arrays:- Supports powerful multi-dimensional arrays (`ndarray`).  
2. Vectorized Operations:- Faster computations without explicit loops.  
3. Broadcasting:- Performs operations on arrays of different shapes efficiently.  
4. Memory Efficient:- Uses less memory compared to Python lists.  
5. Integration:- Works well with other libraries like Pandas, Matplotlib, and SciPy.  


Advantages of NumPy:  
Fast & Efficient:- Performs operations much faster than Python lists.  
Convenient Data Handling:- Easy slicing, indexing, and reshaping of arrays.  
Mathematical Operations:- Supports algebra, statistics, and complex calculations.  
Interoperability:- Works with C, C++, and Fortran for high-performance computing.  


Disadvantages of NumPy:  
Consumes More Memory:- Uses more memory than built-in Python types for small datasets.  
Learning Curve:- Requires understanding of array-based programming.  
Less Flexibility:- Fixed-size arrays (cannot dynamically change size like lists).  


'''