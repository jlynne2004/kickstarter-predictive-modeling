# Load Table into PostgreSQL
import pandas as pd
from sqlalchemy import create_engine

# Load cleaned data
df = pd.read_csv('data/cleaned/ks-projects-201612-cleaned.csv')

# Covert data types
df['goal'] = pd.to_numeric(df['goal'], errors='coerce')
df['pledged'] = pd.to_numeric(df['pledged'], errors='coerce')
df['usd pledged'] = pd.to_numeric(df['usd pledged'], errors='coerce')
df['backers'] = pd.to_numeric(df['backers'], errors='coerce')
df['launched'] = pd.to_datetime(df['launched'], errors='coerce')
df['deadline'] = pd.to_datetime(df['deadline'], errors='coerce')

# Create PostgreSQL connection (replace with your password)
engine = create_engine('postgresql://postgres:S3n!or01@localhost:5432/portfolio_projects')

# Load directly to database
df.to_sql('projects', engine, schema='kickstarter', if_exists='replace', index=False)

print("✅ Data loaded successfully!")