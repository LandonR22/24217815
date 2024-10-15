# Task 1: User Input/System Output
    # Must ask user to input their current location (British National Grid)
    
def get_coordinates(easting, northing):
    
    # Set limits for location of user
    east_min, north_min = 430000, 80000
    east_max, north_max = 465000, 95000
    
    # Parameters to ensure user is inside the box
    return east_min <= easting <= east_max and north_min <= northing <= north_max


def main():

# Start loop
    check_coordinates = True

    while check_coordinates: 
        easting = int(input('Enter your current easting coordinate: '))
        northing = int(input('Enter your current northing coordinate: '))

# Validate coordinates
        check_coordinates = get_coordinates(easting, northing)

        if check_coordinates:
            print('You are in the correct area.')
        else:
            print('You are not in the correct area.')
            
    
if __name__ == "__main__":
    main()
