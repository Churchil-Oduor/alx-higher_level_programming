#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - function inserts a number into a sorted linked list.
 *
 * @head: pointer holding pointer of head node of the list.
 * @number: the number to be inserted into the linked list.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;
	new = malloc(sizeof(new));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;
	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL)
		{
			if ((current->next)->n > number)
			{
				new->next = current->next;
				current->next = new;
				return (new);
			}
			current = current->next;
		}
	}
	return (new);
}
