$(document).ready(function () {
  $("#all_types").click(function () {
    $("#all_types_container").show();
    $("#all_type_logo")
      .removeClass("glyphicon-chevron-down")
      .addClass("glyphicon-chevron-up");
    $("#sort_container").hide();
    $("#sort_rule_logo")
      .addClass("glyphicon-chevron-down")
      .removeClass("glyphicon-chevron-up");
  });

  $("#all_types_container").click(function () {
    $(this).hide();
    $("#all_type_logo")
      .addClass("glyphicon-chevron-down")
      .removeClass("glyphicon-chevron-up");
  });

  $("#sort_rule").click(function () {
    $("#sort_container").show();
    $("#sort_rule_logo")
      .addClass("glyphicon-chevron-up")
      .removeClass("glyphicon-chevron-down");
    $("#all_types_container").hide();
    $("#all_type_logo")
      .removeClass("glyphicon-chevron-up")
      .addClass("glyphicon-chevron-down");
  });

  $("#sort_container").click(function () {
    $(this).hide();
    $("#sort_rule_logo")
      .addClass("glyphicon-chevron-down")
      .removeClass("glyphicon-chevron-up");
  });

  //modify shopping cart

  var addShoppings = document.getElementsByClassName("addShopping");
  var subShoppings = document.getElementsByClassName("subShopping");

  for (let i = 0; i < addShoppings.length; i++) {
    const addShopping = addShoppings[i];
    addShopping.addEventListener("click", function () {
      pid = this.getAttribute("ga");
      //second para is sent to server aka view, third para function
      //receive jsonreponse from corresponding function in view
      //post address important like this
      $.post("/axf/changecart/0/", { productid: pid }, function (data) {
        if (data.status == "success") {
          document.getElementById(pid).innerHTML = data.data;
        } else {
          if (data.data == -1) {
            // window.location = url;
            window.location.href = "http://127.0.0.1:8001/axf/login/";
          }
        }
      });
    });
  }

  for (let i = 0; i < subShoppings.length; i++) {
    const subShopping = subShoppings[i];
    subShopping.addEventListener("click", function () {
      pid = this.getAttribute("ga");

      //second para is sent to server aka view, third para function
      //receive jsonreponse from corresponding function in view
      $.post("/axf/changecart/1/", { productid: pid }, function (data) {
        if (data.status == "success") {
          document.getElementById(pid).innerHTML = data.data;
        } else {
          if (data.data == -1) {
            // window.location = url;
            window.location.href = "http://127.0.0.1:8001/axf/login/";
          }
        }
      });
    });
  }
});
