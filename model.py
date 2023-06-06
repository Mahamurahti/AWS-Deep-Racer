def reward_function(params):
    '''
    Utilize waypoints for track and distance from center line
    '''
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    closest_waypoints = params['closest_waypoints']
    speed = params['speed']
    all_wheels_on_track = params['all_wheels_on_track']
    
    # Starting reward
    reward = 10
    
    # If all wheels on track, good
    if all_wheels_on_track:
        reward += 10
    else:
        reward -= 10
    
    # Track markers from center line to side of track
    marker_1 = 0.2 * track_width
    marker_2 = 0.3 * track_width
    marker_3 = 0.4 * track_width
    marker_4 = 0.5 * track_width
    
    # The closer to center the better
    if distance_from_center <= marker_1:
        reward += 10
    elif distance_from_center <= marker_2:
        reward += 6
    elif distance_from_center <= marker_3:
        reward += 2
    elif distance_from_center <= marker_4:
        reward -= 1
    else:
        reward -= 8
    
    high_speed = 3.00
    slow_speed = 1.10
    unacceptable_speed = 0.90

    # Straight lines we go fast
    fast_waypoints = [1, 2, 3, 4, 5, 6, 13, 14, 15, 17, 18, 20, 21, 25, 26, 27, 28, 30]
    # Coming up to turn we slow down
    medium_waypoints = [7, 8, 12, 16, 19, 22]
    # In turn we go slowww
    slow_waypoints = [9, 10, 11, 23, 24, 29]
    
    if closest_waypoints[1] in fast_waypoints:
        if speed >= high_speed:
            reward += 10
        else:
            reward -= 10
    if closest_waypoints[1] in medium_waypoints:
        if speed <= high_speed and speed >= slow_speed:
            reward += 10
        else:
            reward -= 10
    if closest_waypoints[1] in slow_waypoints:
        if speed <= slow_speed:
            reward += 10
        else:
            reward -= 10
    
    # We don't go too slow
    if speed <= unacceptable_speed: 
        reward -= 7
        
    return float(reward)