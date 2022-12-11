#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*void sum_elf_calories(char file);
void sum_top_three(char file);*/


main() {
    FILE* reader;
    char ch;

    reader = fopen("./day1/calories.txt", "r");

    if (NULL == reader){
        printf("File not found");
    }

    do{
        ch = getline(reader);
        printf("%s", ch);
    } while (ch != EOF);

    fclose(reader);
    return 0;
}

/*void sum_elf_calories(char file){

}

void sum_top_three(char file){

}*/
