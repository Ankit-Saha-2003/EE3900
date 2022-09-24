#include <stdio.h>
#include <stdlib.h>
#include <complex.h>

#define dc double complex 

dc *fft(dc *signal, int N);

dc *fft(dc *signal, int N) {
	if (N == 1) {
		return signal;
	}
	dc *f1 = malloc(N/2 * sizeof(*f1));
	dc *f2 = malloc(N/2 * sizeof(*f2));
	for (int i = 0; i < N/2; i++) {
		f1[i] = signal[2*i];
		f2[i] = signal[2*i + 1];
	}
	dc *F1 = fft(f1, N/2);
	dc *F2 = fft(f2, N/2);
	dc *X = malloc(N * sizeof(*X));
	for (int i = 0; i < N/2; i++) {
		X[i] = 	F1[i] + cexp(-2 * I * M_PI * i / N) * F2[i];
		X[i + N/2] = F1[i] - cexp(-2 * I * M_PI * i / N) * F2[i];
	}
	/*
	if (F1) free(F1);
	if (F2) free(F2);
	if (f1) free(f1);
	if (f2) free(f2);
	*/
	return X;
}
