#include "lists.h"
/**
 * check_cycle - checks to see if list is a cycle
 * @list: linked list
 * Return: 0 for false, 1 true
 */

int check_cycle(listint_t *list)
{
	listint_t *copy;
	listint_t *location;

	copy = list;

	while (copy != NULL)
	{
		location = list;
		while (location != NULL)
		{
			if (location == copy && location->next == copy->next)
				return (1);
			location = location->next;
		}
		copy = copy->next;
	}
	return (0);
}
