/*
 * 计算每列的最小宽度和最大宽度
 */
function rowHeights(rows) {
    // 逐行处理数组rows
    return rows.map(function(row) {
        // 每一个单元格中最大高度
        return row.reduce(function(max, cell) {
            return Math.max(max, cell.minHeight());
        }, 0);
    });
}


function colWights(rows) {
    return rows[0].map(function(_, i) {
        console.log(row[i]);
        return rows.reduce(function(max, row) {
            return Math.max(max, row[i].minWidth());
        }, 0);
    });
}


function TextCell(text) {
    this.text = text.split("\n");
}
TextCell.prototype.minWidth = function() {
    return this.text.reduce(function(width, line) {
        return Math.max(width, line.length);
    }, 0);
};
TextCell.prototype.minHeight = function() {
    return this.text.length;
};


// 测试数据
var rows = [];
for (var i = 0; i < 5; i++) {
    var row = [];
    for (var j = 0; j < 5; j++) {
        if ((j + i) % 2 == 0) {
            row.push(new TextCell("##"));
        } else {
            row.push(new TextCell("  "));
        }
    }
    rows.push(row);
}
console.log(rows);

console.log(rowHeights(rows));
console.log(colWights(rows));
