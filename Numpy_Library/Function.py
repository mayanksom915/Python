# # 1. Array banane ke Functions :-

# # Function            Use                        Example                 
	              
# # np.array()	    Array banana	              np.array([1, 2, 3])
# # np.zeros()	    Zero wala array	              np.zeros(5)
# # np.ones()	        One wala array	              np.ones(5)
# # np.full()	        Same value wala array	      np.full(4, 7)
# # np.arange()	    Range se array banana	      np.arange(1, 10)
# # np.linspace()	    Equal gap wali values	      np.linspace(1, 10, 5)
# # np.eye()	        Identity matrix banana	      np.eye(3)
# # np.empty()	    Uninitialized array banana	  np.empty(5)


# # 2. Array ki Information dene wale Functions :-

# #  Property	         Use	                            Example 
                                 
# # a.ndim	          Dimensions batana                     a.ndim
# # a.shape             Rows aur columns batana	            a.shape
# # a.size	          Total elements batana	                a.size
# # a.dtype	          Data type batana	                    a.dtype
# # a.itemsize	      Ek element ka size bytes mein	        a.itemsize
# # a.nbytes	          Elements ki total memory	            a.nbytes

# # NUMPY FUNCTIONS AND USES

# ## 1. ARRAY CREATION

# 1. np.array()
#    Use: List ko NumPy array mein convert karna.
#    np.array([10, 20, 30, 40])

# 2. np.arange()
#    Use: Given range mein numbers generate karna.
#    np.arange(1, 11)

# 3. np.linspace()
#    Use: Do numbers ke beech equally spaced values generate karna.
#    np.linspace(0, 10, 5)

# 4. np.zeros()
#    Use: Zero values ka array banana.
#    np.zeros((2, 3))

# 5. np.ones()
#    Use: One values ka array banana.
#    np.ones((3, 3))

# 6. np.full()
#    Use: Ek hi value se array banana.
#    np.full((2, 3), 7)

# 7. np.eye()
#    Use: Identity matrix banana.
#    np.eye(3)

# 8. np.random.randint()
#    Use: Random integers generate karna.
#    np.random.randint(1, 100, size=5)

# 9. np.random.rand()
#    Use: 0 se 1 ke beech random values generate karna.
#    np.random.rand(5)

# ## 2. ARRAY INFORMATION

# 10. arr.shape
#     Use: Array ki dimensions ka size batana.
#     arr.shape

# 11. arr.ndim
#     Use: Array kitne dimensions ka hai, batana.
#     arr.ndim

# 12. arr.size
#     Use: Array mein total elements batana.
#     arr.size

# 13. arr.dtype
#     Use: Array ke elements ka data type batana.
#     arr.dtype

# 14. arr.astype()
#     Use: Array ka data type change karna.
#     arr.astype(float)

# ## 3. MATHEMATICAL FUNCTIONS

# 15. np.sum()
#     Use: Array ke elements ka sum nikalna.
#     np.sum(arr)

# 16. np.mean()
#     Use: Average nikalna.
#     np.mean(arr)

# 17. np.median()
#     Use: Median nikalna.
#     np.median(arr)

# 18. np.std()
#     Use: Standard deviation calculate karna.
#     np.std(arr)

# 19. np.var()
#     Use: Variance calculate karna.
#     np.var(arr)

# 20. np.min()
#     Use: Minimum value nikalna.
#     np.min(arr)

# 21. np.max()
#     Use: Maximum value nikalna.
#     np.max(arr)

# 22. np.argmax()
#     Use: Maximum value ka index batana.
#     np.argmax(arr)

# 23. np.argmin()
#     Use: Minimum value ka index batana.
#     np.argmin(arr)

# 24. np.sqrt()
#     Use: Square root nikalna.
#     np.sqrt(arr)

# 25. np.square()
#     Use: Har element ka square nikalna.
#     np.square(arr)

# 26. np.abs()
#     Use: Absolute values nikalna.
#     np.abs(arr)

# 27. np.round()
#     Use: Decimal values ko round karna.
#     np.round(arr, 2)

# ## 4. ARRAY MANIPULATION

# 28. np.reshape()
#     Use: Array ka shape change karna.
#     np.reshape(arr, (2, 3))

# 29. arr.flatten()
#     Use: Multidimensional array ko 1D array banana.
#     arr.flatten()

# 30. arr.ravel()
#     Use: Array ko 1D form mein convert karna.
#     arr.ravel()

# 31. np.transpose()
#     Use: Rows aur columns ko interchange karna.
#     np.transpose(arr)

# 32. np.concatenate()
#     Use: Arrays ko join karna.
#     np.concatenate((a, b))

# 33. np.vstack()
#     Use: Arrays ko vertically join karna.
#     np.vstack((a, b))

# 34. np.hstack()
#     Use: Arrays ko horizontally join karna.
#     np.hstack((a, b))

# 35. np.split()
#     Use: Array ko multiple parts mein divide karna.
#     np.split(arr, 2)

# 36. np.sort()
#     Use: Values ko ascending order mein sort karna.
#     np.sort(arr)

# 37. np.unique()
#     Use: Duplicate values hata kar unique values dena.
#     np.unique(arr)

# ## 5. INDEXING AND FILTERING

# 38. np.where()
#     Use: Condition ke according values select ya replace karna.
#     np.where(arr > 10, arr, 0)

# 39. np.nonzero()
#     Use: Non-zero elements ke indices nikalna.
#     np.nonzero(arr)

# 40. np.isin()
#     Use: Check karna ki values kisi given list mein hain ya nahi.
#     np.isin(arr, [10, 20, 30])

# 41. np.any()
#     Use: Check karna ki kam se kam ek element condition satisfy karta hai ya nahi.
#     np.any(arr > 50)

# 42. np.all()
#     Use: Check karna ki sabhi elements condition satisfy karte hain ya nahi.
#     np.all(arr > 0)

# 43. np.clip()
#     Use: Values ko given minimum aur maximum range mein rakhna.
#     np.clip(arr, 0, 100)

# ## 6. ARRAY COMPARISON AND OPERATIONS

# 44. np.add()
#     Use: Do arrays ko element-wise add karna.
#     np.add(a, b)

# 45. np.subtract()
#     Use: Do arrays ko element-wise subtract karna.
#     np.subtract(a, b)

# 46. np.multiply()
#     Use: Do arrays ko element-wise multiply karna.
#     np.multiply(a, b)

# 47. np.divide()
#     Use: Do arrays ko element-wise divide karna.
#     np.divide(a, b)

# 48. np.dot()
#     Use: Vectors ka dot product ya compatible matrices ka product calculate karna.
#     np.dot(a, b)

# 49. np.unique()
#     Use: Array ki unique values nikalna.
#     np.unique(arr)

# 50. np.cumsum()
#     Use: Cumulative sum nikalna.
#     np.cumsum(arr)

# 51. np.cumprod()
#     Use: Cumulative product nikalna.
#     np.cumprod(arr)

# ## 7. MISSING VALUES AND LOGICAL CHECKS

# 52. np.isnan()
#     Use: Check karna ki values NaN hain ya nahi.
#     np.isnan(arr)

# 53. np.isfinite()
#     Use: Check karna ki values finite hain ya nahi.
#     np.isfinite(arr)

# 54. np.isinf()
#     Use: Check karna ki values infinity hain ya nahi.
#     np.isinf(arr)

# 55. np.nanmean()
#     Use: NaN values ko ignore karke mean nikalna.
#     np.nanmean(arr)

# ## 8. MATRIX FUNCTIONS

# 56. np.diag()
#     Use: Matrix ka diagonal nikalna ya diagonal matrix banana.
#     np.diag(arr)

# 57. np.linalg.inv()
#     Use: Square matrix ka inverse nikalna, agar inverse exist karta ho.
#     np.linalg.inv(matrix)

# 58. np.linalg.det()
#     Use: Square matrix ka determinant nikalna.
#     np.linalg.det(matrix)

# 59. np.linalg.solve()
#     Use: Linear equations ka solution nikalna.
#     np.linalg.solve(A, b)

# 60. np.linalg.eig()
#     Use: Matrix ke eigenvalues aur eigenvectors calculate karna.
#     np.linalg.eig(matrix)

# ## IMPORTANT NOTES

# 5. Array ka output dekhne ke liye:
#    print(np.mean(arr))
