# Searchable Table of Datasets


<script>
function myFunction() {
  var input, filter, table, tr, td, i, j, txtValue;
  input = document.getElementById("searchInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("projectTable");
  tr = table.getElementsByTagName("tr");
  for (i = 1; i < tr.length; i++) { // Start from 1 to skip the header row
    tr[i].style.display = "none"; // Hide all rows initially
    td = tr[i].getElementsByTagName("td");
    for (j = 0; j < td.length; j++) { // Loop through all cells in the row
      if (td[j]) {
        txtValue = td[j].textContent || td[j].innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = ""; // Show row if any cell matches
          break; // Stop checking once a match is found
        }
      }
    }
  }
}
</script>



<style>
input[type="text"] {
  width: 100%; /* Full width of the container */
  padding: 10px; /* Match the padding of table cells */
  margin-bottom: 10px; /* Space below the search bar before the table */
  border: 1px solid black; /* Match the border of the table */
  box-sizing: border-box; /* Ensures padding and border are included in the width */
  font-family: Arial, sans-serif; /* Match the font */
  font-size: 14px; /* Match the font size */
}


#projectTable {
  width: 100%;
  border-collapse: collapse;
}

#projectTable th, #projectTable td {
  border: 1px solid black;
  padding: 10px;
  text-align: left;
}

#projectTable th {
  background-color: #f2f2f2;
}
</style>

<table id="projectTable">
<input type="text" id="searchInput" onkeyup="myFunction()" placeholder="Search for projects or datasets..." title="Type in a name">
  <thead>
    <tr>
    <!-- Table headings go here: -->
      <th>Year</th>
      <th>Project</th>
      <th>Datasets</th>
    </tr>
  </thead>
  <tbody>
  <!-- Each table row will look like this: -->
    <tr>
        <td>2023</td>
      <td><a href="https://github.com/oceanhackweek/ohw23_proj_oil" target="_blank">Oil Spill Monitoring</a></td>
      <td>
        <a href="https://space.oscar.wmo.int/instruments/view/sar_2000" target="_blank">SAR-2000 imaging sensor</a>,
        <a href="https://earth.esa.int/eogateway/missions/cosmo-skymed" target="_blank">COSMO-SkyMed satellite</a>,
        <a href="https://space.oscar.wmo.int/satellites/view/csk_2" target="_blank">CSKS2</a>
      </td>
    </tr>
    <tr>
        <td>2023</td>
      <td><a href="https://github.com/oceanhackweek/tutorials_marine_sdm" target="_blank">Marine Species Distribution Modeling (SDM)</a></td>
      <td>
        <a href="https://oceanhackweek.org/tutorials_marine_sdm/" target="_blank">OBIS via robis</a>,
        <a href="https://oceanhackweek.org/tutorials_marine_sdm/" target="_blank">SMDpredictor R package</a>
      </td>
    </tr>
    <tr>
      <td>2023</td>
      <td><a href="https://github.com/oceanhackweek/ohw23_proj_sea_ice_oscillations" target="_blank">Inertial oscillations in the marginal ice zone</a></td>
      <td>
        <a href="https://lpdaac.usgs.gov/data/get-started-data/collection-overview/missions/s-npp-nasa-viirs-overview/" target="_blank">VIIRS instruments</a>,
        <a href="https://www.nesdis.noaa.gov/our-satellites/currently-flying/joint-polar-satellite-system" target="_blank">Joint Polar Satellite System</a>,
        <a href="https://search.earthdata.nasa.gov/search" target="_blank">EarthDataSearch</a>
      </td>
    </tr>
    <tr>
      <td>2023</td>
      <td><a href="https://github.com/oceanhackweek/ohw23_proj_argo_ml" target="_blank">Machine learning for Argo Data QC</a></td>
      <td><a href="https://argopy.readthedocs.io/" target="_blank">Argo data accessed via argopy</a></td>
    </tr>
    <tr>
      <td>2023</td>
      <td><a href="https://github.com/oceanhackweek/ohw23-proj-habitatmapping" target="_blank">Benthic habitat mapping</a></td>
      <td>
        <a href="https://github.com/oceanhackweek/ohw23-proj-habitatmapping/blob/main/Download%20data.ipynb" target="_blank">Geodata</a>
      </td>
    </tr>
    <tr>
      <td>2023</td>
      <td><a href="https://github.com/oceanhackweek/ohw23_proj_fancymoorings" target="_blank">Mooring processing and data page (“fancy moorings”)</a></td>
      <td>
        <a href="https://catalogue.cioospacific.ca/dataset/ca-cioos_82656721-88e6-4543-90f1-edc35c0f42c9" target="_blank">CIOOS Moorings</a>,
        <a href="https://nwem.apl.washington.edu/erddap/index.html" target="_blank">NANOOS Moorings</a>,
        <a href="https://oceanhackweek.org/ohw23_proj_fancymoorings/" target="_blank">Project website</a>
      </td>
    </tr>
    <tr>
      <td>2023</td>
      <td><a href="https://github.com/oceanhackweek/ohw23_proj_sst" target="_blank">SST spatial distribution prediction using machine learning</a></td>
      <td>
        <a href="https://podaac.jpl.nasa.gov/dataset/MUR-JPL-L4-GLOB-v4.1" target="_blank">MUR Satellite Data</a>,
        <a href="https://podaac.jpl.nasa.gov/dataset/MUR-JPL-L4-GLOB-v4.1" target="_blank">NASA website</a>
      </td>
    </tr>
    <tr>
      <td>2023</td>
      <td><a href="https://github.com/oceanhackweek/ohw23-proj-pamproject" target="_blank">Passive acoustics monitoring</a></td>
      <td>
        <a href="https://registry.opendata.aws/pacific-sound/" target="_blank">Pacific Sound</a>,
        <a href="https://catalogue-imos.aodn.org.au/geonetwork/srv/eng/catalog.search#/metadata/e850651b-d65d-495b-8182-5dde35919616" target="_blank">IMOS Acoustic Data</a>
      </td>
    </tr>
    <tr>
      <td>2023</td>
      <td><a href="https://github.com/oceanhackweek/ohw23_proj_drone_georef" target="_blank">Direct geo referencing drone images</a></td>
      <td>Drone survey carried out in 14 February (CSIRO Kensington)</td>
    </tr>
    <tr>
      <td>2023</td>
      <td><a href="https://github.com/oceanhackweek/ohw23_proj_SAupwelling" target="_blank">Variability of the suppression of South Australian upwelling</a></td>
      <td>
        <a href="http://imos-data.s3-website-ap-southeast-2.amazonaws.com/?prefix=IMOS/ANMN/SA/" target="_blank">SA coastal mooring data</a>,
        <a href="http://imos-data.s3-website-ap-southeast-2.amazonaws.com/?prefix=IMOS/ANMN/NRS/NRSKAI/" target="_blank">SA NRS station data</a>,
        <a href="https://imos.org.au/facilities/nationalmooringnetwork/samoorings" target="_blank">SA moorings summary</a>,
        <a href="https://portal.aodn.org.au/search" target="_blank">AODN portal</a>
      </td>
    </tr>
    <tr>
      <td>2023</td>
      <td><a href="https://github.com/oceanhackweek/ohw23_proj_amplicon" target="_blank">Bioinformatic pipelines for standardized output</a></td>
      <td>
        <a href="https://pythonhosted.org/OBITools/wolves.html" target="_blank">OBITools reference database</a>
      </td>
    </tr>
    <tr>
      <td>2022</td>
      <td><a href="https://github.com/oceanhackweek/ohw22-proj-arcticdata" target="_blank">Arctic observing data access and visualization</a></td>
      <td>
        <a href="https://www.pmel.noaa.gov/dbo/" target="_blank">Distributed Biological Observatory (DBO)</a>,
        <a href="https://arcticdata.io/catalog/data" target="_blank">Arctic data</a>,
        <a href="https://www.ecofoci.noaa.gov/data-links" target="_blank">EcoFOCI</a>,
        <a href="https://data.pmel.noaa.gov/pmel/erddap/search/index.html?page=1&itemsPerPage=1000&searchFor=Arctic+Flux+Data" target="_blank">Arctic Flux data from Saildrones</a>,
        <a href="https://iabp.apl.uw.edu/" target="_blank">International Arctic Buoy Programme (IABP) Data</a>
      </td>
    </tr>
    <tr>
      <td>2022</td>
      <td><a href="https://github.com/oceanhackweek/ohw22-proj-kerchunk" target="_blank">Kerchunk! Bless you</a></td>
      <td>
        <a href="https://registry.opendata.aws/noaa-himawari/" target="_blank">Himawari 8 Sea Surface Temperature (SST)</a>
      </td>
    </tr>
    <tr>
      <td>2022</td>
      <td><a href="https://github.com/oceanhackweek/ohw22-proj-gcmfilters" target="_blank">Mapping eddy flow structures using GCM-Filters</a></td>
      <td>
        NCAR dataset from the <a href="https://catalog.pangeo.io/" target="_blank">Pangeo Catalog</a>
      </td>
    </tr>
    <tr>
      <td>2022</td>
      <td><a href="https://github.com/oceanhackweek/ohw22-proj_SA_ocean_db" target="_blank">Ocean Database for South Atlantic</a></td>
      <td>
        <a href="https://www.marinha.mil.br/chm/dados-do-goos-brasil/pnboia" target="_blank">Brazilian National Buoy Program - PNBOIA.</a>
      </td>
    </tr>
    <tr>
      <td>2022</td>
      <td><a href="https://github.com/oceanhackweek/ohw22-proj-passive-acoustics-data-query" target="_blank">Lightweight ocean passive acoustic data query</a></td>
      <td>
      Ocean Observatories Initiative (OOI), National Centers for Environmental Information (NCEI), and Ocean Networks Canada (OCN) (links needed)
        <!-- <a href="DATASET LINK" target="_blank">DATASET NAME</a> -->
      </td>
    </tr>
    <tr>
      <td>2022</td>
      <td><a href="https://github.com/oceanhackweek/ohw22-proj-xyzt" target="_blank">XYZT - Streamline extraction of data</a></td>
      <td>
        <a href="https://marine.copernicus.eu/" target="_blank">Copernicus</a>,
        <a href="https://research-and-innovation.ec.europa.eu/research-area/environment/oceans-and-seas/eu-marine-strategy-framework-directive_en" target="_blank">EU Marine Strategy Framework Directive (MSFD)</a>
      </td>
    </tr>
    <tr>
      <td>2022</td>
      <td><a href="https://github.com/oceanhackweek/ohw22-proj-ENSO_Prediction" target="_blank">ENSO prediction using Deep Learning</a></td>
      <td>
        <a href="https://www.cesm.ucar.edu/models/cesm2" target="_blank">Community Earth System Model 2 (CESM2) Sea Surface Temperature (SST)</a>
      </td>
    </tr>
    <tr>
      <td>2022</td>
      <td><a href="https://github.com/oceanhackweek/ohw22-proj-oleaje-costeros" target="_blank">Assessing ocean drivers of coastal physical processes (in Spanish)</a></td>
      <td>
        Buoy ADCP data and satellite data (links needed)
        <!-- <a href="DATASET LINK" target="_blank">DATASET NAME</a> -->
      </td>
    </tr>
    <tr>
      <td>2022</td>
      <td><a href="https://github.com/oceanhackweek/ohw22-proj-flow-cytometry" target="_blank">Unsupervised classification of Flow Cytometry TS data</a></td>
      <td>
        <a href="https://seaflow.netlify.app/" target="_blank"> SeaFlow</a> flow cytometer on the <a href="https://hahana.soest.hawaii.edu/hot/" target="_blank"> HOT-297</a> cruise at Station ALOHA in the North Pacific
      </td>
    </tr>
  </tbody>
</table>
