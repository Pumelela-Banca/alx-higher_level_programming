#include "lists.h"

/**
 * delete_dnodeint_at_index - delete node at given index
 *
 * @head: start of list
 * @index: delete at
 *
 * Return: 1 for success and -1  for fail
 */

int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *go;
	unsigned int track;

	if (*head == NULL)
		return (-1);
	go = *head;
	track = 0;
	while (go != NULL)
	{
		if (index == 0)
		{
			go->next->prev = NULL;
			*head = go->next;
			free(go);
			return (1);
		}
		else if (index == track)
		{
			go->next->prev = go->prev;
			go->prev->next = go->next;
			free(go);
			return (1);
		}
		else if ((index == (track + 1)) && go->next == NULL)
		{
			go->prev->next = NULL;
			free(go);
			return (1);
		}
		track++;
		go = go->next;
	}
	return (-1);
}
