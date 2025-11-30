# import seaborn as sns
# import pandas as pd
# import matplotlib.pyplot as plt
#
#
#
# df = pd.read_csv("IRIS.csv")
# df.head()
#
#
#
#
# if 'ID' in df.columns:
#     df = df.drop('ID', axis=1)
#
# print("Unique species in dataset")
# print(df['species'].unique(), "\n")
#
#
#
# def show_stats_for_species(species_name):
#     print(f"Statsitics for {species_name}")
#     species_df = df[df['species'] == species_name]
#
#     print("\nDescribe():")
#     print(species_df.describe())
#
#     print("\n25th Percentile")
#     print(species_df.quantile(0.25, numeric_only=True))
#
#     print("\n50th Percentile")
#     print(species_df.quantile(0.50, numeric_only=True))
#
#     print("\n75th Percentile")
#     print(species_df.quantile(0.75, numeric_only=True))
#
#
# show_stats_for_species("Iris-setosa")
# show_stats_for_species("Iris-versicolor")
# show_stats_for_species("Iris-virginica")
#
#
#
# ## Create a Box plot for each feature in the dataset
#
# features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
#
# for feature in features:
#     sns.boxplot(x='species', y=feature, data=df)
#     plt.title(f"Box plot of {feature} vs Species")
#     plt.show()
#
# # In[ ]:
#
#
# # In[ ]:
#



import pandas as pd

# Load the dataset
df = pd.read_csv('IRIS.csv')

# Filter the dataset for each species
species_list = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

# Iterate through each species and display statistical details
for species in species_list:
    print(f"Statistics for {species}:")
    species_data = df[df['species'] == species]  # Filter data for the species
    print(species_data.describe())  # Display statistical details
    print("\n")
