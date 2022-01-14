close all
clear all

x=0:0.001:2*pi;
f=x;
g=sin(x);
h=f+g;

fig1 = figure;
plot(x,f);
xlabel('x');
ylabel('f(x)');
set(findall(fig1,'type','text'),'fontSize',18)
set(gca,'FontSize',12)

fig1 = figure;
plot(x,g);
xlabel('x');
ylabel('g(x)');
set(findall(fig1,'type','text'),'fontSize',18)
set(gca,'FontSize',12)

fig1 = figure;
plot(x,g+f);
xlabel('x');
ylabel('h(x)');
set(findall(fig1,'type','text'),'fontSize',18)
set(gca,'FontSize',12)


fig1 = figure;
co = conv(f,g);
plot(co);
xlabel('x');
ylabel('h(x)');
set(findall(fig1,'type','text'),'fontSize',18)
set(gca,'FontSize',12)

%%
close all
clear all

Fs = 1000;                    % Sampling frequency
T = 1/Fs;                     % Sample time
L = 1000;                     % Length of signal
t = (0:L-1)*T;                % Time vector
% Sum of a 50 Hz sinusoid and a 120 Hz sinusoid
x = 0.7*sin(2*pi*50*t) + sin(2*pi*120*t); 
y = x + 0.5*randn(size(t));     % Sinusoids plus noise
fig1=figure;
plot(Fs*t(1:50),y(1:50))
axis([-0 50 -2.5 2.5]);
 set(gca,'FontSize',12)

% Construct blurring window.
windowWidth = int16(5);
halfWidth = windowWidth / 2;
gaussFilter = gausswin(7);
gaussFilter = gaussFilter / sum(gaussFilter); % Normalize.

yS = conv(y, gaussFilter)

fig1=figure;
plot(Fs*t(1:50),yS(1:50))
axis([-0 50 -2.5 2.5]);
 set(gca,'FontSize',12)

fig1=figure;
gaussFilterNice = gausswin(25);
gaussFilterNice = gaussFilterNice / sum(gaussFilterNice); % Normalize.
plot(gaussFilterNice)
 set(gca,'FontSize',12)


%% correlation
close all
clear all
clc

x=0:1:200;
y1=1.5*gaussmf(x,[5 120]);
y2=2.5*gaussmf(x,[7 30]);
y=y1+y2;
plot(x,y);axis([0 200 0 4]);
xlabel('gaussmf')
set(gca,'FontSize',12)

y3=3.8*gaussmf(x,[8 170]);
fig1 = figure;
plot(x,y3);axis([0 200 0 4]);
xlabel('gaussmf')
set(gca,'FontSize',12)


X1=xcorr(y,y3,'coeff');
[m,d]=max(X1);
display(max(X1));
delay=d-max(length(y),length(y3));
display(delay);
figure,plot(y);
hold,plot([delay+1:length(y3)+delay],y3,'r');axis([0 200 0 4]);
set(gca,'FontSize',12)