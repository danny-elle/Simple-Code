#include<stdio.h>
#include<stdlib.h> //malloc

typedef struct thing{
	int num;
	struct thing *next;
}thing;

thing *create(int num);
void printThing(thing *t);
thing *prepend(thing *t, int num);
thing *delete(thing *t);


int main(int argc, char *argv[])
{
/*
 *      Creating linked lists in main
 *
 *      //malloc returns void ptr
	thing *thingy = (thing *)malloc(sizeof(thing));
	thing *thingy1 = (thing *)malloc(sizeof(thing));
	thing *thingy2 = (thing *)malloc(sizeof(thing));

	//assign values to your nodes
	thingy->num = 1;
	thingy1->num = 3;
	thingy2->num = 5;
	
	//Link the nodes
	thingy->next = thingy1;
	thingy1->next = thingy2;
	thingy2->next = NULL;

	printf("%d\n", thingy->num);
	printf("%d\n", thingy1->num);
	printf("%d\n", thingy2->num);
	puts("\n");

	//to iterate through the linked list, we created an additional ptr (head) that starts from
	//the first node (thingy) in the linked list
	thing *head = thingy;

	//test whether head is Null, if its not then we iterate through the list printing its values
	//after each print we need to make sure to assign head to point to the next node.
	while( head != NULL)
	{
		printf("%d -> ", head->num);
		head = head->next;
	}
	
	puts("NULL");
*/
	thing *head = create(8);
/*	printf("%d\n", head->num);

	thing *tmp = head;
	
	int i;
	for(i=0; i<=5; i++){
		thing *new = create(i);
		//link head to the new node
		tmp->next = new;
		//move tmp down by pointing it to next
		tmp = tmp->next;
	}
*/
	//assign new linked list to head
	head = prepend(head,0);

	printThing(head);

	head = delete(head);
	printThing(head);


	return 0;
}

thing *create(int num)
{
	thing *thingy = (thing *)malloc(sizeof(thing));
	thingy->num = num;
	thingy->next = NULL;
	return thingy;
}

void printThing(thing *t)
{
	thing *head = t;

	while( head != NULL )
	{
		printf("%d -> ", head->num);
		head = head->next;
	}
	puts("NULL\n");
}

thing *prepend(thing *t, int num)
{
	thing *head = create(num);
	head->next = t;
	return head;
}

thing *delete(thing *t)
{
	//ptr pointing to the next node
	thing *current = t->next;
	free(t);
	return current;
}
