function showForm(type) {
    const container = document.getElementById('form-container');
    container.innerHTML = '';  // clear previous form

    let formHtml = '';

    if (type === 'create') {
        formHtml = `
            <h2>Create Account</h2>
            <form id="createForm" onsubmit="submitForm(event, 'create')">
                <input type="text" name="acc_no" placeholder="Account No" required />
                <input type="text" name="name" placeholder="Name" required />
                <input type="date" name="dob" placeholder="DOB" required />
                <input type="text" name="address" placeholder="Address" required />
                <input type="text" name="mob_no" placeholder="Mobile No" required />
                <input type="number" name="initial_balance" placeholder="Initial Balance" required />
                <button type="submit">Submit</button>
            </form>
        `;
    }
    else if (type === 'deposit' || type === 'withdraw') {
        formHtml = `
            <h2>${type === 'deposit' ? 'Deposit Money' : 'Withdraw Money'}</h2>
            <form id="${type}Form" onsubmit="submitForm(event, '${type}')">
                <input type="text" name="acc_no" placeholder="Account No" required />
                <input type="number" name="amount" placeholder="Amount" required />
                <button type="submit">Submit</button>
            </form>
        `;
    }
    else if (type === 'balance' || type === 'statement') {
        formHtml = `
            <h2>${type === 'balance' ? 'Check Balance' : 'Print Statement'}</h2>
            <form id="${type}Form" onsubmit="submitForm(event, '${type}')">
                <input type="text" name="acc_no" placeholder="Account No" required />
                <button type="submit">Submit</button>
            </form>
        `;
    }

    container.innerHTML = formHtml;
}

function submitForm(event, type) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    const jsonData = {};

    formData.forEach((value, key) => {
        jsonData[key] = value;
    });

    fetch(`http://127.0.0.1:5000/${type}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(jsonData),
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message);
    })
    .catch(err => {
        console.error(err);
        alert('❌ Error occurred.');
    });
}
