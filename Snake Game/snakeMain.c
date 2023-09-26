/******************************************************************************
LINUX SNAKE GAME
*******************************************************************************/
#include <stdio.h>
#include "conio.h" // had to manually import <conio.h>, as I was working with an online compiler
#include <time.h>
#include <stdlib.h>
#include <malloc.h>
#define ESC 27 // definition for escape key
#define SCRWIDTH 80 // modify screen width
#define SCRHEIGHT 25 // modify screen height

typedef struct vibora{ // structure defininition for linked list
    int x, y, i;
    struct vibora *sig, *ant;
}Vibora;

void muestraVibora (Vibora *p);

int main()
{
    int xf, yf, dir = 1, puntaje = 0; // xf and xy for fruit coords, default direction is case 1.
    char t = '@'; // snake body is made of @'s
    Vibora *Inicio, *Final;
    
    Final = (Vibora*)malloc(sizeof(Vibora));
    Inicio = (Vibora*)malloc(sizeof(Vibora));
    
    if(Inicio == NULL){ // in case of failed malloc
        perror("No se puede iniciar el juego.");
        exit(1);
        
    }
    
    textbackground(BLACK);
    clrscr();
    srand(time(NULL));
    
    Inicio -> x = rand()%SCRWIDTH+1; // random starter x
    Inicio -> y = rand()%SCRHEIGHT+1; // random starter y
    Inicio -> sig = NULL;
    Inicio -> ant = NULL;
    
    Final = Inicio; // snake tail starts at head's position
    
    xf = rand()%SCRWIDTH+1;
    yf = rand()%SCRHEIGHT+1;
    
    textcolor(RED); // fruit spawn
    gotoxy(xf, yf);
    cprintf("Ó");
    
    textcolor(BLACK); // color reset
    
    do{
        do{
            // score print
            textcolor(WHITE);
            gotoxy(120,1);
            printf("PUNTAJE: %i", puntaje);
            textcolor(BLACK);
            
            while(Final -> sig != NULL){ // final (tail) hops all the way to the list's end as long as there's a node to hop to.
                Final = Final -> sig;
            }
            
            textcolor(BLACK); // prints in black over snake's print trail
            muestraVibora(Final); // prints snake
            
            while(Final -> ant != NULL){ // final (tail) copies next xy values and moves forward
                Final -> x = Final -> ant -> x;
                Final -> y = Final -> ant -> y;
                Final = Final -> ant;
            }
            
            switch(dir){ // direction switch on key input
                case 1: if(Inicio -> y < 1)
                            Inicio -> y = 25;
                        Inicio -> y--;
                        break;
                case 2: if(Inicio -> x > 79)
                            Inicio -> x = 0;
                        Inicio -> x++;
                        break;
                case 3: if(Inicio -> y > 24)
                            Inicio -> y = 0;
                        Inicio -> y++;
                        break;
                case 4: if(Inicio -> x < 1)
                            Inicio -> x = 80;
                        Inicio -> x--;
                        break;
                
            }
            
            textcolor(YELLOW);
            muestraVibora(Inicio);
            
            system("sleep 0.1");
            
            textcolor(RED); // fruit spawn
            gotoxy(xf, yf);
            cprintf("Ó");
                
            textcolor(BLACK);
                
            if(Inicio -> y == yf && Inicio -> x == xf){ // respawns fruit if eaten
                xf = rand()%SCRWIDTH+1;
                yf = rand()%SCRHEIGHT+1;
                
                puntaje += 1; // score goes up
                
                Vibora *tmp = malloc(sizeof(Vibora)); // tmp variable definition
                tmp -> ant = NULL;  // nothing behind temp
                tmp -> sig = Inicio; // hook tmp to Inicio
                Inicio -> ant = tmp; // hook Inicio to tmp
                Inicio = tmp; // Inicio takes tmp's position for the list to keep growing every cycle
                Inicio -> x = Inicio -> sig -> x;
                Inicio -> y = Inicio -> sig -> y;
                
            }
           
        }while(!kbhit());
        // vvv when kbhit vvv
        t = getch(); // t = tolower(getch()); ||<ctypes.h>|| converts to lowercase
        
        switch(t){ // direction set based on key input
            case 's': dir = 3;
                      break;
            case 'a': dir = 4;
                      break;
            case 'd': dir = 2;
                      break;
            case 'w': dir = 1;
                      break;
                      
        }
        //system("clear"); //screen reset
    
    }while(t!=ESC); // ESC input to exit.
    
    return 0;
}


void muestraVibora (Vibora *p){
    while(p != NULL){ // spawn snake
        gotoxy(p -> x, p -> y);
        cprintf("@"); // cprintf (colorprintfunction) prints in color
        p = p -> sig;
    
    }
    
}

