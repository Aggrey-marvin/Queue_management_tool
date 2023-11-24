const submitBtn = document.getElementById('submit-btn');

submitBtn.addEventListener('click', function (event) {
    event.preventDefault();
    const fieldArray = [
        customerName = document.getElementById('customer-name'),
        phone = document.getElementById('phone'),
        department = document.getElementById('department')
    ];

    let hasNullField = false;
    for(let i = 0; i < fieldArray.length; i++) {
        if (fieldArray[i].value === '') {
            hasNullField = true
        }
    }

    if (hasNullField === true) {
        document.getElementById('warning').style.display = 'block';
    } else {
        document.getElementById('form').submit();
    }
    
    console.log(`These are the values: ${customerName.value} ${phone.value} ${department.value}`);
});