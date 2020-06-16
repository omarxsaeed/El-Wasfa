var password_input = document.getElementsByClassName("password")
var password_confirmation = document.getElementsByClassName("password_confirmation")
var confirmation_message = document.getElementsByClassName("confirmation_message")
var displayname = document.getElementsByClassName("displayname")
var length = document.querySelector("#length")
var lower = document.querySelector("#lower")
var upper = document.querySelector("#upper")
var number = document.querySelector("#number")
var contain = document.querySelector("#contain")



// checks for matching passwords
if (password_confirmation != null) {
  password_confirmation.onkeyup = function() {
    if (password_input.value == password_confirmation.value) {
      confirmation_message.classList.add("valid");
      confirmation_message.classList.remove("invalid");
      confirmation_message.innerHTML = "Passwords Match.";
      password_confirmation.classList.add("is-valid");
      password_confirmation.classList.remove("is-invalid");
    }
    else {
      confirmation_message.classList.add("invalid");
      confirmation_message.classList.remove("valid");
      confirmation_message.innerHTML = "Passwords don't Match.";
      password_confirmation.classList.add("is-invalid");
      password_confirmation.classList.remove("is-valid");
    }
  
}
}
if (displayname =! null){
  displayname.onfocus = function() {
    document.querySelector("#displayname_message").style.display = 'block';
    }
    
    displayname.onblur = function() {
    document.querySelector("#displayname_message").style.display = 'none';
    }
}
if (password_input =! null){
    // displays the password conditions when the input is pressed
    password_input.onfocus = function() {
      document.querySelector(".message").style.display = 'block';
      }
  
    // hides the password conditions
    password_input.onblur = function() {
    document.querySelector(".message").style.display = 'none';
    }

    // When the user starts to type something inside the password field
    password_input.onkeyup = function() {
      // Validate lowercase letters
      var lowerCaseLetters = /[a-z]/g;
      if(password_input.value.match(lowerCaseLetters)) {
        lower.classList.remove("invalid");
        lower.classList.add("valid");
      } else {
        lower.classList.remove("valid");
        lower.classList.add("invalid");
      }

      // Validate capital letters
      var upperCaseLetters = /[A-Z]/g;
      if(password_input.value.match(upperCaseLetters)) {
        upper.classList.remove("invalid");
        upper.classList.add("valid");
      } else {
        upper.classList.remove("valid");
        upper.classList.add("invalid");
      }

      // Validate numbers
      var numbers = /[0-9]/g;
      if(password_input.value.match(numbers)) {
        number.classList.remove("invalid");
        number.classList.add("valid");
      } else {
        number.classList.remove("valid");
        number.classList.add("invalid");
      }

      // Validate length
      if(password_input.value.length >= 8) {
        length.classList.remove("invalid");
        length.classList.add("valid");
      } else {
        length.classList.remove("valid");
        length.classList.add("invalid");
      }
        // Checks if all conditions were met then turns the first message valid
        if(length.classList.contains("valid") && number.classList.contains("valid") && upper.classList.contains("valid") && lower.classList.contains("valid")) {
        contain.classList.remove("invalid");
        contain.classList.add("valid");
        password_input.classList.add("is-valid");
        password_input.classList.remove("is-invalid");


      } else {
        password_input.classList.add("is-invalid");
        password_input.classList.remove("is-valid");
        contain.classList.remove("valid");
        contain.classList.add("invalid");
      }
    }
  }
// Adding and removing ingredient input fields
function add(){
  var max_fields = 10;
  var new_ingredient = parseInt($('#total_ingr').val())+1;
  if (max_fields >= new_ingredient) {
      var new_input = "<div><input class= 'form-control ingr_inp ' type='text' name='ingredient_"+new_ingredient+"'  id='ingredient_"+new_ingredient+"'></div>";
  $('#new_ingr').append(new_input);
  $('#total_ingr').val(new_ingredient)

  }
    }
    function remove(){
      var last_ingr = $('#total_ingr').val();
      if(last_ingr>1){
        $('#ingredient_'+last_ingr).remove();
        $('#total_ingr').val(last_ingr-1);
      }
    }

// Adding and removing direction input fields
function add_dir(){
  var max_fields = 5;
  var new_direction = parseInt($('#total_dir').val())+1;
  if (max_fields >= new_direction) {
      var new_input = "<div><input class= 'form-control ingr_inp' type='text' name='direction_"+new_direction+"' id='direction_"+new_direction+"'></div>";
  $('#new_dir').append(new_input);
  $('#total_dir').val(new_direction)

  }
    }
    function remove_dir(){
      var last_dir = $('#total_dir').val();
      if(last_dir>1){
        $('#direction_'+last_dir).remove();
        $('#total_dir').val(last_dir-1);
      }
    }

// active navbar link
jQuery(function($) {
  var path = window.location.href; // because the 'href' property of the DOM element is the absolute path
  $('ul a').each(function() {
   if (this.href === path) {
    $(this).css("color", "#FF8800");
   }
  });
 });