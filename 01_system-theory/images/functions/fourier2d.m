close all
clear all

wDeg = 1;  %size of image (in degrees)
nPix = 200;  %resolution of image (pixels);

[x,y] = meshgrid(linspace(-wDeg/2,wDeg/2,nPix+1));
x = x(1:end-1,1:end-1);
y = y(1:end-1,1:end-1);

orientation = 90;  %deg (counter-clockwise from horizontal)
sf = 4; %spatial frequency (cycles/deg)

ramp = sin(orientation*pi/180)*x-cos(orientation*pi/180)*y;

grating = sin(2*pi*sf*ramp);

imagesc(grating);colormap(gray);
fig1=figure;
 F = fftshift(fft2(grating));
 imagesc((abs(F))); title('After FFT and fftshift');
colormap(gray);
    set(findall(fig1,'type','text'),'fontSize',18)
    set(gca,'FontSize',12)
   
    
   
    %%
    
close all
clear all

wDeg = 1;  %size of image (in degrees)
nPix = 200;  %resolution of image (pixels);

[x,y] = meshgrid(linspace(-wDeg/2,wDeg/2,nPix+1));
x = x(1:end-1,1:end-1);
y = y(1:end-1,1:end-1);

orientation = 45;  %deg (counter-clockwise from horizontal)
sf = 4; %spatial frequency (cycles/deg)

ramp = sin(orientation*pi/180)*x-cos(orientation*pi/180)*y;

grating = sin(2*pi*sf*ramp);

imagesc(grating);colormap(gray);
fig1=figure;
 F = fftshift(fft2(grating));
 imagesc((abs(F))); title('After FFT and fftshift');
colormap(gray);
    set(findall(fig1,'type','text'),'fontSize',18)
    set(gca,'FontSize',12)
    
    
    %Ideal image
    bla = zeros(200,200);
    bla(98,104)=2000;
    bla(104,98)=2000;
    % F = fftshift(fft2(bla));
% imagesc((abs(F))); title('After FFT and fftshift');
imagesc(bla); title('After FFT and fftshift');
colormap(gray);
    set(findall(fig1,'type','text'),'fontSize',18)
    set(gca,'FontSize',12)

    %%
    
close all
clear all

    img = (imread('FourierBox.tif'));
    imagesc(img);colormap(gray);
fig1=figure;
 F = fftshift(fft2(img));
 imagesc((abs(F))); title('After FFT and fftshift');
colormap(gray);
    set(findall(fig1,'type','text'),'fontSize',18)
    set(gca,'FontSize',12)
fig1=figure;
 F = fftshift(fft2(img));
 imagesc(log(1+abs(F))); title('After FFT and fftshift (log)');
colormap(gray);
    set(findall(fig1,'type','text'),'fontSize',18)
    set(gca,'FontSize',12)   