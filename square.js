const add = require('./add');

function square(num) {
    return num * num;
}

const result = square(add(3, 4)); // Example usage
module.exports = result;