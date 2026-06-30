import numpy as np
from scipy.spatial.distance import cdist

class ThermodynamicProcessorSimulator:
    def __init__(self, system_dimension: int, initial_temperature: float = 100.0):
        self.dim = system_dimension
        self.temperature = initial_temperature
        self.state = np.random.uniform(-1.0, 1.0, size=(system_dimension, 2))
        self.energy_history = []

    def _calculate_system_energy(self, state: np.ndarray) -> float:
        distances = cdist(state, state, 'euclidean')
        return float(np.sum(distances) / (state.shape[0] * 2))

    def compute_step(self, time_step: float, cooling_rate: float):
        gradient = np.zeros_like(self.state)
        epsilon = 1e-5
        base_energy = self._calculate_system_energy(self.state)
        
        for i in range(self.dim):
            for j in range(2):
                perturbed_state = self.state.copy()
                perturbed_state[i, j] += epsilon
                gradient[i, j] = (self._calculate_system_energy(perturbed_state) - base_energy) / epsilon

        thermal_fluctuation = np.random.normal(0, 1, size=self.state.shape)
        stochastic_force = np.sqrt(2.0 * 1.380649e-23 * self.temperature * time_step) * thermal_fluctuation
        
        self.state = self.state - (gradient * time_step) + stochastic_force
        self.temperature *= (1.0 - cooling_rate)
        self.energy_history.append(base_energy)

    def run_equilibrium_cycle(self, max_cycles: int = 1000, dt: float = 0.01, decay: float = 0.005):
        for cycle in range(max_cycles):
            self.compute_step(dt, decay)
            if self.temperature < 1e-4:
                break
        return self.state, self.energy_history
