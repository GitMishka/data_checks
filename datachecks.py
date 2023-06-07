import psycopg2
import pandas as pd
import config
from datetime import datetime

def check_null_values(df):
    return df.isnull().sum().to_dict()

def check_unique_ids(df):
    return {'duplicate_ids': len(df[df.duplicated(['post_id'])])}

def check_data_types(df):
    return df.dtypes.to_dict()

def check_negative_comments(df):
    return {'negative_comments': len(df[df['post_comments'] < 0])}

def check_upvote_ratio_range(df):
    return {'invalid_upvote_ratios': len(df[(df['post_upvote_ratio'] < 0) | (df['post_upvote_ratio'] > 1)])}

def check_future_timestamps(df):
    return {'future_dates': len(df[df['post_timeposted'] > pd.Timestamp.now()])}

conn = psycopg2.connect(
    host=config.pg_host,
    database=config.pg_database,
    user=config.pg_user,
    password=config.pg_password
)

query = "SELECT * FROM reddit_posts_hot"

df = pd.read_sql_query(query, conn)

results = {
    'Null values': check_null_values(df),
    'Duplicate IDs': check_unique_ids(df),
    'Data types': check_data_types(df),
    'Negative comments': check_negative_comments(df),
    'Invalid upvote ratios': check_upvote_ratio_range(df),
    'Future dates': check_future_timestamps(df),
}

results_df = pd.DataFrame.from_dict(results, orient='index')
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
results_df.to_csv(f'data_quality_report_{timestamp}.csv')

conn.close()
