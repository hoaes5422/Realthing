function hello() {
	alert('hello,world!');
		}
let counter = 0;

function count() {
	counter +=1;
	document.querySelector('p').innerHTML = counter;
		
	if (counter % 10 === 0) {
		alert(`Count is now ${counter}`);
	}
	}

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