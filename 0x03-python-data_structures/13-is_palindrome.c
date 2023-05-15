#include "lists.h"
#include <stddef.h>

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the first node in the list
 * Return: pointer to the first node in the new list
 */

void reverse_list(listint_t **head)
{
	listint_t *prev_node = NULL;
	listint_t *current_node = *head;
	listint_t *next_node = NULL;

	while (current_node)
	{
		next_node = current_node->next;
		current_node->next = prev_node;
		prev_node = current_node;
		current_node = next_node;
	}

	*head = prev_node;
}


/**
 * is_palindrome - checks if a singly linked list is a palindrome
 *
 * @head: Pointer to the head node
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *fast_node = *head, *slow_node = *head;
	listint_t *temp_node = *head, *dup_node = NULL;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	while (1)
	{
		fast_node = fast_node->next->next;
		if (fast_node == NULL)
		{
			dup_node = slow_node->next;
			break;
		}
		if (fast_node->next == NULL)
		{
			dup_node = slow_node->next->next;
			break;
		}
		slow_node = slow_node->next;
	}

	reverse_list(&dup_node);

	while (dup_node && temp_node)
	{
		if (temp_node->n == dup_node->n)
		{
			dup_node = dup_node->next;
			temp_node = temp_node->next;
		}
		else
			return (0);
	}

	if (!dup_node)
		return (1);
	return (0);
}
