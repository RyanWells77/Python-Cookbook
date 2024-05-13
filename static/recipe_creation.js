let ingredientCounter = 0;

function addIngredientField() {
    ingredientCounter++;

    var ingredientFields = document.getElementById('ingredient-fields');
    var newIngredientField = document.createElement('div');
    newIngredientField.innerHTML = `
        <label for="new_ingredient_name_${ingredientCounter}">Ingredient Name: </label>
        <input type="text" name="new_ingredient_name_${ingredientCounter}">
        <label for="new_measurement_${ingredientCounter}">Measurement: </label>
        <input type="text" name="new_measurement_${ingredientCounter}">
        <label for="new_unit_${ingredientCounter}">Unit: </label>
        <select name="new_unit_${ingredientCounter}">
            <option value="lb">lb</option>
            <option value="oz">oz</option>
            <option value="cup">cup</option>
            <option value="tbs">tbs</option>
            <option value="tsp">tsp</option>
            <option value="qt">qt</option>
            <option value="pinch">pinch</option>
        </select>
        <!-- Include CSRF token -->
        <input type="hidden" name="csrf_token" value="${crsfToken}">
    `;
    ingredientFields.appendChild(newIngredientField);
}
