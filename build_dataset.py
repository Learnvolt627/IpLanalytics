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
chase['current_score']=g['runs_total'].cumsum()
chase['wickets_fallen']=g['wicket_flag'].cumsum()

chase['wickets_in_hand']=10-chase['wickets_fallen']
chase['balls_remaining']=120-chase['legal_balls_bowled']
chase['runs_needed']= chase['runs_target']-chase['current_score']

chase['crr']= chase ['current_score']/ (chase['legal_balls_bowled'].replace(0,np.nan)/6)
chase['rrr']= chase ['runs_needed']/(chase['balls_remaining'].replace(0,np.nan)/6)
chase['crr']= chase ['crr'].fillna(0)
chase['rrr']= chase ['rrr'].fillna(0)


chase['label']=(chase['batting_team']==chase['match_won_by']).astype(int)

feature_cols = ['match_id', 'season', 'batting_team', 'bowling_team',
                 'current_score', 'wickets_in_hand', 'balls_remaining',
                 'runs_needed', 'crr', 'rrr', 'label']
dataset = chase[feature_cols]
dataset.to_csv("win_probability_dataset.csv", index=False)

print(dataset.shape)
print(dataset.head(10))
print(dataset['label'].value_counts())
print(dataset[['current_score','wickets_in_hand','balls_remaining','runs_needed','crr','rrr']].describe())