# 🎬 Movie & Netflix Analytics

A **Streamlit-based movie analytics dashboard** built with **Python, Pandas, and Streamlit**.

This project analyzes movie data including **box-office revenue, production cost, profit, ratings, genres, ticket sales, runtime, and Netflix viewership** through an interactive web application.

## 📌 Project Overview

The **Movie & Netflix Analytics** application provides an interactive way to explore and analyze movie data.

Users can:

* View overall movie statistics
* Explore individual movies
* Analyze movies by genre
* Analyze Netflix viewer data
* Filter movies by genre and rating
* View financial information
* Download filtered movie data as a CSV file

The application is organized into multiple sections using a Streamlit sidebar.

## ✨ Features

### 📊 Dashboard

The dashboard provides key movie statistics such as:

* Total number of movies
* Average rating
* Total box-office revenue
* Total tickets sold
* Average runtime
* Total production cost
* Total profit
* Top 5 movies by box-office revenue
* Revenue by genre

### 🎥 Movie Explorer

Select a movie and explore its:

* Rating
* Box-office revenue
* Profit
* Runtime
* Genre
* Release year
* Producer
* Production country
* Rating category
* Cast
* Financial details
* Profit margin

### 🎭 Genre Analysis

Analyze movie performance by genre using:

* Average rating
* Total revenue
* Average production cost
* Total tickets sold
* Average rating charts
* Revenue comparison charts

### 📺 Netflix Analysis

The Netflix section analyzes available viewer data and provides:

* Number of movies with Netflix viewer data
* Netflix viewer comparison chart
* Movie-wise Netflix viewer information
* Rating and genre information

### 🔎 Data Filtering

Users can filter the dataset by:

* Movie genre
* Minimum rating

The filtered dataset can also be downloaded as a CSV file.

## 🧮 Data Analysis

The project uses Pandas to create derived metrics such as:

**Production Cost**

Production cost is converted from millions of USD into USD.

**Profit**

```text
Profit = Box Office Revenue - Production Cost
```

**Profit Margin**

```text
Profit Margin = (Profit / Box Office Revenue) × 100
```

The project also categorizes movie ratings into:

* Excellent
* Good
* Average
* Low

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **Streamlit**
* **CSV**
* **Excel**
* **JSON**

The application creates and works with movie data in CSV, Excel, and JSON formats.

## 📂 Project Structure

```text
Movie-Netflix-Analytics/
│
├── app.py
├── Movies.csv
├── Movies.xlsx
├── Movies.json
├── requirements.txt
└── README.md
```

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Movie-Netflix-Analytics.git
```

### 2. Navigate to the project directory

```bash
cd Movie-Netflix-Analytics
```

### 3. Install the required libraries

```bash
pip install pandas streamlit openpyxl
```

Or, if you have a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📈 What I Practiced

This project helped me practice:

* Creating DataFrames with Pandas
* Working with CSV, Excel, and JSON files
* Data transformation
* Data filtering
* Grouping and aggregation
* Calculating derived metrics
* Working with missing values
* Sorting and selecting data
* Building an interactive Streamlit dashboard
* Creating charts and metrics
* Creating downloadable CSV files

## 🔮 Future Improvements

Possible improvements for future versions include:

* Add more movie records
* Connect the application to a real movie dataset
* Add movie search functionality
* Add more interactive visualizations
* Add year-based analysis
* Add advanced filtering options
* Add movie posters and additional metadata
* Deploy the application online

## 👨‍💻 Author

**Ali Shah**

This project was created as part of my journey to develop practical **Python, Pandas, data analysis, and AI engineering skills**.

---

⭐ If you find this project useful, feel free to explore the repository and provide feedback.

