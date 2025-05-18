document.addEventListener("DOMContentLoaded", function () {
    const deleteButtons = document.querySelectorAll(".btn-danger");

    deleteButtons.forEach(button => {
        button.addEventListener("click", function (event) {
            event.preventDefault();

            const confirmDelete = confirm("Czy na pewno chcesz usunąć ten hit?");
            if (confirmDelete) {
                fetch(this.href, {
                    method: "DELETE",
                    headers: { "X-CSRFToken": getCSRFToken() }
                }).then(response => {
                    if (response.status === 204) {
                        this.closest("li").remove();
                    } else {
                        alert("Wystąpił problem przy usuwaniu hitu.");
                    }
                });
            }
        });
    });

    function getCSRFToken() {
        return document.querySelector("[name=csrfmiddlewaretoken]").value;
    }
});
