
// let counter = 0;

// to allow it to continue when page refresh
if (!localStorage.getItem('counter')){
    localStorage.setItem('counter', 0);
}


function hello() {

    const heading = document.querySelector('h1')

    if (heading.innerText === 'Hello') {
        heading.innerText = 'GoodBye!';

    } else {
        heading.innerText = 'Hello';


    }


}

function count() {
    let counter = localStorage.getItem('counter');
    counter++;
    document.querySelector('h1').innerText = counter
    localStorage.setItem('counter', counter);

    // if (counter % 10 === 0) {
    //     alert(`Count is now ${counter}`);
    // }


}
//run this function after the code has finished loading
document.addEventListener('DOMContentLoaded', () => {
    // set it with the localstorage value the inital html elem 
    document.querySelector('h1').innerText = localStorage.getItem('counter')
    
    document.querySelector('button').onclick = count
    // setInterval(count, 1000)

    document.querySelector('form').onsubmit = function() {
       const name = document.querySelector('#name').value;
       alert(`Hello, ${name}`)
    }

});


// local storage
// allow our webpage to store and retrive info 