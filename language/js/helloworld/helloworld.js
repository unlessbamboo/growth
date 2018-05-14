var name = "郑碧峰";
var var1 = 1000;

var cb = function(x) {
    var var2 = 10000;
    return x * var2 * var1
}

var sums = function(x1, x2, x3, x4) {
    var sum = 0;

    console.log("Arguments:", arguments.length);
    console.log(Math.min(arguments));
    for (var item in arguments) {
        sum += arguments[item];
    }
    return sum;

    // if (x2 == undefined) {
    //     return x1;
    // } else if (x3 == undefined) {
    //     return x1 + x2;
    // } else {
    //     return x1 + x2 + x3;
    // }
}


// 创建对象
var Bamboo = {
    sex: true,
    events: ["work", 1, 2, 3]
}

console.log("You name is ", name);
console.log("You have money ", cb(10000));
func_define();
console.log("1 + 2 = ", sums(1, 2));
console.log("1 + 2 + 3 = ", sums(1, 2, 3));

console.log(["x", 1, 2]);
console.log(["x", 1, 2].join("-join-"));
console.log(["x", 1, 2][2]);

for (var item in Bamboo) {
    console.log("-----", item, Bamboo[item]);
}

console.log([1, 2, 3, 4].filter(function(value) {
    return value > 2;
}));

// bind function
var the_set = ["first1", "first2", "first3"];
var ancestry = [
    {name: "first0"}, 
    {name: "first1"}, 
    {name: "first2"}, 
    {name: "first3"}, 
    {name: "first4"}, 
    {name: "first5"}];
function isInSet(set, person) {
    return set.indexOf(person.name) > -1;
}
console.log(ancestry.filter(function(person) {
    return isInSet(the_set, person);
}));
console.log(ancestry.filter(isInSet.bind(null, the_set)));


// 对象操作
// 定义一个函数
function speak(line) {
    console.log("The " + this.type + " rabbit says '" + line + "'.");
};
// 定义一个对象，将方法指向函数
var whiteRabbit = {
    type: "white",
    speak: speak
};
whiteRabbit.speak("White rabbite---");
speak.call({type: "OLD"}, "Oh++++++");

// 对象原型的基原型
console.log(Object.getPrototypeOf({}) == Object.prototype);
// 函数原型
console.log(Object.getPrototypeOf(isNaN) == Function.prototype);
// 数组原型
console.log(Object.getPrototypeOf([]) == Array.prototype);
console.log(Object.getPrototypeOf([]) == Object.prototype);
// 类派生或者对象原型的派生
var protoRabbit = {
    speak: function(line) {
        console.log("The " + this.type + " rabbit says '" + line + "'.");
    }
};
// 将原型对象作为对象的属性
var killRabbit = Object.create(protoRabbit);
killRabbit.type = "killer";
killRabbit.new_attr = "新的属性";
killRabbit.speak(killRabbit.new_attr);

// 构造函数，类似C++
function Rabbit(type) {
    this.type = type;
};
// 利用构造函数建立对象<--->原型之间的关联
var killRabbit = new Rabbit("killer");
var blackRabbit = new Rabbit("black");
console.log(blackRabbit.type);

// 可枚举属性、不可枚举属性（是否隐藏）
// 定义不可枚举属性
var map = {}
Object.defineProperty(Object.prototype, "hiddenNonsense", {enumerable: false, value: "hi"});
map.type1 = "type1";
for (var name in map)
    console.log(name);
console.log(map.hiddenNonsense);
console.log("hiddenNonsense" in map);
console.log(map.hasOwnProperty("hiddenNonsense"));

// 创建无原型（基类）的对象
var map = Object.create(null);
map['type1'] = 'type1';
console.log("toString" in map);
console.log("type1" in map);


// 测试函数声明和定义的位置
function func_define() {
    console.log("测试函数的位置.");
};
