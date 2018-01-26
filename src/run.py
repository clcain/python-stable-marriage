import sys

from marriages_simulation import MarriagesSimulation

def start_simulation(size):
    """Start the stable marriages simulation with the given size.

    Args:
        size: The size of the simulation.
    """
    simulation = MarriagesSimulation(size)
    simulation.populate()
    simulation.set_preferences()
    simulation.match()

def main():
    if len(sys.argv) != 2:
        raise RuntimeError('Insufficient arguments')
    size = int(sys.argv[1])
    start_simulation(size)

if __name__ == '__main__': main()
