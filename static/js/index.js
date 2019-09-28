document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {});
    var elems1 = document.querySelectorAll('.parallax');
    var instances = M.Parallax.init(elems1, {});
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, {});
  });



  