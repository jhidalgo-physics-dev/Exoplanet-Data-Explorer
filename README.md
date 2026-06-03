#Exoplanet Data Explorer

This project analyzes confirmed exoplanet data from the NASA Exoplanet Archive using Python, Pandas, and Matplotlib. The goal is to explore relationships between planetary properties, discovery methods, host stars, and orbital characteristics through scientific data analysis and visualization.

The project demonstrates techniques commonly used in astronomy and data science, including data cleaning, exploratory data analysis, statistical visualization, and interpretation of large scientific datasets.

---

##Project Snapshot

Dataset: NASA Exoplanet Archive (Planetary Systems Composite Data)

Number of Confirmed Exoplanets: 6,291

Language: Python

Libraries: Pandas, NumPy, Matplotlib

Focus Areas:

- Astronomy Data Analysis
- Scientific Computing
- Data Visualization
- Exploratory Data Analysis
- Research Computing

---

##Scientific Questions Investigated

This project explores several questions related to exoplanet science:

- How has exoplanet discovery evolved over time?
- Which detection methods have been most successful?
- What sizes of planets are most commonly discovered?
- How are planetary mass and radius related?
- How does host star temperature influence planetary temperature?
- How does orbital distance affect planetary temperature?

---

##Key Results

###Exoplanet Discoveries by Year

This visualization shows the rapid growth of exoplanet discoveries over the past three decades. Major increases correspond to large survey programs and mission data releases, particularly from the Kepler mission.

---

###Discovery Methods

Transit photometry is by far the dominant discovery method, accounting for the majority of confirmed exoplanets in the dataset. Radial velocity remains the second most productive technique.

---

###Planet Radius Distribution

The distribution reveals distinct populations of planets, including Earth-sized planets, super-Earths, mini-Neptunes, and gas giants. A small number of extreme outliers are also present.

---

###Planet Mass vs Radius

This log-log visualization illustrates the relationship between planetary mass and radius across multiple classes of exoplanets. Distinct populations emerge, including rocky planets, Neptune-like planets, and gas giants.

---

###Planet Temperature vs Host Star Temperature

Planetary equilibrium temperature generally increases with host star temperature, although substantial scatter exists because orbital distance also plays a major role.

---

###Planet Temperature vs Orbital Distance

A clear inverse relationship exists between orbital distance and planetary temperature. Planets located closer to their host stars receive more stellar radiation and are significantly hotter than planets in distant orbits.

---

##Scientific Background

Exoplanets are planets that orbit stars outside our Solar System. Since the first confirmed exoplanet discoveries in the 1990s, thousands of planets have been detected using a variety of observational techniques.

Planetary properties such as mass, radius, orbital distance, and equilibrium temperature provide important insights into planetary formation, composition, and habitability. Large datasets allow researchers to identify statistical trends and compare planetary systems across the galaxy.

---

##Skills Demonstrated

- Python Programming
- Scientific Computing
- Data Cleaning and Preparation
- Exploratory Data Analysis
- Statistical Visualization
- Astronomy Data Analysis
- Pandas DataFrames
- NumPy Operations
- Research Computing
- Technical Documentation

---

##Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- NASA Exoplanet Archive

---

##How to Run

Clone the repository:
git clone https://github.com/jhidalgo-physics-dev/Exoplanet-Data-Explorer.git
cd Exoplanet-Data-Explorer

Install dependencies:
pip install -r requirements.txt

Run the analysis:
python exoplanet_explorer.py

Generated figures will be saved to the figures/ directory.

---

##Future Improvements

- Interactive visualizations using Plotly
- Additional exoplanet classification analysis
- Habitability zone comparisons
- Correlation studies between stellar and planetary properties
- Machine learning classification of exoplanet types
- Automated report generation

---

##Data Source

NASA Exoplanet Archive

https://exoplanetarchive.ipac.caltech.edu

The dataset used in this project was obtained from the Planetary Systems Composite Data table maintained by NASA's Exoplanet Archive.

##About This Project

This project was developed as part of an independent scientific computing portfolio focused on computational physics, astrophysics, and data analysis. The repository demonstrates practical applications of Python programming to real astronomical datasets and showcases techniques commonly used in research and technical environments.
