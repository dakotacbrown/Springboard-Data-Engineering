def weekday_name(day_of_week):
    days = ["none", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    selection = " "
    if day_of_week in range(1, 8):
        selection = days(day_of_week)
    else:
        selection = days(0)

    return selection

    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """