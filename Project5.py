# ---------- Movie Netflix streamlit app ------------

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Movie & Netflix Analytics",
    page_icon="🎬",
    layout="wide"
)

# -------------------- DATA --------------------

Movie_dataset = {

    "movie_name": [
        "Top Gun: Maverick",
        "Superman",
        "Thunderbolts*",
        "Final Destination: Bloodlines",
        "Titanic",
        "Moonlight",
        "Spirited Away",
        "The Social Network",
        "No Country for Old Men",
        "There Will Be Blood",
        "Mission: Impossible III",
        "Edge of Tomorrow",
        "Knight and Day",
        "Lions for Lambs",
        "War of the Worlds"
    ],

    "genre": [
        "Action",
        "Superhero",
        "Superhero",
        "Horror",
        "Romance",
        "Drama",
        "Animation",
        "Drama",
        "Crime",
        "Drama",
        "Action",
        "Sci-Fi",
        "Comedy",
        "Drama",
        "Sci-Fi"
    ],

    "release_year": [
        2022,
        2025,
        2025,
        2025,
        1997,
        2016,
        2001,
        2010,
        2007,
        2007,
        2006,
        2014,
        2010,
        2007,
        2005
    ],

      "cast": [
        "Tom Cruise, Miles Teller, Jennifer Connelly, Jon Hamm, Glen Powell, Val Kilmer",
        "David Corenswet, Rachel Brosnahan, Nicholas Hoult, Skyler Gisondo, Isabela Merced",
        "Florence Pugh, Sebastian Stan, Julia Louis-Dreyfus, David Harbour, Wyatt Russell",
        "Kaitlyn Santa Juana, Teo Briones, Richard Harmon, Brec Bassinger, Tony Todd",
        "Leonardo DiCaprio, Kate Winslet, Billy Zane, Kathy Bates, Gloria Stuart",
        "Mahershala Ali, Naomie Harris, Janelle Monáe, Trevante Rhodes, Ashton Sanders",
        "Rumi Hiiragi, Miyu Irino, Mari Natsuki, Bunta Sugawara",
        "Jesse Eisenberg, Andrew Garfield, Justin Timberlake, Armie Hammer, Rooney Mara",
        "Javier Bardem, Josh Brolin, Tommy Lee Jones, Kelly Macdonald, Woody Harrelson",
        "Daniel Day-Lewis, Paul Dano, Kevin J. O'Connor, Ciarán Hinds",
        "Tom Cruise, Philip Seymour Hoffman, Ving Rhames, Michelle Monaghan, Simon Pegg",
        "Tom Cruise, Emily Blunt, Bill Paxton, Brendan Gleeson, Jeremy Piven",
        "Tom Cruise, Cameron Diaz, Peter Sarsgaard, Viola Davis",
        "Robert Redford, Meryl Streep, Tom Cruise, Michael Peña",
        "Tom Cruise, Dakota Fanning, Miranda Otto, Justin Chatwin, Tim Robbins"
    ],

    "producer": [
        "Jerry Bruckheimer, Tom Cruise, Christopher McQuarrie, David Ellison",
        "Peter Safran, James Gunn",
        "Kevin Feige, Nate Moore",
        "Craig Perry, Jon Watts, Dianne McGunigle",
        "James Cameron, Jon Landau",
        "Adele Romanski, Dede Gardner, Jeremy Kleiner",
        "Toshio Suzuki",
        "Scott Rudin, Dana Brunetti, Michael De Luca",
        "Ethan Coen, Joel Coen, Scott Rudin",
        "JoAnne Sellar, Paul Thomas Anderson, Daniel Lupi",
        "Tom Cruise, Paula Wagner",
        "Tom Lassally, Jeffrey Silver, Jason Hoffs",
        "Cathy Konrad, Beau Flynn",
        "Robert Redford, Matthew Michael Carnahan, Andrew Hauptman",
        "Kathleen Kennedy, Colin Wilson"
    ],

    # Values are in millions of USD
    "production_cost_million": [
        170,
        225,
        180,
        50,
        200,
        1.5,
        19,
        40,
        25,
        25,
        150,
        178,
        117,
        35,
        132
    ],

    "ticket_price": [
        16.41,
        16.00,
        15.50,
        15.50,
        8.00,
        11.00,
        10.00,
        10.00,
        9.00,
        9.00,
        9.00,
        11.00,
        10.00,
        9.00,
        7.50
    ],


    "tickets_sold": [
        165_600_000,
        38_000_000,
        24_000_000,
        20_500_000,
        282_000_000,
        6_000_000,
        36_000_000,
        22_000_000,
        19_000_000,
        8_000_000,
        44_000_000,
        34_000_000,
        26_000_000,
        7_000_000,
        86_000_000
    ],

    # Values are in USD
    "box_office_revenue": [
        1503260455,
        618723803,
        382000000,
        317854739,
        2264812968,
        66953264,
        360798190,
        224920315,
        171627166,
        76195140,
        398479497,
        370541256,
        261930436,
        63211088,
        603874366
    ],

     "netflix_viewers": [
        13_500_000,
        None,
        6_300_000,
        2_100_000,
        1_000_000,
        None,
        None,
        9_500_000,
        None,
        None,
        2_900_000,
        None,
        4_800_000,
        None,
        12_200_000
    ],

    # Rating is out of 10
    "rating": [
        8.2,
        7.0,
        6.7,
        8.0,
        7.4,
        8.6,
        8.6,
        7.8,
        8.2,
        8.2,
        6.9,
        7.9,
        6.3,
        6.2,
        6.6
    ],

    "production_country": [
        "United States",
        "United States",
        "United States",
        "United States",
        "United States",
        "United States",
        "Japan",
        "United States",
        "United States",
        "United States",
        "United States",
        "United States",
        "United States",
        "United States",
        "United States"
    ],

    "movie_id": [
        "tt1745960",
        "tt5950044",
        "tt20969586",
        "tt9619824",
        "tt0120338",
        "tt4975722",
        "tt0245429",
        "tt1285016",
        "tt0477348",
        "tt0469494",
        "tt0450259",
        "tt1631867",
        "tt1013743",
        "tt0891527",
        "tt0407304"
    ],

     # Runtime in minutes
    "runtime_minutes": [
        131,
        129,
        127,
        110,
        194,
        111,
        125,
        120,
        122,
        158,
        126,
        113,
        109,
        92,
        116
    ]


}

df = pd.DataFrame(Movie_dataset)



# Data Loading

df.to_csv("Movies.csv", index=False)
df.to_excel("Movies.xlsx", index=False)
df.to_json("Movies.json")


df_csv = pd.read_csv("Movie.csv")
df_excel = pd.read_excel("Movie.xlsx")
df_json = pd.read_json("Movie.json")


print(df_csv)
print(df_excel)
print(df_json)

# Convert production cost from millions of USD to USD
df["production_cost"] = df["production_cost_million"] * 1_000_000

# Derived metrics
df["profit"] = df["box_office_revenue"] - df["production_cost"]
df["profit_margin"] = (
    df["profit"] / df["box_office_revenue"] * 100
)

def rating_category(rating):
    if rating >= 8:
        return "Excellent"
    elif rating >= 7:
        return "Good"
    elif rating >= 6:
        return "Average"
    return "Low"

df["rating_category"] = df["rating"].apply(rating_category)


# -------------------- SIDEBAR --------------------

st.sidebar.title(" Movie Analytics")

page = st.sidebar.radio(
    "Choose a section",
    [
        "Dashboard",
        "Movie Explorer",
        "Genre Analysis",
        "Netflix Analysis",
        "Data Table"
    ]
)


# -------------------- DASHBOARD --------------------

if page == "Dashboard":
    st.title(" Movie & Netflix Analytics")
    st.write("Explore movie revenue, ratings, production cost, profit, runtime and Netflix viewership.")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Movies", df["movie_name"].nunique())
    col2.metric("Average Rating", f"{df['rating'].mean():.2f} / 10")
    col3.metric("Total Revenue", f"${df['box_office_revenue'].sum()/1e9:.2f}B")
    col4.metric("Total Tickets", f"{df['tickets_sold'].sum()/1e6:.1f}M")

    col5, col6, col7 = st.columns(3)
    col5.metric("Average Runtime", f"{df['runtime_minutes'].mean():.1f} min")
    col6.metric("Total Production Cost", f"${df['production_cost'].sum()/1e9:.2f}B")
    col7.metric("Total Profit", f"${df['profit'].sum()/1e9:.2f}B")

    st.subheader("Top 5 Movies by Box Office Revenue")
    top5 = df.nlargest(5, "box_office_revenue")[
        ["movie_name", "genre", "box_office_revenue", "rating"]
    ].copy()
    top5["box_office_revenue"] = top5["box_office_revenue"] / 1e6
    top5 = top5.rename(columns={"box_office_revenue": "revenue_million_usd"})
    st.dataframe(top5, use_container_width=True, hide_index=True)

    st.subheader("Revenue by Genre")
    genre_revenue = (
        df.groupby("genre")["box_office_revenue"]
        .sum()
        .sort_values(ascending=False) / 1e6
    )
    st.bar_chart(genre_revenue)



# -------------------- MOVIE EXPLORER --------------------

elif page == "Movie Explorer":
    st.title(" Movie Explorer")

    selected_movie = st.selectbox(
        "Select a movie",
        sorted(df["movie_name"].unique())
    )

    movie = df[df["movie_name"] == selected_movie].iloc[0]

    st.subheader(selected_movie)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Rating", f"{movie['rating']:.1f} / 10")
    c2.metric("Revenue", f"${movie['box_office_revenue']/1e6:.1f}M")
    c3.metric("Profit", f"${movie['profit']/1e6:.1f}M")
    c4.metric("Runtime", f"{movie['runtime_minutes']} min")

    st.write(f"**Genre:** {movie['genre']}")
    st.write(f"**Release Year:** {movie['release_year']}")
    st.write(f"**Producer:** {movie['producer']}")
    st.write(f"**Production Country:** {movie['production_country']}")
    st.write(f"**Rating Category:** {movie['rating_category']}")

    st.subheader("Cast")
    st.write(movie["cast"])

    st.subheader("Financial Details")
    details = pd.DataFrame({
        "Metric": [
            "Production Cost",
            "Box Office Revenue",
            "Profit",
            "Profit Margin"
        ],
        "Value": [
            f"${movie['production_cost']/1e6:.2f}M",
            f"${movie['box_office_revenue']/1e6:.2f}M",
            f"${movie['profit']/1e6:.2f}M",
            f"{movie['profit_margin']:.2f}%"
        ]
    })
    st.dataframe(details, use_container_width=True, hide_index=True)



# -------------------- GENRE ANALYSIS --------------------

elif page == "Genre Analysis":
    st.title(" Genre Analysis")

    genre_analysis = df.groupby("genre").agg(
        average_rating=("rating", "mean"),
        total_revenue=("box_office_revenue", "sum"),
        average_cost=("production_cost_million", "mean"),
        total_tickets=("tickets_sold", "sum")
    ).sort_values("total_revenue", ascending=False)

    display = genre_analysis.copy()
    display["total_revenue"] = display["total_revenue"] / 1e6
    display = display.rename(columns={
        "total_revenue": "total_revenue_million_usd"
    })

    st.dataframe(display.round(2), use_container_width=True)

    st.subheader("Average Rating by Genre")
    st.bar_chart(genre_analysis["average_rating"])

    st.subheader("Total Revenue by Genre")
    st.bar_chart(genre_analysis["total_revenue"] / 1e6)



# -------------------- NETFLIX ANALYSIS --------------------

elif page == "Netflix Analysis":
    st.title(" Netflix Analysis")

    netflix_data = df[df["netflix_viewers"].notna()].copy()

    st.metric(
        "Movies with Netflix Viewer Data",
        len(netflix_data)
    )

    st.subheader("Netflix Viewers")
    netflix_chart = (
        netflix_data.set_index("movie_name")["netflix_viewers"]
        .sort_values(ascending=False)
    )
    st.bar_chart(netflix_chart)

    st.subheader("Netflix Viewer Data")
    st.dataframe(
        netflix_data[
            ["movie_name", "netflix_viewers", "rating", "genre"]
        ].sort_values("netflix_viewers", ascending=False),
        use_container_width=True,
        hide_index=True
    )



# -------------------- DATA TABLE --------------------

elif page == "Data Table":
    st.title(" Movie Dataset")

    genre_filter = st.multiselect(
        "Filter by genre",
        sorted(df["genre"].unique())
    )

    min_rating = st.slider(
        "Minimum rating",
        min_value=0.0,
        max_value=10.0,
        value=0.0,
        step=0.1
    )

    filtered_df = df.copy()

    if genre_filter:
        filtered_df = filtered_df[
            filtered_df["genre"].isin(genre_filter)
        ]

    filtered_df = filtered_df[
        filtered_df["rating"] >= min_rating
    ]

    st.write(f"Showing **{len(filtered_df)}** movies.")

    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )

    csv = filtered_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        " Download Filtered CSV",
        data=csv,
        file_name="filtered_movies.csv",
        mime="text/csv"
    )