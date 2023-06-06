#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * insert_node - inserts node in a list
 *
 * @head: head of list
 * @number: data of node
 *
 * Return: new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *new;
	int st;

	st = 0;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return NULL;
	new->n = number;
	prev = *head;
	while (prev->next != NULL)
	{
		if (number > prev->n)
			prev = prev->next;
		else if (number == prev->n)
		{
			new->next = prev->next;
			prev->next = new;
			return (new);
		}
		else if (st == 0 && number < prev->n)
		{
			new->next = prev->next;
			*head = new;
			return (*head);
		}
		else
		{
			new->next = prev->next;
			prev->next = new;
			return (new);
		}
		st++;
	}
	prev->next = new;
	new->next = NULL;
	return (new);
}
