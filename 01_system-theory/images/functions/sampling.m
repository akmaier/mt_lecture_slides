close all
clear all
clc

samplingFactor = 1;

t1  = [ 0 : samplingFactor : 40 ];           % Time Samples
s = ones(1,40/samplingFactor + 1);
t2  = [ 0 : 0.1 : 40 ];           % Time Samples
f  = 500;                       % Input Signal Frequency
fs = 8000;                    % Sampling Frequency
x = sin(2*pi*f/fs*t2);        % Generate Sine Wave  
xS = sin(2*pi*f/fs*t1);        % Generate Sine Wave

fig1 = figure(1);
stem(t1,s,'r');axis([0 40 0 2]);                  % View the samples
set(findall(fig1,'type','text'),'fontSize',18)
set(gca,'FontSize',12)

fig1 = figure(2);
stem(t1*1/fs*1000,xS,'r');axis([0 5 -2 2]);  % View the samples
hold on;
plot(t2*1/fs*1000,x);        % Plot Sine Wave
set(findall(fig1,'type','text'),'fontSize',18)
set(gca,'FontSize',12)

fig1 = figure;
plot(t2*1/fs*1000,x);axis([0 5 -2 2]);        % Plot Sine Wave
set(findall(fig1,'type','text'),'fontSize',18)
set(gca,'FontSize',12)
