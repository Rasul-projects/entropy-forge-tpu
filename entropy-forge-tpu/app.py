import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from engine import ThermodynamicProcessorSimulator

# Page Config
st.set_page_config(page_title="EntropyForge TPU Console", page_icon="🌌", layout="wide")

st.title("🌌 EntropyForge: Thermodynamic Processing Simulation Matrix")
st.markdown("---")

# Sidebar Controls
st.sidebar.header("⚙️ TPU Core Configuration")
nodes = st.sidebar.slider("System Dimension (Matrix Elements)", min_value=10, max_value=100, value=40, step=5)
init_temp = st.sidebar.slider("Initial Thermal Energy ($T_0$)", min_value=50.0, max_value=500.0, value=250.0, step=10.0)
cooling_rate = st.sidebar.slider("Dynamic Thermodynamic Decay Rate", min_value=0.001, max_value=0.02, value=0.008, step=0.001, format="%.3f")
max_cycles = st.sidebar.slider("Maximum Execution Clock Cycles", min_value=100, max_value=2000, value=1200, step=100)

# Main Dashboard Interface
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("System Architecture Profile")
    st.info("""
    **Computing Paradigm:** Non-Von Neumann Continuous-Time Dynamics  
    **Integration Core:** Stochastic Langevin Differential Framework  
    **Target Objective:** Global Minimization via Entropy Exhaustion
    """)
    
    run_sim = st.button("🚀 Trigger Equilibrium Compute Cycle", type="primary", use_container_width=True)

if run_sim:
    # Initialize Engine Core
    tpu = ThermodynamicProcessorSimulator(system_dimension=nodes, initial_temperature=init_temp)
    initial_energy = tpu._calculate_system_energy(tpu.state)
    
    status_box = st.empty()
    status_box.status("⚡ System Initialized. Calibrating thermal grids...")
    
    # Run Simulation Execution Loop
    final_state, energy_log = tpu.run_equilibrium_cycle(max_cycles=max_cycles, dt=0.02, decay=cooling_rate)
    final_energy = energy_log[-1]
    energy_reduction = ((initial_energy - final_energy) / initial_energy) * 100
    
    status_box.success("🎉 Computation complete. Thermal equilibrium attained.")
    
    with col1:
        st.metric(label="Initial Potential Energy State", value=f"{initial_energy:.4f}")
        st.metric(label="Final Equilibrium State Value", value=f"{final_energy:.4f}", delta=f"-{energy_reduction:.2f}% Efficiency Shift")
    
    with col2:
        st.subheader("📊 Real-Time State Convergence Plot")
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(energy_log, color='#8b5cf6', linewidth=2.5, label='System Potential Energy ($E$)')
        ax.set_title('EntropyForge: System Energy Structural Phase Change')
        ax.set_xlabel('Hardware Clock Cycles (Stochastic Steps)')
        ax.set_ylabel('System Potential Energy Value')
        ax.grid(True, linestyle='--', alpha=0.5)
        ax.legend()
        st.pyplot(fig)
else:
    with col2:
        st.warning("👈 Awaiting hardware trigger event. Configure processing dimensions in the panel and click execution.")
