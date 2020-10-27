#include <stdio.h>
#include "fic_wave.h"
#include <errno.h>

FILE    *abre_wave(const char *ficWave, float *fm) {
    FILE    *fpWave;

    if ((fpWave = fopen(ficWave, "r")) == NULL) return NULL;
    if (fseek(fpWave, 44, SEEK_SET) < 0) return NULL;

    //Freq. muestreo
    int freqMuestreo;
    fseek(fpWave, 24, SEEK_SET);
    fread(&freqMuestreo, 4, 1, fpWave);
    *fm = freqMuestreo;

    //Canales
    fseek(fpWave, 22, SEEK_SET);
    int canales = 0;
    fread(&canales, 2, 1, fpWave);
    if(canales != 1){
        fprintf(stderr, "Error: Audio en más de un canal.\n", strerror(errno));
    }

    //Codif.
    fseek(fpWave, 16, SEEK_SET);
    int codif;
    fread(&codif, 4, 1, fpWave);
    if(codif != 16){
        fprintf(stderr, "Error: Audio no codificado con PCM Lineal de 16 bits.\n", strerror(errno));
    }

    return fpWave;
}

size_t  lee_wave(void *x, size_t size, size_t nmemb, FILE *fpWave) {
    return fread(x, size, nmemb, fpWave);
}

void    cierra_wave(FILE *fpWave) {
    fclose(fpWave);
}