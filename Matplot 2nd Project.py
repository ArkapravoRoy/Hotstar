
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv(r"C:\Users\NeelLaptop\Desktop\Python\hotstar.csv")

# Show first 10 rows
print(data.head(10))

# Drop rows with missing values in specified columns
data.dropna(subset=["hotstar_id", "title", "description", "genre", "type", "running_time", "year", "age_rating"])

data.drop(columns="seasons",inplace=True)
data.drop(columns="episodes",inplace=True)

# Show count of missing values in each column
#print(data.isnull().sum())

# Count values in 'type' column
count = data["type"].value_counts()
#print(count)
plt.bar(count.index,count.values,color=["skyblue","orange"])

plt.title("Number of TV shows vs Movies on")
plt.xlabel("Type")

plt.ylabel("Count")
plt.tight_layout()
plt.savefig("TV vs Movies.png")
plt.show()


pie=data["age_rating"].value_counts()
plt.pie(pie,autopct="%1.1f%%",labels=pie.index)
plt.title("Percentage of Age Rating")
plt.tight_layout()
plt.savefig("Age_Rating.png")
plt.show()


cpy=data["year"].value_counts()

plt.plot(cpy.index,cpy.values,color="blue")

plt.title("Number of Movies Releasing Year")
plt.xlabel("Year")
plt.grid()
plt.ylabel("Movies")
plt.tight_layout()
plt.legend()
plt.savefig("Year.png")
plt.show()


copy=data["running_time"].value_counts()
plt.bar(copy.index,copy.values,color=["skyblue","orange"])
plt.title("Total Year")
plt.tight_layout()

plt.xlabel("Running Time")
plt.ylabel("Movies")
plt.savefig("Running time.png")
plt.show()


ount = data["genre"].value_counts()
#print(count)
plt.bar(ount.index,ount.values,color=["skyblue","orange"])

plt.title("Types of Movies")
plt.xlabel("Type")
plt.ylabel("Movie-Types")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("Movies_Type.png")
plt.show()