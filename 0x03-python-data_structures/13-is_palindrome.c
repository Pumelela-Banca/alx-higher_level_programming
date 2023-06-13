#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 *
 * is_palindrome - checks to see if list is palidrome
 *
 * @head: start of list
 *
 * Return: 0 false, 1 true
 */

int is_palindrome(listint_t **head)
{
	listint_t *test, *prev, *new, *temp;
	int sum = 1;

	if (*head == NULL)
		return (1);
	test = prev = *head;
	if (test->next == NULL)
		return (1);
	if (test->next->next == NULL && test->n == test->next->next->n)
		return (1);
	while (test->next != NULL)
	{
		new = malloc(sizeof(listint_t ));
		if (new == NULL)
			exit(EXIT_FAILURE);
		if (sum == 1)
		{
			new->next = NULL;
			new->n = test->n;
		}
		else
		{
			new->next = temp;
			new->n = test->n;
			if (test->n == test->next->n && prev->n == test->next->next->n)
				return (compare(new, test->next));
			else if (test->next->next != NULL && test->n == test->next->next->n &&
					prev->n == test->next->next->next->n)
				return (compare(new, test->next->next));
		}
		sum++;
		temp = new;
		prev = test;
		test = test->next;
	}
	free_listint(new);
	return (0);
}

/**
 * compare - comapres two linked lists
 *
 * @new: new list
 * @old: old list to copmare to
 *
 * Return: 1 if the same and 0 if not
 */

int compare(listint_t *new, listint_t *old)
{
	listint_t *rel, *one, *two;

	rel = new;
	one = new;
	two = old;
	while (two != NULL || one != NULL)
	{
		if (new->n != old->n)
			return (0);
		one = one->next;
		two = two->next;
	}
	free_listint(rel);
	return (1);
}
