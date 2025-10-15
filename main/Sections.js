Sections = {
    "Help": {"Commands": "This is Help/Commands",
     "About":"This is a simple Operating System that works in a Python Emulator"},
    "Commands": "NaN",
    "About": "NaN",
    "Apps": "NaN",
    "Files": "NaN",
    "Quit": "NaN",
};


let currentInput = '';
let currentOperator = '';
let previousInput = '';

const display = document.getElementById('display');

function appendNumber(number) {
    currentInput += number;
    display.value = currentInput;
}

function appendOperator(operator) {
    if (currentInput === '') return; // Prevent starting with an operator
    if (previousInput !== '') {
        calculate(); // Calculate if there's a pending operation
    }
    currentOperator = operator;
    previousInput = currentInput;
    currentInput = '';
    display.value = previousInput + ' ' + currentOperator + ' ';
}

function calculate() {
    if (previousInput === '' || currentInput === '') return; // Need two operands
    
    let result;
    const prev = parseFloat(previousInput);
    const current = parseFloat(currentInput);

    switch (currentOperator) {
        case '+':
            result = prev + current;
            break;
        case '-':
            result = prev - current;
            break;
        case '*':
            result = prev * current;
            break;
        case '/':
            if (current === 0) {
                alert("Cannot divide by zero!");
                clearDisplay();
                return;
            }
            result = prev / current;
            break;
        default:
            return;
    }

    currentInput = result.toString();
    currentOperator = '';
    previousInput = '';
    display.value = currentInput;
}

function clearDisplay() {
    currentInput = '';
    currentOperator = '';
    previousInput = '';
    display.value = '';
}

let d = new Date();

let day = String(d.getDate()).padStart(2, "0");

let month = String(d.getMonth() + 1).padStart(2, "0");

let year = d.getFullYear();

let d1 = day + "/" + month + "/" + year;

console.log(d1);
