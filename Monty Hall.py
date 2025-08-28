import random
import matplotlib.pyplot as plt

def play_one_game(num_doors=3, switch=True, verbose=False):
    """
    Play one round of the Monty Hall problem.
    Returns True if the player wins the car, False otherwise.
    """
    
    car = random.randint(0, num_doors - 1)
    
    
    player_choice = random.randint(0, num_doors - 1)

    
    available_doors = [d for d in range(num_doors) if d != player_choice and d != car]
    monty_opens = random.choice(available_doors)

    if verbose:
        print(f"Car is behind door {car}")
        print(f"Player chose door {player_choice}")
        print(f"Monty opened door {monty_opens} (goat)")

    
    if switch:
        remaining_doors = [d for d in range(num_doors) if d not in (player_choice, monty_opens)]
        player_choice = random.choice(remaining_doors)
        if verbose:
            print(f"Player SWITCHES to door {player_choice}")
    else:
        if verbose:
            print(f"Player STAYS with door {player_choice}")

    
    win = player_choice == car
    if verbose:
        print("Player WINS!" if win else "Player LOSES!")
        print("-" * 30)
    return win


def simulate(trials=10000, num_doors=3):
    """
    Run multiple simulations and compare results of staying vs switching.
    """
    stay_wins = sum(play_one_game(num_doors, switch=False) for _ in range(trials))
    switch_wins = sum(play_one_game(num_doors, switch=True) for _ in range(trials))

    print(f"Out of {trials} trials with {num_doors} doors:")
    print(f"  Staying won {stay_wins} times ({stay_wins/trials:.2%})")
    print(f"  Switching won {switch_wins} times ({switch_wins/trials:.2%})")

    
    plt.bar(["Stay", "Switch"], 
            [stay_wins/trials, switch_wins/trials], 
            color=["red", "green"])
    plt.title(f"Monty Hall Simulation ({num_doors} doors, {trials} trials)")
    plt.ylabel("Win Probability")
    plt.ylim(0, 1)
    plt.show()


if __name__ == "__main__":
    # Run a detailed demo of ONE game
    print("Demo of a single game (verbose mode):")
    play_one_game(num_doors=3, switch=True, verbose=True)

    # Run the simulation
    simulate(trials=10000, num_doors=3)