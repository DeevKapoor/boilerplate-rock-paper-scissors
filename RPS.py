import random

def player(prev_play, opponent_history=[]):
    # Track the opponent's history
    if prev_play:
        opponent_history.append(prev_play)

    # Define counters
    counter_moves = {"R": "P", "P": "S", "S": "R"}

    # Strategy: Use multiple approaches to predict the next move
    def frequency_analysis():
        """Predict the opponent's move based on frequency analysis."""
        if opponent_history:
            counts = {"R": 0, "P": 0, "S": 0}
            for move in opponent_history:
                counts[move] += 1
            most_common_move = max(counts, key=counts.get)
            return counter_moves[most_common_move]
        return random.choice(["R", "P", "S"])

    def pattern_matching():
        """Find patterns in the opponent's play history and predict next move."""
        history_len = len(opponent_history)
        if history_len > 5:
            # Look for repeated sequences
            for length in range(5, 2, -1):  # Check sequences of length 5 to 3
                sequence = opponent_history[-length:]
                for i in range(history_len - length):
                    if opponent_history[i:i+length] == sequence:
                        next_index = i + length
                        if next_index < history_len:
                            return counter_moves[opponent_history[next_index]]
        return None

    def adaptive_strategy():
        """Combine different strategies dynamically."""
        pattern_guess = pattern_matching()
        if pattern_guess:
            return pattern_guess
        return frequency_analysis()

    # First move fallback
    if not opponent_history:
        return random.choice(["R", "P", "S"])

    # Decide the next move using the adaptive strategy
    return adaptive_strategy()
