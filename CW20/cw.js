// 1)
// let userinput = prompt('Enter something: ')
// let userinputtype = parseInt(userinput)
// if (isNaN(userinputtype)) {
//     console.log('string')
// } else {
//     console.log(`type of what you entered: ${typeof userinputtype}`)
// }


// 2)
// let age = prompt("Enter your age: ");
// let toint = parseInt(age);

// if (age >= 0 && age <= 10) {
//     console.log("child");
// } else if (age >= 21 && age <= 18) {
//     console.log("Teen");
// } else if (age >= 19 && age <= 30) {
//     console.log("Adult");
// } else {
//     console.log("Old");
// }

// 3)
function setCookie(name, value, days) {
    const expires = new Date();
    expires.setTime(expires.getTime() + (days * 24 * 60 * 60 * 1000));
    document.cookie = name + "=" + value + ";expires=" + expires.toUTCString();
}

// Function to get the value of a cookie by name
function getCookie(name) {
    const cookieName = name + "=";
    const cookieArray = document.cookie.split(";");

    for (let i = 0; i < cookieArray.length; i++) {
        let cookie = cookieArray[i];
        while (cookie.charAt(0) === " ") {
            cookie = cookie.substring(1);
        }
        if (cookie.indexOf(cookieName) === 0) {
            return cookie.substring(cookieName.length, cookie.length);
        }
    }
    return null;
}
function main() {
    const storedUsername = getCookie("username");
    const username = prompt("Enter your username:");
    if (storedUsername === username) {
        alert("Hello, " + storedUsername + "! Welcome back!");

    } else {

        const username = prompt("Enter your new username:");

        if (!username || username !== "") {
            setCookie("username", username, 7);
        }

    }
}
main();
