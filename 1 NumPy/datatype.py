#using array-scalar type
import numpy as np
dt = np.dtype(np.int32)
print dt  #int32
#int8, int16, int32, int64 can be replaced by equivalent string 'i1', 'i2','i4',
dt = np.dtype('i4')
print dt #int32
dt = np.dtype('>i4')
print dt  #>i4
dt = np.dtype([('age',np.int8)])
print dt #[('age', 'i1')]
a = np.array([(10,),(20,),(30,),(40)],dtype = dt)
print a['age']
student = np.dtype([('name','S20'),('age','i1')])
print student


student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student) 
print a #[('abc', 21, 50.0), ('xyz', 18, 75.0)]


'b' − boolean

'i' − (signed) integer

'u' − unsigned integer

'f' − floating-point

'c' − complex-floating point

'm' − timedelta

'M' − datetime

'O' − (Python) objects

'S', 'a' − (byte-)string

'U' − Unicode

'V' − raw data (void)