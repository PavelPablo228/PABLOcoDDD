#include "Source1.h"
#include <stdbool.h>

void sum(int a, int i);
float mult(float a, float i);
void string(char arr[]);

struct Car
{
    int speed;
    char name[50];
    float weight;
};

struct MyStruct
{
    int width, hight;

};

void calc(struct MyStruct *obj);

int main()
{
    char line[228];
    FILE* file = fopen("test.txt", "r");

    fgets(line, 228, file);
    printf("%s", line);

    fclose(file);



    struct MyStruct square = { 77, 89 };
    calc(&square);

    int num = 0;
    int* pNum = &num;

    printf("%p - %p\n", pNum, &num);

    *pNum = 22;
    printf("%d - %d\n", *pNum, num);

    struct Car bmw;
    bmw.speed = 330;
    strcpy(bmw.name, "BMW XM");
    bmw.weight = 2695.95f;
    
    struct Car merc = { 280, "Mercedes-benz G-wagon 63 AMG", 2640.52f };
    printf("%s, max speed: %d, weight: %f\n", bmw.name, bmw.speed, bmw.weight);
    printf("%s, max speed: %d, weight: %f\n", merc.name, merc.speed, merc.weight);

 
    sum(79, 22);
    int x = 9, y = 8;
    sum(x, y);

    string("hi");
    char word[] = { 's', 'o', 'm', 'e' };
    string(word);

    float result = mult(2.9f, 6.4f);
    printf("%f\n", result);

    return 0;
}

void calc(struct MyStruct *obj) {
    int res = obj->width * obj->hight;
    printf("Result: %d\n", res);
}

void sum(int a, int i) {
    int res = a - i;
    printf("Result: %d\n", res);
}

void string(char arr[]) {
    printf("%s\n", arr);
}

float mult(float a, float i) {
    float res = a * i;
    printf("Result: %f\n", res);
    return res;
}



    int arr[] = { 2, 5, 6, 33, 99 };
    arr[2] = 6;
    printf("%d\n", arr[2]);

    float num[5];
    num[0] = 2.4f;
    num[1] = 8.5f;
    num[2] = 97.7f;

    char wor[] = { 'W', 'e', 'q', 't' };
    char word[] = "Hi, man!";

    word[2] = 'T';
    printf("%s\n", word);

    int array[4][5] = {
        {2, 3, 4},
        {6, 77, 8},
        {9, 12, 120, 25},
        {55, 3, 1, 29, 99}
    };

    array[2][3] = 44;
    printf("%d\n", array[2][3]);

    int x = 22;
     
    if (x > 99 && x == 22) {
        printf("Yeah\n");
    }
    else if (x > 100) {
        printf("X is right \n");
        if (x == 108)
            printf("X is not good\n");
    }
    else {
        printf("Nah\n");
    }

    bool isHazCarr = true;
    if (isHazCarr == true)
        printf("Yes\n");
    else
        printf("No\n");


    int s = 12;

    switch (s) {
    case 10: 
        printf("10"); 
        break;
    case 13:
        printf("13");
        break;
    case 122:
        printf("122");
        break;
    case 14:
        printf("14");
        break;
    case 19:
        printf("19");
        break;
    default:
        printf("Error\n");
        break;
        
    }


    for (float s = 77; s > 17; s /= 2) {
        printf("%f\n", s);
    }

    bool NUM = true;
    int w = 5;
    while (NUM == true) {
        printf("Enter text: ");
        scanf_s("%d\n", &w);
        if (w == 2)
            NUM == false;
        
    }

   int q = 4;
    while (q < 40) {
        printf("%d\n", q);
        q++;
    }

    bool NUM = false;
    do {
        printf("Yeah\n");
    } while (NUM);

    for (int e = 0; e < 7; e++) {
        if (e == 5)
            break;

        if (e % 2 == 0)
            continue;

        printf("%d\n", e);
    }

    int arr[] = { 4, 55, 78, 42, -9 };
    for (int i = 0; i <= 4; i++) {
        printf("%d\n", arr[i]);
    }
    printf("\n");
    int min = arr[0];
    int max = arr[0];
    for (int i = 0; i <= 4; i++) {
        if (arr[i] < min)
            min = arr[i];
        if (arr[i] > max)
            max = arr[i];
    }
    printf("Minimum: %d\n", min);
    printf("Maximum: %d\n", max);



    return 0;
}
