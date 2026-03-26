# Game Analyzer

This script performs backend analysis of football games and calculates probabilities.

## Features
- Analyze match statistics
- Calculate probabilities for different outcomes
- Generate insights based on game data

## Usage
1. Import the module.
2. Use the `analyze_games()` function to analyze games.
3. Use the `calculate_probability()` function to get probability estimates.

## Functions

### analyze_games(games: List[Dict[str, Any]]) -> None
- Analyze the provided list of games.

### calculate_probability(team1_stats: Dict[str, Any], team2_stats: Dict[str, Any]) -> float
- Calculate the probability of team 1 winning against team 2 based on their statistics.

## Example
```python
if __name__ == '__main__':
    games = [
        {'team1': 'Team A', 'team2': 'Team B', 'score1': 1, 'score2': 2},
        {'team1': 'Team C', 'team2': 'Team D', 'score1': 3, 'score2': 1}
    ]
    analyze_games(games)
    prob = calculate_probability(team1_stats, team2_stats)
    print(f'Probability of Team A winning: {prob}')
```

## Requirements
- Python 3.7+
- NumPy
- Pandas

## Conclusion
Use this file to analyze football games and derive statistical insights.