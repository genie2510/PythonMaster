import json


def read_match_data(file_path):
    # Open and read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # 1. Extract Match Information
    print("=== Match Summary ===")
    teams = data.get("match", {}).get("teams", {})
    india_summary = teams.get("india", {})
    england_summary = teams.get("england", {})

    print(f"India: {india_summary.get('score')}/{india_summary.get('wickets')} in {india_summary.get('overs')} overs")
    print(
        f"England: {england_summary.get('score')}/{england_summary.get('wickets')} in {england_summary.get('overs')} overs")
    print(f"Result: {england_summary.get('result', 'N/A')}\n")

    # 2. Extract India's Innings Data
    print("=== India Innings ===")
    india_innings = data.get("india_innings", {})
    india_total = india_innings.get("total", {})
    print(f"Total: {india_total.get('runs')}/{india_total.get('wickets')} in {india_total.get('overs')} overs")

    # Batting
    print("\nBatting:")
    for batter in india_innings.get("batting", []):
        if "dismissal" in batter:
            print(
                f"  {batter['batsman']:<20} | {batter['runs']:<3} ")
        else:
            print(f"  {batter['batsman']:<20} | {batter['runs']:<3} (Extras)")

    # Fall of wickets
    print("\nFall of Wickets:")
    for fow in india_innings.get("fall_of_wickets", []):
        print(f"  {fow}")

    # Bowling
    print("\nBowling (England):")
    for bowler in india_innings.get("bowling", []):
        print(
            f"  {bowler['bowler']:<18} | {bowler['wickets']} wickets ")

    # 3. Extract England's Innings Data
    print("\n=== England Innings ===")
    england_innings = data.get("england_innings", {})
    england_total = england_innings.get("total", {})
    print(f"Total: {england_total.get('runs')}/{england_total.get('wickets')} in {england_total.get('overs')} overs")

    # Batting
    print("\nBatting:")
    for batter in england_innings.get("batting", []):
        if "dismissal" in batter:
            print(
                f"  {batter['batsman']:<20} | {batter['runs']:<3} ")
        else:
            print(f"  {batter['batsman']:<20} | {batter['runs']:<3} (Extras)")

    # Fall of wickets
    print("\nFall of Wickets:")
    for fow in england_innings.get("fall_of_wickets", []):
        print(f"  {fow}")

    # Bowling
    print("\nBowling (India):")
    for bowler in england_innings.get("bowling", []):
        print(
            f"  {bowler['bowler']:<18} | {bowler['wickets']} ")


if __name__ == "__main__":
    file_path = "match_data.json"
    read_match_data(file_path)
