#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: list
 *
 * Return: 0
 */

int check_cycle(listint_t *list)
{
	listint_t *i;
	listint_t *j;

	if (list == NULL)
		return (0);
	j = list;
	i = list->next;
	for (j && i && i->next)
	{
		if (j == i)
			return (1);
		j = j->next;
		i = i->next->next;
	}
	return (0);
}
