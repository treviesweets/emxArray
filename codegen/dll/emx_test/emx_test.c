/*
 * emx_test.c
 *
 * Code generation for function 'emx_test'
 *
 */

/* Include files */
#include "rt_nonfinite.h"
#include "emx_test.h"
#include "emx_test_emxutil.h"

/* Function Definitions */
void emx_test(const emxArray_real_T *in, emxArray_real_T *res)
{
  int i0;
  int loop_ub;
  i0 = res->size[0] * res->size[1];
  res->size[0] = 1;
  res->size[1] = in->size[1];
  emxEnsureCapacity((emxArray__common *)res, i0, (int)sizeof(double));
  loop_ub = in->size[0] * in->size[1];
  for (i0 = 0; i0 < loop_ub; i0++) {
    res->data[i0] = in->data[i0] * in->data[i0];
  }
}

/* End of code generation (emx_test.c) */
