$(document).ready(function () {
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
          document.getElementById("price" + pid).innerHTML = data.price;
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
          document.getElementById("price" + pid).innerHTML = data.price;
        }

        if (data.data == 0) {
          var li = document.getElementById("li" + pid);
          li.parentNode.removeChild(li);
        }
      });
    });
  }

  var ischose = document.getElementsByClassName("ischose");
  for (let i = 0; i < ischose.length; i++) {
    ischose = ischose[i];
    ischose.addEventListener("click", function () {
      pid = this.getAttribute("goodid");
      $.post("/axf/changecart/2/", { productid: pid }, function (data) {
        if (data.status == "success") {
          // window.location.href=("http://127.0.0.1:8000/axf/cart/");
          var sign = document.getElementById("a" + pid);
          sign.innerHTML = data.data;
        }
      });
    });
  }

  var ok = document.getElementById("ok");
  ok.addEventListener("click", function () {
    var f = confirm("Do you want to check out");
    if (f) {
      $.post("/axf/saveorder/", function (data) {
        if ((data.status = "success")) {
          window.location.href = "http://127.0.0.1:8000/axf/cart/";
        }
      });
    }
  });
});
