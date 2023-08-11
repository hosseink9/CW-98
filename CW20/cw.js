// 1)
// let userinput = prompt('Enter something: ')
// let userinputtype = parseInt(userinput)
// if (isNaN(userinputtype)) {
//     console.log('string')
// } else {
//     console.log(`type of what you entered: ${typeof userinputtype}`)
// }


// 2)
let age = prompt("Enter your age: ");
let toint = parseInt(age);

if (age >= 0 && age <= 10) {
    console.log("child");
} else if (age >= 21 && age <= 18) {
    console.log("Teen");
} else if (age >= 19 && age <= 30) {
    console.log("Adult");
} else {
    console.log("Old");
}