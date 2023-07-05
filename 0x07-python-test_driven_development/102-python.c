#include <stdio.h>
#include <Python.h>

void print_python_string(PyObject *p) {
    if (!PyUnicode_Check(p)) {
        printf("[.] string object info\n");
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    Py_ssize_t size;
    const char *str = PyUnicode_AsUTF8AndSize(p, &size);

    printf("[.] string object info\n");
    printf("  type: %s\n", p->ob_type->tp_name);
    printf("  length: %zd\n", size);
    printf("  value: %s\n", str);
}
