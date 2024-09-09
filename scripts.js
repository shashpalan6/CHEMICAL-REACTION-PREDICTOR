document.getElementById('reaction-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const reaction = document.getElementById('reaction-input').value;
    
    fetch('/get-reaction', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ reaction: reaction })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('type').textContent = data.type;
        document.getElementById('product').textContent = data.details.Products;
        document.getElementById('scientific-name').textContent = data.details.Scientific_Name;
        document.getElementById('general-name').textContent = data.details.General_Name;
        document.getElementById('smiles-format').textContent = data.details.SMILES_Format;
        document.getElementById('molecular-weight').textContent = data.details.Molecular_Weight;
        document.getElementById('result').classList.remove('hidden');

        // Add animation here
        document.getElementById('result').classList.add('animate');
    });
});
