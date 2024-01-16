#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - function that checks if a singly linked
 * list has a cycle in it.
 *
 * @list: node to a singly linked list.
 * Return: 0 if there is no cycle else 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *fast;
	listint_t *slow;

	if (list->next == NULL)
		return (0);

	fast = malloc(sizeof(list));
	slow = malloc(sizeof(list));

	if (fast == NULL || slow == NULL)
		return (-1);

	fast = (list->next)->next;
	slow = list->next;

	do {

		if (fast == slow)
			return (1);
		else if (fast == NULL || slow == NULL)
			return (0);

		fast = (fast->next)->next;
		slow = slow->next;

	} while (1);

	return (0);
}
