#include "lists.h"

/**
 * check_cycle - checks if there's a circcle in he list
 *
 * @list: pointer to the list's first node
 *
 * Return: 1 if true and 0 if false
 */

int check_cycle(listint_t *list)
{
	listint_t *lead = list, *next_node = list;

	while (next_node != NULL && lead != NULL && lead->next != NULL)
	{
		next_node = next_node->next;
		lead = lead->next->next;

		if (next_node == lead)
			return (1);
	}

	return (0);
}
