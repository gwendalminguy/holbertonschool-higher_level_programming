document.addEventListener('DOMContentLoaded', function () {
  const adding = document.querySelector('#add_item');
  const removing = document.querySelector('#remove_item');
  const clearing = document.querySelector('#clear_list');
  const myList = document.querySelector('ul.my_list');

  adding.addEventListener('click', () => {
    const newItem = document.createElement('li');
    newItem.innerText = 'Item';
    myList.appendChild(newItem);
  });

  removing.addEventListener('click', () => {
    const lastItem = myList.lastElementChild;
    myList.removeChild(lastItem);
  });

  clearing.addEventListener('click', () => {
    let lastItem = myList.lastElementChild;
    while (lastItem) {
      myList.removeChild(lastItem);
      lastItem = myList.lastElementChild;
    }
  });
});
