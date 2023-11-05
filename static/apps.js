document.addEventListener("DOMContentLoaded", function () {
    const spouseCheckbox = document.getElementById("id_spouse_check");
    const childCheckbox = document.getElementById("id_child_checkbox");
    const numberOfChildrenInput = document.getElementById("id_number_of_children");
    const totalMemberInput = document.getElementById("id_total_member");
    const amountInput = document.getElementById("id_amount");
    const totalAmountInput = document.getElementById("id_total_amount");
    const paymentMethodSelect = document.getElementById("id_payment_method");
    const serviceChargeInput = document.getElementById("id_service_charge");
    const handCashToDiv = document.getElementById("hand_cash_to_div");

    const baseFee = 2000;
    const spouseFee = 2000;
    const childFee = 1000;

    // Function to toggle the display of the number of children input
    function toggleNumberOfChildrenInput() {
        const numberOfChildrenDiv = document.getElementById("numberOfChildrenDiv");
        numberOfChildrenDiv.style.display = childCheckbox.checked ? "block" : "none";
        if (!childCheckbox.checked) {
            numberOfChildrenInput.value = "";
        }
        calculateTotal();
    }

    // Function to calculate the total number of members and update the amount
    function calculateTotal() {
        let totalMember = 1; // Start with 1 for the alumna/alumnus themselves
        let totalAmount = baseFee; // Base fee for the alumna/alumnus

        // Add spouse and children to the total member and amount if applicable
        if (spouseCheckbox.checked) {
            totalMember += 1;
            totalAmount += spouseFee;
        }

        if (childCheckbox.checked && numberOfChildrenInput.value) {
            let numberOfChildren = parseInt(numberOfChildrenInput.value, 10);
            totalMember += numberOfChildren;
            totalAmount += childFee * numberOfChildren;
        }

        // Update the total members and base amount on the form
        totalMemberInput.value = totalMember;
        amountInput.value = totalAmount.toFixed(2); // Assuming we want to round to two decimal places

        // Update service charge based on the payment method
        let serviceCharge = 0;
        if (paymentMethodSelect.value === 'handcash') {
            serviceCharge = 0; // No service charge for hand cash
            handCashToDiv.style.display = "block";
        } else {
            handCashToDiv.style.display = "none";
            serviceCharge = totalAmount * (paymentMethodSelect.value === 'bkash' ? 0.015 : 0.015); // Service charge for bkash and nagad
        }

        // Update the service charge and the total amount including service charge
        serviceChargeInput.value = serviceCharge.toFixed(2);
        let totalPayable = totalAmount + serviceCharge;
        totalAmountInput.value = totalPayable.toFixed(2);
    }

    // Event listeners
    childCheckbox.addEventListener("change", toggleNumberOfChildrenInput);
    spouseCheckbox.addEventListener("change", calculateTotal);
    numberOfChildrenInput.addEventListener("input", calculateTotal);
    paymentMethodSelect.addEventListener("change", calculateTotal);

    // Initial calculation on page load
    calculateTotal();
});
