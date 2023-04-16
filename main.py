from neuron import h, gui

soma = h.Section(name='soma')
h.psection()

dir(soma)
# Run the simulation
help(soma.connect)

soma.insert('pas')

print("type(soma) = {}".format(type(soma)))
print("type(soma(0.5)) ={}".format(type(soma(0.5))))

mech = soma(0.5).pas
print(dir(mech))
print(mech.g)
print(soma(0.5).pas.g)

asyn = h.AlphaSynapse(soma(0.5))
dir(asyn)

print("asyn.e = {}".format(asyn.e))
print("asyn.gmax = {}".format(asyn.gmax))
print("asyn.onset = {}".format(asyn.onset))
print("asyn.tau = {}".format(asyn.tau))


asyn.onset = 20
asyn.gmax = 1
h.psection()

v_vec = h.Vector()             # Membrane potential vector
t_vec = h.Vector()             # Time stamp vector
v_vec.record(soma(0.5)._ref_v)
t_vec.record(h._ref_t)

h.tstop = 50
h.run()

# Plot the results
import matplotlib.pyplot as plt
plt.figure(figsize=(8,4)) # Default figsize is (8,6)
plt.plot(t_vec, v_vec)
plt.xlabel('time (ms)')
plt.ylabel('mV')
plt.show()