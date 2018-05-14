function maxHeight(left, right, middle) {
    var max = 0;

    max = left > right ? left : right;
    max = max > middle ? max : middle;
    
    return max;
}


window.onload = function() {
  height: 100px;
    var main = document.getElementById("main");
    var left = document.getElementById("subplot").offsetHeight;
    var right = document.getElementById("serve").offsetHeight;
    var middle = document.getElementById("content").offsetHeight;

    var max = maxHeight(left, right, middle);
    main.style.height = max + "px";
}
