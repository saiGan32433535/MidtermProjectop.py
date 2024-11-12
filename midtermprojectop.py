
import pandas as pd
#Kirtitej Gandham Midterm Project


# reads and processes the CSV file that contains all of imdb's tv show date which includes a large variety of diffrent tv shows
tv_show = pd.read_csv('imdb_tvshows.csv')

#This fucntion is used to recommendtv shows to the user based on the genre they prefer

def my_recommended_shows(genre):

  # This basicaly serves as the filter for the dataframe. Based on the user input on genre, it will filter out the other genre's and also filter out any ratings lower than what was stated
    if genre == "Action":
        recommend = tv_show[(tv_show['Genres'].str.contains("Action")) & (tv_show['Rating'] > 8.8)]
    elif genre == "Drama":
        recommend = tv_show[(tv_show['Genres'].str.contains("Drama")) & (tv_show['Rating'] > 8.5)]
    elif genre == "Fantasy":
        recommend = tv_show[(tv_show['Genres'].str.contains("Fantasy")) & (tv_show['Rating'] > 8.5)]
    elif genre == "Adventure":
        recommend = tv_show[(tv_show['Genres'].str.contains("Adventure")) & (tv_show['Rating'] > 8.5)]
    elif genre == "Thriller":
        recommend = tv_show[(tv_show['Genres'].str.contains("Thriller")) & (tv_show['Rating'] > 8.5)]
    elif genre == "Sci-Fi":
        recommend = tv_show[(tv_show['Genres'].str.contains("Sci-Fi")) & (tv_show['Rating'] > 8.5)]
    elif genre == "Mystery":
        recommend = tv_show[(tv_show['Genres'].str.contains("Mystery")) & (tv_show['Rating'] > 8.5)]
    elif genre == "Crime":
        recommend = tv_show[(tv_show['Genres'].str.contains("Crime")) & (tv_show['Rating'] > 8.5)]
    elif genre == "Romance":
        recommend = tv_show[(tv_show['Genres'].str.contains("Romance")) & (tv_show['Rating'] > 8.5)]
    else:
        print("Sorry I can't give any recomendations.")

        #if user prints any other genre not stated it will print this out and an error will run. Note: must input exactly as my code asks. inputs must starts with uppercase letters or it will not run. example you must type Action instead of action


#returns the show tittles from the dataframe that has been filtered
    return recommend['Title']

# asks for user input on the genre
genre = input("What types of shows would you like me to recommend? Choose from some of my favorite genres- Action, Drama, Comedy, Fantasy, Adventure, Thriller, Sci-Fi, Mystery, Crime, and Romance: ").strip()

#This calls the function my_recommended_shows(genre)
recommended_shows = my_recommended_shows(genre)


print("My Recommended Shows:")
print(recommended_shows)
# shows all the recommended shows from the specific genre with higher ratings

