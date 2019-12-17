#include <Python.h>


#if defined(__cplusplus) || defined(c_plusplus)
extern "C" {
#endif


#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)

static PyObject *hello(PyObject *);
static const PyMethodDef *register_module(void);

#else

static PyObject *hello();
static const PyMethodDef *register_module();

#endif


#if defined(__cplusplus) || defined(c_plusplus)
}
#endif


#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
PyMODINIT_FUNC PyInit_hello(void)
#else
PyMODINIT_FUNC PyInit_hello()
#endif
{

    static struct PyMethodDef methods[] = {
      {
        "hello",
        (PyCFunction)hello,
        METH_NOARGS,
        "Test output hello function."
      },
      {NULL, NULL, 0, NULL}
    };

    static struct PyModuleDef module = {
      PyModuleDef_HEAD_INIT,
      "hello",
      NULL,
      -1,
      methods
    };

  return (PyModule_Create(&module));

}


#if defined(__STDC__) || defined(__cplusplus) || defined(c_plusplus)
static PyObject *hello(PyObject *self)
#else
static PyObject *hello(self)
PyObject *self;
#endif
{

    puts("Hello, World.");

    return (Py_None);

}
