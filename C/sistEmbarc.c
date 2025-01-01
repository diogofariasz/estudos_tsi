#include <stdio.h>
#include "pico/stdlib.h"

// Definição dos pinos
#define PINO_LED_VERMELHO 2
#define PINO_LED_AMARELO 3
#define PINO_LED_VERDE 4
#define PINO_LED_PEDESTRE 5
#define PINO_BUZZER 6
#define PINO_BOTAO 7

// Função para configurar os pinos
void configurar_pinos() {
    gpio_init(PINO_LED_VERMELHO);
    gpio_set_dir(PINO_LED_VERMELHO, GPIO_OUT);

    gpio_init(PINO_LED_AMARELO);
    gpio_set_dir(PINO_LED_AMARELO, GPIO_OUT);

    gpio_init(PINO_LED_VERDE);
    gpio_set_dir(PINO_LED_VERDE, GPIO_OUT);

    gpio_init(PINO_LED_PEDESTRE);
    gpio_set_dir(PINO_LED_PEDESTRE, GPIO_OUT);

    gpio_init(PINO_BUZZER);
    gpio_set_dir(PINO_BUZZER, GPIO_OUT);

    gpio_init(PINO_BOTAO);
    gpio_set_dir(PINO_BOTAO, GPIO_IN);
    gpio_pull_up(PINO_BOTAO); 
}

// Função para emitir o som intermitente no buzzer
void buzzer_intermitente(int tempo) {
    for (int i = 0; i < tempo; i++) {
        gpio_put(PINO_BUZZER, 1);
        sleep_ms(500); 
        gpio_put(PINO_BUZZER, 0);
        sleep_ms(500); 
    }
}

// Função principal de controle dos semáforos
int main() {
    Serial.begin(115200); 
    setvbuf(stdout, NULL, _IONBF, 0); 
    configurar_pinos();

    while (true) {
        gpio_put(PINO_LED_VERDE, 1);
        gpio_put(PINO_LED_AMARELO, 0);
        gpio_put(PINO_LED_VERMELHO, 0);
        gpio_put(PINO_LED_PEDESTRE, 0);
        buzzer_intermitente(0); 
        sleep_ms(8000);  

        gpio_put(PINO_LED_VERDE, 0);
        gpio_put(PINO_LED_AMARELO, 1);
        sleep_ms(2000); 

        gpio_put(PINO_LED_AMARELO, 0);
        gpio_put(PINO_LED_VERMELHO, 1);
        sleep_ms(10000);  

        // Verifica se o botão foi pressionado
        if (gpio_get(PINO_BOTAO) == 0) {
            gpio_put(PINO_LED_VERMELHO, 0);
            gpio_put(PINO_LED_PEDESTRE, 1);
            buzzer_intermitente(15); 
            sleep_ms(15000);  
            
            gpio_put(PINO_LED_PEDESTRE, 0);
        }
    }

    return 0;
}
