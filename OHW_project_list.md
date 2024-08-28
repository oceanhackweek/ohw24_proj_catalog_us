# OHW Project Datasets of the Past

## OHW23 Projects
List of OHW23 projects and datasets used:

1. The [Oil Spill Monitoring](https://github.com/oceanhackweek/ohw23_proj_oil) team used images taken from a [SAR-2000](https://space.oscar.wmo.int/instruments/view/sar_2000) imaging sensor on the second [COSMO-SkyMed](https://earth.esa.int/eogateway/missions/cosmo-skymed) satellite called [CSKS2](https://space.oscar.wmo.int/satellites/view/csk_2).
2. The [Marine SDM](https://github.com/oceanhackweek/tutorials_marine_sdm) team produced a beautiful tutorial accessing OBIS via `robis` and environmental data via the `SMDpredictor` R package. Their tutorial is already so good that we should highlight it on the website, IMO.
 https://oceanhackweek.org/tutorials_marine_sdm/ 
3. [Inertial oscillations in the marginal ice zone](https://github.com/oceanhackweek/ohw23_proj_sea_ice_oscillations): used data from the [VIIRS instruments](https://lpdaac.usgs.gov/data/get-started-data/collection-overview/missions/s-npp-nasa-viirs-overview/) installed on the [Joint Polar Satellite System](https://www.nesdis.noaa.gov/our-satellites/currently-flying/joint-polar-satellite-system). Cloud-based data from the Suomi-NPP and JPSS-1/NOAA-20 satellites was accessed from [EarthDataSearch](https://search.earthdata.nasa.gov/search).
4. [Machine learning for Argo Data QC](https://github.com/oceanhackweek/ohw23_proj_argo_ml): data accessed via argopy.
5. [Benthic habitat mapping](https://github.com/oceanhackweek/ohw23-proj-habitatmapping): used some kind of geodata but I can't tell from where at a glance. [This notebook](https://github.com/oceanhackweek/ohw23-proj-habitatmapping/blob/main/Download%20data.ipynb) seems to be for downloading data
6. [Mooring processing and data page (“fancy moorings”)](https://github.com/oceanhackweek/ohw23_proj_fancymoorings): used data from [CIOOS Moorings](https://catalogue.cioospacific.ca/dataset/ca-cioos_82656721-88e6-4543-90f1-edc35c0f42c9) and [NANOOS Moorings](https://nwem.apl.washington.edu/erddap/index.html). They also made their own [website](https://oceanhackweek.org/ohw23_proj_fancymoorings/). 
7. [SST spatial distribution prediction using machine learning](https://github.com/oceanhackweek/ohw23_proj_sst): used MUR Satellite Data (2002-present) from an S3 bucket, and [NASA website](https://podaac.jpl.nasa.gov/dataset/MUR-JPL-L4-GLOB-v4.1)
8. [Passive acoustics monitoring](https://github.com/oceanhackweek/ohw23-proj-pamproject): used https://registry.opendata.aws/pacific-sound/ and imos-data/IMOS/ANMN/Acoustic/ (maybe [this one](https://catalogue-imos.aodn.org.au/geonetwork/srv/eng/catalog.search#/metadata/e850651b-d65d-495b-8182-5dde35919616)?)
9. [Direct geo referencing drone images](https://github.com/oceanhackweek/ohw23_proj_drone_georef): Drone survey carried out in 14 February (CSIRO Kensington)
10. [Variability of the suppression of South Australian upwelling](https://github.com/oceanhackweek/ohw23_proj_SAupwelling): IMOS bucket for SA coastal mooring data: http://imos-data.s3-website-ap-southeast-2.amazonaws.com/?prefix=IMOS/ANMN/SA/
IMOS bucket for SA NRS station data: http://imos-data.s3-website-ap-southeast-2.amazonaws.com/?prefix=IMOS/ANMN/NRS/NRSKAI/
SA coastal moorings and NRS station technical summary, where you can find the code names for active and deactivated moorings which are important to download the data from the IMOS bucket: https://imos.org.au/facilities/nationalmooringnetwork/samoorings
AODN portal: https://portal.aodn.org.au/search 
11. [Bioinformatic pipelines for standardized output](https://github.com/oceanhackweek/ohw23_proj_amplicon): Created a custom reference database using only fish species from the OBITools reference database (see the [Wolves tutorial](https://pythonhosted.org/OBITools/wolves.html) for more information).

## OHW22 Projects

1. [Arctic observing data access and visualization](https://github.com/oceanhackweek/ohw22-proj-arcticdata): used data from the [Distributed Biological Observatory (DBO)](https://www.pmel.noaa.gov/dbo/), [Arctic data](https://arcticdata.io/catalog/data),
[EcoFOCI](https://www.ecofoci.noaa.gov/data-links), [Arctic Flux data from Saildrones](https://data.pmel.noaa.gov/pmel/erddap/search/index.html?page=1&itemsPerPage=1000&searchFor=Arctic+Flux+Data), and the [International Arctic Buoy Programme (IABP) Data](https://iabp.apl.uw.edu/). They might have used even more beyond this, and have details on their GH README.

1. [Kerchunk! Bless you](https://github.com/oceanhackweek/ohw22-proj-kerchunk): used data from [Himawari 8 Sea Surface Temperature](https://registry.opendata.aws/noaa-himawari/).

1. [Mapping eddy flow structures using GCM-Filters](https://github.com/oceanhackweek/ohw22-proj-gcmfilters): used an NCAR dataset from the [Pangeo Catalog](https://catalog.pangeo.io/).

1. [Ocean Database for South Atlantic](https://github.com/oceanhackweek/ohw22-proj_SA_ocean_db): used data from the [Brazilian National Buoy Program - PNBOIA](https://www.marinha.mil.br/chm/dados-do-goos-brasil/pnboia). 

1. [Lightweight ocean passive acoustic data query](https://github.com/oceanhackweek/ohw22-proj-passive-acoustics-data-query): used data from Ocean Observatories Initative (OOI), National Centers for Environmental Information (NCEI), and Ocean Networks Canada (OCN)

1. [XYZT - Streamline extraction of data](https://github.com/oceanhackweek/ohw22-proj-xyzt): used data from [Copernicus](https://marine.copernicus.eu/) and the [EU MSFD](https://research-and-innovation.ec.europa.eu/research-area/environment/oceans-and-seas/eu-marine-strategy-framework-directive_en).

1. [ENSO prediction using Deep Learning](https://github.com/oceanhackweek/ohw22-proj-ENSO_Prediction): used coarsened CESM2 Large Ensemble members (SST fields) from 1° to 3° resolution and used the first 10 of 100 CESM2 LE members. Maybe from a CMIP catalog, hard to tell.

1. Radar Doppler Spectra imaging data quality control: missing gH repository for this project, need to search [OHW repo list](https://github.com/orgs/oceanhackweek/repositories).

1. [Assessing ocean drivers of coastal physical processes (in Spanish)](https://github.com/oceanhackweek/ohw22-proj-oleaje-costeros): used buoy ADCP data and satellite data (links needed).

1. [Nutrient Profile Clustering](https://github.com/oceanhackweek/ohw22-proj-clusters-nutrients) - only has 1 commit, looks like it was never finished.

1. [Unsupervised classification of Flow Cytometry TS data](https://github.com/oceanhackweek/ohw22-proj-flow-cytometry): used data from the [SeaFlow](https://seaflow.netlify.app/) flow cytometer on the [HOT-297](https://hahana.soest.hawaii.edu/hot/) cruise at Station ALOHA in the North Pacific.

1. [SiMCosta Buoy](https://github.com/oceanhackweek/ohw22-proj-simcosta): used [SiMCosta Datasets from Buoy SC-1](https://simcosta.furg.br/home)

1. [Biofouled](https://github.com/oceanhackweek/ohw22-proj-biofouled): used oxygen data from OOI moorigs accessible. 

1. [Langrangian dispersion](https://github.com/oceanhackweek/ohw22-proj-lagrange_points)

1. [Extreme events / anomaly detection](https://github.com/oceanhackweek/ohw22-proj-Extreme_event)

1. [Seismic Wave Speed From an Alaska Earthquake](https://github.com/oceanhackweek/ohw22-proj-earthquakes)

1. [Evaluation of biological indicators in the Galapagos (in Spanish)](https://github.com/oceanhackweek/ohw22-proj-biodiversity-indicators)

1. [The ultimate collection of plotting example notebooks](https://github.com/oceanhackweek/ohw22-proj-plot_this_and_that)

1. [FrontFinder](https://github.com/oceanhackweek/ohw22-proj-front-finder)

1. [Project Video Data Processing](https://github.com/oceanhackweek/ohw22-proj-video-data-processing)