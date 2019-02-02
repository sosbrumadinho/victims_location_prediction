%% Plotar campo de velocidades
%

u = zeros(length(Reg),1);
v = zeros(length(Reg),1);

for r = 1:length(Reg)
    V = Reg(r,5);
    ap = Reg(r, 6);
    u(r) = Reg(r, 7)*V;
    v(r) = Reg(r, 8)*V;
    
end

figure(2);
quiver(Reg(1:end, 1), Reg(1:end, 2), u, v)