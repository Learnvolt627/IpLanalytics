import pandas as pd
df=pd.read_csv("IPL.csv")


# print( 'a',335982 in df['match_id'].values)
# print('b',df['match_id'].dtype)
# print('c' ,df['match_id'].head(10).tolist())

# print('d', df['match_type'].unique)
# print('e' ,df['event_name'].unique()[:15])
# print('f' ,df['gender'].unique())
# print('g' ,df['team_type'].unique())

# real_id=df.loc[df['innings'].isin([1,2]), 'match_id'].iloc[0]
# print('h' ,real_id)
# sample=df[df['match_id']==real_id]
# print('i' ,sample[['innings','over','ball','runs_batter','runs_total','runs_target']].head(10))

# second_innings =df[(df['match_id']==335982)& (df['innings']==2)]
# print("rows in 2nd innings;", len(second_innings))
# print(second_innings[['innings','over','ball','runs_batter','runs_total','runs_target']].head(10))
# print(second_innings[['innings','over','ball','runs_batter','runs_total','runs_target']].tail(10))

sample= df[(df['match_id']==335982) & (df['innings']==2)]
cols = ['over','ball','ball_no','valid_ball','runs_total','wicket_kind','player_out','striker_out']
print(sample[cols].head(10))

print("--every wicket that feel in this innings--")
fell = sample[sample['player_out'].notna()]
print(fell[['over','ball','ball_no','player_out','wicket_kind','striker_out']])