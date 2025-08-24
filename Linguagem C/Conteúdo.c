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

//Outra forma de calcular média

#include <stdio.h>

int main(){
    float prova1, prova2, média;
    scanf("%f", &prova1);
    scanf("%f", &prova2);
    média = (prova1 + prova2) / 2.0;
    printf("%.2f", média);
    
return 0;

}

// Multiplicação 

#include <stdio.h>

int main(){
    int valor, multiplicando, resultado;
    printf("Digite um valor: ");
    scanf("%i", &valor);
    printf("Digite outro valor: ");
    scanf("%i", &multiplicando);
    resultado = (valor * multiplicando);
    printf("O resultado é: %i", resultado);

    
return 0;
    
}

//Outra forma de multiplicar

#include <stdio.h>

int calc_multiplicando(int valor, int multiplicando);

int main(){
    int valor, multiplicando, resultado;
    printf("Digite o primeiro valor: ");
    scanf("%i", &valor);
    printf("digite o segundo valor: ");
    scanf("%i", &multiplicando);
    resultado = calc_multiplicando(valor, multiplicando);
    printf("O resultado é: %i", resultado);
    
return 0;

}

int calc_multiplicando(int valor, int multiplicando){
    int resultado;
    resultado = (valor * multiplicando);
    return resultado;
    
}

