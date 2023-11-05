# Weather API Exercise

## Setup

Documentation about the API and the format of the responses is available at
[http://www.7timer.info/doc.php](http://www.7timer.info/doc.php).  You will
need to reference this material as you complete the assignment.  

Just like the videos, we will be adding to the weather API example! You should
aim to complete all the following parts.  But before you dive into
completing the tasks below, spend some time reading the code to familiarize
yourself with what is provided.  

## Part 1: Add a New City

Add a new city. You can usually find the coordinates for a city on the wikipedia
page for a city, then look on the panel on the right side for "coordinates".

Once you have the coordinates, format them the same way that the existing
entries are written. Note that "S" or "south" is negative and "N" or "north" is
positive. Add the new city to the list in `map_city_to_coords` and try it.

## Part 2: Wind Direction

Add a feature to the program, so that it shows the wind direction alongside the
temperature. Show the wind direction in a descriptive way, for example display
"from the southwest" instead of "SW" and "from the north" instead of "N".

Also, you will have to reference the API documentation in order to interpret
what the values contained in the API response actually mean.  

Once completed, the output displaying the weather data for a particular hour
should look like the following:

```text
The temperature is 10 and the wind is approaching at 3.4-8.0m/s (moderate) from the south
```

Hint: Open the `api_output.json` file and look for `wind`. Remember that a
dictionary can contain other dictionaries. It's sometimes easier to get the
data in two steps.

## Part 3: Avoid Saving to File

Currently the program saves the json information to a file, and then reads the
information back in from the file. This is unnecessary - isn't there a way to
get the information without needing to save to a file first? Modify the program
so that it doesn't save to a file.

Hints:

- Right now the `get_api_results` function does not need to return anything,
  but you can change it so that it will `return` a value at the end.
- The data type returned by the `decode()` method is a string.
- And remember that there is a function `json.loads()` that loads from a string 
  instead of a file.
