

// document.getElementById("add-rating-button").addEventListener("click", function() {
//     console.log("event listener is working when Add Rating & Comment button is clicked.")
//     document.getElementById("rating-form").style.display = "block";
// });

const favoriteIcon = document.getElementById("favorite-icon");
const addRating = document.getElementById("add-rating-button");
const update = document.getElementById("update-rating-button");

if (addRating) {
    addRating.addEventListener("click", function () {
        console.log("event listener is working when Add Rating & Comment button is clicked.")
        document.getElementById("rating-form").style.display = "block";
    });
}

if (update) {
    update.addEventListener("click", function () {
        console.log("event listener is working when Edit Rating & Comment button is clicked.")
        document.getElementById("rating-form").style.display = "block";
    });
}
// document.getElementById("update-rating-button").addEventListener("click", function() {
//     console.log("event listener is working when Edit Rating & Comment button is clicked.")
//     document.getElementById("rating-form").style.display = "block";
// });

document.addEventListener("DOMContentLoaded", function () {
    function toggleFavorite() {
        console.log("Toggle favorite function called");
        const id = document.getElementById('hidden_id').value;
        fetch(`/add_update_favorite/${id}`)
            .then(response => response.json())
            .then(data => {
                const favoriteIcon = document.getElementById("favorite-icon");
                console.log(data);
                if (data.is_favorite) {
                    favoriteIcon.classList.remove("far");
                    favoriteIcon.classList.add("fas");
                } else {
                    favoriteIcon.classList.remove("fas");
                    favoriteIcon.classList.add("far");
                }
            })
            .catch(error => {
                console.error("Error:", error);
            });
    }



    function updateFavoriteIcon() {
        const isFavorite = favoriteIcon.dataset.isFavorite === 'True';

        console.log("Initial favorite status:", isFavorite);

        if (isFavorite) {
            favoriteIcon.classList.remove("far");
            favoriteIcon.classList.add("fas");
        } else {
            favoriteIcon.classList.remove("fas");
            favoriteIcon.classList.add("far");
        }
    }

    updateFavoriteIcon();


    if (favoriteIcon) {
        favoriteIcon.addEventListener("click", toggleFavorite);
    }
})