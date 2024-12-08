    // Populate appliance table
const appliances = [
    { name: "Tube Light", watts: 40 },
    { name: "Energy Savers", watts: 25 },
    { name: "LED Bulbs", watts: 7 },
    { name: "Fans", watts: 100 },
    { name: "Fans(AC/DC)", watts: 30 },
    { name: "TVs", watts: 250 },
    { name: "LED TVs 32\"", watts: 50 },
    { name: "Washing Machines", watts: 800 },
    { name: "Freezers", watts: 350 },
    { name: "Refrigerators", watts: 350 },
    { name: "Computers", watts: 250 },
    { name: "Water Pumps 1HP", watts: 700 },
    { name: "Irons", watts: 1000 },
    { name: "Split ACs 1 Ton", watts: 1800 },
    { name: "Split ACs 1.5 Ton", watts: 2400 },
    { name: "Split ACs 2 Ton", watts: 3000 }
];

const tableBody = document.getElementById("appliance-table");
appliances.forEach((appliance) => {
    const row = document.createElement("tr");
    row.innerHTML = `
        <td>${appliance.name}</td>
        <td>${appliance.watts}</td>
        <td><input type="number" min="0" value="0" data-watts="${appliance.watts}" oninput="calculateTotal()"></td>
    `;
    tableBody.appendChild(row);
});

function calculateTotal() {
    const inputs = document.querySelectorAll("#appliance-table input[type='number']");
    let totalLoad = 0;
    inputs.forEach((input) => {
        const watts = parseInt(input.dataset.watts);
        const quantity = parseInt(input.value) || 0;
        totalLoad += watts * quantity;
    });
    document.getElementById("total-load").value = totalLoad;
}

function submitData() {
    alert("Total Load Calculated: " + document.getElementById("total-load").value + " Watts");
}
