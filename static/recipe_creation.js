let ingredientCounter = 0;

function addIngredientField() {
    ingredientCounter++;

    const ingredientFields = document.getElementById('ingredient-fields');

    let newIngredientField = document.createElement('div');
    
    newIngredientField.innerHTML = `
        <label for="ingredient_name-${ingredientCounter}">Ingredient Name:</label>
        <input type="text" name="ingredient_name[]" id="ingredient_name-${ingredientCounter}">
        <label for="measurement-${ingredientCounter}">Measurement:</label>
        <input type="text" name="measurement[]" id="measurement-${ingredientCounter}">
        <label for="unit-${ingredientCounter}">Unit:</label>
        <select name="unit[]" id="unit-${ingredientCounter}">
            <option value="lb">lb</option>
            <option value="oz">oz</option>
            <option value="cup">cup</option>
            <option value="tbs">tbs</option>
            <option value="tsp">tsp</option>
            <option value="qt">qt</option>
            <option value="pinch">pinch</option>
        </select>
    `;
    ingredientFields.appendChild(newIngredientField);
}

function addRecipe() {
    const recipeName = document.getElementById('recipe_name').value;
    const description = document.getElementById('description').value;
    const instructions = document.getElementById('instructions').value;
    
    const ingredients = [];
    const ingredientInputs = document.querySelectorAll('[name^="ingredient_name"]');
    const measurementInputs = document.querySelectorAll('[name^="measurement"]');
    const unitInputs = document.querySelectorAll('[name^="unit"]');
    
    for (let i = 0; i < ingredientInputs.length; i++) {
        const ingredientName = ingredientInputs[i].value;
        const measurement = measurementInputs[i].value;
        const unit = unitInputs[i].value;
        ingredients.push({ ingredient_name: ingredientName, measurement, unit });
    }

      // Prepare the data to be sent in the request body
      const data = {
        name: recipeName,
        description: description,
        instructions: instructions,
        ingredients: ingredients
    };
    console.log("this is in data: ", data)

    // Make a POST request to the server endpoint
    fetch('/add_recipe', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to add recipe');
        }
        return response.json();
    })
    .then(data => {
        console.log(data); // Log the server response
        // Optionally, display a success message or redirect the user
    })
    .catch(error => {
        console.error('Error adding recipe:', error);
        // Optionally, display an error message to the user
    });
    
}

document.addEventListener('DOMContentLoaded', function() {
    const recipeForm = document.getElementById('recipe-form');
    recipeForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission
        addRecipe(); // Call addRecipe() function
        console.log("addRecipe function called")
    });
});
