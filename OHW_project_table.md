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
      <th>Dataset</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Oil Spill Monitoring</td>
      <td>SAR-2000 imaging sensor on the second COSMO-SkyMed satellite called CSKS2</td>
    </tr>
    <tr>
      <td>Marine SDM</td>
      <td>OBIS via robis and environmental data via the SMDpredictor R package</td>
    </tr>
    <tr>
      <td>Inertial oscillations in the marginal ice zone</td>
      <td>VIIRS instruments installed on the Joint Polar Satellite System; data from the Suomi-NPP and JPSS-1/NOAA-20 satellites was accessed from <a href="https://search.earthdata.nasa.gov/search" target="_blank" rel="noopener noreferrer">EarthDataSearch</a></td>
    </tr>
    <tr>
      <td><a href="https://github.com/oceanhackweek/ohw23-proj-habitatmapping" target="_blank" rel="noopener noreferrer">Benthic habitat mapping</a></td>
      <td>geodata</td>
    </tr>
    <tr>
      <td>Machine learning for Argo Data QC</td>
      <td>Argo data accessed via argopy</td>
    </tr>
  </tbody>
</table>
