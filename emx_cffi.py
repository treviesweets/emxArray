# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#
# USING CFFI for Python - replacement for ctypes
#

import cffi

# <codecell>

ffi = cffi.FFI()
ffi.cdef("""
typedef struct emxArray_real_T;

struct emxArray_real_T {
    double data;
    int size;
    int allocatedSize;
    int numDimensions;
    bool canFreeData;
};



""")

#ffi.cdef("""
#int add(int, int);
#""")

#C = ffi.verify("""
#int add(int a, int b) {
#    return a + b;
#}
#""")

ffi.dlopen('/home/trevorsweetnam/Dropbox/notebooks/eef/emxarr/codegen/dll/emx_test/emx_test.so')

#C = ffi.verify()

# <codecell>


# <codecell>


# <codecell>

#import pybindgen
#import sys

# <codecell>

#cd /home/trevorsweetnam/Dropbox/notebooks/eef/emxarr/codegen/dll/emx_test/html/

# <codecell>

# set up the module
#mod = pybindgen.Module('emx_test_emxAPI')

# <codecell>

# add an include
#mod.add_include('"rt_nonfinite.h"')
#mod.add_include('"emx_test.h"')
#mod.add_include('"emx_test_emxAPI.h"')
#mod.add_include('"emx_test_emxutil.h"')

# <codecell>

# set up the functions - name, outputs, inputs
#mod.add_function('emxCreateND_real_T', ) # create an empty emxArray
#mod.add_function('emxCreateWrapperND_real_T', ) # create an emxArray from existing data
#mod.add_function('emxCreateWrapper_real_T', ) # create an emxArray from existin data
#mod.add_function('emxCreate_real_T', ) # create an empty emxArray
#mod.add_function('emxDestroyArray_real_T', ) # destroy the array and dealocate memory

# <codecell>


