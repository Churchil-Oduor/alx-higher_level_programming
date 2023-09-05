#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a list has a cycle.
 *
 * @list: head node of the list.
 * Return: 0 if no cycle else 1.
 */

int check_cycle(listint_t *list)
{
	listint_t *node;

	if (list->next == NULL)
		return (0);

	node = malloc(sizeof(list));

	if (node == NULL)
		return (-1);

	node->n = list->n;
	node->next = list->next;
	while (node->next != NULL)
	{
		if (node->next == list)
			return (1);
		node = node->next;
	}
	return (0);
}
