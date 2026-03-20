% Time vector
t = linspace(0, 10, 100);

% Parameters
A = 1;
gamma = 0.2;
omega = 2;

% Model
y = A * exp(-gamma * t) .* cos(omega * t);

% Plot
plot(t, y);
title('Damped Oscillation - MATLAB');
xlabel('Time');
ylabel('Amplitude');
