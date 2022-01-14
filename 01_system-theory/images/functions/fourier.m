close all
clear all

%% Time specifications:
   Fs = 100;                      % samples per second
   dt = 1/Fs;                     % seconds per sample
   StopTime = 1;                  % seconds
   t = (0:dt:StopTime-dt)';
   N = size(t,1);

   Fc = 5;                       % hertz
   x = cos(2*pi*Fc*t);

    X = fftshift(fft(x));

   dF = Fs/N;                      % hertz
   f = -Fs/2:dF:Fs/2-dF;           % hertz
   
   fig1 = figure;
   plot(f,abs(X)/N);
   xlabel('Frequency (in hertz)');
   title('Magnitude Response');
   
    set(findall(fig1,'type','text'),'fontSize',18)
    set(gca,'FontSize',12)

   figure;
   plot(t,x);
   set(findall(fig1,'type','text'),'fontSize',18)
   set(gca,'FontSize',12)

   
   %%
   
Fs = 1000;                    % Sampling frequency
T = 1/Fs;                     % Sample time
L = 1000;                     % Length of signal
t = (0:L-1)*T;                % Time vector
% Sum of a 50 Hz sinusoid and a 120 Hz sinusoid
x = 0.7*sin(2*pi*50*t) + sin(2*pi*120*t); 
y = x + 2*randn(size(t));     % Sinusoids plus noise
fig1=figure;
plot(Fs*t(1:50),y(1:50))
title('Signal Corrupted with Zero-Mean Random Noise')
xlabel('time (milliseconds)')
    set(findall(fig1,'type','text'),'fontSize',18)
    set(gca,'FontSize',12)

NFFT = 2^nextpow2(L); % Next power of 2 from length of y
Y = fft(y,NFFT)/L;
f = Fs/2*linspace(0,1,NFFT/2+1);
fig1=figure;
% Plot single-sided amplitude spectrum.
plot(f,2*abs(Y(1:NFFT/2+1))) 
title('Single-Sided Amplitude Spectrum of y(t)')
xlabel('Frequency (Hz)')
ylabel('|Y(f)|')
    set(findall(fig1,'type','text'),'fontSize',18)
    set(gca,'FontSize',12)
