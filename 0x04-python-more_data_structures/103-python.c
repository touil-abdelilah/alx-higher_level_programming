#include <Python.h>

void print_python_bytes(PyObject *p) {
    printf("[.] bytes object info\n");
    if (PyBytes_Check(p)) {
        Py_ssize_t size = PyBytes_Size(p);
        printf("  size: %ld\n", size);

        // Attempt to convert to string
        PyObject *string_repr = PyObject_Repr(p);
        const char *string_value = PyUnicode_AsUTF8(string_repr);
        printf("  trying string: %s\n", string_value);

        // Print up to 10 bytes
        printf("  first %ld bytes: ", (size < 10) ? size : 10);
        for (Py_ssize_t i = 0; i < ((size < 10) ? size : 10); ++i) {
            printf("%02x ", (unsigned char)PyBytes_AS_STRING(p)[i]);
        }
        printf("\n");
        Py_XDECREF(string_repr);
    } else {
        printf("  [ERROR] Invalid Bytes Object\n");
    }
}

void print_python_list(PyObject *p) {
    Py_ssize_t size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
    
    for (Py_ssize_t i = 0; i < size; ++i) {
        PyObject *element = PyList_GetItem(p, i);
        printf("Element %ld: ", i);

        if (PyBytes_Check(element)) {
            print_python_bytes(element);
        } else if (PyLong_Check(element)) {
            printf("int\n");
        } else if (PyFloat_Check(element)) {
            printf("float\n");
        } else if (PyTuple_Check(element)) {
            printf("tuple\n");
        } else if (PyList_Check(element)) {
            printf("list\n");
        } else if (PyUnicode_Check(element)) {
            printf("str\n");
        } else {
            printf("Unknown Type\n");
        }
    }
}

