close all;
clear all;

% Define parameters to plot original sawtooth

tr = [-1 0 0 1 1 2 2];
yr = [0 1 0 1 0 1 0];

% Plot Truncated Fourier Series Approximation (N = 1)

N = 1;                   % define number of terms to use (n = -N..N)
c0 = 0.5;                % define dc bias coefficient
t = -1:0.001:2;          % define time values for y(t)
y = c0 * ones(size(t));  % let initial y = c0 (dc bias) for all times

for n = -N:-1,           % compute y for negative n
  cn = exp(j*pi/2)/(2*pi*n);
  y = y + real(cn * exp(j*n*2*pi*t));
end;
                         % compute y for positive n and add to y
for n = 1:N,             % found using negative n
  cn = exp(j*pi/2)/(2*pi*n);
  y = y + real(cn * exp(j*n*2*pi*t));
end;

subplot(2,2,1);          % plot approximation
plot(t,y,'LineWidth',2); 
hold;
plot(tr,yr,':','Color','red','LineWidth',2.5); 
hold;
xlabel('time (seconds)');
ylabel('y(t) approximation');
title('Truncated FS, n=1');

% Plot Truncated Fourier Series Approximation (N = 2)

N = 2;                   % define number of terms to use (n = -N..N)
c0 = 0.5;                % define dc bias coefficient
t = -1:0.001:2;          % define time values for y(t)
y = c0 * ones(size(t));  % let initial y = c0 (dc bias) for all times

for n = -N:-1,           % compute y for negative n
  cn = exp(j*pi/2)/(2*pi*n);
  y = y + real(cn * exp(j*n*2*pi*t));
end;
                         % compute y for positive n and add to y
for n = 1:N,             % found using negative n
  cn = exp(j*pi/2)/(2*pi*n);
  y = y + real(cn * exp(j*n*2*pi*t));
end;

subplot(2,2,2);          % plot approximation
plot(t,y,'LineWidth',2);
hold;
plot(tr,yr,':','Color','red','LineWidth',2.5);
hold;
xlabel('time (seconds)');
ylabel('y(t) approximation');
title('Truncated FS, n=2');

% Plot Truncated Fourier Series Approximation (N = 3)

N = 3;                   % define number of terms to use (n = -N..N)
c0 = 0.5;                % define dc bias coefficient
t = -1:0.001:2;          % define time values for y(t)
y = c0 * ones(size(t));  % let initial y = c0 (dc bias) for all times

for n = -N:-1,           % compute y for negative n
  cn = exp(j*pi/2)/(2*pi*n);
  y = y + real(cn * exp(j*n*2*pi*t));
end;
                         % compute y for positive n and add to y
for n = 1:N,             % found using negative n
  cn = exp(j*pi/2)/(2*pi*n);
  y = y + real(cn * exp(j*n*2*pi*t));
end;

subplot(2,2,3);          % plot approximation
plot(t,y,'LineWidth',2);
hold;
plot(tr,yr,':','Color','red','LineWidth',2.5);
hold;
xlabel('time (seconds)');
ylabel('y(t) approximation');
title('Truncated FS, n=3');

% Plot Truncated Fourier Series Approximation (N = 10)

N = 10;                  % define number of terms to use (n = -N..N)
c0 = 0.5;                % define dc bias coefficient
t = -1:0.001:2;          % define time values for y(t)
y = c0 * ones(size(t));  % let initial y = c0 (dc bias) for all times

for n = -N:-1,           % compute y for negative n
  cn = exp(j*pi/2)/(2*pi*n);
  y = y + real(cn * exp(j*n*2*pi*t));
end;
                         % compute y for positive n and add to y
for n = 1:N,             % found using negative n
  cn = exp(j*pi/2)/(2*pi*n);
  y = y + real(cn * exp(j*n*2*pi*t));
end;

subplot(2,2,4);          % plot approximation
plot(t,y,'LineWidth',2);
hold;
plot(tr,yr,':','Color','red','LineWidth',2.5);
hold;
xlabel('time (seconds)');
ylabel('y(t) approximation');
title('Truncated FS, n=10');


figureHandle = gcf;
set(findall(figureHandle,'type','text'),'fontSize',20)

%%
close all;
clear all;

% Define parameters to plot original sawtooth

tr = [-3 -1 -1 1 1 3];
yr = [-1 1 -1 1 -1 1];

% Plot Truncated Fourier Series Approximation (N = 1)

N = 1;                   % define number of terms to use (n = -N..N)
c0 = 0.5;                % define dc bias coefficient
t = -1:0.001:2;          % define time values for y(t)
y = c0 * ones(size(t));  % let initial y = c0 (dc bias) for all times


plot(tr,yr,'Color','red','LineWidth',2.5);
hold;
xlabel('time');
ylabel('y(t)');

opt.fontname = 'helvetica';
opt.fontsize = 8;
centeraxes(gca,opt);
figureHandle = gcf;
set(findall(figureHandle,'type','text'),'fontSize',20)