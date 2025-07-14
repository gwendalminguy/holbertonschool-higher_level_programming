const list = document.querySelector('ul.my_list');
const add = document.querySelector('#add_item');

add.addEventListener('click', () => {
	let newItem = document.createElement('li');
	newItem.innerText = 'Item';
	list.appendChild(newItem);
});
