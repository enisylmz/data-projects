# Boolean indexing and Filtering
import numpy as np
arr= np.array([1,2,3,4,5,6,7,8,9])

# arrayde cift sayıları bulma yontemi
evens = arr[arr %2 ==0]
print('Evens number in array',evens)

# Arrayda 3 ten buyuk sayıları 0 a cevirme gibi seyler falan filan
arr[arr >3]=0
print('Modified array \n',arr)