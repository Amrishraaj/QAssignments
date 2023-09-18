
document.querySelector('#deliver-here').addEventListener('click', function(e) {
  e.preventDefault();
  alert('Your address has been saved.');
});


document.querySelector("#address-edit").addEventListener('click', function(e) {
  const address = document.querySelector('.editable-address');
  address.contentEditable = true;
  
});


document.querySelector('#pay').addEventListener('click', function(e) {
  e.preventDefault();
  const inputs = document.querySelectorAll('.payment-area input');
  let cardNumber = inputs[0].value;
  let validThru = inputs[1].value;
  let cvv = inputs[2].value;
  let name = inputs[3].value;  
  const regex = /^(0[1-9]|1[0-2])\/?([0-9]{2})$/;

  if (cardNumber.length !== 16) {
    alert('Please enter a valid card number.');
    return;
  }
  else if (!regex.test(validThru)) {
    alert('Please enter a valid expiration date.');
    return;
  }
  
  else if (cvv.length !== 3) {  
    alert('Please enter a valid CVV.');
    return;
  }
  else if (name.length < 3) {
    alert('Please enter a valid name.');
    return;
  }
  else {
    alert('Your payment has been processed.');
  }
});