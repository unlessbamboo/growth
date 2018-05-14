/*
 * 提取文档中所有缩略语(abbreviations), 并使用<dl>来呈现
 */
function displayAbbreviations() {
    if (!document.getElementsByTagName || ! document.createElement ||
        !document.createTextNode) return false;

    var abbreviations = document.getElementsByTagName('abbr');
    if (abbreviations.length < 1) return false;
    
    var defs = new Array();
    // 遍历所有abbreviations
    for (var i=0; i<abbreviations.length; i++) {
        var current_abbr = abbreviations[i];
        if (current_abbr.childNodes.length < 1) continue;
        
        var definition = current_abbr.getAttribute('title');
        defs[current_abbr.lastChild.nodeValue] = definition;
    }

    // 创建<dl>
    var dlist = document.createElement('dl');
    for (key in defs) {
        var difination = defs[key];
        // dt
        var dtitle = document.createElement('dt');
        var dtitle_text = document.createTextNode(key);
        dtitle.appendChild(dtitle_text);

        // dd
        var ddesc = document.createElement('dd');
        var ddesc_text = document.createTextNode(definition);
        ddesc.appendChild(ddesc_text);

        dlist.appendChild(dtitle);
        dlist.appendChild(ddesc);
    }
    if (dlist.childNodes.length < 1) return false;

    // create title
    var header = document.createElement('h2');
    var head_text = document.createTextNode('Abbreviations');
    header.appendChild(head_text);

    document.body.appendChild(header);
    document.body.appendChild(dlist);
}

addLoadEvent(displayAbbreviations);
