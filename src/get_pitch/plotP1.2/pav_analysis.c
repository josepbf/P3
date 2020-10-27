#include <math.h>
#include "pav_analysis.h"

float compute_power(const float *x, unsigned int N) {
    float sum=0;
    for(int i=0; i<N; i++){
        sum = sum + x[i]*x[i];
    }
    return 10*log10(sum/N);
}

float compute_am(const float *x, unsigned int N) {
    float sum=0;
    for(int i=0; i<N; i++){
        sum = sum + fabsf(x[i]);
    }
    return sum/N;
}

float compute_zcr(const float *x, unsigned int N, float fm) {
    float sum = 0;
    for(int i=1; i<N; i++){
        if(((x[i]>0)&&(x[i-1]<0))||((x[i]<0)&&(x[i-1]>0))){
            sum++;
        }
    }
    return (fm/2)*sum/(N-1);
}

float doesNothing(const float *x, unsigned int N){
    float ret=0;
    for(int i=0; i<N; i++){
        ret = ret + x[i];
    }
    return ret;
}
