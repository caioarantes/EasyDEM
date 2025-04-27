dem_datasets_pt = {"Copernicus Global Digital Elevation Model (GLO-30)": {
        "ID": "COPERNICUS/DEM/GLO30",
        "Resolution": [30],
        "Coverage": "Global",
        "Description": "A Digital Surface Model (DSM) that includes Earth's surface features such as buildings, infrastructure, and vegetation, derived from the WorldDEM product.",
        "Info": "<b>Copernicus GLO-30</b> <br>"
                "<b>ID:</b> COPERNICUS/DEM/GLO30 <br>"
                "<b>Resolution:</b> 30 meters <br>"
                "<b>Coverage:</b> Global <br>"
                "The Copernicus DEM is a Digital Surface Model (DSM) which represents the surface of the Earth including buildings, infrastructure and vegetation. This DEM is derived from an edited DSM named WorldDEM&trade, i.e. flattening of water bodies and consistent flow of rivers has been included. Editing of shore- and coastlines, special features such as airports and implausible terrain structures has also been applied. The WorldDEM product is based on the radar satellite data acquired during the TanDEM-X Mission, which is funded by a Public Private Partnership between the German State, represented by the German Aerospace Centre (DLR) and Airbus Defence and Space. More details are available in the dataset documentation. Earth Engine asset has been ingested from the DGED files."
                "(<a href='https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_DEM_GLO30/'>Source</a>)"
    },
    "NASADEM": {
        "ID": "NASA/NASADEM_HGT/001",
        "Resolution": [30],
        "Coverage": "Global",
        "Description": "A refined reprocessing of SRTM data, incorporating auxiliary datasets for improved accuracy and void reduction.",
        "Info": "<b>NASADEM</b> <br>"
                "<b>ID:</b> NASA/NASADEM_HGT/001 <br>"
                "<b>Resolution:</b> 30 meters <br>"
                "<b>Coverage:</b> Global <br>"
                "NASADEM is a reprocessing of SRTM data, with improved accuracy by incorporating auxiliary data from ASTER GDEM, ICESat GLAS, and PRISM datasets. The most significant processing improvements involve void reduction through improved phase unwrapping and using ICESat GLAS data for control."
              "(<a href='https://developers.google.com/earth-engine/datasets/catalog/NASA_NASADEM_HGT_001/'>Source</a>)"
    },
    "ASTER Global Digital Elevation Model (GDEM)": {
        "ID": "NASA/ASTER_GED/AG100_003",
        "Resolution": [100],
        "Coverage": "Global",
        "Description": "The Advanced Spaceborne Thermal Emission and Reflection Radiometer Global Emissivity Database (ASTER-GED) is a comprehensive product developed by NASA's JPL and Caltech. It includes elevation data, mean emissivity, LST, NDVI, and standard deviations for ASTER Thermal Infrared bands.",
        "Info": "<b>ASTER GDEM</b> <br>"
                "<b>ID:</b> NASA/ASTER_GED/AG100_003 <br>"
                "<b>Resolution:</b> 100 meters <br>"
                "<b>Coverage:</b> Global <br>"
                "The Advanced Spaceborne Thermal Emission and Reflection Radiometer Global Emissivity Database (ASTER-GED) was developed by the National Aeronautics and Space Administration's (NASA) Jet Propulsion Laboratory (JPL), California Institute of Technology. This product includes the mean emissivity and standard deviation for all 5 ASTER Thermal Infrared bands, mean land surface temperature (LST) and standard deviation, a re-sampled ASTER GDEM, land-water mask, mean Normalized Difference Vegetation Index (NDVI) and standard deviation, and observation count. ASTER-GED land surface temperature and emissivity (LST&E) are generated using the ASTER Temperature Emissivity Separation (TES) algorithm in combination with a Water Vapor Scaling (WVS) atmospheric correction method using MODIS MOD07 atmospheric profiles and the MODTRAN 5.2 radiative transfer model. This product was derived from clear-sky pixels for all available ASTER data (2000-2008)."
                "(<a href='https://developers.google.com/earth-engine/datasets/catalog/NASA_ASTER_GED_AG100_003/'>Source</a>)"
    },
    "JAXA ALOS Global Digital Surface Model (AW3D30)": {
        "ID": "JAXA/ALOS/AW3D30/V3_2",
        "Resolution": [30],
        "Coverage": "Global",
        "Description": "A global digital surface model (DSM) dataset at ~30-meter resolution, derived from the high-resolution (5-meter) World 3D Topographic Data.",
        "Info": "<b>JAXA ALOS DSM (AW3D30)</b> <br>"
                "<b>ID:</b> JAXA/ALOS/AW3D30/V3_2 <br>"
                "<b>Resolution:</b> 30 meters <br>"
                "<b>Coverage:</b> Global <br>"
                "ALOS World 3D - 30m (AW3D30) is a global digital surface model (DSM) dataset with a horizontal resolution of approximately 30 meters (1 arcsec mesh). The dataset is based on the DSM dataset (5-meter mesh version) of the World 3D Topographic Data. More details are available in the dataset documentation."
                "(<a href='https://developers.google.com/earth-engine/datasets/catalog/JAXA_ALOS_AW3D30_V3_2/'>Source</a>)"
    },
    "GMTED2010 (Global Multi-resolution Terrain Elevation Data 2010)": {
        "ID": "USGS/GMTED2010_FULL",
        "Resolution": [250, 500, 1000],
        "Coverage": "Global",
        "Description": "A global elevation dataset derived from multiple sources, replacing the GTOPO30 Elevation Model, with coverage at multiple resolutions.",
        "Info": "<b>GMTED2010</b> <br>"
                "<b>ID:</b> USGS/GMTED2010_FULL <br>"
                "<b>Resolutions:</b> 250, 500, and 1000 meters <br>"
                "<b>Coverage:</b> Global <br>"
                "The Global Multi-resolution Terrain Elevation Data 2010 (GMTED2010) dataset contains elevation data for the globe collected from various sources at 7.5 arc-seconds resolution. More details are available in the dataset report."
                "(<a href='https://developers.google.com/earth-engine/datasets/catalog/USGS_GMTED2010_FULL/'>Source</a>)"
    },
    "SRTM Digital Elevation Data Version 4": {
        "ID": "CGIAR/SRTM90_V4",
        "Resolution": [90],
        "Coverage": "Near-global (60°N to 56°S)",
        "Description": "A void-filled version of the Shuttle Radar Topography Mission (SRTM) 90-meter resolution data.",
        "Info": "<b>SRTM Digital Elevation Data V4</b> <br>"
                "<b>ID:</b> CGIAR/SRTM90_V4 <br>"
                "<b>Resolution:</b> ~90 meters <br>"
                "<b>Coverage:</b> Near-global (between 60°N and 56°S latitude) <br>"
                "The Shuttle Radar Topography Mission (SRTM) digital elevation dataset was originally produced to provide consistent, high-quality elevation data at near global scope. This version of the SRTM digital elevation data has been processed to fill data voids, and to facilitate its ease of use."                
                "(<a href='https://developers.google.com/earth-engine/datasets/catalog/CGIAR_SRTM90_V4/'>Source</a>)"
    },
    "NASA SRTM Digital Elevation 30m": {
        "ID": "USGS/SRTMGL1_003",
        "Resolution": [30],
        "Coverage": "Near-global (60°N to 56°S)",
        "Description": "This dataset provides the higher 30-meter resolution SRTM data. It's a foundational dataset for many regional and global studies requiring detailed elevation information.",
        "Info": "<b>NASA SRTM Digital Elevation 30m</b> <br>"
                "<b>ID:</b> USGS/SRTMGL1_003 <br>"
                "<b>Resolution:</b> ~30 meters <br>"
                "<b>Coverage:</b> Near-global (between 60°N and 56°S latitude) <br>"
                "The Shuttle Radar Topography Mission (SRTM, see Farr et al. 2007) digital elevation data is an international research effort that obtained digital elevation models on a near-global scale. This SRTM V3 product (SRTM Plus) is provided by NASA JPL at a resolution of 1 arc-second (approximately 30m). This dataset has undergone a void-filling process using open-source data (ASTER GDEM2, GMTED2010, and NED), as opposed to other versions that contain voids or have been void-filled with commercial sources. For more information on the different versions see the SRTM Quick Guide."                
                "(<a href='https://developers.google.com/earth-engine/datasets/catalog/USGS_SRTMGL1_003/'>Source</a>)"
    }
}
