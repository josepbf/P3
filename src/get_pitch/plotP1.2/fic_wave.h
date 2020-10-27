#ifndef FIC_WAVE_H
#define FIC_WAVE_H

FILE    *abre_wave(const char *ficWave, float *fm);
size_t  lee_wave(void *x, size_t size, size_t nmemb, FILE *fpWave);
void    cierra_wave(FILE *fpWave);

#endif  /* FIC_WAV_H    */