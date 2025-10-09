def get_league_table(results):
    """Builds an ordered league table from a list of football results"""
    league_table = {}
    for home, away in results:
        home_team, home_score = home
        away_team, away_score = away
        if home_score > away_score:
            if home_team not in league_table:
                league_table[home_team] = 0
            league_table[home_team] += 3
        elif home_score < away_score:
            if away_team not in league_table:
                league_table[away_team] = 0
            league_table[away_team] += 3
        else:
            if home_team not in league_table:
                league_table[home_team] = 0
            league_table[home_team] += 1
            if away_team not in league_table:
                league_table[away_team] = 0
            league_table[away_team] += 1

    items = [(team, points) for team, points in league_table.items()]
    items = sorted(items, key=lambda x: x[1], reverse=True)
    return items

