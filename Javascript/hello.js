
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


if (!localStorage.getItem('counter')) { 
    localStorage.setItem('counter', 0);}
            
function count() {  
    let counter = localStorage.getItem('counter');
    counter++;
    document.querySelector('p').innerHTML = counter;
    localStorage.setItem('counter', counter);}

document.addEventListener('DOMContentLoaded', function() {  
    document.querySelector('p').innerHTML = localStorage.getItem('counter');
    document.querySelector('#count').onclick = count;
});

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

	document.querySelector('#num1').onsubmit = function() {
		const name = document.querySelector('#name').value;
		alert(`Hello ${name}!`);
	};
});
// Javascript for task 
document.addEventListener('DOMContentLoaded', function() {
			
	document.querySelector('#haydo').disabled = true; 
			
			
	document.querySelector('#task').onkeyup = function() {
		if (document.querySelector('#task').value.length > 0 ) {
			document.querySelector('#haydo').disabled = false;
			}
		else {
				document.querySelector('#haydo').disabled = true;
			}
		}
					
	document.querySelector('#num2').onsubmit = function() {
			
	const task = document.querySelector('#task').value;

	if (task === "Delete") {
		document.querySelector('#tasksss') = '';
	}

	const li = document.createElement('li');
			
	li.innerHTML = task;

	document.querySelector('#tasksss').append(li)
	document.querySelector('#task').value = '';
	document.querySelector('#haydo').disabled = true;
	return false;
				
	}
})



document.addEventListener('DOMContentLoaded', function() {

	document.querySelector('#h5f1').onsubmit = function() {
		fetch('http://api.exchangeratesapi.io/v1/latest?access_key=112544a7f6ef07e90323fe92cc19b4b9&USD')
		.then(response => response.json())
		.then(data => {
		const currency = document.querySelector('#currency').value.toUpperCase();
		const rate = data.rates[currency];
		if (rate !== undefined) {
			const result = `1 USD is equal to ${rate.toFixed(3)} ${currency}`;
		document.querySelector('#result').innerHTML = result;
		} else {
		document.querySelector('#result').innerHTML = 'Invalid currency.';
				}
			})
			.catch(error => {
		console.log('Error:', error);
			});
			return false;
			}
			});



