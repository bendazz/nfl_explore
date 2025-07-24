#!/usr/bin/env python3
"""
Example analysis script for NFL team data files.
This demonstrates how to work with the team-specific CSV files.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_team_performance(team_abbr):
    """
    Example analysis of a team's performance using their CSV file.
    
    Args:
        team_abbr (str): Team abbreviation (e.g., 'KC', 'BUF', 'PHI')
    """
    
    # Find the team file
    team_files = {
        'ARI': 'ARI_Cardinals_2024.csv',
        'ATL': 'ATL_Falcons_2024.csv', 
        'BAL': 'BAL_Ravens_2024.csv',
        'BUF': 'BUF_Bills_2024.csv',
        'CAR': 'CAR_Panthers_2024.csv',
        'CHI': 'CHI_Bears_2024.csv',
        'CIN': 'CIN_Bengals_2024.csv',
        'CLE': 'CLE_Browns_2024.csv',
        'DAL': 'DAL_Cowboys_2024.csv',
        'DEN': 'DEN_Broncos_2024.csv',
        'DET': 'DET_Lions_2024.csv',
        'GB': 'GB_Packers_2024.csv',
        'HOU': 'HOU_Texans_2024.csv',
        'IND': 'IND_Colts_2024.csv',
        'JAX': 'JAX_Jaguars_2024.csv',
        'KC': 'KC_Chiefs_2024.csv',
        'LA': 'LA_Rams_2024.csv',
        'LAC': 'LAC_Chargers_2024.csv',
        'LV': 'LV_Raiders_2024.csv',
        'MIA': 'MIA_Dolphins_2024.csv',
        'MIN': 'MIN_Vikings_2024.csv',
        'NE': 'NE_Patriots_2024.csv',
        'NO': 'NO_Saints_2024.csv',
        'NYG': 'NYG_Giants_2024.csv',
        'NYJ': 'NYJ_Jets_2024.csv',
        'PHI': 'PHI_Eagles_2024.csv',
        'PIT': 'PIT_Steelers_2024.csv',
        'SEA': 'SEA_Seahawks_2024.csv',
        'SF': 'SF_49ers_2024.csv',
        'TB': 'TB_Buccaneers_2024.csv',
        'TEN': 'TEN_Titans_2024.csv',
        'WAS': 'WAS_Commanders_2024.csv'
    }
    
    if team_abbr not in team_files:
        print(f"Team {team_abbr} not found. Available teams: {list(team_files.keys())}")
        return
    
    filename = f"team_data/{team_files[team_abbr]}"
    
    print(f"Loading data for {team_abbr}...")
    df = pd.read_csv(filename)
    
    # Basic team info
    team_name = df['team_full_name'].iloc[0]
    team_conf = df['team_conference'].iloc[0]
    team_div = df['team_division'].iloc[0]
    
    print(f"\n=== {team_name} Analysis ===")
    print(f"Conference: {team_conf}")
    print(f"Division: {team_div}")
    print(f"Total plays analyzed: {len(df)}")
    
    # Filter to plays where this team had possession
    team_plays = df[df['posteam'] == team_abbr].copy()
    print(f"Plays with {team_abbr} on offense: {len(team_plays)}")
    
    # Basic offensive statistics
    print("\n--- Offensive Performance ---")
    
    # Passing stats
    pass_plays = team_plays[team_plays['pass_attempt'] == 1]
    if len(pass_plays) > 0:
        completion_pct = (pass_plays['complete_pass'].sum() / len(pass_plays)) * 100
        avg_pass_yards = pass_plays['passing_yards'].mean()
        pass_epa = pass_plays['epa'].mean()
        
        print(f"Passing attempts: {len(pass_plays)}")
        print(f"Completion percentage: {completion_pct:.1f}%")
        print(f"Average yards per pass: {avg_pass_yards:.1f}")
        print(f"Average EPA per pass: {pass_epa:.3f}")
    
    # Rushing stats  
    rush_plays = team_plays[team_plays['rush_attempt'] == 1]
    if len(rush_plays) > 0:
        avg_rush_yards = rush_plays['rushing_yards'].mean()
        rush_epa = rush_plays['epa'].mean()
        
        print(f"Rushing attempts: {len(rush_plays)}")
        print(f"Average yards per rush: {avg_rush_yards:.1f}")
        print(f"Average EPA per rush: {rush_epa:.3f}")
    
    # Red zone efficiency
    red_zone_plays = team_plays[team_plays['yardline_100'] <= 20]
    if len(red_zone_plays) > 0:
        red_zone_tds = red_zone_plays['touchdown'].sum()
        red_zone_efficiency = (red_zone_tds / len(red_zone_plays)) * 100
        print(f"Red zone efficiency: {red_zone_efficiency:.1f}% ({red_zone_tds} TDs in {len(red_zone_plays)} plays)")
    
    # Third down conversions
    third_downs = team_plays[team_plays['down'] == 3]
    if len(third_downs) > 0:
        third_down_conversions = third_downs['third_down_converted'].sum()
        third_down_pct = (third_down_conversions / len(third_downs)) * 100
        print(f"Third down conversion rate: {third_down_pct:.1f}% ({third_down_conversions}/{len(third_downs)})")
    
    # Home vs Away performance
    print("\n--- Home vs Away Performance ---")
    home_plays = team_plays[team_plays['posteam_type'] == 'home']
    away_plays = team_plays[team_plays['posteam_type'] == 'away']
    
    if len(home_plays) > 0 and len(away_plays) > 0:
        home_epa = home_plays['epa'].mean()
        away_epa = away_plays['epa'].mean()
        print(f"Home EPA per play: {home_epa:.3f} ({len(home_plays)} plays)")
        print(f"Away EPA per play: {away_epa:.3f} ({len(away_plays)} plays)")
    
    return df, team_plays

def create_team_visualization(team_abbr):
    """Create some basic visualizations for a team."""
    
    # This is a simplified version - students can expand on this
    print(f"\nCreating visualizations for {team_abbr}...")
    print("(Visualization code would go here - students can build this out!)")
    print("Ideas for charts:")
    print("- EPA by quarter")
    print("- Pass vs Rush efficiency")
    print("- Performance by down and distance")
    print("- Weekly performance trends")

if __name__ == "__main__":
    # Example usage
    print("NFL Team Analysis Example")
    print("=" * 40)
    
    # Analyze a specific team (change this to any team abbreviation)
    team_to_analyze = "KC"  # Kansas City Chiefs
    
    df, team_plays = analyze_team_performance(team_to_analyze)
    create_team_visualization(team_to_analyze)
    
    print(f"\nData loaded successfully! The DataFrame 'df' contains all plays.")
    print(f"The DataFrame 'team_plays' contains only {team_to_analyze} offensive plays.")
    print(f"\nNext steps for students:")
    print(f"1. Explore the data: df.head(), df.columns, df.describe()")
    print(f"2. Filter for specific situations: red zone, 3rd down, etc.")
    print(f"3. Calculate additional metrics: success rate, explosive plays, etc.")
    print(f"4. Create visualizations using matplotlib or seaborn")
    print(f"5. Compare with other teams by loading their files")
