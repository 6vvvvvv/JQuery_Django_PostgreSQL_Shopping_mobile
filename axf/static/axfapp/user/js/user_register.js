$(document).ready(function () {
  account = document.getElementById("account");
  passwd1 = document.getElementById("passwd1");
  passwd2 = document.getElementById("passwd2");

  accounterr = document.getElementById("accounterr");
  checkerr = document.getElementById("checkerr");
  pass1err = document.getElementById("pass1err");
  pass2err = document.getElementById("pass2err");

  account.addEventListener(
    "focus",
    function () {
      accounterr.style.display = "none";
      checkerr.style.display = "none";
    },
    false
  );

  // //ajax method
  // account.addEventListener("blur",function(){
  //     var inputStr=this.value
  //     if(inputStr.length < 6|| inputStr.length>20) {
  //         accounterr.style.display="block"
  //         return
  //     }
  //     else{
  //         // verify account if occupied
  //         console.log("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
  //         $.ajax({
  //             url:"/checkuserid",
  //             typeof:"post",
  //             typedata:"json",
  //             success:function(data){
  //                 console.log(data)
  //                 if(data.status=="error"){
  //                     checkerr.style.display="block"
  //                 }
  //             }
  //         })
  //     }
  // },false)

  account.addEventListener(
    "blur",
    function () {
      var inputStr = this.value;
      if (inputStr.length < 6 || inputStr.length > 20) {
        accounterr.style.display = "block";
        return;
      }

      // verify account if occupied
      console.log("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&");
      //second parameter will pass to view and (data) will then receive from view,data={"data":"user exist","status":"error"}
      $.post("checkuser/", { userid: inputStr }, function (data) {
        //receive json from view
        if (data.status == "error") {
          checkerr.style.display = "block";
        }
      });
    },
    false
  );

  passwd1.addEventListener(
    "focus",
    function () {
      pass1err.style.display = "none";
    },
    false
  );

  passwd1.addEventListener(
    "blur",
    function () {
      var inputStr = this.value;
      if (inputStr != passwd2.value) {
        pass1err.style.display = "block";
      }
    },
    false
  );

  passwd2.addEventListener(
    "focus",
    function () {
      pass2err.style.display = "none";
    },
    false
  );

  passwd2.addEventListener(
    "blur",
    function () {
      pass1err.style.display = "none";
      var inputStr = this.value;
      if (inputStr != passwd1.value) {
        pass2err.style.display = "block";
      }
    },
    false
  );
});
