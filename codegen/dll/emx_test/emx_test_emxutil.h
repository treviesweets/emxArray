/*
 * emx_test_emxutil.h
 *
 * Code generation for function 'emx_test_emxutil'
 *
 */

#ifndef __EMX_TEST_EMXUTIL_H__
#define __EMX_TEST_EMXUTIL_H__

/* Include files */
#include <stddef.h>
#include <stdlib.h>
#include <string.h>
#include "rtwtypes.h"
#include "emx_test_types.h"

/* Function Declarations */
#ifdef __cplusplus

extern "C" {

#endif

  extern void emxEnsureCapacity(emxArray__common *emxArray, int oldNumel, int
    elementSize);
  extern void emxFree_real_T(emxArray_real_T **pEmxArray);
  extern void emxInit_real_T(emxArray_real_T **pEmxArray, int numDimensions);

#ifdef __cplusplus

}
#endif
#endif

/* End of code generation (emx_test_emxutil.h) */
