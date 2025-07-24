#!/usr/bin/env python3
"""
Script to split the large NFL play-by-play data into team-specific files.
This makes the data more manageable for students to work with.
"""

import pandas as pd
import os
from pathlib import Path

def split_pbp_by_team():
    """Split the play-by-play data into team-specific files."""
    
    print("Loading teams data...")
    # Load teams data for team names and metadata
    teams_df = pd.read_csv('teams.csv')
    
    # Create a dictionary mapping team abbreviations to full names
    team_info = {}
    for _, row in teams_df.iterrows():
        team_abbr = row['team_abbr']
        team_info[team_abbr] = {
            'team_name': row['team_name'],
            'team_nick': row['team_nick'],
            'team_conf': row['team_conf'],
            'team_division': row['team_division']
        }
    
    print("Creating team_data directory...")
    # Create directory for team files
    team_dir = Path('team_data')
    team_dir.mkdir(exist_ok=True)
    
    print("Processing play-by-play data in chunks...")
    # Read the large CSV file in chunks to manage memory
    chunk_size = 10000
    team_data = {}
    
    for chunk in pd.read_csv('pbp_2024.csv', chunksize=chunk_size):
        print(f"Processing chunk with {len(chunk)} rows...")
        
        # For each team, collect plays where they were either home or away
        for team_abbr in team_info.keys():
            if team_abbr not in team_data:
                team_data[team_abbr] = []
            
            # Get plays where this team was involved (home or away)
            team_plays = chunk[
                (chunk['home_team'] == team_abbr) | 
                (chunk['away_team'] == team_abbr)
            ].copy()
            
            if len(team_plays) > 0:
                # Add team metadata to each play
                team_plays['team_full_name'] = team_info[team_abbr]['team_name']
                team_plays['team_nickname'] = team_info[team_abbr]['team_nick']
                team_plays['team_conference'] = team_info[team_abbr]['team_conf']
                team_plays['team_division'] = team_info[team_abbr]['team_division']
                
                team_data[team_abbr].append(team_plays)
    
    print("Saving team-specific files...")
    # Save each team's data to a separate CSV file
    for team_abbr, team_chunks in team_data.items():
        if team_chunks:  # Only save if team has data
            team_df = pd.concat(team_chunks, ignore_index=True)
            
            # Sort by game_date and play_id for chronological order
            team_df = team_df.sort_values(['game_date', 'play_id'])
            
            # Save to CSV
            filename = f"team_data/{team_abbr}_{team_info[team_abbr]['team_nick']}_2024.csv"
            team_df.to_csv(filename, index=False)
            
            print(f"Saved {len(team_df)} plays for {team_info[team_abbr]['team_name']} to {filename}")
    
    print("\nTeam split complete!")
    print(f"Individual team files saved in: {team_dir}")
    
    # Create a summary file
    create_team_summary(team_info)

def create_team_summary(team_info):
    """Create a summary file listing all team files."""
    
    summary_content = """# NFL Team Data Files - 2024 Season

This directory contains individual team files split from the main play-by-play dataset.
Each file contains all plays from games where that team participated (both home and away games).

## File Naming Convention
Files are named: `{TEAM_ABBR}_{TEAM_NICKNAME}_2024.csv`

## Additional Columns Added
Each team file includes these extra columns for convenience:
- `team_full_name`: Official team name
- `team_nickname`: Team nickname/mascot
- `team_conference`: AFC or NFC
- `team_division`: Division within conference

## Available Team Files

"""
    
    # Add each team to the summary
    for team_abbr, info in team_info.items():
        summary_content += f"- **{team_abbr}_{info['team_nick']}_2024.csv**: {info['team_name']} ({info['team_conf']} {info['team_division']})\n"
    
    summary_content += """
## Usage Tips

1. **Start with one team**: Pick your favorite team or a team with interesting storylines
2. **Compare divisions**: Use teams from the same division for comparative analysis
3. **Conference analysis**: Compare AFC vs NFC teams
4. **File size**: Each team file is much smaller and more manageable than the full dataset
5. **Join with roster data**: Use the main players_2024.csv file to add player information

## Example Analysis Ideas

- Analyze your team's offensive efficiency by quarter
- Compare home vs away performance
- Study red zone efficiency
- Track key players' contributions throughout the season
- Examine how your team performs in close games

Happy analyzing! 🏈
"""
    
    with open('team_data/README.md', 'w') as f:
        f.write(summary_content)
    
    print("Team summary file created: team_data/README.md")

if __name__ == "__main__":
    split_pbp_by_team()
