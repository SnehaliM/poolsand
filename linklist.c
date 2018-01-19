#include<stdio.h>
struct node
{
	int info;
	struct node *next;
};
struct node *i=NULL;
struct node *n=NULL;
void addbeg(int x)
{
	struct node *head;
	head=(struct node*)malloc(sizeof (struct node));
	if(head==NULL)
	{
		head->info=x;
		if(i==NULL)
		{
			head->next=NULL;
			head=n=i;
		}
		else
		{
			head->next=i;
			i=head;
		}
	}
}
void del()
{
	struct node *head;
	if(n==NULL)
	i=head;
	else
	{
		printf("%d ",head->info);
		free(head);
	}
}
void printlist()
{
	struct node *head;
	while(head!=NULL)
	{
	printf("%d ",head->info);
	head=head->next;
}

}
void main()
{
	int j,k;
	for(j=0;j<3;j++)
	{
		printf("enter no. in the node:");
		scanf("%d",&k);
    	addbeg(k);
	}
	printlist();
	del();
	
}
