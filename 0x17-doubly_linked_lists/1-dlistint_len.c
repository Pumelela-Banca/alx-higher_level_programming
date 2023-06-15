#include "lists.h"

/**
 * dlistint_len - counts number of elements in a list
 *
 * @h: head
 *
 * Return: size of list
 */

size_t dlistint_len(const dlistint_t *h)
{
	const dlistint_t *cou;
	size_t len;

	cou = h;
	if (h == NULL)
		return (0);
	if (cou->next == NULL)
		return (1);
	len = 0;
	while (cou != NULL)
	{
		cou = cou->next;
		len++;
	}
	return (len);
}
