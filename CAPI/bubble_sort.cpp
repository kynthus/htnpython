#include <Python.h>

namespace {

static PyObject* bubblesort (PyObject* self, PyObject* seq) {
  Py_ssize_t i, j, n;
  PyObject *a, *b, *list;
  int cmp;

  Py_INCREF(seq);
  list = PySequence_List(seq);
  Py_DECREF(seq);

  n = PyObject_Size(list);

  if (n < 0)
    return NULL; // error

  for (i = 1; i < n; ++i) for (j = 1; j < n - i + 1; ++j) {
    a = PyList_GetItem(list, j);
    Py_INCREF(a);
    b = PyList_GetItem(list, j - 1);
    Py_INCREF(b);

    cmp = PyObject_RichCompareBool(a, b, Py_LT); // a < b

    if (cmp == -1) { // error
      Py_DECREF(a);
      Py_DECREF(b);
      return NULL;
    }

    if (cmp == 1) {
      PyList_SetItem(list, j, b);
      PyList_SetItem(list, j - 1, a);
    } else {
      Py_DECREF(a);
      Py_DECREF(b);
    }
  }
  
  return list;
}

static PyMethodDef MySortMethods[] = {
  {"bubblesort", (PyCFunction)bubblesort, METH_O, "Apply bubble sort to given list."},
  {NULL, NULL, 0, NULL}
};

static struct PyModuleDef mysortmodule = {
  PyModuleDef_HEAD_INIT,
  "mysort",
  NULL,
  -1,
  MySortMethods
};

PyMODINIT_FUNC PyInit_mysort (void) {
  return PyModule_Create(&mysortmodule);
}

}
