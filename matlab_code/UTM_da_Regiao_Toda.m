
P1 = [-44.110107,	-20.110183];
P2 = [-44.169931,	-20.169895];

P3 = [-44.169931,	-20.110183];
P4 = [-44.110107,	-20.169895];


[P1_UTM_x, P1_UTM_y]  = deg2utm(P1(2), P1(1));
[P2_UTM_x, P2_UTM_y] = deg2utm(P2(2), P2(1));
[P3_UTM_x, P3_UTM_y] = deg2utm(P3(2), P3(1));
[P4_UTM_x, P4_UTM_y] = deg2utm(P4(2), P4(1));


fprintf('P1 = [%1.6f %1.6f] \n',P1_UTM_x, P1_UTM_y);
fprintf('P2 = [%1.6f %1.6f] \n',P2_UTM_x, P2_UTM_y);
fprintf('P3 = [%1.6f %1.6f] \n',P3_UTM_x, P3_UTM_y);
fprintf('P4 = [%1.6f %1.6f] \n',P4_UTM_x, P4_UTM_y);

Limite = [P1;P2;P3;P4];