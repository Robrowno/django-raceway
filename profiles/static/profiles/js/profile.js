function init(){
    let saveProfileBtn = document.getElementById("saveProfileBtn");
    saveProfileBtn.style.display = "none";
}


function enableProfileForm() {
    let saveProfileBtn = document.getElementById("saveProfileBtn");
    saveProfileBtn.style.display = "flex";
    $("input").attr("disabled", false);

    let editProfileBtn = document.getElementById("editProfileBtn");
    editProfileBtn.style.display = "none";
}
function ajaxRequest(formDataArray){
    $.ajax({
        type: "POST",
        url: "update-profile/",
        data: formDataArray,
        success: function(response) {
            console.log(response);
            $("#alert-container")
            .append($(`<div role="alert" id="alert-box" class="alert text-center alert-primary alert-dismissible fade show "> \
                          <strong>${response.status}</strong> \
                          </button> \
                        </div>`));
                        setTimeout(function(){
                            $("#alert-box").fadeOut(function(){
                                $(this).fadeIn(1000);
                                $(this).remove();

                            });
                         }, 3000);
                         
        },
        error: function(error) {
            $("#alert-container")
            .append($(`<div role="alert" id="alert-box" class="alert text-center alert-danger alert-dismissible fade show "> \
                          <strong>${response.status}</strong> \
                          </button> \
                        </div>`));
                        setTimeout(function(){
                            $("#alert-box").fadeOut(function(){
                                $(this).fadeIn(1000);
                                $(this).remove();

                            });
                         }, 3000);
        }
    });
   setTimeout(()=>{
    location.reload(); 
   },2050)
}
function disableProfileForm() {
    let formDataArray = $('#profileFormID').serializeArray();
    let editProfileBtn = document.getElementById("editProfileBtn");
    editProfileBtn.style.display = "flex";
    $("input").attr("disabled", true);

    let saveProfileBtn = document.getElementById("saveProfileBtn");
    saveProfileBtn.style.display = "none";
    ajaxRequest(formDataArray);
}
function validateLength(input) {
    if (input.value.length < 3) {
        input.value = input.value.slice(0, 3);
    }
    if (input.value.length > 3) {
        input.value = input.value.slice(0, 3);
    }
}

