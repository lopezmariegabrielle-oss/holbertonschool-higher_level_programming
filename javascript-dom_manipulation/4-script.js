const addItem = document.querySelector('#add_item');
const myList = document.querySelector('.my_list');
addItem.addEventListener('click', function () {
  const newLi = document.createElement('li');
  newLi.textContent = 'Item';
  myList.appendChild(newLi);
});