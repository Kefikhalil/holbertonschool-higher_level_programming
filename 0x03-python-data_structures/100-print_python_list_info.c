#include <Python.h>
#include <stdio.h>
void print_python_list_info(PyObject *p)
for ( ; i < length; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %lu: %s\n", i, Py_TYPE(obj)->tp_name);
	}
