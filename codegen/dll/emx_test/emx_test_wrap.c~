#include "emx_test_emxAPI.h"
#include "emx_test.h"

void emx_wrap(double *x, int szx, double *y, int szy) 

{
  emxArray_real_T *pEmx;
  emxArray_real_T *pEmy;

  /* Create input emxArray assuming 2-dimensional input */
  /* emxCreateWrapper_real_T(double *data, int rows, int cols) */
  pEmx = emxCreateWrapper_real_T(x, szx, szy);

  /* Create output emxArray (assumes that the output is not */
  /* written before allocation occurs) assuming 2-D output  */
  pEmy = emxCreateWrapper_real_T(NULL, szx, szy);

  /* Call generated code (call foobar_initialize/terminate elsewhere) */
  emx_test(pEmx, pEmy);

  /* Unpack result - You may want to MALLOC storage in *y and */
  /* MEMCPY there alternatively                               */
  y = pEmy->data;
  /* szy[0] = pEmy->size[0]; 				      */
  /* szy[1] = pEmy->size[1]; 				      */

  /* Clean up any memory allocated in the emxArrays (e.g. the size vectors) */
  emxDestroyArray_real_T(pEmx);
  emxDestroyArray_real_T(pEmy);
}
