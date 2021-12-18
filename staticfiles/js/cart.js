function AddToCart(product_id){
    let qty = document.getElementById('product_quantity').value;
    qty = parseInt(qty)
    let d = {
        product_id:product_id,
        count:qty,
        }
    let data = JSON.stringify(d)
	  if (window.XMLHttpRequest) {
      var xhttp=new XMLHttpRequest();
    } else {  // code for IE6, IE5
        var xhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xhttp.onreadystatechange = function() {
    if (xhttp.readyState === 4 && xhttp.status === 200) {
        var data = JSON.parse(this.responseText);
        let message = document.querySelector("#message");
        let messageText = document.querySelector("#message_text");
        console.log(data["success"])
        if(data["success"] === 200){
            messageText.innerHTML = `<h1>Success ! Product added to cart! </h1>`
        }else{
            messageText.innerHTML = `<h1>Error ! Something is wrong ! </h1>`
        }

        message.style.transition = "all 0.6s";
        message.style.opacity = "1";
        message.style.top = "100px";

    }else{

      }
    }
    var url = "/cart/add/"
    xhttp.open("GET", url+`?data=${data}`, true);
    xhttp.send();
}
function closeMessage(){
          let message = document.querySelector("#message");
        message.style.transition = "all 0.6s";
        message.style.opacity = "0";
        message.style.top = "-100px";
}

	// let priceInput = document.getElementById("product_quantity");
	// var priceInputMax = document.getElementById('price-max'),
	// 		priceInputMin = document.getElementById('price-min');
    //
	// priceInputMax.addEventListener('click', function(){
	// 	priceInput++
	// });
    //
	// priceInputMin.addEventListener('click', function(){
	// 	priceInput--
	// });