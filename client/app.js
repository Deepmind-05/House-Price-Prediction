// communicates with server and gives what it wants
//function
$(document).ready(function(){
    loadLocationNames();

   function loadLocationNames() {
       // $.get("http://127.0.0.1:5000/get_location_names", function (data, status) {
       $.get("/api/get_location_names", function (data, status) {
           if (data) {
               let locations = data.locations;
               let locationDropdown = $('#location')
               locationDropdown.empty();

               locationDropdown.append(new Option("Selection Location", ""));

               for (let i in locations) {
                   locationDropdown.append(new Option(locations[i], locations[i]));
               }

           }
       });
   }
    //to store bath and bhk from clicked buttons
    let bhk = null;
    let bath = null;

    $('button[name="bhk"]').on('click', function () {
        bhk = $(this).val();
        //remove 'selected' class from all bhk buttons
        $('button[name="bhk"]').removeClass('selected');
        //Add 'selected' class to the clicked one
         $(this).addClass('selected');
    });
    $('button[name="bath"]').on('click', function () {
        bath = $(this).val();
        //remove 'selected' class from all bhk buttons
        $('button[name="bath"]').removeClass('selected');
        //Add 'selected' class to the clicked one
         $(this).addClass('selected');
    });
   $('form').on('submit', function(e) {
       e.preventDefault(); // prevent page default

       const sqft = $('input[name="sqft"]').val();
       const location = $('#location').val();

       if (!sqft || isNaN(sqft) || parseFloat(sqft) <= 0) {
            alert("Please enter a valid number for total area (sqft).");
            return;
       }
        if(!sqft || !bhk || !location || !bhk) {
            alert("Please fill all the fields");
            return;
        }

        $.post("http://127.0.0.1:5000/predict_home_price", {
            sqft: parseFloat(sqft),
            location: location,
            bhk: parseInt(bhk),
            bath: parseInt(bath)
        }, function(data) {
            if(data.estimated_price) {
                $('#estimatedPrice').text("Estimated Price: $" + data.estimated_price + "Lakh");
            } else {
                $('#estimatedPrice').text("Could not estimate price.");
            }
        }).fail(function(xhr) {
            alert("Error: " + xhr.responseText);
        });
   });
});