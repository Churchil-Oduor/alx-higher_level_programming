#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>
#include "lists.h"

int count_nodes(listint_t **head);
/**
 * is_palindrome - checks if a linked-list is palindrome.
 * @head: head node of the linked list.
 * Return: 1 if a palindrome 0 else.
 */

int is_palindrome(listint_t **head)
{
	listint_t *node;
	int num, is_palindrome, index, i, *first_set, *second_set;

	is_palindrome = 0;
	num = count_nodes(head);

	if (num == 0 || (num % 2) != 0)
		return (is_palindrome);

	first_set = malloc(sizeof(int) * (num / 2));
	second_set = malloc(sizeof(int) * (num / 2));

	if (first_set == NULL || second_set == NULL)
		return (0);

	node = *head;
	index = 0;
	while (node->next != NULL)
	{
		if ((index + 1) == (num / 2) + 1)
			break;
		first_set[index] = node->n;
		index++;
		node = node->next;
	}

	index = 0;
	while (node->next != NULL)
	{
		second_set[index] = node->n;
		index++;
		node = node->next;
	}
	second_set[index] = node->n;
	for (i = 0; i < (num / 2); i++)
	{
		if (first_set[i] != second_set[(num / 2) - 1 - i])
		{
			is_palindrome = 0;
			break;
		}
		is_palindrome = 1;
	}
	free(first_set);
	free(second_set);
	return (is_palindrome);
}

/**
 * count_nodes - counts the number of nodes in a linked list.
 * @head: head node of linked list.
 * Return: total number of nodes in the linked list.
 */

int count_nodes(listint_t **head)
{
	listint_t *node;
	int num;

	node = *head;
	num = 1;
	if (node == NULL)
		return (num);

	while (node->next != NULL)
	{
		num++;
		node = node->next;
	}

	return (num);
}

