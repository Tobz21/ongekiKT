# ongekiKT
working with Kamaitachi scores of your オンゲキ profile and displaying them

## Necessity
I was unable to find a method to export and display data from Kamaitachi for the game オンゲキ, so I created one myself

With this, you can find and calculate things like songs of the NEW rating frame and their ratings, which Kamaitachi doesn't do as of writing.

## Usage
- Requires Python 3.11.5
- Assumes data is of bright MEMORY ACT 2, NEW frame is set with this taken into account

1. Save `javascript:(function(d){if(location.origin=="https://kamai.tachi.ac"){var s=d.createElement("script");s.src="https://gist.githack.com/Tobz21/baaad8565fb8e17b45f224e4fd686324/raw/25c839245fba1595fe3175f6cf3ddb840d74bbf7/ongkTry.js";d.body.append(s);}})(document)`  as a bookmark, click it on Kamaitachi page or run it in the console when logged in on the page.

2. Save the downloaded 'ongekirating.tachi' file to a directory for the following
3. Download ongeki_const_all.json and ongekiscript.py to the same directory

4. Run ongekiscript.py on a terminal to get print output

The current output is set to calculate your rated plays by the chart constants, print the best 30 and b30 average to terminal and print the top 20 NEW plays 

## Limitations
- UNTESTED with LUNATIC difficulty.
  - No LUNATIC in my オンゲキ json currently, so I must put it there to be able to test it works
  - SHOULD only affect the NEW score categorization (see below)
- Not sure what 'is_unknown' is in the cc json. It mostly appears in the Basic and Advanced.
  - If we take it literally, it probably means they did not calculate the chart constants and just used the displayed level, as often chart constants are found by manual calculations and estimation
  - Or potentially the chart constants have no variation (similar to Arcaea cc behaviour on lower difficulty)
- Only tested on Windows

## Future Work
- Export instead of just printing at terminal
  - Potentially b30 image generation like Qman's オンゲキ does, but with the json support like their チュウニズム INT does
- Fix python script to take into account LUNATIC difficulty scores and release date 
  - For when difficulty = LUNATIC, use the lunatic added date instead of default date release
- Take into account and display more metrics, maybe in a nice way like how beerpsi's chuni bot shows judgements
  - Maybe make an equivalent ongeki bot with a kamaitachi hook to profile ???
- Devise a REACHABLE rating, by b30 + n15 + max(r15)
- Support オンゲキ bright MEMORY ACT 3 when it releases for my cab on MYT
- Test on Linux/Unix based systems and ensure cross platform (especially with root directory)

## Acknowledgements
- beer-psi for their bookmarklet script which this one is heavily based off of
- キューマン・エノビクト (Qman / reiwa.f5.si ) for their build of オンゲキ chart constant json and b30 gen site
- wikiwiki.jp for their detailed explanation of オンゲキ rating system components


