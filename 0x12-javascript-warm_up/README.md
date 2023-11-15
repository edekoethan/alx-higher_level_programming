0x12. JavaScript - Warm up
JavaScript

JavaScript is used for many things. Here, you will use JavaScript for 2 reasons:

Scripting (same as we did with Python)
Web front-end

Variables:

Definition: Variables are containers for storing data values. In JavaScript, you can declare variables using the var, let, or const keywords.
Example:
javascript
Copy code
var x = 10; // using var (older way)
let y = "Hello, World!"; // using let (block-scoped)
const pi = 3.14; // using const (immutable)
Functions:

Definition: Functions are blocks of reusable code designed to perform a particular task. They are defined using the function keyword.
Example:
javascript
Copy code
function greet(name) {
  return "Hello, " + name + "!";
}

console.log(greet("Alice")); // Output: Hello, Alice!
Dictionary/Object:

Definition: In JavaScript, dictionaries are implemented as objects. Objects are collections of key-value pairs, where each key must be unique.
Example:
javascript
Copy code
var person = {
  name: "John",
  age: 30,
  city: "New York"
};

console.log(person.name); // Output: John
Set:

Definition: Sets are collections of unique values. They are useful when you want to store multiple items without duplicates.
Example:
javascript
Copy code
var mySet = new Set([1, 2, 3, 2, 1]);
console.log(mySet); // Output: Set { 1, 2, 3 }
Regular Expressions (Regex):

Definition: Regular expressions are patterns used for matching character combinations in strings. They provide a powerful and flexible way to search, match, and manipulate text.
Example:
javascript
Copy code
var pattern = /\d{2}-\d{2}-\d{4}/; // Matches a date pattern like 01-01-2022
var dateString = "12-31-2023";

if (pattern.test(dateString)) {
  console.log("Valid date format");
} else {
  console.log("Invalid date format");
}
