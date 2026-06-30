import numpy as np
import matplotlib.pyplot as plt
from engine import ThermodynamicProcessorSimulator

def run_benchmark():
    print("====================================================")
    print("INITIALIZING ENTROPYFORGE THERMODYNAMIC COPROCESSOR")
    print("====================================================\n")
    
    tpu = ThermodynamicProcessorSimulator(system_dimension=40, initial_temperature=250.0)
    initial_energy = tpu._calculate_system_energy(tpu.state)
    print(f"[Hardware State] Initial System Energy: {initial_energy:.4f}")
    
    final_state, energy_log = tpu.run_equilibrium_cycle(max_cycles=1200, dt=0.02, decay=0.008)
    print(f"[Performance] Final Optimized Energy: {energy_log[-1]:.4f}")
    
    plt.figure(figsize=(10, 5))
    plt.plot(energy_log, color='#8b5cf6', linewidth=2.5, label='System Potential Energy ($E$)')
    plt.title('EntropyForge: Non-Von Neumann Energy State Convergence')
    plt.xlabel('Hardware Clock Cycles')
    plt.ylabel('System Potential State Value')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.savefig('thermodynamic_convergence.png')
    print("\n[Artifact Saved] Generated 'thermodynamic_convergence.png'")

if __name__ == "__main__":
    run_benchmark()
