# NFL Teams Data Column Reference Guide

This dataset contains 17 columns of NFL team information including identification, branding, colors, and visual assets. Below is a comprehensive guide to each column and what it represents.

## Basic Team Identification

| Column Name | Description |
|-------------|-------------|
| team_abbr | Three-letter team abbreviation (e.g., NE, GB, DAL) |
| team_name | Full official team name (e.g., "New England Patriots") |
| team_id | Unique numerical identifier for each team |
| team_nick | Team nickname/mascot (e.g., "Patriots", "Packers", "Cowboys") |

## League Structure and Organization

| Column Name | Description |
|-------------|-------------|
| team_conf | Conference affiliation (AFC or NFC) |
| team_division | Division within conference (e.g., "AFC East", "NFC North") |

## Team Branding and Colors

| Column Name | Description |
|-------------|-------------|
| team_color | Primary team color (hex color code, e.g., #002244) |
| team_color2 | Secondary team color (hex color code) |
| team_color3 | Tertiary team color (hex color code) |
| team_color4 | Quaternary team color (hex color code) |

## Visual Assets and Logos

| Column Name | Description |
|-------------|-------------|
| team_logo_wikipedia | URL to team logo from Wikipedia |
| team_logo_espn | URL to team logo from ESPN |
| team_wordmark | URL to team wordmark/text logo |
| team_conference_logo | URL to conference logo (AFC/NFC) |
| team_league_logo | URL to NFL league logo |
| team_logo_squared | URL to squared/standardized team logo |

---

## NFL Conference and Division Structure

### AFC (American Football Conference)

#### AFC East
- **BUF** - Buffalo Bills
- **MIA** - Miami Dolphins  
- **NE** - New England Patriots
- **NYJ** - New York Jets

#### AFC North  
- **BAL** - Baltimore Ravens
- **CIN** - Cincinnati Bengals
- **CLE** - Cleveland Browns
- **PIT** - Pittsburgh Steelers

#### AFC South
- **HOU** - Houston Texans
- **IND** - Indianapolis Colts
- **JAX** - Jacksonville Jaguars
- **TEN** - Tennessee Titans

#### AFC West
- **DEN** - Denver Broncos
- **KC** - Kansas City Chiefs
- **LAC** - Los Angeles Chargers
- **LV** - Las Vegas Raiders

### NFC (National Football Conference)

#### NFC East
- **DAL** - Dallas Cowboys
- **NYG** - New York Giants
- **PHI** - Philadelphia Eagles
- **WAS** - Washington Commanders

#### NFC North
- **CHI** - Chicago Bears
- **DET** - Detroit Lions
- **GB** - Green Bay Packers
- **MIN** - Minnesota Vikings

#### NFC South
- **ATL** - Atlanta Falcons
- **CAR** - Carolina Panthers
- **NO** - New Orleans Saints
- **TB** - Tampa Bay Buccaneers

#### NFC West
- **ARI** - Arizona Cardinals
- **LA** - Los Angeles Rams (also appears as LAR)
- **SF** - San Francisco 49ers
- **SEA** - Seattle Seahawks

## Understanding Team Colors

### Color Format
- All colors are provided in **hexadecimal format** (e.g., #002244)
- These can be used directly in data visualizations, websites, and graphics
- Primary colors are typically the most dominant team colors
- Secondary through quaternary colors provide accent and alternate options

### Common Color Patterns
- **Primary (team_color)**: Usually the dominant uniform color
- **Secondary (team_color2)**: Often the complementary or accent color
- **Tertiary/Quaternary**: Additional colors for logos, trim, or alternate uniforms

## Logo and Visual Asset Usage

### Logo Types
- **team_logo_wikipedia**: Standard team logos, good for general use
- **team_logo_espn**: ESPN's standardized logos, consistent sizing
- **team_wordmark**: Text-based team logos/wordmarks
- **team_logo_squared**: Standardized square format, good for data viz

### Conference and League Logos
- **team_conference_logo**: AFC or NFC conference logos
- **team_league_logo**: Official NFL shield logo

## Historical Team Information

### Team Location Changes
The dataset includes historical team abbreviations:
- **OAK** - Oakland Raiders (now Las Vegas Raiders - LV)
- **SD** - San Diego Chargers (now Los Angeles Chargers - LAC)  
- **STL** - St. Louis Rams (now Los Angeles Rams - LA/LAR)

### Team Name Changes
- **WAS** - Washington Commanders (formerly Washington Redskins/Football Team)

## Practical Applications

### Data Visualization
- Use team colors for consistent branding in charts and graphs
- Team logos can enhance visual presentations
- Hex color codes work directly in most plotting libraries

### Joining with Other Datasets
- Use `team_abbr` to join with play-by-play and roster data
- `team_id` provides an alternative unique identifier
- Consistent with other NFL datasets using standard abbreviations

### Web Development and Apps
- Logo URLs provide ready-to-use images
- Color codes enable consistent team theming
- Wordmarks useful for headers and titles

### Fantasy Sports Applications
- Team branding for fantasy team displays
- Conference/division organization for scheduling
- Visual elements for user interfaces

## Notes for Using This Data

1. **Color Consistency**: Use the provided hex codes to maintain official team branding in visualizations.

2. **Logo Usage**: External URLs may change over time. Consider downloading and hosting locally for production applications.

3. **Team Abbreviations**: Stick to the standard 2-3 letter abbreviations used across NFL datasets.

4. **Historical Data**: Be aware that some teams have changed locations/names. The dataset includes both current and historical abbreviations.

5. **Image Rights**: Team logos are trademarked. Ensure proper usage rights for commercial applications.

6. **Data Freshness**: Team information generally remains stable but can change with relocations or rebranding.

## Color Scheme Examples

### Popular Team Color Combinations
- **Patriots**: Navy (#002244) and Red (#C60C30)
- **Packers**: Green (#203731) and Gold (#FFB612)  
- **Cowboys**: Navy (#002244) and Silver (#B0B7BC)
- **Chiefs**: Red (#E31837) and Gold (#FFB612)
- **Steelers**: Black (#000000) and Gold (#FFB612)

This teams dataset is perfect for creating visually appealing and branded NFL analytics, dashboards, and applications. Combined with your play-by-play and roster data, you have everything needed for comprehensive NFL data analysis with proper team branding and visual identity!
