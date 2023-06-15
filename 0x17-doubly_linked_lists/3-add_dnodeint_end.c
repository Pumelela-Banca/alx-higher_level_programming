#include "lists.h"

/**
 * add_dnodeint_end - add node at end of list
 *
 * @head: head of list
 * @n: data
 *
 * Return: new node
 */

dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *new, *temp;

	new = malloc(sizeof(dlistint_t));
	if (new == NULL)
		return (NULL);
	if (*head == NULL)
	{
		new->next = NULL;
		new->prev = NULL;
		new->n = n;
		*head = new;
		return (new);
	}

	temp = *head;
	while (temp != NULL)
	{
		if (temp->next == NULL)
		{
			new->next = NULL;
			new->prev = temp;
			new->n = n;
			temp->next = new;
			break;
		}
		temp = temp->next;
	}
	return (new);
}
