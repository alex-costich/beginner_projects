/******************************************************************************

MINESWEEPER - ALEJANDRO COSTICH SANDOVAL

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>


char mineField[10][10] = {
        {'0','0','0','0','0','0','0','0','0','0'},
        {'0','1','1','1','1','1','1','1','1','0'},
        {'0','1','1','1','1','1','1','1','1','0'},
        {'0','1','1','1','1','1','1','1','1','0'},
        {'0','1','1','1','1','1','1','1','1','0'},
        {'0','1','1','1','1','1','1','1','1','0'},
        {'0','1','1','1','1','1','1','1','1','0'},
        {'0','1','1','1','1','1','1','1','1','0'},
        {'0','1','1','1','1','1','1','1','1','0'},
        {'0','0','0','0','0','0','0','0','0','0'},
        
    };
    
char printField[10][10] = {
    {' ','1','2','3','4','5','6','7','8',' ',},
    {'1','-','-','-','-','-','-','-','-','1',},
    {'2','-','-','-','-','-','-','-','-','2',},
    {'3','-','-','-','-','-','-','-','-','3',},
    {'4','-','-','-','-','-','-','-','-','4',},
    {'5','-','-','-','-','-','-','-','-','5',},
    {'6','-','-','-','-','-','-','-','-','6',},
    {'7','-','-','-','-','-','-','-','-','7',},
    {'8','-','-','-','-','-','-','-','-','8',},
    {' ','1','2','3','4','5','6','7','8',' ',}
    
};

void fieldPrint();
void fieldPrintXray();

int main()
{
    
    int i, j, k, bombsAround = 0, lose = 0, bombX, bombY, replay = 1, levelLock = 1;
    srand(time(NULL));
    
    while(replay == 1){
    // Plant bombs
    for (k = 0; k < 5; k++){
        bombX = rand() % 10;
        bombY = rand() % 10;
        
        if(mineField[bombX][bombY] == '9' || mineField[bombX][bombY] == '0')
            k--;
        else{
            mineField[bombX][bombY] = '9'; 
            // printf("Bomba plantada. \n");        FOR TESTING
        }
    }
    
    if (levelLock != 1){
        for (k = 0; k < 5; k++){
        bombX = rand() % 10;
        bombY = rand() % 10;
        
        if(mineField[bombX][bombY] == '9' || mineField[bombX][bombY] == '0')
            k--;
        else{
            mineField[bombX][bombY] = '9'; 
            // printf("Bomba plantada. \n");        FOR TESTING
        }
    }
        
    }
    
    fieldPrintXray();    //FOR TESTING
    
    while(lose != 1){
        system("clear");
        bombsAround = 0;
        fieldPrint();
        
        printf("\nIngrese la posición a la que se quiere mover en x. ");
        scanf("%i", &j);
        printf("Ingrese la posición a la que se quiere mover en y. ");
        scanf("%i", &i);
        
        // Bomb check
        if (mineField[i][j] == '1'){
            // printf("Checando bombas...\n");      FOR TESTING
            if (mineField[i+1][j] == '9') bombsAround++;
            if (mineField[i+1][j+1] == '9') bombsAround++;
            if (mineField[i+1][j-1] == '9') bombsAround++;
            if (mineField[i][j+1] == '9') bombsAround++;
            if (mineField[i][j-1] == '9') bombsAround++;
            if (mineField[i-1][j] == '9') bombsAround++;
            if (mineField[i-1][j+1] == '9') bombsAround++;
            if (mineField[i-1][j-1] == '9') bombsAround++;
            
            printField[i][j] = bombsAround + 48;
            // printf("Guardando bombas...\n");     FOR TESTING
        }
        else if (mineField[i][j] == '9'){
            lose = 1;
            printField[i][j] = '*';
            fieldPrint();
            printf("\nPerdiste.\n");
        }
     
    }
    
    
    printf("¿Quieres jugar el siguiente nivel? 1 = Si, 0 = No.\n");
    scanf("%i", &replay);
    if(replay == 1)
        levelLock = 0;
        lose = 0;
    }
    system("clear");
    printf("Gracias por jugar.");
    
    return 0;
}


void fieldPrint(){
   // system("clear");
    int h, l;
    
    for(h = 0; h < 10; h++){
        printf("\n");
        for(l = 0; l < 10; l++)
            printf("%c ", printField[h][l]);
    }
    
    printf("\n");
    
}


//XRAY FOR TESTING

void fieldPrintXray(){
    printf("\n\n");
    int h, l;
    
    for(h = 0; h < 10; h++){
        printf("\n");
        for(l = 0; l < 10; l++)
            printf("%c ", mineField[h][l]);
    }
    
    printf("\n");
    
}





