/*
 * 提取所有的<blockquote>标签中的cite链接并在每一个<blockquote>的后面
 */
function displayCitations() {
    if (!document.getElementsByTagName || !document.createElement ||
        !document.createTextNode) return false;

    // 获取所有引用
    var quotes = document.getElementsByTagName('blockquote');
    for (var i=0; i<quotes.length; i++) {
        var url = quotes[i].getAttribute('cite');
        if (!url) continue;

        // 获取<blockquote>中的所有元素节点
        var quoteChildren = quotes[i].getElementsByTagName('*');
        if (quoteChildren.length < 1) continue;
        var elem = quoteChildren[quoteChildren.length - 1];
        
        // 创建链接标记
        var link = document.createElement('a');
        var link_text = document.createTextNode('source');
        link.appendChild(link_text);
        link.setAttribute('href', url);
        var superscript = document.createElement('sup');
        superscript.appendChild(link);

        // 添加到最后一个节点
        elem.appendChild(superscript);
    }
}

addLoadEvent(displayCitations);
