
# SQLAlchemy One to Many Lab Continued

## Objectives

1.  Create multiple "has many"/"belongs to" relationships with SQLAlchemy
2.  Add data to the database for each table and ensure that the data is properly related to other tables
3.  Query the database containing the "has many"/"belongs to" relationships

## Sports, Players, Teams, Cities
Okay, so, we have just finished creating our first has many / belongs to relationship. Now lets take it a step further and add in another layer, since, domains adn relationships will generally be bigger than just two tables. Let's look at sports teams. One sports team will have many players. But what does our sports team belong to? Specifically, what is a sports team affiliated with that other sports teams may also be affiliated with? A City? That's right! But wait! Can't a team also belong to a specific sport? That's also right! This is analagous to a song belonging to a particular genre, but that can get a bit tricky when we get into songs that are chill electro pop funk -- that's too many genres!!

Back to our sports. Let's build these models out in our **models.py** file. The models below list the attributes each should contain as well as its relationship to other models. Our job is to take this information and create the SQLAlchemy tables.

> **Note:** Because we are going to leverage the relationships between these tables, there is no need for us duplicate information accross tables. For example, players do not need to be instantiated with the name of the team they play for as long as they are related with that team. However, we will want to be able to query a player instance for their team. Be sure to create your tables so that they provide this functionality for all relationships.

* **Players**:
    - Name
    - Number (if applicable)
    - Height
    - Weight
    - *Belongs to a team*
    
* **Teams**:
    - Name
    - *Belongs to a city*    
    - *Belongs to a sport*
    - *Has many players*    

* **Sports**:
    - Name
    - *Has many teams*    

* **City**:
    - Name
    - State
    - *Has many teams*    


## Instructions

1. In the **models.py** file, create the SQLAlchemy schema and for each of our models.
2. The two cities we will be working with are New York, New York, and Los Angeles, California
3. The two sports we will be working with are Basketball and Baseball
4. We have provided for us csv files containing the roster data for the LA Lakers, LA Dodgers, NY Knicks, and NY Yankees. Read these files using pandas to turn this data into objects we can use to populate our tables. Remember to also create the appropriate relationships as we create the class instance objects and commit them to the tables in our data base.
5. Once the data has been created and our relationships are set up, we can go ahead an start working on our queries. Open the **queries.py** file and fill out the functions with the necessary code to meet the deliverables.

