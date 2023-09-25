#include <Python.h>
/**
 * print_python_list -  function prints information about a Python list.
 * @p: a pointer to apython object
 * Return: nothing
*/
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid list object\n");
		return;
	}
}
/**
 * print_python_bytes -function prints information about a Python bytes object.
 * @p: pointer to a python object
 * Return: nothing
*/
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "Invalid bytes object\n");
		return;
	}
}
/**
 * print_python_float - function print information about a Python float object
 * @p: pointer to a python object
 * Return: nothing
*/
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "Invalid float object\n");
		return;
	}
}
