#include "lists.h"

/**
 * get_dnodeint_at_index - get node at index
 *
 * @head: start of list
 * @index: return node at
 *
 * Return: node
 */

dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	dlistint_t *go;
	unsigned int at;

	go = head;
	at = 0;
	while (go != NULL)
	{
		if (at == index)
			return (go);
		go = go->next;
		at++;
	}
	return (NULL);
}
