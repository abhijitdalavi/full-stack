/* This is our testing file */

const functions = require('./functions');

// Example test: passing in the func we intend to test with sample parameters,
// and providing the value we expect the answer "toBe"
test('Adds 2 + 2 to equal 4', () => {
    expect(functions.add(2, 2)).toBe(4);
});

// Another similar test, except this time we test against what the answer should not be
test('Adds 2 + 2 to NOT equal 5', () => {
    expect(functions.add(2, 2)).not.toBe(5);
});

// Check func to return null
test('Should return null', () => {
    expect(functions.isNull()).toBeNull;
});

// Check input val, will pass if input is a falsy value
test('Should be falsy', () => {
    expect(functions.checkVal(null)).toBeFalsy;
});

// Check user; 'toBe' doesn't work on objects because of reference, use 'toEqual' instead to check for expected value
test('User should be Bill Bob', () => {
    expect(functions.createUser()).toEqual({
        firstName: 'Bill',
        lastName: 'Bob'
    });
});

// Less than/greater than; using logic created right inside test call
test('Should be under 2000', () => {
    const load1 = 555;
    const load2 = 600;
    expect(load1 + load2).toBeLessThan(2000);
});

// Regex check for uppercase I and lowercase I
test('No I in team', () => {
    expect('team').not.toMatch(/I/i);
});

// Testing async data (use "expect.assertions" AND return the promise when testing async data)
test('User fetched should be Ervin Howell', () => {
    expect.assertions(1);
    return functions.fetchUser()
        .then(data => {
            expect(data.name).toEqual('Ervin Howell')
        });
});

// Using async await syntax
test('Async await should be Ervin Howell', async() => {
    expect.assertions(1);
    const data = await functions.fetchUser();
    expect(data.name).toEqual('Ervin Howell');
})

// Check func to make sure is defined
test('Adds 2 + 2 to be defined', () => {
    expect(functions.add(2, 2)).toBeDefined;
});

// Check func to make sure it's not undefined
test('Adds 2 + 2 to NOT be undefined', () => {
    expect(functions.add(2, 2)).not.toBeUndefined;
});

// Check func to match anything an if statement would treat as true
test('Adds 2 + 2 to be Truthy', () => {
    expect(functions.add(2, 2)).toBeTruthy;
});

// Check func to match anything an if statement would treat as false
test('Adds 2 + 2 to be Falsy', () => {
    expect(functions.add(2, 2)).toBeFalsy;
});