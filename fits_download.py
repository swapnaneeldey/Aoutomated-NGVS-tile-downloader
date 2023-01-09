import os
import requests
import time

# Set the base URL for the CADC download page
base_url = 'https://ws.cadc-ccda.hia-iha.nrc-cnrc.gc.ca/raven/files/cadc:CFHTSG/'

# Get the input from the user
for tile_id in []:##"NGVS+0-7", "NGVS-1-7","NGVS-2-7", "NGVS+1-6", "NGVS+0-6", "NGVS-1-6", "NGVS-2-6", "NGVS-3-6", "NGVS+5+2"
    start_time_one_tile = time.time()
    print("tile_id", tile_id)
    tile_name = tile_id.replace('-', 'm').replace('+', 'p')
 # Set the base destination directory
    base_destination_dir = '/path/to/code/tiles'

    # Create a new directory with the name of the tile ID in the base destination directory
    destination_dir = os.path.join(base_destination_dir, tile_name)
    os.makedirs(destination_dir, exist_ok=True)
    for file_type in []: ## "filter name egs. G, U, I2, Z etc.
        start_time_one_file = time.time()
    # Construct the full URL by concatenating the base URL, the tile ID, and the file type
        url = base_url + tile_id + '.' + file_type + '.fits'

    # Send a GET request to the download URL to download the file
        response = requests.get(url)
       # If the request was successful, save the file to the specified destination directory
        if response.status_code == 200:


                # Join the destination directory with the file name
            file_path = os.path.join(destination_dir, tile_id + '.' + file_type + '.fits')

            with open(file_path, 'wb') as f:
                f.write(response.content)
            print('Successfully downloaded file to', file_path)
        else:
            print('Failed to download file from URL:', url)
        end_time_one_file = time.time()
        print(tile_id + '.' + file_type + '.fits', "time taken:", 
              end_time_one_file - start_time_one_file)
    end_time_one_tile = time.time()
    print("Time_taken_one_tile =", end_time_one_tile - start_time_one_tile, "sec") 
