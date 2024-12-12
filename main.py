from RPS_game import play, quincy, mrugesh, kris, abbey
from RPS import player

# Test your player function against the bots
print("Playing against Quincy:")
play(player, quincy, 1000, verbose=True)

print("\nPlaying against Mrugesh:")
play(player, mrugesh, 1000, verbose=True)

print("\nPlaying against Kris:")
play(player, kris, 1000, verbose=True)

print("\nPlaying against Abbey:")
play(player, abbey, 1000, verbose=True)
