import numpy as np
import matplotlib.pyplot as plt
from engine import ThermodynamicProcessorSimulator

def run_benchmark():
    print("====================================================")
    print("INITIALIZING ENTROPYFORGE THERMODYNAMIC COPROCESSOR")
    print("====================================================\n")
    
    system_nodes = 40 
    tpu = ThermodynamicProcessorSimulator(system_dimension=system_nodes, initial_temperature=250.0)
    
    initial_energy = tpu._calculate_system_energy(tpu.state)
    print(f"[Hardware State] Initial System Entropy/Energy State: {initial_energy:.4f}")
    print("[Processing] Running Natural Thermodynamic Minimization Cycles...")
    
    final_state, energy_log = tpu.run_equilibrium_cycle(max_cycles=1200, dt=0.02, decay=0.008)
    final_energy = energy_log[-1]
    
    print("\n====================================================")
    print("COMPUTATION CYCLE COMPLETE")
    print("====================================================")
    print(f"[Performance] Initial Energy: {initial_energy:.4f} -> Final Energy: {final_energy:.4f}")
    print(f"[Efficiency Metric] Total System Energy Reduction: {((initial_energy - final_energy)/initial_energy)*100:.2f}%")
    
    # Save the physical convergence plot as a verification artifact
    plt.figure(figsize=(10, 5))
    plt.plot(energy_log, color='#8b5cf6', linewidth=2.5, label='System Potential Energy ($E$)')
    plt.title('EntropyForge: Non-Von Neumann Energy State Convergence')
    plt.xlabel('Hardware Clock Cycles (Stochastic Steps)')
    plt.ylabel('System Potential State Value')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.savefig('thermodynamic_convergence.png')
    print("\n[Artifact Saved] Generated 'thermodynamic_convergence.png'")

if __name__ == "__main__":
    run_benchmark()
