def rank_movies_by_popularity():
    return '''
        SELECT title,
        RANK() over(partition by genres order by popularity desc) as ranking
        FROM movies_data
        LIMIT 100;
    '''

