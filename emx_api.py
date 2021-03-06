# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#
# Matlab Coder Generated C Code uses a data structure to represent variable sized matlab arrays
#  it's called emx_array
# This code tries to interface with a very simple matlab script called emx_test 
#   that takes an array and multiplies each element by itself
# emx test looks like this in matlab
#
# function res = emx_test ( in )
#     res = in .* in;
# end
#
# so basically it multiplies each element of the matrix by itself
# therefore [1., 2., 4., 8., 16.] should become [1., 4., 8., 64., 256.]
#
#   A number of options are described below in order of success
#

## Speed results for a 1000 long vector ##
#  
# TestEmxAPI() with data conversions creating pointers etc....(note this function can only accept vectors)
# 100 loops, best of 3: 3.24 ms per loop
#
# TestEmxNumpy()
# 100 loops, best of 3: 2.28 ms per loop

# Random Note: the Linux 'nm' command is really useful for listing the functions exposed by a .dll or .so
#            use nm -g (for external) <filename>

# <codecell>

import ctypes
import numpy
from os.path import expanduser

# set the directory for the c .so
home_dir = expanduser("~")
LIBTEST = home_dir + '/Dropbox/notebooks/eef/emxarr/codegen/dll/emx_test/'

# load the .so (dynamic library) using ctypes
EMX = ctypes.cdll.LoadLibrary(LIBTEST + 'emx_test.so')
init = EMX.emx_test_initialize()
print '\nInitialize...\n'

data_in = numpy.random.rand(1000)

# <codecell>

def TestEmxNumpy(data_in):
    """ Test the EMX Api provided by the matlab coder 
        TestEmxAPI below works...this is trying to get a 
        numpy version to work
    """

    # Create a data structure to hold the pointer generated by 
    #  emxCreateWrapper...
    class Opaque(ctypes.Structure):
        pass
    
    # create an empty array of the same size for the output
    data_ou = numpy.zeros(data_in.shape)
    
    # create a pointer for these arrays
    inp = data_in.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    oup = data_ou.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    
    # get the shape of the array and set the ncols and rows
    nrows = ctypes.c_int(data_in.shape[0])
    if len(data_in.shape) == 1:
        ncols = ctypes.c_int(1)
    else:
        ncols = ctypes.c_int(data_in.shape[1])

    # use EMX.emxCreateWrapper_real_T(double *data, int rows, int cols) to generate an emx wrapping the data 
    # input arg types are a pointer to the data NOTE it's not great to have to resize the ctypes.c_double
    EMX.emxCreateWrapper_real_T.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_int, ctypes.c_int]
    # a pointer to the emxArray is returned and stored in Opaque
    EMX.emxCreateWrapper_real_T.restype = ctypes.POINTER(Opaque)
    
    # use emxCreateWrapper
    in_emx = EMX.emxCreateWrapper_real_T(inp, nrows, ncols)
    ou_emx = EMX.emxCreateWrapper_real_T(oup, nrows, ncols)
    
    # so now we have to emx's created and have pointers to them we can run the emx_test
    EMX.emx_test(in_emx, ou_emx)
            
    # clear the heap removing the emx 
    EMX.emxDestroyArray_real_T(in_emx)
    EMX.emxDestroyArray_real_T(ou_emx)

    return data_ou
    
#data_in = numpy.array([1., 2., 4., 8., 16.])
#%timeit data_ou = TestEmxNumpy(data_in) 

# <codecell>

def TestEmxAPI(data_in):
    """ Test the EMX Api provided by the matlab coder 
        Note this API only works for vectors for some reason
    """

    # Create a data structure to hold the pointer generated by 
    #  emxCreateWrapper...
    class Opaque(ctypes.Structure):
        pass
    
    L = len(data_in)
    # create an empty array of the same size for the output
    data_ou = [0] * L
    
    # put this in a ctypes array
    ina = (ctypes.c_double * L)(*data_in)
    oua = (ctypes.c_double * L)(*data_ou)
    # create a pointer for these arrays & set the rows and columns of the matrix
    inp = ctypes.pointer(ina)
    oup = ctypes.pointer(oua)
    
    nrows = ctypes.c_int(1)
    ncols = ctypes.c_int(L)

    # use EMX.emxCreateWrapper_real_T(double *data, int rows, int cols) to generate an emx wrapping the data 
    # input arg types are a pointer to the data NOTE it's not great to have to resize the ctypes.c_double
    EMX.emxCreateWrapper_real_T.argtypes = [ctypes.POINTER(ctypes.c_double * L), ctypes.c_int, ctypes.c_int]
    # a pointer to the emxArray is returned and stored in Opaque
    EMX.emxCreateWrapper_real_T.restype = ctypes.POINTER(Opaque)
    # use emxCreateWrapper
    in_emx = EMX.emxCreateWrapper_real_T(inp, nrows, ncols)
    ou_emx = EMX.emxCreateWrapper_real_T(oup, nrows, ncols)
    
    # so now we have to emx's created and have pointers to them we can run the emx_test
    # emx test looks like this in matlab
    #
    # function res = emx_test ( in )
    #     res = in .* in;
    # end
    #
    # so basically it multiplies each element of the matrix by itself
    # 
    # therefore [1., 2., 4., 8., 16.] should become [1., 4., 8., 64., 256.]

    EMX.emx_test(in_emx, ou_emx)
    
    # clear the heap removing the emx 
    EMX.emxDestroyArray_real_T(in_emx)
    EMX.emxDestroyArray_real_T(ou_emx)
    
    data_ou = oua[:L]

    return data_ou

#data_in = [1., 2., 4., 8., 16.]
#%timeit data_ou = TestEmxAPI(data_in)

# <codecell>

### NOTE THIS DOESN'T WORK PROPERLY ###
class EmxArray(ctypes.Structure):

    boolean_T = ctypes.c_ubyte
    _fields_ = [
        ('data', ctypes.POINTER(ctypes.c_double)),
        ('size', ctypes.POINTER(ctypes.c_int)),
        ('allocatedSize', ctypes.c_int),
        ('numDimensions', ctypes.c_int),
        ('canFreeData', boolean_T)]

    __all__ = ['boolean_T', 'emxArray_real_T']

    
    # would be nice to have a way of printing the contents etc
    #def __str__(self):
    #    return str(self.data)

def TestEMX():
    """ Test the EMX """
    # define some data

    data_in = [1., 2., 4., 8., 16.]
    L = len(data_in)

    ina = EmxArray()
    ina.data = (ctypes.c_double * L)(*data_in)
    ina.size = (ctypes.c_int * 1)(L)
    ina.allocatedSize = 5
    ina.numDimensions = 2
    ina.canFreeData = False

    # set up an array where the output can be stored
    out = EmxArray()
    out.data = (ctypes.c_double * L)(*[0] * L)
    out.size = (ctypes.c_int * 1)(L)
    out.allocatedSize = 5
    out.numDimensions = 2
    out.canFreeData = False

    # create pointers to the two arrays
    #ina_p = ctypes.pointer(ina)
    #out_p = ctypes.pointer(out)

    print 'Before: '
    print 'In: ', ina.data[:L]
    print ina
    #print ina_p
    print 'Out:', out.data[:L]
    print out
    #print out_p

    # --- now emx_test takes a double and returns a double and an EmxArray
    # emx_test takes a pointer to an array and a pointer to an array out
    print '\nRunning emx_test.....\n'
    EMX.emx_test.argtypes = [ctypes.POINTER(EmxArray), ctypes.POINTER(EmxArray)]
    EMX.emx_test.restype = None
    #EMX.emx_test(ina_p, out_p)

    EMX.emx_test(ctypes.byref(ina), ctypes.byref(out))
    
    print 'After: '
    print 'In: ', ina.data[:L]
    print ina
    #print ina_p
    print 'Out:', out.data[:L]
    print out
    #print out_p

#TestEMX()

# <codecell>

### NOTE MATLAB SCRIPT NEEDS TO BE ALTERED TO TEST THIS ONE ###
def TestDouble():
    """
        Test passing a double to emx_test - this works ok...
    """
    #
    # Proof that this works for a single double
    #

    ina = ctypes.c_double(2)

    print 'Before: '
    print 'In: ', ina.value

    # --- now emx_test takes a double and returns a double and an EmxArray
    # emx_test takes a pointer to an array and a pointer to an array out
    print '\nRunning emx_test\n'
    EMX.emx_test.argtypes = [ctypes.c_double]
    EMX.emx_test.restype = ctypes.c_double
    out = EMX.emx_test(ina)

    print 'After: '
    print 'Out: ', out

