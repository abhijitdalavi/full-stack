const axios = require('axios');

// Sample funcs to use for testing
const functions = {
    add: (num1, num2) => num1 + num2,
    isNull: () => null,
    checkVal: (x) => x,
    createUser: () => {
        const user = { firstName: 'Bill' };
        user['lastName'] = 'Bob';
        return user;
    },
    fetchUser: () => axios.get('https://jsonplaceholder.typicode.com/users/2')
        .then(res => res.data)
        .catch(err => 'fetch error'),
}

// Export funcs
module.exports = functions;