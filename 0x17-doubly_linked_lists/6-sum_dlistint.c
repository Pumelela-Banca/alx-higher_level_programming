#include "lists.h"

/**
 * sum_dlistint - sum all data in list
 *
 * @head: start
 * Return: sum of all data
 */

int sum_dlistint(dlistint_t *head)
{
	dlistint_t *go;
	int sum;

	go = head;
	if (go == NULL)
		return (0);
	sum = 0;
	while (go != NULL)
	{
		sum += go->n;
		go = go->next;
	}
	return (sum);
}
