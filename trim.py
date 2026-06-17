import pandas as pd

df=pd.read_csv('IPL.csv')

keep_cols= ['match_id','season', 'batter','bowler','runs_batter', 'striker_out','toss_winner','toss_decision',
            'match_won_by','batting_team']

df_trimmed=df[keep_cols]
df_trimmed.to_csv('IPL_trimmed.csv', index=False)