
document.addEventListener('DOMContentLoaded', function() {
	document.querySelector('select').onchange = function () {
		document.querySelector('h1').style.color = this.value;

	};
});
function hello() {
	alert('hello,world!');
		}

document.addEventListener('DOMContentLoaded',function() {
	document.querySelector('#hello').onclick = hello;
})
// for the hello function
let counter = 0;
function count() {
	counter +=1;
	document.querySelector('p').innerHTML = counter;
		
	if (counter % 10 === 0) {
		alert(`Count is now ${counter}`);
	}
	}
// this if for the count function
document.addEventListener('DOMContentLoaded',function() {
	document.querySelector('#count').onclick = count;
})

function Change() {
	const heading = document.querySelector('h1');
	// let heading = document.querySelector('h1'); 
	if (heading.innerHTML === 'Hello!') {
		heading.innerHTML = 'Goodbye!';
		} 
	else {
		heading.innerHTML = 'Hello!';
			 }
		}
document.addEventListener('DOMContentLoaded',function() {
	document.querySelector('#heading').onclick = Change;
})
// for the change function
document.addEventListener('DOMContentLoaded', function() {

	document.querySelector('form').onsubmit = function() {
		const name = document.querySelector('#name').value;
		alert(`Hello ${name}!`);
	};
});
// Javascript for task 
document.addEventListener('DOMContentLoaded', function() {
			
	document.querySelector('#submit').disabled = true; 
			
			
	document.querySelector('#task').onkeyup = function() {
		if (document.querySelector('#task').value.length > 0 ) {
			document.querySelector('#submit').disabled = false;
			}
		else {
				document.querySelector('#submit').disabled = true;
			}
		}
					
	document.querySelector('form').onsubmit = function() {
			
	const task = document.querySelector('#task').value;

	if (task === "Delete") {
		document.querySelector('#tasksss') = '';
	}

	const li = document.createElement('li');
			
	li.innerHTML = task;

	document.querySelector('#tasksss').append(li)
	document.querySelector('#task').value = '';
	document.querySelector('#submit').disabled = true;
	return false;
				
	}
})





