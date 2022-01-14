% Script for testing the centeraxes.m function

clear
clf
clc
%subplot(211)
x = -2*pi:.1:2*pi;
y1=sin(x);
y2=cos(x);
plot(x,y1);
hold all;
plot(x,y2);
set(gca,'ylim',[-1 1],'xlim',[-4 4],'xtick',-4:4,'ytick',-1:1)
xlabel('t');
ylabel('y(t)')

opt.fontname = 'helvetica';
opt.fontsize = 8;

%centeraxes(gca);
centeraxes(gca,opt);