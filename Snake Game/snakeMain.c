/******************************************************************************

Snech.

*******************************************************************************/
#include <stdio.h>
#include "conio.h"
#include <time.h>
#include <stdlib.h>
#include <malloc.h>
#define ESC 27 // escape key
#define SCRWIDTH 80 // screen width
#define SCRHEIGHT 25 // screen height

typedef struct vibora{
    int x,y, i;
    struct vibora *sig, *ant;
}Vibora;

void muestraVibora (Vibora *p);

int main()
{
    int xf, yf, dir = 1, puntaje = 0;
    char t = '@';
    Vibora *Inicio, *Final;
    
    Final = (Vibora*)malloc(sizeof(Vibora));
    Inicio = (Vibora*)malloc(sizeof(Vibora));
    
    if(Inicio == NULL){ // == is not equal to =
        perror("No se puede iniciar el juego.");
        exit(1);
        
    }
    
    textbackground(BLACK);
    clrscr();
    srand(time(NULL));
    
    Inicio -> x = rand()%SCRWIDTH+1;
    Inicio -> y = rand()%SCRHEIGHT+1;
    Inicio -> sig = NULL;
    Inicio -> ant = NULL;
    
    Final = Inicio;
    
    xf = rand()%SCRWIDTH+1;
    yf = rand()%SCRHEIGHT+1;
    
    textcolor(RED); // spawn fruit
    gotoxy(xf, yf);
    cprintf("Ó");
    
    textcolor(BLACK); // resetting colors
    
    do{
        do{
            textcolor(WHITE);
            gotoxy(120,1);
            printf("PUNTAJE: %i", puntaje);
            textcolor(BLACK);
            
            while(Final -> sig != NULL){ // Final hops all the way to the list's end
                Final = Final -> sig;
            }
            
            textcolor(BLACK); // Prints in black over the snake's tail
            muestraVibora(Final);
            
            while(Final -> ant != NULL){ // Final copies next xy values and moves forward
                Final -> x = Final -> ant -> x;
                Final -> y = Final -> ant -> y;
                Final = Final -> ant;
            }
            
            switch(dir){ // direction switch
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
            
            textcolor(RED); // spawn fruit
            gotoxy(xf, yf);
            cprintf("Ó");
                
            textcolor(BLACK);
                
            
            if(Inicio -> y == yf && Inicio -> x == xf){ // respawn fruit if eaten
                xf = rand()%SCRWIDTH+1;
                yf = rand()%SCRHEIGHT+1;
                
                puntaje += 1;
                
                Vibora *tmp = malloc(sizeof(Vibora)); // tmp variable definition
                tmp -> ant = NULL;  // nothing behind temp
                tmp -> sig = Inicio; // hook tmp to Inicio
                Inicio -> ant = tmp; // hook Inicio to tmp
                Inicio = tmp; // Inicio takes tmp's position for the list to keep growing through cycles
                Inicio -> x = Inicio -> sig -> x;
                Inicio -> y = Inicio -> sig -> y;
                
            }
           
        }while(!kbhit());
        
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
        
        //system("clear"); // reset screen
    
    }while(t!=ESC);
    
    return 0;
}


void muestraVibora (Vibora *p){
    while(p != NULL){ // spawn snake
        gotoxy(p -> x, p -> y);
        cprintf("@"); // cprintf (colorprintfunction) prints in color
        p = p -> sig;
    
    }
    
}

