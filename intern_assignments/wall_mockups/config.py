
import os
#import envrioment

Base_Path = os.environ.get("Mockups_Scraping", "C:/VS_Code_folder/Scraping_for_mockups/Image_scraping")

Driver_Path = os.environ.get(Base_Path, os.environ)
