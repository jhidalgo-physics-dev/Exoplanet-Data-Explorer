import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("figures", exist_ok=True)

df = pd.read_csv("data/exoplanets.csv", comment="#")

print("Dataset Loaded Successfully")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")

# Discoveries by year
discoveries_by_year = df["disc_year"].value_counts().sort_index()

plt.figure(figsize=(12, 6))
plt.bar(
    discoveries_by_year.index,
    discoveries_by_year.values
)
plt.xlabel("Discovery Year")
plt.ylabel("Number of Confirmed Exoplanets")
plt.title("Confirmed Exoplanet Discoveries by Year")
plt.grid(True)
plt.tight_layout()
plt.savefig("figures/discoveries_by_year.png", dpi=300)
plt.show()

print("\nDataset Statistics")
print("-" * 50)

print(
    f"Total confirmed exoplanets: {len(df)}"
)

print(
    f"Discovery methods: "
    f"{df['discoverymethod'].nunique()}"
)

print(
    f"Earliest discovery year: "
    f"{df['disc_year'].min()}"
)

print(
    f"Latest discovery year: "
    f"{df['disc_year'].max()}"
)

method_counts = (
    df["discoverymethod"]
    .value_counts()
    .head(10)
)

plt.figure(figsize=(10, 6))

method_counts.plot(kind="bar", logy=True)

plt.title(
    "Top Exoplanet Discovery Methods"
)

plt.xlabel("Discovery Method")
plt.ylabel("Number of Planets")

plt.tight_layout()

plt.savefig(
    "figures/discovery_methods.png",
    dpi=300
)

plt.show()

planet_radii = df["pl_rade"].dropna()

planet_radii = planet_radii[planet_radii < 25]

plt.figure(figsize=(10,6))

df["pl_rade"].dropna().hist(
    bins=50
)

plt.xlabel("Planet Radius [Earth Radii]")
plt.ylabel("Number of Planets")
plt.title("Distribution of Confirmed Exoplanet Sizes")

plt.tight_layout()

plt.savefig(
    "figures/planet_radius_distribution.png",
    dpi=300
)

plt.show()

print("\nPlanet Radius Statistics")
print("-" * 40)

print(f"Mean radius: {planet_radii.mean():.2f}")
print(f"Median radius: {planet_radii.median():.2f}")
print(f"Largest radius: {planet_radii.max():.2f}")

plt.figure(figsize=(10,6))

subset = df[
    (df["pl_rade"].notna()) &
    (df["pl_bmasse"].notna()) &
    (df["pl_rade"] < 25) &
    (df["pl_bmasse"] < 2000)
]

plt.scatter(
    subset["pl_rade"],
    subset["pl_bmasse"],
    alpha=0.15,
    s=8
)

plt.xlabel("Planet Radius [Earth Radii]")
plt.ylabel("Planet Mass [Earth Masses]")
plt.title("Planet Mass vs Radius")
plt.xscale("log")
plt.yscale("log")

plt.grid(True)
plt.tight_layout()
plt.savefig(
    "figures/mass_vs_radius.png",
    dpi=300
)

plt.show()

plt.figure(figsize=(10, 6))

temp_data = df[
    (df["st_teff"].notna()) &
    (df["pl_eqt"].notna())
]

plt.scatter(
    temp_data["st_teff"],
    temp_data["pl_eqt"],
    alpha=0.2,
    s=10
)

plt.xlabel("Stellar Effective Temperature [K]")
plt.ylabel("Planet Equilibrium Temperature [K]")
plt.title("Planet Temperature vs Host Star Temperature")

plt.grid(True)
plt.tight_layout()

plt.savefig(
    "figures/planet_vs_stellar_temperature.png",
    dpi=300
)

plt.show()

plt.figure(figsize=(10,6))

orbit_data = df[
    (df["pl_orbsmax"].notna()) &
    (df["pl_eqt"].notna())
]

plt.scatter(
    orbit_data["pl_orbsmax"],
    orbit_data["pl_eqt"],
    alpha=0.2,
    s=10
)

plt.xscale("log")

plt.xlabel("Orbital Distance [AU]")
plt.ylabel("Planet Equilibrium Temperature [K]")
plt.title("Planet Temperature vs Orbital Distance")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "figures/temperature_vs_distance.png",
    dpi=300
)

plt.show()
