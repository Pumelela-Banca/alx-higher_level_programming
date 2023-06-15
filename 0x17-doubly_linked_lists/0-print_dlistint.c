#include "lists.h"

/**
 * print_dlistint - prints all the elements of a list
 *
 * @dlistint_t: doubly linked list
 *
 * Return: numbber of nodes
 */

size_t print_dlistint(const dlistint_t *h)
{
	dlistint_t *go;
	size_t num;

	go = h;
	if (go == NULL)
		return (0);
	num = 1;
	while (go != NULL)
	{
		printf("%d\n", go->n)
		go = go->next
		num++
	}
	return (num);
}
