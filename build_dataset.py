import numpy as np
import pandas as pd

df=pd.read_csv("IPL.csv")

chase = df[df['innings']==2].copy()

before=chase['match_id'].nunique()

#we drop matches with no clear winner 
chase = chase[chase['match_won_by'].notna()]


#also drop matches where winner was decided by superovers

chase=chase[chase['superover_winner'].isna()]

after= chase["match_id"].nunique()

print(f"matches before cleaning : {before}, after cleaning: {after}")


chase['wicket_flag']= chase['player_out'].notna().astype(int)

g= chase.groupby('match_id')

chase['legal_balls_bowled']= g['valid_ball'].cumsum()
chase['current_score']=g['runs-total'].cumsum()
chase['wickets_fallen']=g['wicket_flag'].cumsum()

chase['wickets_in_hand']=10-chase['wickets_fallen']
chase['balls_remaining']=120-chase['legal_balls_bowled']
chase['runs_needed']= chase['runs_target']-chase['current_score']

