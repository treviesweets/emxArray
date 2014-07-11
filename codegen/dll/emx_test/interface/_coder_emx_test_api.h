/*
 * _coder_emx_test_api.h
 *
 * Code generation for function 'emx_test'
 *
 */

#ifndef ___CODER_EMX_TEST_API_H__
#define ___CODER_EMX_TEST_API_H__
/* Include files */
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include "tmwtypes.h"
#include "mex.h"
#include "emlrt.h"

/* Type Definitions */
#ifndef struct_emxArray_real_T
#define struct_emxArray_real_T
struct emxArray_real_T
{
    double *data;
    int *size;
    int allocatedSize;
    int numDimensions;
    boolean_T canFreeData;
};
#endif /*struct_emxArray_real_T*/
#ifndef typedef_emxArray_real_T
#define typedef_emxArray_real_T
typedef struct emxArray_real_T emxArray_real_T;
#endif /*typedef_emxArray_real_T*/

/* Function Declarations */
extern void emx_test_initialize(emlrtContext *aContext);
extern void emx_test_terminate(void);
extern void emx_test_atexit(void);
extern void emx_test_api(const mxArray *prhs[1], const mxArray *plhs[1]);
extern void emx_test(emxArray_real_T *in, emxArray_real_T *res);
extern void emx_test_xil_terminate(void);

#endif
/* End of code generation (_coder_emx_test_api.h) */
