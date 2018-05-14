var id='purchase';

function getElementsByClassName(node, classname){
    if (node.getElementsByClassName) {
        return node.getElementsByClassName(classname);
    } else {
        var results = new Array();
        var elems = node.getElementsByTagName('*');
        for (var i=0; i < elems.length; i++) {
            if (elems[i].className.indexOf(classname) != -1) {
                results[results.length] = elems[i]
            }
        }
    }
}

var items = document.getElementsByTagName('li')
for (var i=0; i < items.length; i++) {
    // alert(typeof items[i]);
}


var shoppping = document.getElementById('purchase');
var sales = getElementsByClassName(shoppping, 'sale');
for (var i=0; i < sales.length; i++) {
    // alert(sales[i].innerText);
    // alert(sales[i].innerHTML);
}


var paras = document.getElementsByTagName('p');
for (var i=0; i < paras.length; i++){
    var title_text = paras[i].getAttribute('title');
    if (title_text != null) {
        alert(title_text);
    }
}
