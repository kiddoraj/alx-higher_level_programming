#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        printf("[ERROR] Invalid PyListObject\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        const char *type = Py_TYPE(item)->tp_name;
        printf("Element %ld: %s\n", i, type);
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("[ERROR] Invalid PyBytesObject\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    Py_ssize_t i;
    Py_ssize_t max_display = (size < 10) ? size : 10;

    printf("[*] Python bytes info\n");
    printf("[*] Size of the Python Bytes = %ld\n", size);
    printf("first %ld bytes: ", max_display);

    for (i = 0; i < max_display; i++) {
        printf("%02x", (unsigned char)PyBytes_AS_STRING(p)[i]);
        if (i < max_display - 1)
            printf(" ");
    }

    printf("\n");
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        printf("[ERROR] Invalid PyFloatObject\n");
        return;
    }

    double value = PyFloat_AsDouble(p);

    printf("[*] Python float info\n");
    printf("[*] Value: %f\n", value);
}


