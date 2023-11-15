1. Objects:
JavaScript is an object-oriented programming language, and objects are one of its fundamental data types. Objects in JavaScript are collections of key-value pairs, where each key is a string (or symbol) and each value can be any data type, including other objects. Objects allow you to group related data and functions together.

Example of an object:

javascript
Copy code
let person = {
  name: "John",
  age: 30,
  isStudent: false,
  sayHello: function() {
    console.log("Hello!");
  }
};
You can access properties and methods of an object using dot notation or square brackets:

javascript
Copy code
console.log(person.name);       // Output: John
console.log(person['age']);     // Output: 30
person.sayHello();              // Output: Hello!
2. Scopes:
In JavaScript, the scope is the context in which variables are declared. There are two main types of scope: global scope and local scope.

Global Scope: Variables declared outside of any function or block have global scope and can be accessed throughout the entire program.

javascript
Copy code
let globalVar = "I'm global";

function exampleFunction() {
  console.log(globalVar);  // Output: I'm global
}
Local Scope: Variables declared inside a function or block have local scope and are only accessible within that function or block.

javascript
Copy code
function exampleFunction() {
  let localVar = "I'm local";
  console.log(localVar);   // Output: I'm local
}
3. Closures:
A closure is created when a function is defined within another function (nested function) and has access to the outer function's variables. The inner function "closes over" the outer function's scope, retaining access to its variables even after the outer function has finished executing.

javascript
Copy code
function outerFunction() {
  let outerVar = "I'm outer";

  function innerFunction() {
    console.log(outerVar);
  }

  return innerFunction;
}

let closureFunction = outerFunction();
closureFunction();  // Output: I'm outer
In this example, innerFunction is a closure because it can access the outerVar variable from its containing function, outerFunction.
