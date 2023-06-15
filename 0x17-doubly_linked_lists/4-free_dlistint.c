#include "lists.h"

/**
 * free_dlistint - free memory from list
 *
 * @head: start of list
 *
 * Return: void
 */

void free_dlistint(dlistint_t *head)
{
	dlistint_t *go, *temp;

	go = head;
	while (go != NULL)
	{
		temp = go->next;
		free(go);
		go = temp;
	}
}
