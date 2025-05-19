#include <SDL.h>
#include <iostream>
#include <string>
#include <vector>

// Struttura per rappresentare un punto
struct Point {
    int x;
    int y;
};

// Funzione per disegnare una linea
void drawLine(SDL_Renderer* renderer, int x1, int y1, int x2, int y2) {
    SDL_RenderDrawLine(renderer, x1, y1, x2, y2);
}

// Funzione per disegnare un cerchio (approssimato con segmenti)
void drawCircle(SDL_Renderer* renderer, int centerX, int centerY, int radius) {
    for (int i = 0; i < 360; ++i) {
        double angle1 = 2.0 * M_PI * i / 360;
        double angle2 = 2.0 * M_PI * (i + 1) / 360;
        int x1 = centerX + radius * cos(angle1);
        int y1 = centerY + radius * sin(angle1);
        int x2 = centerX + radius * cos(angle2);
        int y2 = centerY + radius * sin(angle2);
        SDL_RenderDrawLine(renderer, x1, y1, x2, y2);
    }
}

int main(int argc, char* argv[]) {
    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        std::cerr << "SDL could not initialize! SDL_Error: " << SDL_GetError() << std::endl;
        return 1;
    }

    SDL_Window* window = SDL_CreateWindow("Disegno 'you'", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 600, 400, SDL_WINDOW_SHOWN);
    if (window == nullptr) {
        std::cerr << "Window could not be created! SDL_Error: " << SDL_GetError() << std::endl;
        return 1;
    }

    SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
    if (renderer == nullptr) {
        std::cerr << "Renderer could not be created! SDL_Error: " << SDL_GetError() << std::endl;
        return 1;
    }

    SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255); // Imposta il colore di disegno a bianco
    SDL_RenderClear(renderer); // Pulisce lo schermo

    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255); // Imposta il colore di disegno a nero

    // Definisci le coordinate per disegnare la 'y', la 'o' e la 'u'
    int start_x = 100;
    int start_y = 200;

    // Disegna la 'y'
    drawLine(renderer, start_x, start_y - 50, start_x + 25, start_y);
    drawLine(renderer, start_x + 25, start_y, start_x + 50, start_y - 50);
    drawLine(renderer, start_x + 25, start_y, start_x + 25, start_y + 50);

    // Disegna la 'o'
    drawCircle(renderer, start_x + 100, start_y, 25);

    // Disegna la 'u'
    drawLine(renderer, start_x + 175, start_y - 50, start_x + 175, start_y + 25);
    drawCircle(renderer, start_x + 200, start_y + 25, 25);
    drawLine(renderer, start_x + 225, start_y - 50, start_x + 225, start_y + 25);

    SDL_RenderPresent(renderer); // Aggiorna lo schermo con ciò che è stato disegnato

    SDL_Event event;
    bool quit = false;
    while (!quit) {
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                quit = true;
            }
        }
        SDL_Delay(10); // Piccolo ritardo per non sovraccaricare la CPU
    }

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}