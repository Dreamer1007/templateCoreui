    var TabData = []


    function uploadFile() {


      var form = document.getElementById("CreateModelForm")
      var formdata = new FormData(form)

<<<<<<< HEAD
  $('#file').parse({
    config: {
      delimiter: "," | ".",
      complete: displayHTMLTable,
    }
});
=======
      $('#file').parse({
        config: {
          delimiter: ";",
          complete: displayHTMLTable,
        }
      });
      }
>>>>>>> aeac38630d72be0b55c5b9e341a117091c1e6744

    function displayHTMLTable(results) {

      var table = "<table class='table'>";
      var data = results.data;

      table += "<tr>";

      for (k = 0; k < data[0].length; k++) {
        table += "<td>";
        table += `<input type="checkbox" aria-label="Checkbox for following text input" onClick=AddData('${data[0][k]}')>`;
        table += "</td>";
      }
      table += "</tr>";
      for (i = 0; i < data.length; i++) {
        table += "<tr>";
        var row = data[i];
        var cells = row.join(",").split(",");

        for (j = 0; j < cells.length; j++) {
          table += "<td>";
          table += cells[j];
          table += "</td>";
        }
        table += "</tr>";
      }
      table += "</table>";
      $("#parsed_csv_list").html(table);
    }



    /*  $.ajax({
    type: 'POST',
    url: '/CreateModal',
    data: formdata,
    contentType: false,
    cache: false,
    processData: false,
    success: function(data) {
        console.log(data);
    },
  });
*/




    $('#file').on('change', function () {
      var fileName = $(this).val();
      $(this).next('.custom-file-label').html(fileName);
    })


    function AddData(data) {

      if (!TabData.includes(data)) {
        TabData.push(data)
      } else {
        TabData = TabData.filter(x => {
          return x != data
        })
      }


    }
    $(document).ready(function () {
      $("#SendData").click(function () {
        $.ajax({
          type: 'POST',
          url: '/receivedata',
          contentType: "application/json",
          data: JSON.stringify(TabData),
          success: function (data) {
            console.log(data);
          },
        });
      });
    });


    function SendData() {
      alert("clicked");

    }