from preswald import connect, get_df, query, table, text, plotly
import plotly.express as px

connect()
df = get_df("my_dataset")

text("# Titanic Dataset Analysis")

text("""
This app analyzes the famous Titanic dataset.
We're exploring passenger information and visualizing survival rates.
""")

text("## Full Passenger Dataset")
table(df, title="All Titanic Passengers")

sql = 'SELECT * FROM my_dataset WHERE Age = 18 AND Survived = 1'
survivors_df = query(sql, 'my_dataset')
text("## Filtered Data: Adult Survivors")
table(survivors_df, title="Passengers Over 18 Who Survived")

text("## Visualization: Age Distribution by Survival")
fig = px.histogram(
    df,
    x="Age",
    color="Survived",
    nbins=50,
    title="Passenger Age Distribution",
    labels={'Survived': 'Survival Status'}
)

plotly(fig)
