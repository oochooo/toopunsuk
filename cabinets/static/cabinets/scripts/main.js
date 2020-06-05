console.log('mainjs')


function collapseNav() {
    var x = document.getElementById("dasTopnav");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
  }