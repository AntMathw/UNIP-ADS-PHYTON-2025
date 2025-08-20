#include <stdio.h>;

int main(){
    float distancia = 438;
    float tempo = 6;
    float velocidade = distancia / tempo;
    printf("%.2f", velocidade);
return 0;
}

//Calculo da Média

#include <stdio.h>;

float calc_media(float p1, float p2);

int main(){
    float prova1, prova2, média;
    printf("Digite o valor da primeira prova");
    scanf("%f", &prova1);
    printf("Digite o valor da segunda prova");
    scanf("%f", &prova2);
    média = calc_media(prova1, prova2);
    printf("O resultado da média é: %.2f", média);
    return 0;
}

float calc_media(float p1, float p2){
    float média;
    média = (p1 + p2) / 2.0;
    return média;
    
}
