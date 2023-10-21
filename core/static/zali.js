alert("hello");
let itemCart = document.getElementById('itemCart');
let productItems = document.getElementById('{{item.id}}');
let addToCart = document.getElementById('addtocart');


addToCart.addEventListener('click', function(){
    alert('item added');
    itemCart.innerHTML = productItems;
})