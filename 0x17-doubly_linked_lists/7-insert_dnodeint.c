#include "lists.h"

/**
 * insert_dnodeint_at_index - insert node at given index
 *
 * @h: start of  list
 * @idx: insert at index
 * @n: data
 *
 * Return: new adress of node or NULL if failed
 */

dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	dlistint_t *go, *temp, *new;
	unsigned int at;

	go = temp = *h;
	at = 1;
	if (idx == 0)
		return (add_dnodeint(h, n));
	new = malloc(sizeof(dlistint_t));
	if (new == NULL)
		return (NULL);
	while (go != NULL)
	{
		if ((at == idx) && go->next != NULL)
		{
			new->next = go->next;
			go->next = new;
			new->prev = go;
			new->n = n;
			new->next->prev = new;
			return (new);
		}
		go = go->next;
		at++;
	}
	free(new);
	if (at == (idx + 1))
		return (add_dnodeint_end(h, n));
	return (NULL);
}
