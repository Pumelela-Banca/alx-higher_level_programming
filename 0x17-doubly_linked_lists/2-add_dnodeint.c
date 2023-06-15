#include "lists.h"

/**
 * add_dnodeint - add node at start of list
 *
 * @head: head of list
 * @n: data
 *
 * Return: address of new element
 */

dlistint_t *add_dnodeint(dlistint_t **head, const int n)
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
	else
	{
		temp = *head;
		new->next = *head;
		new->prev = NULL;
		temp->prev = new;
		new->n = n;
		*head = new;
		return (new);
	}
}
