%% SoA analysis code
% Mukesh 3rd March 2022

% path and subject info
datapath = 'C:\Users\mukes.DESKTOP-PFSHT1J\Downloads\IB_new_task_March5\data\';
subject = '001';

cd([datapath,subject]);

% read all csv files
csvfiles = dir('*.csv');

% data holder variable to compile all blocks
Data_all = {};

% loop to complie all the blocks data 
for i = 2:length(csvfiles)
    
    [num, txt, raw] = xlsread(csvfiles(i).name);
    
    Data_header = raw(1,[116, 118, 85, 30, 38, 103, 39, 78, 92]);
    Data = raw(3:size(raw,1),[116, 118, 85, 30, 38, 103, 39, 78, 92]);

    Data_all = [Data_all; Data];

end

% check and assign condition based on intention and actual ball motion
I = Data_all(:,4); % intention column
A = Data_all(:,5); % actual motion column

I_left = ismember(I,'left'); % get index of all left intention
I_right = ismember(I,'right'); % get index of all right intention

A_L = strcmp(A,'L'); % get index of all left actual motion
A_R = strcmp(A,'R');  % get index of all right actual motion

l_correct = I_left == A_L; % get index for trials that match left intention with left ball motion
r_correct = I_right == A_R; % get index for trials that match right intention with right ball motion

both_correct = l_correct + r_correct; % combine left and right index

intended_trials = find(both_correct==2); % all intended trials index
unintended_trials = find(both_correct==0); % all unintended trials index

Data_all_intended = Data_all(intended_trials,:); % data for intended trials
Data_all_unintended = Data_all(unintended_trials,:); % data for unintended trials

% get intended trials based on actual delay 
In_delay_0 = find(cell2mat(Data_all_intended(:,7))==0);
In_delay_200 = find(cell2mat(Data_all_intended(:,7))==0.2);
In_delay_400 = find(cell2mat(Data_all_intended(:,7))==0.4);
In_delay_600 = find(cell2mat(Data_all_intended(:,7))==0.6);
In_delay_800 = find(cell2mat(Data_all_intended(:,7))==0.8);
In_delay_1000 = find(cell2mat(Data_all_intended(:,7))==1);
In_delay_1200 = find(cell2mat(Data_all_intended(:,7))==1.2);
In_delay_1400 = find(cell2mat(Data_all_intended(:,7))==1.4);
In_delay_1600 = find(cell2mat(Data_all_intended(:,7))==1.6);
In_delay_1800 = find(cell2mat(Data_all_intended(:,7))==1.8);
In_delay_2000 = find(cell2mat(Data_all_intended(:,7))==2);

% get unintended trials based on actual delay
Un_delay_0 = find(cell2mat(Data_all_unintended(:,7))==0);
Un_delay_200 = find(cell2mat(Data_all_unintended(:,7))==0.2);
Un_delay_400 = find(cell2mat(Data_all_unintended(:,7))==0.4);
Un_delay_600 = find(cell2mat(Data_all_unintended(:,7))==0.6);
Un_delay_800 = find(cell2mat(Data_all_unintended(:,7))==0.8);
Un_delay_1000 = find(cell2mat(Data_all_unintended(:,7))==1);
Un_delay_1200 = find(cell2mat(Data_all_unintended(:,7))==1.2);
Un_delay_1400 = find(cell2mat(Data_all_unintended(:,7))==1.4);
Un_delay_1600 = find(cell2mat(Data_all_unintended(:,7))==1.6);
Un_delay_1800 = find(cell2mat(Data_all_unintended(:,7))==1.8);
Un_delay_2000 = find(cell2mat(Data_all_unintended(:,7))==2);

%% plot all estimates of each delay and color if ball moved in the intended
% direction (Green) or unintended direction (black)
figure;
plot(cell2mat(Data_all_intended(:,7)).*1000,cell2mat(Data_all_intended(:,8)),'.g','MarkerSize',20)
hold on
plot(cell2mat(Data_all_unintended(:,7)).*1000,cell2mat(Data_all_unintended(:,8)),'.k','MarkerSize',20)

in_mdl = fitlm(cell2mat(Data_all_intended(:,7)).*1000,cell2mat(Data_all_intended(:,8)))
un_mdl = fitlm(cell2mat(Data_all_unintended(:,7)).*1000,cell2mat(Data_all_unintended(:,8)))


in_h = plot(in_mdl,'color',[0, 1, 0]);
hold on
un_h = plot(un_mdl,'color',[0, 0, 0]);

plot(cell2mat(Data_all_intended(:,7)).*1000,cell2mat(Data_all_intended(:,8)),'.g','MarkerSize',20)
hold on
plot(cell2mat(Data_all_unintended(:,7)).*1000,cell2mat(Data_all_unintended(:,8)),'.k','MarkerSize',20)

set([in_h(1) in_h(1)],'color','g')
set([in_h(2) in_h(2)],'color','g')
set([in_h(3) in_h(3)],'color','g')
set([in_h(4) in_h(4)],'color','g')
set([un_h(1) un_h(1)],'color','k')
set([un_h(2) un_h(2)],'color','k')
set([un_h(3) un_h(3)],'color','k')
set([un_h(4) un_h(4)],'color','k')

legend off

xlabel('Actual delay (ms)');
ylabel('Estimated delay (ms)');
legend ({'Intended','Unintended'})
xlim([-100 2100]);
ylim([-100 2100]);
title('Linear regression')
%% plot only means of each delay and color if ball moved in the intended
% direction (Green) or unintended direction (black)
figure;
plot(mean(cell2mat(Data_all_intended(In_delay_0,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_0,8))),'.g','MarkerSize',20)
hold on
plot(mean(cell2mat(Data_all_unintended(Un_delay_0,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_0,8))),'.k','MarkerSize',20)

plot(mean(cell2mat(Data_all_intended(In_delay_200,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_200,8))),'.g','MarkerSize',20)
plot(mean(cell2mat(Data_all_unintended(Un_delay_200,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_200,8))),'.k','MarkerSize',20)

plot(mean(cell2mat(Data_all_intended(In_delay_400,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_400,8))),'.g','MarkerSize',20)
plot(mean(cell2mat(Data_all_unintended(Un_delay_400,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_400,8))),'.k','MarkerSize',20)

plot(mean(cell2mat(Data_all_intended(In_delay_600,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_600,8))),'.g','MarkerSize',20)
plot(mean(cell2mat(Data_all_unintended(Un_delay_600,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_600,8))),'.k','MarkerSize',20)

plot(mean(cell2mat(Data_all_intended(In_delay_800,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_800,8))),'.g','MarkerSize',20)
plot(mean(cell2mat(Data_all_unintended(Un_delay_800,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_800,8))),'.k','MarkerSize',20)

plot(mean(cell2mat(Data_all_intended(In_delay_1000,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_1000,8))),'.g','MarkerSize',20)
plot(mean(cell2mat(Data_all_unintended(Un_delay_1000,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_1000,8))),'.k','MarkerSize',20)

plot(mean(cell2mat(Data_all_intended(In_delay_1200,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_1200,8))),'.g','MarkerSize',20)
plot(mean(cell2mat(Data_all_unintended(Un_delay_1200,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_1200,8))),'.k','MarkerSize',20)

plot(mean(cell2mat(Data_all_intended(In_delay_1400,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_1400,8))),'.g','MarkerSize',20)
plot(mean(cell2mat(Data_all_unintended(Un_delay_1400,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_1400,8))),'.k','MarkerSize',20)

plot(mean(cell2mat(Data_all_intended(In_delay_1600,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_1600,8))),'.g','MarkerSize',20)
plot(mean(cell2mat(Data_all_unintended(Un_delay_1600,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_1600,8))),'.k','MarkerSize',20)

plot(mean(cell2mat(Data_all_intended(In_delay_1800,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_1800,8))),'.g','MarkerSize',20)
plot(mean(cell2mat(Data_all_unintended(Un_delay_1800,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_1800,8))),'.k','MarkerSize',20)

plot(mean(cell2mat(Data_all_intended(In_delay_2000,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_2000,8))),'.g','MarkerSize',20)
plot(mean(cell2mat(Data_all_unintended(Un_delay_2000,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_2000,8))),'.k','MarkerSize',20)

xlabel('Actual delay (ms)');
ylabel('Estimated delay (ms)');
legend ({'Intended','Unintended'})
xlim([-100 2100]);
ylim([-100 2100]);

%% plot with error bars
figure;
errorbar(mean(cell2mat(Data_all_intended(In_delay_0,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_0,8))),std(cell2mat(Data_all_intended(In_delay_0,8))),'.g','MarkerSize',20)
hold on
errorbar(mean(cell2mat(Data_all_unintended(Un_delay_0,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_0,8))),std(cell2mat(Data_all_unintended(Un_delay_0,8))),'.k','MarkerSize',20)

errorbar(mean(cell2mat(Data_all_intended(In_delay_200,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_200,8))),std(cell2mat(Data_all_intended(In_delay_200,8))),'.g','MarkerSize',20)
errorbar(mean(cell2mat(Data_all_unintended(Un_delay_200,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_200,8))),std(cell2mat(Data_all_unintended(Un_delay_200,8))),'.k','MarkerSize',20)

errorbar(mean(cell2mat(Data_all_intended(In_delay_400,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_400,8))),std(cell2mat(Data_all_intended(In_delay_400,8))),'.g','MarkerSize',20)
errorbar(mean(cell2mat(Data_all_unintended(Un_delay_400,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_400,8))),std(cell2mat(Data_all_unintended(Un_delay_400,8))),'.k','MarkerSize',20)

errorbar(mean(cell2mat(Data_all_intended(In_delay_600,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_600,8))),std(cell2mat(Data_all_intended(In_delay_600,8))),'.g','MarkerSize',20)
errorbar(mean(cell2mat(Data_all_unintended(Un_delay_600,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_600,8))),std(cell2mat(Data_all_unintended(Un_delay_600,8))),'.k','MarkerSize',20)

errorbar(mean(cell2mat(Data_all_intended(In_delay_800,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_800,8))),std(cell2mat(Data_all_intended(In_delay_800,8))),'.g','MarkerSize',20)
errorbar(mean(cell2mat(Data_all_unintended(Un_delay_800,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_800,8))),std(cell2mat(Data_all_unintended(Un_delay_800,8))),'.k','MarkerSize',20)

errorbar(mean(cell2mat(Data_all_intended(In_delay_1000,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_1000,8))),std(cell2mat(Data_all_intended(In_delay_1000,8))),'.g','MarkerSize',20)
errorbar(mean(cell2mat(Data_all_unintended(Un_delay_1000,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_1000,8))),std(cell2mat(Data_all_unintended(Un_delay_1000,8))),'.k','MarkerSize',20)

errorbar(mean(cell2mat(Data_all_intended(In_delay_1200,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_1200,8))),std(cell2mat(Data_all_intended(In_delay_1200,8))),'.g','MarkerSize',20)
errorbar(mean(cell2mat(Data_all_unintended(Un_delay_1200,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_1200,8))),std(cell2mat(Data_all_unintended(Un_delay_1200,8))),'.k','MarkerSize',20)

errorbar(mean(cell2mat(Data_all_intended(In_delay_1400,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_1400,8))),std(cell2mat(Data_all_intended(In_delay_1400,8))),'.g','MarkerSize',20)
errorbar(mean(cell2mat(Data_all_unintended(Un_delay_1400,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_1400,8))),std(cell2mat(Data_all_unintended(Un_delay_1400,8))),'.k','MarkerSize',20)

errorbar(mean(cell2mat(Data_all_intended(In_delay_1600,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_1600,8))),std(cell2mat(Data_all_intended(In_delay_1600,8))),'.g','MarkerSize',20)
errorbar(mean(cell2mat(Data_all_unintended(Un_delay_1600,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_1600,8))),std(cell2mat(Data_all_unintended(Un_delay_1600,8))),'.k','MarkerSize',20)

errorbar(mean(cell2mat(Data_all_intended(In_delay_1800,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_1800,8))),std(cell2mat(Data_all_intended(In_delay_1800,8))),'.g','MarkerSize',20)
errorbar(mean(cell2mat(Data_all_unintended(Un_delay_1800,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_1800,8))),std(cell2mat(Data_all_unintended(Un_delay_1800,8))),'.k','MarkerSize',20)

errorbar(mean(cell2mat(Data_all_intended(In_delay_2000,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_2000,8))),std(cell2mat(Data_all_intended(In_delay_2000,8))),'.g','MarkerSize',20)
errorbar(mean(cell2mat(Data_all_unintended(Un_delay_2000,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_2000,8))),std(cell2mat(Data_all_unintended(Un_delay_2000,8))),'.k','MarkerSize',20)

xlabel('Actual delay (ms)');
ylabel('Estimated delay (ms)');
legend ({'Intended','Unintended'})
xlim([-100 2100]);
ylim([-100 2100]);

%% plot overall confidence rating 

in_conf = cell2mat(Data_all_intended(:,9));
un_conf = cell2mat(Data_all_unintended(:,9));

figure;
% plot(1,mean(in_conf),'.','color',[0 1 0],'MarkerSize',20);
% hold on
% plot(2,mean(un_conf),'.','color',[0 0 0],'MarkerSize',20);
errorbar(1,mean(in_conf),std(in_conf),'.','color',[0 1 0],'MarkerSize',20);
hold on
errorbar(2,mean(un_conf),std(un_conf),'.','color',[0 0 0],'MarkerSize',20);
xticks([1,2]);
xticklabels({'Intended','Unintended'})
ylabel('Control confidence rating')
xlim([0,3])
ylim([0 7])
%% plot only means of each delay and color if ball moved in the intended
% direction (Green) or unintended direction (black)
figure;
plot3(mean(cell2mat(Data_all_intended(In_delay_0,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_0,8))),mean(cell2mat(Data_all_intended(In_delay_0,9))),'.g','MarkerSize',20)
hold on
plot3(mean(cell2mat(Data_all_unintended(Un_delay_0,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_0,8))),mean(cell2mat(Data_all_unintended(Un_delay_0,9))),'.k','MarkerSize',20)

plot3(mean(cell2mat(Data_all_intended(In_delay_200,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_200,8))),mean(cell2mat(Data_all_intended(In_delay_200,9))),'.g','MarkerSize',20)
plot3(mean(cell2mat(Data_all_unintended(Un_delay_200,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_200,8))),mean(cell2mat(Data_all_unintended(Un_delay_200,9))),'.k','MarkerSize',20)

plot3(mean(cell2mat(Data_all_intended(In_delay_400,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_400,8))),mean(cell2mat(Data_all_intended(In_delay_400,9))),'.g','MarkerSize',20)
plot3(mean(cell2mat(Data_all_unintended(Un_delay_400,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_400,8))),mean(cell2mat(Data_all_unintended(Un_delay_400,9))),'.k','MarkerSize',20)

plot3(mean(cell2mat(Data_all_intended(In_delay_600,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_600,8))),mean(cell2mat(Data_all_intended(In_delay_600,9))),'.g','MarkerSize',20)
plot3(mean(cell2mat(Data_all_unintended(Un_delay_600,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_600,8))),mean(cell2mat(Data_all_unintended(Un_delay_600,9))),'.k','MarkerSize',20)

plot3(mean(cell2mat(Data_all_intended(In_delay_800,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_800,8))),mean(cell2mat(Data_all_intended(In_delay_800,9))),'.g','MarkerSize',20)
plot3(mean(cell2mat(Data_all_unintended(Un_delay_800,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_800,8))),mean(cell2mat(Data_all_unintended(Un_delay_800,9))),'.k','MarkerSize',20)

plot3(mean(cell2mat(Data_all_intended(In_delay_1000,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_1000,8))),mean(cell2mat(Data_all_intended(In_delay_1000,9))),'.g','MarkerSize',20)
plot3(mean(cell2mat(Data_all_unintended(Un_delay_1000,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_1000,8))),mean(cell2mat(Data_all_unintended(Un_delay_1000,9))),'.k','MarkerSize',20)

plot3(mean(cell2mat(Data_all_intended(In_delay_1200,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_1200,8))),mean(cell2mat(Data_all_intended(In_delay_1200,9))),'.g','MarkerSize',20)
plot3(mean(cell2mat(Data_all_unintended(Un_delay_1200,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_1200,8))),mean(cell2mat(Data_all_unintended(Un_delay_1200,9))),'.k','MarkerSize',20)

plot3(mean(cell2mat(Data_all_intended(In_delay_1400,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_1400,8))),mean(cell2mat(Data_all_intended(In_delay_1400,9))),'.g','MarkerSize',20)
plot3(mean(cell2mat(Data_all_unintended(Un_delay_1400,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_1400,8))),mean(cell2mat(Data_all_unintended(Un_delay_1400,9))),'.k','MarkerSize',20)

plot3(mean(cell2mat(Data_all_intended(In_delay_1600,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_1600,8))),mean(cell2mat(Data_all_intended(In_delay_1600,9))),'.g','MarkerSize',20)
plot3(mean(cell2mat(Data_all_unintended(Un_delay_1600,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_1600,8))),mean(cell2mat(Data_all_unintended(Un_delay_1600,9))),'.k','MarkerSize',20)

plot3(mean(cell2mat(Data_all_intended(In_delay_1800,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_1800,8))),mean(cell2mat(Data_all_intended(In_delay_1800,9))),'.g','MarkerSize',20)
plot3(mean(cell2mat(Data_all_unintended(Un_delay_1800,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_1800,8))),mean(cell2mat(Data_all_unintended(Un_delay_1800,9))),'.k','MarkerSize',20)

plot3(mean(cell2mat(Data_all_intended(In_delay_2000,7)).*1000),mean(cell2mat(Data_all_intended(In_delay_2000,8))),mean(cell2mat(Data_all_intended(In_delay_2000,9))),'.g','MarkerSize',20)
plot3(mean(cell2mat(Data_all_unintended(Un_delay_2000,7)).*1000),mean(cell2mat(Data_all_unintended(Un_delay_2000,8))),mean(cell2mat(Data_all_unintended(Un_delay_2000,9))),'.k','MarkerSize',20)

xlabel('Actual delay (ms)');
ylabel('Estimated delay (ms)');
zlabel('Control confidence rating');
legend ({'Intended','Unintended'})
xlim([-100 2100]);
ylim([-100 2100]);
zlim([0 7]);
grid on


