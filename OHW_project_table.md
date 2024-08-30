# Searchable Table of Datasets


<script>
function myFunction() {
  var input, filter, table, tr, td, i, j, txtValue;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
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

<input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for projects or datasets..." title="Type in a name">

<style>
#myTable {
  width: 100%;
  border-collapse: collapse;
}

#myTable th, #myTable td {
  border: 1px solid black;
  padding: 10px;
  text-align: left;
}

#myTable th {
  background-color: #f2f2f2;
}
</style>

<table id="myTable">
  <thead>
    <tr>
      <th>Project</th>
      <th>Datasets</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="https://github.com/oceanhackweek/ohw23_proj_oil" target="_blank">Oil Spill Monitoring</a></td>
      <td>
        <a href="https://space.oscar.wmo.int/instruments/view/sar_2000" target="_blank">SAR-2000 imaging sensor</a>,
        <a href="https://earth.esa.int/eogateway/missions/cosmo-skymed" target="_blank">COSMO-SkyMed satellite</a>,
        <a href="https://space.oscar.wmo.int/satellites/view/csk_2" target="_blank">CSKS2</a>
      </td>
    </tr>
    <tr>
      <td><a href="https://github.com/oceanhackweek/tutorials_marine_sdm" target="_blank">Marine SDM</a></td>
      <td>
        <a href="https://oceanhackweek.org/tutorials_marine_sdm/" target="_blank">OBIS via robis</a>,
        <a href="https://oceanhackweek.org/tutorials_marine_sdm/" target="_blank">SMDpredictor R package</a>
      </td>
    </tr>
    <tr>
      <td><a href="https://github.com/oceanhackweek/ohw23_proj_sea_ice_oscillations" target="_blank">Inertial oscillations in the marginal ice zone</a></td>
      <td>
        <a href="https://lpdaac.usgs.gov/data/get-started-data/collection-overview/missions/s-npp-nasa-viirs-overview/" target="_blank">VIIRS instruments</a>,
        <a href="https://www.nesdis.noaa.gov/our-satellites/currently-flying/joint-polar-satellite-system" target="_blank">Joint Polar Satellite System</a>,
        <a href="https://search.earthdata.nasa.gov/search" target="_blank">EarthDataSearch</a>
      </td>
    </tr>
    <tr>
      <td><a href="https://github.com/oceanhackweek/ohw23_proj_argo_ml" target="_blank">Machine learning for Argo Data QC</a></td>
      <td><a href="https://argopy.readthedocs.io/" target="_blank">Argo data accessed via argopy</a></td>
    </tr>
    <tr>
      <td><a href="https://github.com/oceanhackweek/ohw23-proj-habitatmapping" target="_blank">Benthic habitat mapping</a></td>
      <td>
        <a href="https://github.com/oceanhackweek/ohw23-proj-habitatmapping/blob/main/Download%20data.ipynb" target="_blank">Geodata</a>
      </td>
    </tr>
    <tr>
      <td><a href="https://github.com/oceanhackweek/ohw23_proj_fancymoorings" target="_blank">Mooring processing and data page (“fancy moorings”)</a></td>
      <td>
        <a href="https://catalogue.cioospacific.ca/dataset/ca-cioos_82656721-88e6-4543-90f1-edc35c0f42c9" target="_blank">CIOOS Moorings</a>,
        <a href="https://nwem.apl.washington.edu/erddap/index.html" target="_blank">NANOOS Moorings</a>,
        <a href="https://oceanhackweek.org/ohw23_proj_fancymoorings/" target="_blank">Project website</a>
      </td>
    </tr>
    <tr>
      <td><a href="https://github.com/oceanhackweek/ohw23_proj_sst" target="_blank">SST spatial distribution prediction using machine learning</a></td>
      <td>
        <a href="https://podaac.jpl.nasa.gov/dataset/MUR-JPL-L4-GLOB-v4.1" target="_blank">MUR Satellite Data</a>,
        <a href="https://podaac.jpl.nasa.gov/dataset/MUR-JPL-L4-GLOB-v4.1" target="_blank">NASA website</a>
      </td>
    </tr>
    <tr>
      <td><a href="https://github.com/oceanhackweek/ohw23-proj-pamproject" target="_blank">Passive acoustics monitoring</a></td>
      <td>
        <a href="https://registry.opendata.aws/pacific-sound/" target="_blank">Pacific Sound</a>,
        <a href="https://catalogue-imos.aodn.org.au/geonetwork/srv/eng/catalog.search#/metadata/e850651b-d65d-495b-8182-5dde35919616" target="_blank">IMOS Acoustic Data</a>
      </td>
    </tr>
    <tr>
      <td><a href="https://github.com/oceanhackweek/ohw23_proj_drone_georef" target="_blank">Direct geo referencing drone images</a></td>
      <td>Drone survey carried out in 14 February (CSIRO Kensington)</td>
    </tr>
    <tr>
      <td><a href="https://github.com/oceanhackweek/ohw23_proj_SAupwelling" target="_blank">Variability of the suppression of South Australian upwelling</a></td>
      <td>
        <a href="http://imos-data.s3-website-ap-southeast-2.amazonaws.com/?prefix=IMOS/ANMN/SA/" target="_blank">SA coastal mooring data</a>,
        <a href="http://imos-data.s3-website-ap-southeast-2.amazonaws.com/?prefix=IMOS/ANMN/NRS/NRSKAI/" target="_blank">SA NRS station data</a>,
        <a href="https://imos.org.au/facilities/nationalmooringnetwork/samoorings" target="_blank">SA moorings summary</a>,
        <a href="https://portal.aodn.org.au/search" target="_blank">AODN portal</a>
      </td>
    </tr>
    <tr>
      <td><a href="https://github.com/oceanhackweek/ohw23_proj_amplicon" target="_blank">Bioinformatic pipelines for standardized output</a></td>
      <td>
        <a href="https://pythonhosted.org/OBITools/wolves.html" target="_blank">OBITools reference database</a>
      </td>
    </tr>
  </tbody>
</table>
