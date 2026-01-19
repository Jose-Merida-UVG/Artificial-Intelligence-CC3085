import random


# Environment class, simulates a temperature that can be cooled or heated up
class Environment:

    # Assign random temperature on initialization
    def __init__(self):
        self.temperature = random.uniform(10, 30)

    # Sensor simulation, returns the temperature
    def get_percept(self):
        return self.temperature

    # Agent action simulation, modifies temperature accordingly
    def update(self, action):
        match action:
            # Cool
            case "enfriar":
                self.temperature -= 1

            # Heat up
            case "calentar":
                self.temperature += 1

            # Idle
            case "esperar":
                pass


# Agent class, simulates an agent that perceives its environment and takes actions
# to modify it
class Agent:

    # Take action based on perception
    def act(self, perception):
        # Cool if hot
        if perception > 25:
            return "enfriar"

        # Heat up if cold
        elif perception < 18:
            return "calentar"

        # Idle if ideal
        else:
            return "esperar"


# Main loop, runs 10 iterations of perceiving temperature and modifications
def main():
    # Initialize environment & agent
    env = Environment()
    agent = Agent()

    # 10 loop run
    for i in range(10):

        # Get perceived temperature
        temp = env.get_percept()

        # Get corresponding agent action
        action = agent.act(temp)

        # Update the environment with agent's action
        env.update(action)

        # Get new temperature
        new_temp = env.get_percept()

        # Print iteration information
        print(
            f"Iteración: {i + 1}. Temperatura Inicial: {temp:.2f}. Acción del Agente: {action}. Nueva Temperatura: {new_temp:.2f}"
        )
    temp = env.get_percept()


main()
