/*
    GENE TREE - ACS
*/

#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#include <string.h>

struct node {
    char name[10];
    struct node *left, *right;
};

void pre(struct node* n);
void in(struct node* n);
void post(struct node* n);

int main() {
    struct node* granny;
    granny = (struct node*)malloc(sizeof(struct node));
    
    if (granny == NULL) {
        return 1;
    }
    
    strcpy(granny->name, "Socorro");
    
    granny->left = (struct node*)malloc(sizeof(struct node));
    strcpy(granny->left->name, "Silvia");
    
    granny->left->left = NULL;
    granny->left->right = NULL;
    granny->right = (struct node*)malloc(sizeof(struct node));
    strcpy(granny->right->name, "Irma");
    
    granny->right->left = NULL;
    granny->right->right = NULL;
    
    // GRANDCHILDREN
    granny->left->left = (struct node*)malloc(sizeof(struct node));
    strcpy(granny->left->left->name, "Alejandro");
    
    granny->left->left->left = NULL;
    granny->left->left->right = NULL;
    granny->left->right = (struct node*)malloc(sizeof(struct node));
    strcpy(granny->left->right->name, "Vidal");
    
    granny->left->right->left = NULL;
    granny->left->right->right = NULL;
    granny->right->right = (struct node*)malloc(sizeof(struct node));
    strcpy(granny->right->right->name, "Jorge");
    
    granny->right->right->left = NULL;
    granny->right->right->right = NULL;
    granny->right->left = (struct node*)malloc(sizeof(struct node));
    strcpy(granny->right->left->name, "Armando");
    
    granny->right->left->left = NULL;
    granny->right->left->right = NULL;
    
    printf("Preorder:\n");
    pre(granny);
    printf("\n");
    
    printf("Inorder:\n");
    in(granny);
    printf("\n");
    
    printf("Postorder:\n");
    post(granny);
    printf("\n");
    return 0;
    
}

void pre(struct node* n) { // Preorder function
    if(n==NULL)
        return;
    printf("%s ", n->name);
    pre(n->left);
    pre(n->right);
}

void in(struct node* n) { // Inorder function
    if(n==NULL)
        return;
    in(n->left);
    printf("%s ", n->name);
    in(n->right);
}

void post(struct node* n) {// Postorder function
    if(n==NULL)
        return;
    post(n->left);
    post(n->right);
    printf("%s ", n->name);
}
