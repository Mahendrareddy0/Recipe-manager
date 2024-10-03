document.getElementById('recipe-form').addEventListener('submit', function (event) {
    event.preventDefault();

    const name = document.getElementById('recipe-name').value;
    const ingredients = document.getElementById('ingredients').value.split(',').map(ingredient => ingredient.trim());
    const instructions = document.getElementById('instructions').value;

    addRecipe(name, ingredients, instructions);

    // Clear the form
    document.getElementById('recipe-form').reset();
});

function addRecipe(name, ingredients, instructions) {
    const recipeList = document.getElementById('recipe-list');
    const listItem = document.createElement('li');

    listItem.innerHTML = `
        <strong>${name}</strong><br>
        <em>Ingredients:</em> ${ingredients.join(', ')}<br>
        <em>Instructions:</em> ${instructions}
        <button class="delete-btn" onclick="deleteRecipe(this)">Delete</button>
    `;

    recipeList.appendChild(listItem);
}

function deleteRecipe(button) {
    const listItem = button.parentElement;
    listItem.remove();
}
