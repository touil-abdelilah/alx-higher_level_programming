#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_list - prints info about Python lists
 * @p: PyObject
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t i, size;

    printf("[*] Python list info\n");
    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
        if (strcmp(Py_TYPE(PyList_GetItem(p, i))->tp_name, "bytes") == 0)
            print_python_bytes(PyList_GetItem(p, i));
    }
}

/**
 * print_python_bytes - prints info about Python bytes objects
 * @p: PyObject
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t i, size;
    char *str;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    printf("  size: %ld\n", size);

    str = PyBytes_AsString(p);
    printf("  trying string: %s\n", str);

    printf("  first 10 bytes: ");
    for (i = 0; i < size && i < 10; i++)
        printf("%02x ", str[i] & 0xff);

    for (; i < 10; i++)
        printf("00 ");
    printf("\n");
}
