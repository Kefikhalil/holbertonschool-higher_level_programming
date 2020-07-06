#include <Python.h>
#include <stdio.h>
void print_python_list_info(PyObject *p)
{
PyObject *obj;
size_t x = 0;
size_t length = PyList_Size(p);
printf("[*] Size of the Python List = %lu\n", length);
printf("[*] Allocated = %lu\n", ((PyListObject *)(p))->allocated);
while ( ; x < length; x++)
{
obj = PyList_GetItem(p, x);
printf("Element %lu: %s\n", x, Py_TYPE(obj)->tp_name);
}
}
